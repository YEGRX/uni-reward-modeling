# LatentAtlas U5-PB1 Predictive-U Capacity and Spatial Topology Localization

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在复用 P4096、known-VAE、reward-free 的 development protocol 中，承接 [latentatlas-u5pb0-target-free-predictive-bottleneck](latentatlas-u5pb0-target-free-predictive-bottleneck.md)，定位 PB0 的 compact predictive-U 缺口主要来自：

1. token capacity；
2. decoder 的显式 Spatial Write；
3. U 内部的 Spatial Read / spatial organization；
4. 或当前冻结 bottleneck family 仍不足。

Case B 冻结为“原 decoder 没有合格的显式 spatial Write”。本实验只做 architecture localization，不读取 Reward、Reward Head、RGB、H/H-bar，也不评估 unseen VAE。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u5pb1-predictive-u-capacity-spatial-topology.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- P4096 fold-0 transport：train/validation/evaluation=`2868/408/820` identities。
- Source：SD `[4,64,64]` + FLUX `[16,64,64]`。
- Target：DCAE `[32,16,16]`。
- Train-only per-view/per-channel normalization。
- 五个 deterministic pairing nulls。
- Common-stream identity bootstrap：5,000 replicates，seed=`2026082502`。
- Evaluation 只打开一次；evaluation 后训练为 0。
- 这不是 K64 RGB Anchor/relative-Anchor 实验，但仍使用 dense matched cross-VAE identities，不能称为 unpaired 或广义 anchor-free learning。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### Final decision

```text
VERIFIED
READ_SPATIAL_TOPOLOGY_LIMITED
NOT_SUPPORTED_WITHIN_5_PERCENT
```

### Main evaluation

| 模型 | MSE ↓ | EV ↑ | pairing | U noncollapse | compact deficit |
|---|---:|---:|---|---|---:|
| B3 | 0.290828 | 0.705474 | PASS | N/A | reference |
| Q16-R | 0.724537 | 0.266251 | PASS | PASS | 1.491288 |
| Q32 | 0.657847 | 0.333789 | PASS | PASS | 1.261977 |
| Q64 | 0.561684 | 0.431175 | PASS | PASS | 0.931325 |
| Q128 | 0.494707 | 0.499003 | PASS | PASS | 0.701027 |
| Q64-W | 0.577349 | 0.415310 | PASS | FAIL | 0.985190 |
| S64-W | **0.382204** | **0.612937** | PASS | PASS | **0.314191** |
| SG80-W | 0.422719 | 0.571907 | PASS | PASS | 0.453499 |

### Registered localization

- Capacity：点值单调改善，但 Q128 gap-closure=`0.529918 [0.524733,0.535143]`，未达到 lower `>0.75`，因此 `NEGATIVE_INTERVAL`。
- Write：`A_write=-0.057837 [-0.063175,-0.052337]`，`Q64-W` 比 Q64 更差，`NEGATIVE_INTERVAL`。
- Read：`A_read=0.681086 [0.677725,0.684378]`，`PASS`。
- Hybrid：global advantage=`-0.443389 [-0.452197,-0.434538]`，`NEGATIVE_INTERVAL`。
- 所有 primary 模型 pairing gate 均通过；五个 null 只是 comparative controls，不是 permutation p-value。
- 最优 `S64-W` 的 compact-deficit upper=`0.318670`，仍远高于 strict-U `<0.05`，所以 `minimal_adequate_u=null`。

### Integrity

- Result seal SHA-256：`49100e1b349a05172ed929ccf1650d6b9d5999fa7b28d32e4d9a55f568e59156`
- Terminal inventory SHA-256：`918e101c2c13a9da05d8a780661da0e5a2bf162ab57de6852a6903f3a151c0ce`
- Verifier：hash/arithmetic/classification/access/one-evaluation/predecessor immutability 全部通过，verifier 没有训练。
- PB1 focused/adjacent regression：`169 passed`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

本结果支持：在当前冻结 predictive-U family 内，增加容量有帮助但不充分；单独添加 Spatial Write 无益；在相同 Write 下让 U 具有明确 spatial organization 带来大幅、稳定改善。因此 headline 是 `READ_SPATIAL_TOPOLOGY_LIMITED`。

它不支持把 `S64-W` 晋升为 canonical U。`S64-W` 虽是最佳 U 候选，仍比 B3 留下约 31.4% registered compact deficit。结果也不证明 fresh-holdout、unseen-VAE、Reward/Flow/Diffusion transfer、多 seed 稳定性或全局最优架构。

后续 [latentatlas-u5pb1r1-residual-information-localization](latentatlas-u5pb1r1-residual-information-localization.md) 已对这部分 deficit 做 frozen forward-only 诊断。Validation 显示 mid+high frequency 占比为 `0.827552 [0.820041,0.834740]`，但 channel/patch concentration 均为负、source evidence 不确定，故分类为 `RESIDUAL_LOCALIZATION_INCONCLUSIVE`。其 Evaluation authority 在任何 forward 前因 hash-schema mismatch 停止并已消费；该后续 attempt 未 `FINALIZED/VERIFIED`，不改变本页已封存的 PB1 结果。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

冻结建议是 `DO_NOT_PROMOTE_AND_RESOLVE_REGISTERED_GRAY_ZONES`。后续 PB1R1 已定位 residual，但 Validation 分类为 `RESIDUAL_LOCALIZATION_INCONCLUSIVE / DO_NOT_SELECT_NEW_ARCHITECTURE`；Q64-W 的 sealed registered noncollapse failure 仍是 effective rank=`15.271196` 未超过 `16.0`。

当前不自动启动 PB2、Reward transfer、新 seed/fold 或 canonical-U promotion。若要补 PB1R1 的 secondary Evaluation，只能另冻 corrected protocol、new run identity 与真正新的 authority，不能续跑已消费 attempt。

## Sources

- [来源快照](../source-snapshots/latentatlas-u5pb1-predictive-u-capacity-spatial-topology.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u5pb1-predictive-u-capacity-spatial-topology.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
