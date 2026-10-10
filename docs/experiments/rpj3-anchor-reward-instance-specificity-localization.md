# RPJ3 Anchor Reward Instance Specificity Localization

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在冻结 RPJ2 全部模型、Reward Reader、Projector、Anchor banks、teacher choices 与 registration checkpoints 的前提下，定位一个单一机制问题：Anchor 在 RPJ2 中恢复了 81%–95% supervised Reward adaptation 且 interface retrieval 为 100%，为什么旧 representation-specificity gate 仍然失败？

本实验属于 `ADAPTIVE_FROZEN_MECHANISM_DIAGNOSTIC`，承接 [rpj2-projector-noncollapse-anchor-mechanism](rpj2-projector-noncollapse-anchor-mechanism.md)，但不修改 RPJ1/RPJ2 的 frozen classification。

## Config

[历史配置摘要](../../configs/experiments/rpj3-anchor-reward-instance-specificity-localization.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Frozen known-VAE pseudo-unseen official HPDv3 DEV。
- 已在 RPJ2 消费过的 mechanism lockbox，仅作为 diagnostic replay surface，不重新称 fresh lockbox。
- Frozen SD / FLUX / DCAE representation cache、authoritative text cache、RPJ2 Teacher/SUP/Anchor/NoReg checkpoints。
- 新 null family：`GLOBAL_SD`、`PAIR_RO`、`PAIR_SP`、`PROMPT_RO`、nuisance-matched random orientation；每类 5 个预冻结 seeds。

Authority / access：

- official TEST orientation / forward / metrics：`0 / 0 / 0`
- new training fits：`0`
- network / RGB access：`0 / 0`

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### Frozen headline

`ORIGINAL_RPJ2_SPECIFICITY_GATE_CONFOUNDED_BY_SIDE_PRESERVATION`

### 核心定位

1. 旧 RPJ2 representation shuffle 被自动分类为 `PAIR_ORIENTATION_PRESERVING_NULL`：替换了完整 pair，但继续保持 preferred/rejected orientation。
2. Identical-representation sanity 严格得到 margin=`0`、Accuracy=`0.5`、BT-NLL=`log(2)`。
3. Teacher、SUP、Anchor 在新的 orientation-destroying primary `PAIR_RO` 下，SD/FLUX/DCAE 全部 `PASS`；Anchor 的 `GLOBAL_SD` 也为 3/3 `PASS`。
4. `PAIR_SP` 相对 `PAIR_RO` 的 Anchor Accuracy 提升：SD=`+0.093067`、FLUX=`+0.102373`、DCAE=`+0.099547`；对应 NLL 改善=`+0.091812/+0.102672/+0.091977`，三 target 都检测到 preference-side distribution signal。
5. PROMPT_RO 与 nuisance-matched controls 三 target 全部 `PASS`；Anchor↔SUP margin Pearson=`0.820165/0.889755/0.826121`，Spearman=`0.721828/0.835542/0.729904`。
6. 三个 target 的 failure localization 均为 `RPJ2_FAILURE_LOCALIZED_TO_OLD_NULL_SEMANTICS`。

| Target | Teacher PAIR_RO | SUP PAIR_RO | Anchor PAIR_RO | Anchor GLOBAL_SD | Localized bottleneck |
|---|---|---|---|---|---|
| SD | PASS | PASS | PASS | PASS | old null semantics |
| FLUX | PASS | PASS | PASS | PASS | old null semantics |
| DCAE | PASS | PASS | PASS | PASS | old null semantics |

### Terminal verification

- Exact RPJ2 replay：`PASS`。
- CUDA 1024-row backend parity：三 target 与两 surfaces 全部 `max_abs=0 / sign=1 / Pearson=1`。
- Scientific disk-only replay：`PASS`，mismatches=`0`。
- Completed replay：`PASS`，inventory failures=`0`。
- Inventory：`35` files，`63,730,438` bytes。
- Spec SHA256：`b2360f1ffc98590ac7940da967c4eba7b26c95ab7dc5061148e9a5c926032f52`。
- Null manifest SHA256：`f2305d458a5d19ffbb44b5445eaf5fd2c70b5f4d0d6a5ba369b2f086fc912528`。
- Decision SHA256：`c7f9e2f95864f8a88d9b79f9ae34c23e1cc2511d091a358ea55908a8d7bb860e`。
- Verifier receipt SHA256：`167a6d64a2ee18db05801ef6ef9e2f1904975531e34a3595077cd384e44a07be`。
- Result seal SHA256：`575cbfedf814a8ec3535d88c093324feb8b4bea039a29dfc6eb9c798ff9eb353`，status=`SEALED`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

RPJ3 支持这样的受限解释：在冻结 known-VAE pseudo-unseen development artifacts 上，Anchor Reward gain 确实依赖当前 image-specific representation；RPJ2 的 strict failure 主要来自旧 null 保留 preference orientation，因此它测到了 label-side / dataset-level structure，而不是纯粹破坏 instance identity。

这不等于“回写 RPJ2 为 PASS”。RPJ2 的 sealed classification 必须原样保留，因为 RPJ3 是后续 adaptive diagnostic，并使用了已消费 surface。当前证据也不证明 fresh confirmation、真正 unseen VAE、universal onboarding 或部署可用。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

冻结动作：`PROMOTE_TO_FRESH_AUTHORITY_AND_TRUE_UNSEEN_VAE`。

下一实验不应继续训练更强 Projector、扩大 Anchor K 或在当前 DEV 上调参。应先冻结当前方法，再申请 genuinely fresh authority 与真正 unseen-VAE evaluation；只有 fresh gate 通过，才能把本次机制支持升级为确认性 onboarding 证据。

## Sources

- [来源快照](../source-snapshots/rpj3-anchor-reward-instance-specificity-localization.txt)，原页面定位 `wiki-store/wiki/experiments/rpj3-anchor-reward-instance-specificity-localization.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
