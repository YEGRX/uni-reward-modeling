# LatentAtlas U4 Reference 与 Consensus-U 开发实验报告

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

### 2.1 研究背景

[latentatlas-u4a4-reward-free-p4096-crossfit-correspondence-specificity](latentatlas-u4a4-reward-free-p4096-crossfit-correspondence-specificity.md) 已经在历史 development cohort 上建立了一个重要前提：使用正确跨 VAE identity correspondence 拟合时，F 与 N 两种 mapping family 都能在样本外评价中稳定优于五个 permutation null。

但 U4-A4 没有解决三个更进一步的问题：

1. 正确配对信号是否依赖某一个固定 reference target？
2. 能否不依赖手工 arithmetic reference，直接学习一个 deterministic consensus U？
3. 如果 point representation 不足，distributional U 是否能提供额外价值；复杂 Flow 是否优于简单 Gaussian？

### 2.2 本批实验目标

本批实验共享同一冻结 P4096 authority，并拆为三个相互独立的诊断 track：

- **U4-A5-R1 — Reference-U Necessity**：比较 `H_SD`、`H_FLUX` 与 `H_BAR`，检验是否存在跨 F/N 一致优选的单一 reference。
- **U4-A6-D2 — Deterministic Consensus-U**：检验 learned deterministic consensus 是否同时具备 correct-pairing specificity、noncollapse 与 arithmetic-reference noninferiority。
- **U4-A6-PROB — Distributional Consensus-U**：比较 Point、diagonal Gaussian 与 conditional Flow，检验 distributional representation 的新增价值。

本实验不以任何候选已是 universal/canonical/Reward U 为前提。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u4-development-final-experiment-report.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

### 4.1 公共 population

- Authority：冻结的 P4096 paired identity population。
- Registered views：SD、FLUX、DCAE 三种 VAE representation。
- Correspondence：同一 RGB identity 在不同 VAE 中的 matched latent。
- Null controls：冻结的 whole-row permutation pairings，保持 target-row multiset 不变，只破坏 identity correspondence。
- U4-A5-R1 使用 P4096 五折 cross-fit。
- U4-A6-D2 与 U4-A6-PROB 使用 fold 0：3,276 fit identities、820 evaluation identities。

### 4.2 Access boundary

本批实验没有访问：

- H1105；
- Reward labels、orientation、checkpoint、model 或 evaluator；
- validation/test identities、latent、metric 或 model output；
- fresh authority；
- 网络或 CUDA。

每个有效 replay/pilot 均只有一次 registered materialization，16 项 forbidden counters 全部为零，且没有持久化 per-identity prediction、embedding、rank、nearest-neighbour 或 bootstrap-sample payload。

### 4.3 Anchor 口径

这里使用的是 P4096 大规模同图跨 VAE correspondence，可视为 **dense paired onboarding**。它不是早期 K=64 的低成本 Anchor onboarding，因此成功结果不能表述为“少量 Anchor 已完成新 VAE 接入”。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 结果总览

| Track | Frozen classification | Correct vs null | Baseline comparison | Collapse | 主要结论 |
|---|---|---|---|---|---|
| U4-A5-R1 | `REFERENCE_RESULTS_MIXED_ON_HISTORIC_DEV` | 6/6 target×family gates 通过 | F prefers SD；N prefers FLUX | 无 validity failure | 三种 reference 都有 specificity，但无统一 reference |
| U4-A6-D2 | `DETERMINISTIC_CONSENSUS_U_NOT_CORRESPONDENCE_SPECIFIC` | Specificity 实际通过 | Arithmetic noninferiority 失败 | Noncollapse 通过 | 当前 learned consensus 有结构但弱于简单 baseline |
| U4-A6-PROB | `DISTRIBUTIONAL_U_FEASIBLE_BUT_FLOW_NOT_NECESSARY` | Gaussian、Flow specificity 通过 | Gaussian adds value；Flow 不 adds value | 两者均通过 | Simple Gaussian 可行，Flow 暂无必要 |

### 7.2 U4-A5-R1：Reference-U Necessity

六个 target-by-family specificity gates 全部通过：

| Target / family | Relative cNRMSE LB | R@1 LB | MRR LB |
|---|---:|---:|---:|
| SD / F | 0.406224 | 0.635010 | 0.719393 |
| SD / N | 0.248391 | 0.231934 | 0.311678 |
| FLUX / F | 0.218381 | 0.110596 | 0.195962 |
| FLUX / N | 0.472304 | 0.646729 | 0.724975 |
| BAR / F | 0.297083 | 0.365234 | 0.473485 |
| BAR / N | 0.383890 | 0.481689 | 0.567016 |

Reference preference 不统一：

- F prefers SD；SD 相对更优 alternative 的 lower bounds 为 `(0.106625, 0.257568, 0.236287)`。
- N prefers FLUX；FLUX 相对更优 alternative 的 lower bounds 为 `(0.085295, 0.153076, 0.147789)`。
- BAR 在两个 family 中都不是 materially stronger，也没有同时对另外两个 target noninferior。
- Single cross-family preferred target 不存在。

因此，A5-R1 不支持“arithmetic barycenter 是唯一必要 reference”，也没有识别出 SD、FLUX 或 BAR 中的 canonical U。

Decision SHA-256：`7930fb63f8601742f7255a50a107b36828b5b11e3a08b1deef13a2e5801387a8`。
Inventory SHA-256：`e35cc7fd9cd154f6aa7bd324ce78532ff3a8bb1721e72af8276a7b768523bff3`。

