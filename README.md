# LatentAtlas：让异构 VAE 低成本复用冻结的 Latent Reward Model

**目标：让使用不同 VAE 的生成模型接入同一个下游 Reward Model，同时保持 Reward Model 的权重不变。** 当前使用 DiNa，研究重点是少量同图 Anchor 学得的接口能否用于真实生成过程的 Noisy State。

[最近实验](docs/experiments/recent/README.md) · [Related Work](docs/related_work/README.md) · [历史实验索引](docs/experiments/index.md) · [详细历史概览](docs/history/project-overview-through-20261010.md)

## 1. 我们为什么做这件事

潜空间 Reward Model 通常依赖特定 VAE 的表示。换一个 VAE 后，原 Reward Model 能否继续使用，是模型复用中的实际问题。[PRISM §4.5](https://arxiv.org/html/2606.20310v1#S4.SS5)也指出这种 latent-domain 耦合及解码—重编码开销，并将 latent-space alignment / cross-model adapters 列为未来方向。

早期设想是构建统一的“latent 的 latent”。同图配对接口在已有实验中表现出可行性后，研究转向了更具体的问题：**用轻量接口翻译上游表示，保留下游已经学到的评分能力。** 低成本是目标，实际端到端收益需要结合接口、去噪和编解码开销评价。

## 2. 用什么方法：同图 Anchor + Projector

不同 VAE 虽然坐标不同，但可以编码同一批图片。这些对应样本提供跨空间监督；相似内容在不同表示中可能保留可学习的关系，这是方法的出发假设。

1. **Anchor：**把同一张图分别输入源 VAE 和 DiNa 对应的参考 VAE，得到配对 latent。
2. **Projector：**用这些配对坐标学习源空间到参考空间的映射；典型设置为64张 FIT，另64张 VAL用于坐标选模。
3. **Frozen Reward：**将映射结果交给原 DiNa，接口训练使用 latent 坐标监督，DiNa 权重保持不变。

```text
同一张图 x ── 源 VAE Encoder ── Projector ──┐
                                          ├─ 同一冻结 DiNa 评分路径
同一张图 x ── 参考 VAE Encoder ────────────┘
```

这里的参考是 **SD3.5 的 VAE 潜空间**；SD3.5 本身是扩散模型。打乱同图配对、替换映射结构和改变 Anchor 数量，分别用于检验对应关系、接口能力和监督规模的作用。

**Native Agreement 怎么算？** 对同一对候选图，比较原生路径与映射路径的 DiNa 排序是否一致。常用报告排除 Native 精确平局、映射路径平局计半分。它衡量原评分行为保留多少；人类偏好准确率和实际选择收益另外评价。

## 3. 为什么现在关注 Noisy State

前期主要训练和检查的是 **Clean latent 接口**，它建立了跨 VAE 接入的基础。DiNa 的底层网络则接收 noisy latent、时间步和文本条件；clean 输入评分封装还会构造参考噪声，二者需要区分。

LRM 的应用目标是在生成尚未结束时进行评价和选择。因此当前比较两条路线：

```text
直接路线：真实 Source Noisy State ── 原 Clean Projector ── DiNa
估计桥：  真实 Source Noisy State ── 当步 Clean Prediction ── 原 Projector ── DiNa
```

两条路线都固定输入尺度、时间和文本合同。人工前向加噪与真实采样轨迹分别验证；最终关心的是能否保持有用的选择，以及能否减少实际生成成本。

## 4. 最近做到了什么（更新至 2026-10-21）

| 实验 | 已有结果 | 目前说明什么 |
| --- | --- | --- |
| [D73：Clean 接入与强基线](docs/experiments/recent/README.md#d73)，64 FIT + 64 VAL，DEV28 | REC 的 Native agreement：FLUX **94.7237%**、Cosmos **94.6362%**；对比空间 Affine、Interposer-MSE/cycle、A2 | Clean 功能复用有开发域证据；两个来源仍使用同一已消费28组 |
| [DEV28：跨路径混合评分](docs/experiments/recent/README.md#mixed) | 混合路径额外失配 **3.5696pp**；两折 offset 校准后为 **0.8252pp** | 同路径保序与跨路径共同标尺是不同问题；新组校准确认未做 |
| [LRM-R1：真实终态](docs/experiments/recent/README.md#r1)，4 Prompt、8图 | REC 与强 Affine 均分后都保持 **4/4** Native 选择；逐流为7/8与8/8 | 这批终态上普通 Affine 已能解释选择能力 |
| [LRM-R2：Reward 有效性](docs/experiments/recent/README.md#r2)，同8图 | 原生 DiNa 与 PickScore 只在 **1/4** Prompt 同选 | 需要目标生成分布上的人类偏好依据；两模型分歧尚不能决定谁正确 |
| [LRM-N1：真实 Noisy State](docs/experiments/recent/README.md#n1)，2 Prompt、4轨迹、8状态 | clean-estimate→REC 两时点各 **2/2** 同选；raw-noisy→REC 后期降至 **1/2** | 当前支持估计桥的这次小样本观察，直接 noisy 接入跨时点仍不稳定 |

**当前判断：Clean 接入已形成实测基础；真实 Noisy State 的零训练直接迁移尚未稳定。** 最近小实验主要核对冻结 DiNa 的功能保持，人类质量收益、独立新组泛化和端到端加速仍待验证。约95%的 Clean Agreement不能直接替代这些问题。

## 5. 接下来要回答的问题

- 在新的真实生成内容上，冻结 DiNa 的选择是否符合任务所需的人类偏好？
- 以当前 clean-estimate bridge 和强 Affine 为对照，少量 Clean Anchor 能否支持不同噪声阶段的功能复用？
- 接口和去噪预测带来的成本，能否换来真实的早期选择收益？

跨空间映射、Model Stitching 和 noisy-latent stitching 都有相关前作；研究差别、监督权限及比较要求集中在 [Related Work](docs/related_work/README.md)。

## 仓库怎么读

- [近期实验总览](docs/experiments/recent/README.md)：16份研究记录、11份主要报告、4份原结果CSV及来源指纹。
- [历史索引](docs/experiments/index.md)与[逐次日志](docs/experiment_log.md)：原87条归档记录；Q32、HPS等历史结论保留。
- [文档核对入口](docs/evidence-and-reproduction.md)：仓库根目录运行 `bash scripts/reproduce.sh --check`，检查既有归档文件和表格，不调用模型。

Maintainer: YEGRX · Last update: 2026-10-21
