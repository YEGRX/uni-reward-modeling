# LatentAtlas U4-B1D0：Source / Head / Reference Adequacy Localization

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在 [latentatlas-u4b1-284-exploratory-fresh-functional-specificity](latentatlas-u4b1-284-exploratory-fresh-functional-specificity.md) 的 direct `SOURCE_H` gate 失败后，先定位 source latent、冻结 Reward Head 与 candidate reference `H` 之间的 adequacy blocker，再决定是否有资格冻结修复候选。

本实验严格按下列顺序推进：

```text
定位 source/head/reference adequacy
        ↓
仅在 direct source ceiling 通过时冻结唯一修复候选
        ↓
再用未消费 fresh authority 做 source-only gate
        ↓ SOURCE_H Pass only
最后才评价 DCAE correct-vs-null
```

U4-B1D0 复用了已经消费的 B1-284 authority，因此是 `adaptive development`、`non-fresh`、`non-confirmatory`。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u4b1d0-source-head-reference-adequacy.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Cohort：已消费的 B1-284 SVG development cohort
- Pair count：284
- Image count：568
- Authority status：`CONSUMED_FRESH_REUSED_AS_ADAPTIVE_DEVELOPMENT`
- Source views：`H64`、`CONCAT_U128`、`RAW_SD64`、`RAW_FLUX256`、`RAW_CONCAT320`
- Reward orientation、SD/FLUX token 与 provider manifest 均以冻结绝对路径和 SHA-256 绑定。
- 本实验没有打开新的 fresh authority，也没有读取或评价 DCAE correct-vs-null。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 Zero-training localization

最佳零训练组合为：

```text
svg_unlabeled / shared bridge / taskaware head / H_SCORE_MEAN
```

- Accuracy：`0.535211 [0.485915, 0.584507]`
- BT-NLL：`0.719140`，upper=`0.743589`
- Absolute gate：`FAIL`

因此，仅改变 normalization、H aggregation 或切换现有 shared/task-aware bridge/head，不能恢复 source adequacy。

### 7.2 Five-fold direct linear source ceilings

| View | Accuracy | BT-NLL | Gate |
|---|---:|---:|---|
| `H64` | `0.482394` | `1.007065` | FAIL |
| `CONCAT_U128` | `0.492958` | `1.240826` | FAIL |
| `RAW_SD64` | `0.517606` | `0.860888` | FAIL |
| `RAW_FLUX256` | `0.457746` | `1.301217` | FAIL |
| `RAW_CONCAT320` | `0.457746` | `1.363800` | FAIL |

`RAW_SD64` 是最佳 direct linear ceiling，但仍未通过 gate。按冻结的 early-stop，Stage C 未打开，没有合格候选可冻结；DCAE evaluation count=`0`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 8.1 当前结果能说明什么

- B1-284 的 blocker 不能由简单 normalization、representation mean/score mean 切换，或现有 shared/task-aware bridge/head 选择直接修复。
- 在当前 284-pair 跨域 SVG cohort 和固定线性 reader 容量下，所有 source views 都没有达到冻结修复候选所需的 absolute adequacy gate。
- 按协议停止在 source localization 层，避免在已消费 authority 上反复选择复杂模型。

### 8.2 当前结果不能说明什么

- `SOURCE_LATENT_ADEQUACY_UNRESOLVED` 不等于 source latent 不含 Reward 信息。
- 不能否定非线性 direct reader、更大同域 source-training authority、新 reference 或新 VAE adapter。
- 不能评价 DCAE mapping、correct-vs-null specificity、fresh Reward transfer、canonical/universal `U` 或 unseen-VAE onboarding。
- 五折线性 probe 的失败只约束当前 cohort、view、reader capacity 与 gate，不是一般性不可达证明。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

1. 获取更大、独立、合法封存的 source-development authority，先在 source-only 条件下恢复 reader/reference。
2. 只用 development authority 选择并冻结唯一 H-compatible repair candidate。
3. 使用另一份未消费 fresh authority，只评价 `SOURCE_H` absolute adequacy。
4. 只有 `SOURCE_H` 同时通过 Accuracy 与 BT-NLL 的冻结 gates，才释放 DCAE correct-vs-five-nulls。
5. 若 fresh `SOURCE_H` 再次失败，结论仍停在 source/head/reference 层，不评价 mapping failure。

下一阶段的数据准备与 source-only reader 开发可能需要 GPU 编码；U4-B1D0 本身已经结束且为 CPU-only，当前无需租用 GPU 服务器。

## Sources

- [来源快照](../source-snapshots/latentatlas-u4b1d0-source-head-reference-adequacy.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u4b1d0-source-head-reference-adequacy.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
