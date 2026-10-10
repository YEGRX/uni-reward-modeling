# LatentAtlas U4-A5 Reference-U Necessity

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在不访问 Reward、H1105、validation/test 或 fresh authority 的前提下，比较三种固定候选参考空间：`H_SD`、`H_FLUX` 与算术 barycenter `H_BAR`。核心问题是：correct correspondence specificity 是否只在某一个 reference target 上成立，以及是否存在跨 mapping family 一致偏好的单一候选。

该实验延续 [latentatlas-u4a4-reward-free-p4096-crossfit-correspondence-specificity](latentatlas-u4a4-reward-free-p4096-crossfit-correspondence-specificity.md)，但不把任何候选预先称为 canonical U。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u4a5-reference-u-necessity.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- 只使用冻结 P4096 paired identities；五折 cross-fit，每折 fit/evaluation identity-disjoint。
- 三个 target：SD reference、FLUX reference、raw arithmetic barycenter reference。
- Pairing：correct 加五个固定 whole-row permutation null。
- Mapping family：解析 F 与非线性 N。
- 总计 360 个 aggregate evaluation cells；不持久化 per-identity prediction、rank 或 embedding。

本实验中的 paired identities 属于 dense transductive onboarding，不等于少量 Anchor onboarding。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### Original attempt: operationally invalid

原 attempt 已完成全部 360 cells，但 terminal N adequacy 将完整 270-cell multi-target registry 直接交给要求 target-local 90 cells 的 assessor。Disk verifier 因 `ValueError: N adequacy arithmetic drift` 正确失败。

原树中保存的 `BLOCKED_PREMEASUREMENT` 没有通过 completed verifier，不能提升为科学分类。原 attempt 保持不变；R1 是独立标记的 `adaptive_replay / non_confirmatory / operational_repair`。

### R1 verified classification

正式分类：**`REFERENCE_RESULTS_MIXED_ON_HISTORIC_DEV`**。

| Target / family | Relative cNRMSE LB | R@1 LB | MRR LB |
|---|---:|---:|---:|
| SD / F | 0.406224 | 0.635010 | 0.719393 |
| SD / N | 0.248391 | 0.231934 | 0.311678 |
| FLUX / F | 0.218381 | 0.110596 | 0.195962 |
| FLUX / N | 0.472304 | 0.646729 | 0.724975 |
| BAR / F | 0.297083 | 0.365234 | 0.473485 |
| BAR / N | 0.383890 | 0.481689 | 0.567016 |

六个 target-by-family specificity gates 全部通过，但 reference preference 不统一：

- F prefers SD；SD 相对更好 alternative 的 lower bounds 为 `(0.106625, 0.257568, 0.236287)`。
- N prefers FLUX；FLUX 相对更好 alternative 的 lower bounds 为 `(0.085295, 0.153076, 0.147789)`。
- BAR 在两个 family 中都不是 materially stronger，也没有同时对两个 alternative noninferior。
- 没有 single cross-family preferred target。

Decision SHA-256：`7930fb63f8601742f7255a50a107b36828b5b11e3a08b1deef13a2e5801387a8`。Inventory SHA-256：`e35cc7fd9cd154f6aa7bd324ce78532ff3a8bb1721e72af8276a7b768523bff3`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

本实验最重要的结论不是 “BAR 失败”，而是：三个候选 target 都保留 correct-pairing specificity，然而哪个 reference 更好依赖 mapping family。当前无法用这一组 development evidence 选出唯一 canonical reference。

它削弱了“raw arithmetic barycenter 是唯一必要 target”的假设，也没有支持“SD 或 FLUX 单独就是 universal U”。Reference selection 仍是 unresolved model-selection problem。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本实验 hard stop，不自动追加 target、architecture 或 authority。若以后继续，应把 reference selection 与 Reward functional confirmation 分开冻结；不能使用当前 development result 事后挑 target，再称其为 confirmatory。

当前和报告阶段均为 CPU-only；不需要 GPU 服务器。

## Sources

- [来源快照](../source-snapshots/latentatlas-u4a5-reference-u-necessity.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u4a5-reference-u-necessity.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
