# DINA0-R1 外部 DiNa 原生裁判资格检验

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

独立检验外部冻结 DiNa 经自身 SD3.5 VAE 原生路径，是否能在已消费开发偏好数据上提供可泛化的 Reward 信号。研究缺口（research gap）是区分裁判自身资格与跨 VAE 接口恢复；本阶段无需 Anchor。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-dina0-r1-native-qualification.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

DIAG643行、EXTERNAL2619行，6524张准入 RGB，均为历史已消费 development authority。future12455行仍为 `RETIRED_UNVERIFIED_FOR_FUTURE_CONFIRMATION`，行/方向零读取；old TEST 零读取。本结果不是 fresh confirmation。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

| 指标 | DIAG | EXTERNAL（主判定） |
|---|---:|---:|
| Native Accuracy | 54.666% | 50.420% |
| 中央90%区间 | 51.477%–57.854% | 48.815%–51.989% |
| Accuracy−chance 单侧95%下界 | +1.477个百分点 | −1.185个百分点 |
| PAIR_RO均值 Accuracy | 50.295% | 48.931% |
| Native−PAIR_RO gain下界 | +0.902个百分点 | −0.256个百分点 |
| Raw-margin AUROC（诊断） | 0.5474 | 0.5140 |

EXTERNAL两项主要下界与方向检查失败；pair-swap、noncollapse与DIAG point Accuracy通过。自动字段 `diag_direction_consistent` 实际要求两个surface的A/B点准确率全部>.5，因EXTERNAL A侧49.220%而失败；DIAG自身A/B点准确率56.306%/52.903%均>.5。不可仅按字段名误读。

全部103986评分组合、415944科学Reward前向、6524 VAE编码完成，fits=0。完整回传110542文件、952722437字节，SHA256全部匹配；Mac独立20k重放PASS、指标/判定完全相同；全部3262行、52192个条件与score缓存精确对应。

Source: `raw/experiments/latentatlas/dina0-r1-final-2026-09-14/DINA0_metrics.json`、`DINA0_automatic_decision.json`、`transfer-verification.json`、`independent-replay-verification.json`、`independent-cache-verification.json`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

2026-09-15解释补充：本封存结果在当前研究中定位为 **external/OOD diagnostic**。约50%仅描述既定外部数据及runtime，不能直接与论文HPDv3数字比较，也不能据此判定DiNa本身无效。之前缺少的是source-domain sanity/parity check，外部实验并非无价值。原数值、自动UNQUALIFIED及旧DINA1停止记录保持，不回写旧seal。新SRC0/SHIFT0/REG1将分别回答源域资格、dataset/task shift、representation/interface registration和target Reward reuse；见 [latentatlas-dina-src0-source-domain-parity](latentatlas-dina-src0-source-domain-parity.md)。

Source: `raw/experiments/latentatlas/dina-src0-best-evidence-2026-09-15/research-intent-clarification.md`。

当前固定DiNa原生路径未在注册外部开发数据上证明满足冻结裁判资格。DIAG有限信号不足以支持外部资格；这不等于所有DiNa用途无效，也不否定整个LatentAtlas。PAIR_RO外部区间48.218%–49.642%，不能声称该对照回到chance。Wrong Prompt等诊断不替代主门槛。

新的协议修订解除DINA0与Anchor证明的耦合。旧DINA1-R1和GFI预检仍作为历史独立记录保留。完整解释见 `raw/experiments/latentatlas/dina0-r1-final-2026-09-14/dina0-final-report-zh.md`。

## Possible Conflict / 待确认冲突

旧DINA1-R1要求future12455行全局未消费与完整Anchor disjointness；后续用户修订将未来confirmation资格退役，但保留零读取。旧Source：`raw/experiments/latentatlas/dina1-preflight-2026-09-08/DINA_USER_PROTOCOL.md`；新Source：`raw/experiments/latentatlas/dina0-r1-preparation-2026-09-09/DINA_PROTOCOL_AMENDMENT.md`。这是后续授权覆盖，不回写旧seal。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

2026-09-15 用户新方向：继续使用DiNa，独立调查数据集/推理契约。见 [latentatlas-dina-dataset-runtime-diagnostic](latentatlas-dina-dataset-runtime-diagnostic.md)。这是新诊断，不改变本页封存结论；HPDv3源域评分尚未完成。

按协议停止本次DINA0路线，不创建DINA1-R2，不进行u/K/分辨率或模型capacity搜索。可能改进（possible improvement）仅为未来另行注册的任务/数据分布机制诊断；当前结果不能确定失败原因。未来确认需真正fresh external human-preference authority。

完整结果与缓存均已在本地，无需保持GPU或远程电脑运行。定时检查在最终交付时停用。旧云电源状态未核实。

相关：`latentatlas`（原wiki关联）、[latentatlas-rgen1-reward-external-generalization](latentatlas-rgen1-reward-external-generalization.md)、[latentatlas-dina1-external-frozen-reward-functional-registration](latentatlas-dina1-external-frozen-reward-functional-registration.md)、[latentatlas-gfi1-group-frozen-interface-registration](latentatlas-gfi1-group-frozen-interface-registration.md)。

## Sources

- [来源快照](../source-snapshots/latentatlas-dina0-r1-native-qualification.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-dina0-r1-native-qualification.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
