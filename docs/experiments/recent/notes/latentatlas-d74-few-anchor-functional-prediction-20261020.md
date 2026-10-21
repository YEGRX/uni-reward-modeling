> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# D74：有限 Anchor 的冻结功能收益预测

## 1. Date

2026-10-20；22:17闭环记录，P0、拟合、坐标、真实评分及独立复算完成；正式决定 **NO_GO_PREDICTION**。

## 2. Purpose

检验Reward评价前可得的坐标信息，是否能够预测REC相对强空间Affine的Native agreement收益，并改善接口选择或Anchor预算。C主线保持；P0审计、D74-0资格实验、D74-1条件推进、独立确认分阶段。

## 3. Code Version / Commit

新实现 `scripts/latentatlas-d74/`；D73依赖原字节及SHA固定。工作区已有修改保留，采用逐文件SHA，未以当前Git HEAD冒充完整执行版本。原主文与Supplement已备份，见 `baseline-preservation.json`。

## 4. Dataset / Input

两来源Cosmos/T0与FLUX/T0，同图FIT64按SHA排序分成A/B各32，再取各前16；VAL64独立于FIT。每来源五任务：16A、16B、32A、32B、64。n64复用原REC前1000更新及旧Affine候选。功能评价固定历史DEV28前四完整组、144物理候选对、流0/1；原生科学评分和文本条件复用。DEV已消费，两个来源共用图像，均非独立确认。

## 5. Parameters

REC固定lr=.001、1000更新、batch32、每125步坐标VAL。Affine固定reflect k1/3/5和zero-mask k3、各五ridge，按BF16坐标VAL选点。参数训练Anchor-only，RM完全冻结，预测输入无当前RM响应。封存范围及预算见 `pilot-scope-r1.json` 和 `D74_EXPERIMENT_PROTOCOL.md`。

## 6. Command

受控入口 `train_pilot.py`、`linear_subset_pilot.py`；运行spec、计量回执及代码身份均保存在 `docs/latentatlas-anchor-theory-2026-10-17/d74-execution/`。远端工作目录 `/opt/latentatlas/d74-20261020-r1`；恢复前先检查已有任务，禁止重复训练。

## 7. Results

- P0补充线性控制：恒1通道一起zero-pad，覆盖移除激活后的REC边界偏置。两来源各五ridge均真实拟合，联合坐标选择仍保留原reflect k5。
- P0 Cosmos Interposer BN探针：MSE版本VAL NMSE由.12871170变为.12884059（+0.1001%）；Cycle由.13350776变为.12712772（−4.7788%），达到事前1%实质变化门槛。仅重估BN统计，权重未变、0 RM。它限定Interposer归因，未解释下游差距。
- D74-0 Affine八子集：160拟合、10240 FP64 VAL及10240 BF16 VAL，supervisor99.776秒；全部选reflect k5。逐图汇总、160系数SHA及预算验收见结果回执。
- REC八组训练完成：8000更新、256000训练前向与反向、4096 VAL，监督4695.029秒。Cosmos四组均选择1000步；FLUX16A/16B/32A/32B分别选择875/625/875/750步。主控逐trial复算预算和8点坐标选模。
- 第一次坐标缓存在180秒硬限终止：115 REC、114 Affine调用，228份完整缓存，无新RM。I/O测量指向同步写开销；一次修订借用已完成阶段节余、保持原GPU总预算，R2硬限1200秒。科学规则、样本和接口不变；失败调用累计收费。

- 坐标R2完成640 REC+640 Affine缓存；功能前X1/X2/X3与规则原字节封存。
- 两来源各6336科学+200技术DiNa、440预测前向；无新文本/VAE/生成。四组/144物理对/两流中，REC的10项agreement点估计均高于强Affine。Cosmos增益5.575–8.188 pp，FLUX1.394–2.613 pp。
- 预定坐标选择在四项FLUX选错接口。十个相关设置等权agreement：Always REC90.889%、Always Affine86.446%、Coordinate VAL90.157%。没有新增主要决策收益。
- FLUX-16A坐标VAL和margin MSE更差，但agreement高2.091 pp；四个单组和删组均正，提供具体端点分离案例。全体七项描述区间跨零，两项删组反号，不能宣称十项总体稳定胜出。
- 主控核对两算法及本地重算133,540数值，最大差9.715e−17；2,116有效BF16载荷SHA一致，原论文57文件保持。GPU阶段总8,725.646秒，含失败；13,072新增RM，详见资源账本。

## 8. Analysis

正式 **NO_GO_PREDICTION**：停止当前D74-1特征/阈值扩展，保留少Anchor功能迁移及坐标—分差—排序偏好分离的开发证据。X3重复X1，X2没有事前决策阈值；四组结果不支持最小Anchor预算。强Affine与zero-mask控制均保留；Interposer BN的配方边界单列。理论四项证明作为诊断与信息边界工具，没有形成新DiNa预测定理。

## 9. Problems

跨Mac/WSL方差存在最大5.96e−8差异，已绑定历史方差并明确容差，保留失败0拟合回执。BN重估不能替代真实批次训练；原Interposer属于适配合同对照。四组pilot区间只用于探索，10个任务并不独立。当前已训练接口后再作选择不计节省训练成本。

独立确认资产并行核查：主控重新核对source400纯身份清单（400组、14400对、3600图像SHA）和历史消费审计；全部400组已用于source qualification。现有索引尚未证明存在未消费且满足C合同的新Anchor池及评价组，状态为`NOT_READY_FROM_REVIEWED_ASSETS`，范围限于已审入口。本轮未读取待确认Reward标签、未启动P3。单任务配对访问为n张FIT加64张VAL，分别80/96/128张。

## 10. Next Steps

优先C论文冻结正式REC/强Affine后的独立组确认。当前已审资产未取得未消费合格组；不以旧source400或SVG替代。具体32组准备规模及证据门见最终决定，尚非已启动预算。D74-1与P3未运行，无待续跑GPU任务。结果已本地回收，可关闭服务器，实际电源状态未知。

## 11. Sources

- `raw/projects/latentatlas/d74-20261020/user-request.txt`
- [最终科研决定](../reports/d74-decision.md)
- [完整真实结果](../reports/d74-results.md)、复现与资源（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/d74-execution/D74_REPRODUCIBILITY/README.md`）
- P0审计（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/d74-execution/D74_BASELINE_AUDIT.md`）
- 协议（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/d74-execution/D74_EXPERIMENT_PROTOCOL.md`）
- Affine子集结果（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/d74-execution/affine-subsets-result-sol-r1.md`）
- 诊断命题与边界（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/d74-execution/D74_THEORY.md`）
- 独立确认资产核查（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/d74-execution/independent-asset-readiness-sol.md`）、`independent-asset-root-check-r1.json`。
- `latentatlas`、`latentatlas-theory-map`、`latentatlas-research-decisions`、`latentatlas-paper-framework`。
