# LatentAtlas Anchor Budget Replication

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在 [latentatlas-anchor-feasibility-pilot](latentatlas-anchor-feasibility-pilot.md) 已显示三种 VAE 之间存在 anchor-relative correspondence 后，检验结论是否依赖单一 anchor bank，并测量 anchor 数量 K、relation operator 和 soft temperature 对结果的影响。

本实验只回答 anchor-budget / anchor-seed robustness，不把结果解释为高层语义统一、unified latent space 或 Reward transfer。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-anchor-budget-replication.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- 复用第一轮 COCO val2017 固定 256-image latent cache。
- 三组互斥 64-anchor banks，对应 seeds `2026080901 / 2026080902 / 2026080903`。
- 剩余 64 images 作为所有条件共享的固定 queries。
- VAE families: SD-VAE、FLUX VAE、DC-AE。
- 三组 bank 在索引上严格互斥，因此不是概率意义上完全独立的随机样本。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### Anchor budget 主结果

三个 seeds 的 macro pair-average（误差为 sample standard deviation）：

| K | 最佳 condition | R@1 | R@5 | MRR | worst-pair R@1 |
| --- | --- | --- | --- | --- | --- |
| 8 | global | 0.464±0.038 | 0.806±0.045 | 0.614±0.040 | 0.451 |
| 16 | global | 0.664±0.036 | 0.909±0.005 | 0.771±0.024 | 0.630 |
| 32 | global | 0.758±0.018 | 0.952±0.004 | 0.841±0.011 | 0.745 |
| 64 | rank | 0.829±0.038 | 0.969±0.005 | 0.890±0.023 | 0.732 |

Global R@1 的增量为 `+0.200 / +0.094 / +0.037`，说明在 K≈32 后明显趋于饱和。Rank 到 K=64 仍继续受益。

### Operator 与 pair-specific 结果

- K=8/16/32 的 macro 最佳是 global，K=64 的最佳是 rank。
- K=64 global 的 R@1 为 `0.795±0.005`，虽然低于 rank，但 seed 波动更小，且 worst-pair R@1 为 `0.771`，高于 rank 的 `0.732`。
- K=64 的 pair-specific 最佳分别为：SD↔FLUX soft@0.15 `0.904±0.039`；SD↔DC-AE rank `0.875±0.062`；FLUX↔DC-AE global `0.779±0.025`。
- Soft tau 的较好点从 K=8/16 的 `0.30` 转向 K=32/64 的 `0.15`；`tau=0.03` 明显过尖。
- 双向 correspondence 不对称。K=64 rank 中，FLUX→DC-AE 为 `0.661±0.009`，DC-AE→FLUX 为 `0.802±0.050`。

### Null 与 seed 稳定性

- R@1 和 R@5 均为 `432/432` 个有向结果达到 empirical `p<0.05`。
- R@1 最大 p=`0.01493`，最小 observed-minus-null effect=`0.09055`。
- 72 个 pair/condition seed summaries 的 R@1 std：mean=`0.0470`、median=`0.0492`、max=`0.1160`。
- Best-seed 次数为 `22 / 26 / 24`，没有某个 anchor bank 独占最佳结果。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 阶段判断

**Anchor-budget / anchor-seed robustness 得到支持。** 三个互斥 anchor banks 下信号普遍显著，K 曲线清晰，证明上一轮结果不是只依赖某一组幸运 anchors。

**完整 GO-A 暂不最终判定。** 三组 seed 共用同一批 64 queries，并来自同一 256-image pool，因此尚未验证 data/query seed robustness。下一步需运行真正独立 anchor pool + query pool 的 Experiment C。

**GO-B 未判断，GO-C 不启动。** Pixel/color/frequency/semantic baselines 尚未完成，在此之前不训练 shared projector 或 Reward Head。

### 当前工程默认值

- 如果优先稳定性与 worst-pair：以 global 作为默认 baseline。
- 如果只追求 K=64 macro correspondence：同时报告 rank。
- Soft relation 不宜作为默认值，必须进行 pair-与 K-specific 调参。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

1. Experiment C：至少 3 个独立 anchor+query replicates，条件允许时每个 replicate 使用 512 images。
2. 增加 Pixel、Color、Frequency baselines，再按成本选择 DINOv2 或 CLIP 之一作为 semantic baseline。
3. 加入 wrong-anchor-bank / mismatched-anchor-identity negative control。
4. 在上述门控前保持零训练，不引入 projector 或 Reward Head。

## Sources

- [来源快照](../source-snapshots/latentatlas-anchor-budget-replication.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-anchor-budget-replication.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
