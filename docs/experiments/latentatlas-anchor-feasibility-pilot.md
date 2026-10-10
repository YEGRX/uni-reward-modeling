# LatentAtlas Anchor Feasibility Pilot

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

轻量验证同一组 RGB anchors 是否能将 SD-VAE、FLUX VAE 和 DC-AE 的异构 latent 转成跨 VAE 可比较的相对表示，并定位当前思路的可行性与问题。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-anchor-feasibility-pilot.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- COCO val2017：固定 256 张真实 RGB 图像。
- 16 anchors + 240 queries。
- Seed: `20260808`。
- Canonical input: RGB、512×512、中心裁剪、`[-1,1]`。
- 三个 VAE 使用逐像素相同的 tensor。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### Latent caches

| VAE | Shape | Dtype | Encode time | Peak VRAM |
| --- | --- | --- | --- | --- |
| SD-VAE | `[256,4,64,64]` | FP16 | 7.51 s | 3.18 GiB |
| FLUX VAE | `[256,16,64,64]` | BF16 | 7.68 s | 3.18 GiB |
| DC-AE | `[256,32,16,16]` | FP32 | 14.64 s | 3.74 GiB |

### 最强双向检索

| Pair | Operator | A→B R@1 / R@5 | B→A R@1 / R@5 |
| --- | --- | --- | --- |
| SD ↔ FLUX | rank | 0.5625 / 0.8333 | 0.5708 / 0.8875 |
| SD ↔ DC-AE | global | 0.4625 / 0.7417 | 0.5292 / 0.7708 |
| FLUX ↔ DC-AE | rank | 0.4375 / 0.7667 | 0.5167 / 0.8375 |

### Raw geometry

- SD ↔ FLUX：Spearman 0.7974；kNN overlap 0.6042。
- SD ↔ DC-AE：Spearman 0.7735；kNN overlap 0.5571。
- FLUX ↔ DC-AE：Spearman 0.7380；kNN overlap 0.5712。

### Statistical outcome

- 18/18 directed pair/operator 结果均满足 Recall@1 empirical `p = 1/201 ≈ 0.004975`。
- Top-1 命中为 55–137/240，远超过单样本异常。
- 预注册结论：**Go**。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

实验观察到强烈的 cross-VAE correspondence signal。三个 encoder 的 query-query raw geometry 本来就高度相关，说明它们虽然维度和压缩率不同，仍保留相似的图像结构。共享 anchors 把这些异构 raw latents 转成统一宽度的相对坐标，使同图检索成为可能。

rank relation 在包含 FLUX 的两个 pair 上最强，表明相似度次序比绝对尺度更稳健；涉及 DC-AE 时 global cosine 也很强。soft relation 一致偏弱，可能是 `tau=0.07` 在只有 16 anchors 时过尖。

当前证据只能支持“anchor-relative correspondence 值得继续验证”，不能写成已经证明统一潜空间或 Reward transfer。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

1. K = 8 / 16 / 32 / 64 anchor ablation。
2. 至少 3 个 data/anchor seeds 与 held-out anchor pools。
3. `tau = 0.03 / 0.07 / 0.15 / 0.3`。
4. 增加 random anchors、像素统计与视觉特征 baselines。
5. 多 seed 复现后再测试小 projector，暂不加入 Reward Head。

## Sources

- [来源快照](../source-snapshots/latentatlas-anchor-feasibility-pilot.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-anchor-feasibility-pilot.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
