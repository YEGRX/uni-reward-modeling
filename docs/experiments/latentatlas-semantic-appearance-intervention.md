# LatentAtlas Semantic-Preserving Appearance Intervention

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在 [latentatlas-shared-geometry-explanation](latentatlas-shared-geometry-explanation.md) 发现 Pixel/Color 等低层 baseline 对原始 cross-VAE correspondence 解释力很强之后，主动改变图像外观，检验 correspondence 是否会随颜色、高频、模糊敏感结构一起消失。

本实验 E1 不训练 projector、Reward Head 或 VAE。它只回答：对同一批图片施加语义尽量保持的 appearance intervention 后，SD、FLUX、DC-AE 的 anchor-relative identity correspondence 和 relational geometry 能保留多少。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-semantic-appearance-intervention.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- 复用 256 张已哈希审计的固定源图。
- 每张图生成五个条件：Original、Grayscale、Color Jitter、Gaussian Blur、Frequency attenuation。
- 总计 1,280 张确定性变换图。
- 三种冻结 VAE：SD-VAE ft-MSE、FLUX.1-schnell VAE、DC-AE f32c32。
- 三组互斥 64-anchor banks；固定 64 queries。
- 相关页面：`latent-space`（原wiki关联）、`variational-autoencoder`（原wiki关联）、`representation-alignment`（原wiki关联）。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### Primary macro result

| Condition | Macro global R@1 | Matched retention |
| --- | ---: | ---: |
| Original | 0.795139 | — |
| Grayscale | 0.689236 | 0.873204 |
| Color Jitter | 0.767361 | 0.964518 |
| Gaussian Blur | 0.674479 | 0.863670 |
| Frequency | 0.830729 | 1.049675 |

四个 intervention retention 全部超过 0.80，预注册判定为 **Strong**。

三个 seed 的结果方向一致；波动最大的是 Gaussian Blur，seed-level macro retention 为 `0.855 / 0.786 / 0.950`，但均未出现整体崩塌。

### Null and wrong-anchor

- Minimum observed-minus-null effect: `0.202891`。
- Maximum empirical p: `0.000999 = 1/1001`。
- Wrong-anchor mean R@1 effect: `0.752894`。
- Wrong-anchor minimum R@1 effect: `0.421875`。
- Wrong-anchor coverage: 54 registered cells。

干预后的 residual correspondence 仍依赖正确 shared-anchor identity。

### Directional asymmetry

最弱方向是 Gaussian Blur 下的 `DC-AE→FLUX`：

`retention = 0.311356 ± 0.061410`。

相反方向 `FLUX→DC-AE` 为 `0.861930 ± 0.229820`。这说明 architecture family 和 retrieval direction 会显著影响 appearance robustness。

### Retrieval 与 geometry 的分离

Color Jitter 的 macro identity retention 为 `0.964518`，但 within-VAE geometry Spearman 只有：

- SD-VAE: `0.360797 ± 0.007651`；
- FLUX: `0.402789 ± 0.006828`；
- DC-AE: `0.567341 ± 0.025403`。

因此，同图 identity 仍可检索，不代表 query-query 的完整 geometry 或邻域结构不变。

### Formal output and integrity

- 180 directional rows；
- 90 pair-average rows；
- 180 seed-summary rows；
- 240 retention-summary rows；
- 72 within-VAE geometry rows；
- 144 neighbor-overlap rows；
- 90 cross-VAE geometry rows；
- 102 cross-seed geometry-summary rows；
- 180 null-summary rows与 180 个长度 1,000 的 null arrays；
- 54 wrong-anchor rows；
- 768 Original reproduction rows；
- 5 张必需审计图；
- Remote formal verifier: `verified: true`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 正式结论

**Strong / pass。** 当前 shared identity correspondence 不能仅由本实验测试的 chromatic color、颜色/亮度扰动、高频细节或 blur-sensitive appearance 因素解释。

### 与 Experiment D 的合并解释

[latentatlas-shared-geometry-explanation](latentatlas-shared-geometry-explanation.md) 表明低层特征对原始 correspondence 有较强解释力；E1 表明主动扰动其中多个因素后，identity correspondence 仍大部分保留。最稳妥的综合解释是：

- 低层 appearance 对 correspondence 有贡献；
- 被测试的任何单个 appearance component 都不是总体 correspondence 的唯一必要来源；
- 残留信号可能来自形状、布局、局部物体结构、其他统计不变量或真正语义，当前尚不能区分。

### 必须限制的主张

- Robust identity correspondence ≠ Full geometry invariance。
- Appearance robustness ≠ Semantic causality。
- Cross-VAE matching ≠ Unified latent coordinate system。
- Geometry correspondence ≠ Reward sufficiency。
- Frequency retention > 1 不代表语义更强，只表示该干预后匹配相对 Original 更容易。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

1. 与导师讨论“identity retrieval robust，但 geometry 不完全 invariant”是否应成为论文的核心 framing。
2. 执行 **DINO local/patch semantic probe**，而不是继续只用 global CLS。
3. 优先检查 Blur 下 DC-AE→FLUX 的方向性脆弱是否来自 spatial resolution、channel layout 或局部平滑响应差异。
4. 可进一步构造同语义不同外观 / 同外观不同语义的 matched pairs。
5. 在 semantic/local evidence 通过前，继续冻结 projector、Reward Head、preference training 与 reward transfer。

## Sources

- [来源快照](../source-snapshots/latentatlas-semantic-appearance-intervention.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-semantic-appearance-intervention.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
