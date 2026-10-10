# LatentAtlas C1-R Fresh-Authority Multi-Seed LOO Confirmation

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

审计当前 Reward authority 是否包含从未参与 G0.1 train/validation/test、C0/C1 test、Anchor、architecture/hyperparameter selection 或人工调优的 fresh confirmatory preference pairs。只有存在有效且 image-disjoint 的新 authority，才允许执行三 seeds × 四 conditions 的 C1-R confirmation。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-c1r-fresh-authority-audit.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Current Reward dataset: `Rapidata/human-coherence-preferences-images`
- Frozen revision: `72c0ebefc7ef3bebe22643fc709a6e94c22b5b02`
- Official shards: `53/53`
- Audited source rows: `63,748`
- G0.1 pair manifest SHA-256: `23faea933a176eb3c3fd2b52d6006491b62b6ae3ae4d72b978e61803415e8acd`
- G0.1 split manifest SHA-256: `83a96bcdeb2805e1743b4555c5a1366558612dc5033598c777295b3016ab64ea`
- G0.1 official Parquet replay: `pass`

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

```text
status = NO_FRESH_CONFIRMATORY_AUTHORITY
```

| Source-row category | Rows | Valid `preferred_source_side` | Fresh image IDs |
|---|---:|---:|---:|
| G0.1 usable / already consumed | 56,074 | 56,074 | 0 |
| Exact aggregate ties | 7,673 | 0 | 0 |
| Aggregate/detailed mismatch | 1 | 0 | 0 |
| **Total** | **63,748** | **56,074** | **0** |

已消费 usable pairs 的 train/validation/test=`44,839/5,593/5,642`；unique images=`5,201/708/723`。整个 frozen snapshot 和 usable 集合都恰好包含同一组 `6,632` unique image IDs，因此：

- `all_dataset_images - consumed_images = 0`；
- `untouched image IDs=0`；
- `eligible_oriented_not_usable = 0`；
- 7,673 个 ties 的 orientation 全部为 `null`；
- 唯一 mismatch row 15,579 的 G0.1 orientation 为 `null`，其两个 image IDs 和 prompt 也都已出现在 consumed usable authority 中，而且该异常已被先前人工审计。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

当前数据集不能在不复用既有测试信息的前提下支持独立 confirmatory C1-R。旧 test 重新随机划分、从 validation 切 test、换 seed 后继续使用旧 test，均不满足 fresh authority 定义；exact ties 也不能被重新解释成 preference labels。

因此没有进入第二道 latent-cache coverage gate。C1-R 的 12 个 models、pretest seal、fresh label authority、paired component bootstrap 和 final decision 均未产生。C1-Mini 的 Case B 继续保持 **single-seed descriptive evidence**，不能升级为稳定的 unseen-VAE generalization failure conclusion。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

等待人工提供或批准新的 Reward authority。不得自动抓取新数据、改用旧 validation/test、重新划分旧 authority，或把 C1/C0 已消费 test 称为 fresh confirmation。新的 authority 需要先独立冻结 pair/image/prompt/source-row/component IDs 与 orientations，再审计三 VAE latent coverage。

## Sources

- [来源快照](../source-snapshots/latentatlas-c1r-fresh-authority-audit.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-c1r-fresh-authority-audit.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
