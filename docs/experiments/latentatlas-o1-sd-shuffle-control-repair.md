# LatentAtlas O1-SD Shuffle Control Repair

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

修复 [latentatlas-o1-independent-clean-latent-oracle-smoke](latentatlas-o1-independent-clean-latent-oracle-smoke.md) 中 SD null control 的 checkpoint-selection leakage risk。O1-v0 原 protocol 只置乱 train labels，却用真实 validation labels early stop；O1-SD-C 将 train/validation labels 分别独立置乱，五次训练全部结束后才一次性打开真实 test labels。

本实验不重新训练 SD real reader，不训练 FLUX/DC-AE，不改变 feature、reader、split、cache、normalization、optimizer 或 test set，也不启动 O1-v1。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-o1-sd-shuffle-control-repair.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Frozen SD real Test Accuracy: `0.5929203629493713`。
- Frozen SD real BT-NLL: `0.6690412759780884`。
- Pair counts: train/validation/test=`605/168/226`。
- Unique image counts: train/validation/test=`481/114/118`。
- 所有跨 split image intersections=`0`。
- SD deterministic clean latent shape=`[4,64,64]`，`missing_latents=0`。
- Normalization 继续只拟合 481 个 train images 的 channel mean/std/RMS feature。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

| Seed | Test Acc | Test BT-NLL |
|---:|---:|---:|
| 2026081401 | 49.56% | 0.704358 |
| 2026081402 | 53.10% | 0.679757 |
| 2026081403 | 52.21% | 0.683446 |
| 2026081404 | 46.02% | 0.682620 |
| 2026081405 | 62.39% | 0.661424 |

Null accuracy distribution：

- mean=`0.526549`
- population std=`0.054552`
- min=`0.460177`
- max=`0.623894`
- range=`0.163717`
- `count(null_acc >= real_acc)=1`

五个 run 的 train/validation permutation hashes 分别唯一且两组不相交。Artifact 独立重算确认所有统计、CSV 和 permutation hashes 与输入精确一致；O1/O1-SD-C focused suite 为 `34 passed`，fresh repository suite 为 `1637 passed in 546.67s`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 问题 1：原 SD shuffle=59.29% 是否能够被 repaired null replication 复现？

只被部分复现：`1/5` repaired null 达到或超过 real `59.29%`，该 seed 为 `2026081405`（`62.39%`）。其余四个为 `46.02%–53.10%`。

### 问题 2：repaired null distribution 是否总体接近 random 50%？

均值 `52.65%` 接近 random `50%`，但整体分布不稳定：population std=`5.46%`，range=`16.37%`，覆盖 `46.02%–62.39%`。这符合预注册 Case C 的“大幅波动”描述。

### 问题 3：SD real=59.29% 是否因此获得更可信的 Reward-signal interpretation？

**暂时不能。** 四个 null 低于 real，说明原 `59.29%` 不是五次均可稳定复现；但一个 repaired null 达到 `62.39%`，且整体 range 超过 `15%`。在当前 226-pair test set 下，单次 SD shuffle control 不可靠，因此不能把 SD real 干净归因于 Reward supervision。

这五个 null seeds 仅用于 smoke diagnosis，不是正式显著性检验，也不支持 shared Reward space、cross-VAE alignment 或 unseen-VAE generalization。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

实验在 Case C 停止。不自动增加 seed、不重跑 FLUX/DC-AE、不重新训练 SD real、不运行 O1-v1，也不进入 cross-VAE canonicalization。若未来另行批准，应把 SD null variance / dataset bias 审计作为独立实验设计，而不是继续抽 seed 获得想要的答案。

## Sources

- [来源快照](../source-snapshots/latentatlas-o1-sd-shuffle-control-repair.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-o1-sd-shuffle-control-repair.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
