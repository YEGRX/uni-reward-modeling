> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# LRM-R1 正式科研决定

**决定：`AFFINE_SUFFICIENT_IN_PILOT`。**

**现有 LatentAtlas 值得进入一次范围明确的独立 LRM 使用确认。** 直接REC与强Affine在本轮真实FLUX终态上均保留4/4组的两流均分选择；强Affine还保留8/8逐流排序。下一次投入的理由是确认“简单Anchor接口能否在新生成候选上保持有用的冻结Reward选择”，当前证据没有提供额外优化REC或新建可靠性算法的理由。

该决定的“sufficient”指当前四组候选的同源Best-of-2选择，而非绝对分数相等、总体统计等效或普遍部署通过。评分前未找到可用于当前T1的既定功能数值门槛，本轮未事后补设阈值。

## 五个直接回答

| 问题 | 实际答案 |
|---|---|
| 1. 旧REC能合法处理真实FLUX终态吗？ | **能。** 原生终态血缘、BF16 decoder输入、源VAE权重和正式REC均已核验；8/8实际decoder重放逐像素及PNG SHA一致。 |
| 2. 是否保留完整T1 DiNa的主要行为？ | **当前四组的平均选择保留，分数保真不完整。** B的逐流排序7/8，均分选择4/4、regret0；Score MAE1.218750，bias−1.218750。dev-03一流反转且均分margin仅.03125。 |
| 3. q_gen/q_cycle能定位什么？ | 相对RMSE8.216%–20.344%；C的Score MAE1.308594、逐流7/8，dev-03均分变精确平局。没有观察到重编码修复，源输入差异不是当前可单独确立的主因。 |
| 4. 强Affine已达到相似功能吗？ | **在本轮选择任务上已达到，且逐流更稳定。** D为8/8逐流、4/4均分选择、regret0，Margin MSE.106323，REC为.107910。D的score也偏移，MAE1.294922。 |
| 5. 是否值得进入独立确认与完整成本实验？ | **值得独立确认，完整成本实验暂不优先。** 新组上同时确认功能保真与参考Reward有效性后，再判断成本收益是否值得测量。 |

## 对已有论文和研究投入的影响

- **保留**旧C论文的Clean配对适配及D73匹配强基线结果。它们有各自的数据、T0目标和评分合同，本轮没有重写或替代原证据；原稿57文件逐SHA保持。
- **新增**真实FLUX原生终态的合法接入与有限候选选择复用证据。它将Clean证据接到实际生成终态，但仍属于历史开发域诊断。
- **收缩**“REC的非线性是本场景功能复用所必需”的叙事。本轮强Affine已经复现所有选择，没有REC专属功能优势。
- **保留未定**绝对分数共同标尺、跨生成器混选、人类偏好收益、Noisy中间状态与端到端加速。本实验评价终态、同源Best-of-2。
- **不启动**新的LRM可靠性独立路线。当前发现可由普通映射、score偏移及margin稳定性解释，尚无需要复杂新理论或算法的异常。

## 为什么独立确认仍值得

技术门槛已实测通过；两种固定Anchor-only接口在真实生成终态上均保留四个组选择。因此“接口完全不能服务原生生成输入”的广泛否定与本轮数据不符。强Affine的竞争力使后续确认可以围绕实际能力推进，避免把研究价值绑在特定接口结构。

同时，当前A与同图历史PickScore仅1/4组同选，且没有人类偏好标签。若冻结参考本身在新图像域不能产生目标质量收益，复制它的选择就缺少应用价值。正式状态为 `REWARD_VALIDITY_NOT_ESTABLISHED`，它是后续应用确认的关键缺口。

## 最小新增证据与继续/停止依据

若用户决定继续，独立确认需要：冻结接口和协议后产生的新Prompt候选组；保留A/B/D及匹配评分流；独立目标偏好依据或有资格的质量评价，并事先确定主指标及可接受差异。C作为失败定位臂按需使用。独立数据应避免再次使用已消费的四个DEV组；样本量由允许误差与组级统计设计决定，不能把本轮4/4直接外推成样本量依据。

继续条件是新组上选择保真达到预定要求，且参考Reward选择具有目标质量价值；若只有共同score偏移而排序保留，后续贡献围绕该实际使用范围；若Affine同样充分，使用简单接口；若A自身没有目标价值，则停止该应用扩展；若新组上直接接口失效，再依据预定诊断定位合同、输入或目标差异。

**以上是缺失证据说明，没有在本轮启动新实验。** 本轮已用完科学64+技术16的RM上限，完成独立复算、失败分析和正式决定后停止。本轮没有待续跑或排队任务。真实GPU阶段已结束，70文件已取回，服务器可关闭；实际电源状态未知。

## 证据入口

- [真实四路径实验及全部数值](lrm-r1-results.md)。
- 失败与竞争解释（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_R1_REAL_INTERFACE_QUALIFICATION/FAILURE_DIAGNOSIS.md`）。
- 输入合同（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_R1_REAL_INTERFACE_QUALIFICATION/LATENT_CONTRACT_VERIFICATION.md`）、身份审查（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_R1_REAL_INTERFACE_QUALIFICATION/ASSET_AND_IDENTITY_AUDIT.md`）。
- [原始分数CSV](../tables/lrm-r1-four-path-results.csv)、原始逐查询账本（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_R1_REAL_INTERFACE_QUALIFICATION/FOUR_PATH_SCORE_LEDGER.jsonl`）。
- 独立复算（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_R1_REAL_INTERFACE_QUALIFICATION/REPRODUCIBILITY/root-independent-audit.json`）、实际资源账本（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_R1_REAL_INTERFACE_QUALIFICATION/REPRODUCIBILITY/resource-ledger.json`）。
