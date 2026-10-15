# LatentAtlas O1-v1 Lightweight Spatial Clean-Latent Reward Oracle

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在不引入 Anchor、Shared U、cross-VAE sharing 或预训练 reward model 的前提下，分别检验 SD-VAE、FLUX-VAE、DC-AE 的完整 deterministic clean latent 是否含有可被轻量 spatial reader 独立读取的 human preference / Reward signal。

O1-v1 与 [latentatlas-o1-independent-clean-latent-oracle-smoke](latentatlas-o1-independent-clean-latent-oracle-smoke.md) 的唯一本质区别，是保留 `C×H×W` 的 local/spatial organization，而不再先压缩为 channel mean/std/RMS。数据契约继续来自 [latentatlas-reward-data-preflight-g01](latentatlas-reward-data-preflight-g01.md)，null protocol 沿用 [latentatlas-o1-sd-shuffle-control-repair](latentatlas-o1-sd-shuffle-control-repair.md) 的 train/validation 双置乱修复。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-o1-v1-lightweight-spatial-oracle.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Dataset: Rapidata human coherence pairwise preference。
- Cache-covered subset: `999` usable pairs、`713` unique reward images。
- Pair counts: train/validation/test = `605 / 168 / 226`。
- Unique image counts: train/validation/test = `481 / 114 / 118`。
- 三个 split 的 image intersection 均为 `0`；`missing_latents=0`。
- SD latent: `[4,64,64]`；FLUX latent: `[16,64,64]`；DC-AE latent: `[32,16,16]`。
- 每个 VAE 的 channel normalization 只用 481 张 unique train images，在 image + spatial 维拟合 population mean/std；validation/test 只复用 train statistics。
- 18 个 checkpoint 全部冻结并校验 SHA-256 后，真实 test labels 只打开一次；`test_label_open_count=1`。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

| VAE | Real Acc | Real BT-NLL | Best Val NLL | Epoch | Null Acc Mean±Std | Null Acc Min–Max | Null NLL Mean±Std | ΔAcc | ΔNLL | Null≥Real | Gate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| SD | 62.83% | 0.657236 | 0.666273 | 5 | 55.66%±3.52% | 50.88%–60.18% | 0.684805±0.008911 | +7.17% | +0.027569 | 0/5 | preliminary_positive |
| FLUX | 56.19% | 0.665850 | 0.671706 | 2 | 50.97%±5.06% | 43.81%–56.64% | 0.691582±0.011148 | +5.22% | +0.025732 | 1/5 | preliminary_positive |
| DC-AE | 61.06% | 0.633225 | 0.682258 | 2 | 49.29%±3.21% | 46.02%–54.87% | 0.694940±0.003580 | +11.77% | +0.061715 | 0/5 | preliminary_positive |

Null test accuracy（seed `1401..1405`）：

- SD：`50.88 / 60.18 / 53.98 / 53.98 / 59.29%`。
- FLUX：`46.46 / 55.75 / 43.81 / 52.21 / 56.64%`。
- DC-AE：`46.46 / 50.44 / 48.67 / 46.02 / 54.87%`。

与 O1-v0 real accuracy 的同 split 描述性比较：SD `+3.54%`，FLUX `-1.77%`，DC-AE `-1.77%`。因此 spatial reader 没有在三个 VAE 上一致超过 mean/std/RMS reader。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 8.1 是否存在 independently readable Reward signal？

三个 VAE 都通过预注册 smoke gate：real accuracy 高于 `null mean + 1 population std`，real BT-NLL 优于 null mean，且 real 至少超过 4/5 null。O1-v1 因而提供 preliminary evidence，支持“heterogeneous clean VAE latents independently contain readable Reward information”。这不是 formal significance test，也不证明 Reward-sufficient universal space。

### 8.2 SD 是否得到确认？

SD real=`62.83%`，null=`55.66%±3.52%`，5/5 null 均低于 real，且 `ΔNLL=+0.027569`。相较 O1-v0/O1-SD-C 的 unresolved 状态，SD readability 获得更可信的 preliminary smoke 支持。

### 8.3 Spatial structure 是否普遍更容易读取？

不能作普遍肯定。SD 相比 O1-v0 上升 `3.54%`，但 FLUX/DC-AE 都下降约 `1.77%`。正确结论是：spatial reader 让三个 VAE 都呈现 real-vs-null separation，但没有统一提高 absolute real accuracy。

### 8.4 Memorization risk

- SD：best train/validation NLL=`0.638969/0.666273`，`pretest_memorization_risk=False`。
- FLUX：`0.665098/0.671706`，`pretest_memorization_risk=False`。
- DC-AE：`0.642757/0.682258`，`pretest_memorization_risk=True`，原因是 train drop 大而 validation gain 仅 `0.003326`。DC-AE 虽通过 real-vs-null gate，解释时仍必须保留该 warning。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

O1-v1 到此停止，不升级 reader、不增加 null seed、不自动启动后续实验。当前 smoke evidence 足以停止继续做 Independent Oracle，并允许把 `Direct Shared Reader vs Minimal Reward Canonical U` 作为下一项独立、另行批准的设计问题；这不等于 O1-v1 已经证明 cross-VAE canonicalization 可行。

## Sources

- [来源快照](../source-snapshots/latentatlas-o1-v1-lightweight-spatial-oracle.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-o1-v1-lightweight-spatial-oracle.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
