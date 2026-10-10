# LatentAtlas DINO Local / Patch Semantic Probe

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在 [latentatlas-semantic-appearance-intervention](latentatlas-semantic-appearance-intervention.md) 表明 cross-VAE identity correspondence 对多种外观干预仍有韧性之后，Experiment F 检查 DINOv2-small 的局部 patch 表征是否比 global CLS 更接近三个 VAE 的 anchor-relative 结构。

本实验不训练 projector、Reward Head、VAE 或偏好模型，只比较四种固定 probe：CLS、mean-patch、local-set（Chamfer-style）和 spatial-patch。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-dino-local-patch-probe.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- 复用 256 张固定并哈希审计的 RGB 图像。
- 三组互斥 64-anchor banks；固定 64 queries。
- 三种冻结 VAE：SD-VAE ft-MSE、FLUX.1-schnell VAE、DC-AE f32c32。
- 冻结 DINOv2-small，固定 revision `ed25f3a31f01632728cabb09d1542f84ab7b0056`。
- 三个 anchor seeds；global cosine 与 rank relation。
- 相关页面：`dino`（原wiki关联）、`vision-transformer`（原wiki关联）、`representation-alignment`（原wiki关联）、`latent-space`（原wiki关联）。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### Global-primary macro evidence

| Probe | Pair-average R@1 | Geometry Spearman |
| --- | ---: | ---: |
| CLS | 0.061632 | 0.080457 |
| Mean patch | 0.074653 | 0.074040 |
| Local set | 0.084201 | 0.103893 |
| Spatial patch | **0.099826** | 0.097906 |

### 相对 CLS 的 paired improvement

| Probe | Macro ΔR@1 | Seed SD | Macro ΔSpearman | Macro Δneighbor | Worst-VAE ΔSpearman |
| --- | ---: | ---: | ---: | ---: | ---: |
| Mean patch | +0.013021 | 0.022553 | -0.006417 | +0.024566 | -0.065481 |
| Local set | +0.022569 | 0.019890 | **+0.023436** | +0.020747 | -0.026964 |
| Spatial patch | **+0.038194** | 0.015697 | +0.017449 | **+0.027604** | -0.040818 |

Spatial patch 的 R@1 从 CLS 的 `0.061632` 提高到 `0.099826`，绝对增加 `0.038194`；local-set 则给出最高的 geometry Spearman `0.103893`。

### 稳定性和控制

- Mean-patch geometry 是唯一 macro 为负的 probe/family cell。
- Local-set 与 spatial-patch 的 retrieval、geometry、neighbor macro 均为正；VAE/seed 正向计数大部分达到 2/3 门槛。
- 但每个 patch probe 的 worst-VAE geometry delta 都为负，说明 geometry improvement 不具有跨 VAE 普适性。
- 方向差异明显：VAE→DINO 减 DINO→VAE 的 macro R@1 差为 local `+0.092014`、spatial `+0.098958`。
- Spatial correct-minus-permuted macro R@1 effect 为 `+0.021467`，但最差经验 p-value 为 `1.0`；不能声称正确 patch index 在所有 cell 中都必要。
- 最终预注册标签为 **Partial Local Support**，没有注册 winner。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 可以支持的结论

局部/空间 DINO 表征确实比 CLS 提供了更多 aggregate correspondence 证据：spatial-patch 最有利于 identity retrieval 与 neighborhood，local-set 最有利于整体 geometry。

这使项目从“外观鲁棒但语义未知”推进到“局部视觉表征具有部分解释力”。它说明继续研究 local semantic structure 是合理的，但证据仍不是 Strong。

### 为什么只有 Partial

强门槛要求同一个 probe 在 retrieval、geometry、neighbor、VAE、seed 和 direction consistency 上同时通过。虽然 local/spatial 的三个 macro family 均为正，worst-VAE geometry 仍为负，direction asymmetry 也很大；至少一个 direction-specific consistency 条件没有满足，因此不能命名 Strong winner。

### 与 Experiment D / E1 的综合解释

- [latentatlas-shared-geometry-explanation](latentatlas-shared-geometry-explanation.md)：Pixel/Color 对原始 correspondence 有较强解释力。
- [latentatlas-semantic-appearance-intervention](latentatlas-semantic-appearance-intervention.md)：主动改变多个外观因素后 identity correspondence 大部分保留。
- Experiment F：local/spatial DINO 比 CLS 更能解释部分 aggregate correspondence，但跨 VAE、方向和空间控制不统一。

最稳妥 framing 是：cross-VAE correspondence 同时含有外观、局部结构和可能的语义相关成分；当前没有单一表示或因素能够完整解释它。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

1. 与导师讨论：核心发现是“local/spatial aggregate improvement + architecture/direction heterogeneity”，而不是“统一语义空间”。
2. 将 Experiment F 冻结为 geometry-explanation 阶段的终点。
3. 若导师认可，另行预注册 **Minimal Reward-Sufficiency**：只检验已观测 correspondence 是否足以支持一个最小、受控的 reward discrimination task。
4. 下一实验必须保留 CLS/local/spatial ablation、VAE family 分层、双方向报告和独立 held-out data/query replication。
5. 在新设计获批前不启动 Reward Head、preference training 或 reward transfer。

## Sources

- [来源快照](../source-snapshots/latentatlas-dino-local-patch-probe.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-dino-local-patch-probe.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