### 7.3 U4-A6-D2：Deterministic Consensus-U

实际 gate state：

- Specificity lower bounds `(relative cNRMSE, R@1, MRR)=(0.158261, 0.150000, 0.124974)`，全部通过。
- Variance mass=`16.550848`，effective rank=`37.521936`，64 active dimensions；noncollapse 通过。
- Worst-view R@1=`0.895122`，lower=`0.876829 > 1/820`；chance gate 通过。
- VAE probe balanced accuracy=`0.421545 <= 0.433333`；VAE probe gate 通过。
- Architecture、matched streams 与 training integrity 全部通过。
- 相对 arithmetic reference，R@1/MRR point gap=`-0.065854/-0.048732`，lower=`-0.087805/-0.064485`；没有达到 `>= -0.02` 的 noninferiority threshold。
- Failure reasons 只有 `noninferiority`。

冻结 fallback classification 的名称比实际 gate state 更宽。准确解释是：

> Learned deterministic consensus 非塌缩并含 correct-pairing-specific structure，但相对 arithmetic reference 的检索损失超过注册容忍度。

Decision SHA-256：`8a079465076677c760eeca590313694ec69d2e197e567cfce385a605b6863fe4`。
Inventory SHA-256：`9b806e59bec63d4ab5bdaaf3303dd2ca04402862d6686da362282183b0d6e55e`。

### 7.4 U4-A6-PROB：Distributional Consensus-U

| System | cNRMSE | R@1 | MRR | Energy | Calibration error |
|---|---:|---:|---:|---:|---:|
| Point | 0.419571 | 0.998374 | 0.998950 | 1.559275 | 0.818595 |
| Gaussian | 0.485829 | 0.994715 | 0.996622 | 0.154735 | 0.174047 |
| Flow | 0.437064 | 0.989837 | 0.993776 | 1.689232 | 0.055758 |
| Flow shuffled | 1.304822 | 0.000000 | 0.007175 | 5.532565 | 0.409118 |

关键注册结果：

- Gaussian vs null specificity=`(0.354501, 0.026423, 0.017669)`，通过。
- Gaussian vs Point retrieval lower=`(-0.006504, -0.004225)`，通过 noninferiority。
- Gaussian vs Point relative energy-gain lower=`0.899367`，通过 added-value gate。
- Flow vs shuffled 的 energy/MRR degradation lower=`0.691115/0.984158`，说明 Flow 确实依赖 condition。
- Flow vs Point relative energy-gain lower=`-0.092358`，没有 registered added value。
- Flow vs Gaussia

（其余历史细节见来源快照。）

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 8.1 本实验建立了什么

第一，正确跨 VAE correspondence 中确实存在可学习、能够拒绝 permutation null 的共享结构。该结论不依赖唯一的 SD、FLUX 或 BAR reference target。

第二，shared structure 的存在不自动意味着任意 learned consensus 都优于简单 reference。A6-D2 表明当前 deterministic consensus 已经学到结构，但 arithmetic reference 仍是更强的检索基线。

第三，对 uncertainty 做最小参数化具有潜在价值。A6-PROB 中 simple Gaussian 仅轻微损失 retrieval，却显著改善 energy score，是本批实验中最明确的新候选。

第四，更复杂的模型不自动更好。Flow condition-shuffle control 证明其确实使用输入条件，但它仍没有取得相对 Point 或 Gaussian 的 registered added value。

### 8.2 本实验没有建立什么

本实验不能证明：

- 已得到 universal、canonical 或 Reward-aligned U；
- SD、FLUX、BAR 或 Gaussian 已被选为最终 reference/representation；
- fixed Shared Reward Head 能在 onboarded VAE 上工作；
- Reward transfer、unseen-VAE onboarding 或 zero-target-Reward functionality 已实现；
- 结果能推广到 fresh holdout、新 VAE、新任务或新数据分布；
- P4096 dense pairing 等价于低成本 Anchor onboarding；
- 所有 deterministic consensus 或 Flow architecture 都不可能有效。

### 8.3 当前课题阶段

最准确的阶段定位是：

> **Reward-free development 中已经建立 correspondence-specific candidate mechanism，并找到 simple Gaussian distributional candidate；reference identity、Reward functionality、fresh generalization 与 unseen-VAE onboarding 仍未解决。**

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本批实验完成后执行 hard stop，不自动追加 target、architecture、Flow、Reward、fresh-data 或 unseen-VAE 实验。

若未来另行批准并取得真正 fresh functional authority，建议：

1. 将 simple diagonal Gaussian 作为预冻结候选，而不是继续增加 Flow 复杂度；
2. 将 reference selection 作为独立 unresolved gate，避免按当前 development result 事后挑选 SD 或 FLUX；
3. 冻结 Shared Reward Head、mapping family、hyperparameters 与 model-selection rule；
4. 在完全未被当前开发流程消费的 Reward authority 上，一次性比较 correct、permutation null 与 direct baseline；
5. 只有 structural 与 functional gates 同时通过，才讨论 canonical U 或 unseen-VAE onboarding。

以上只是 suggested-only research direction，未在本批 authority 上执行。

GPU 状态：本批实验与报告均为 CPU-only；不需要开启或维持租用 GPU 服务器。

## Sources

- [来源快照](../source-snapshots/latentatlas-u4-development-final-experiment-report.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u4-development-final-experiment-report.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
