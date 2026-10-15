# LatentAtlas O1 Independent Clean-Latent Reward Oracle Smoke

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

独立检验 SD-VAE、FLUX-VAE、DC-AE 各自的 deterministic clean latent 中，是否存在可被 `channel mean/std/RMS + small MLP` 直接读取的真实 human pairwise preference signal。

本实验只研究三个独立映射，不研究 cross-VAE transfer，不训练 Shared Reward Model，也不使用 Anchor relation、Shared U、G1/G2 model/checkpoint/result。相关输入契约来自 [latentatlas-reward-data-preflight-g01](latentatlas-reward-data-preflight-g01.md)。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-o1-independent-clean-latent-oracle-smoke.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Dataset authority: Rapidata human coherence pairwise preference 的冻结 G0.1 artifacts。
- Cache-covered subset: `999` usable pairs、`713` reward images。
- Pair counts: train/validation/test = `605 / 168 / 226`。
- Unique image counts: train/validation/test = `481 / 114 / 118`。
- train/validation/test image intersections: 全部为 `0`。
- SD latent shape: `[4,64,64]`；feature dimension `12`。
- FLUX latent shape: `[16,64,64]`；feature dimension `48`。
- DC-AE latent shape: `[32,16,16]`；feature dimension `96`。
- Missing latents: `0`。
- Test-label authority: 六次训练全部完成后 one-shot 打开，`open_count=1`。

每个 latent 在 FP32 下计算 channel-wise mean、population std（`correction=0`）和 RMS，并按该顺序拼接。每个 VAE 的 normalization 只用 481 张 unique train images 独立拟合。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

| VAE | Test Acc | BT-NLL | Best Val NLL | Best Epoch | Shuffle Acc |
|---|---:|---:|---:|---:|---:|
| SD | 59.29% | 0.669041 | 0.682523 | 2 | 59.29% |
| FLUX | 57.96% | 0.660897 | 0.678479 | 3 | 51.33% |
| DC-AE | 62.83% | 0.642266 | 0.679457 | 2 | 49.56% |

验证记录：

- `[O1 AUDIT]` 与预期 counts/shapes 完全一致，`missing_latents=0`。
- artifact schema/hash/CSV/report 检查通过。
- `loss-curves.png` 为 `1500×1500`，六个 real/shuffle train/validation curves 已视觉检查，无裁切。
- O1 focused suite: `23 passed`。
- Repository full suite: `1626 passed in 496.74s`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 问题 1：三个 VAE 是否分别显示明显 Reward signal？

按本 smoke 的 descriptive rule（Test Acc `>55%`），三个 real-label readers 都显示候选直接可读 signal：SD `59.29%`、FLUX `57.96%`、DC-AE `62.83%`。其中 SD 的 shuffle control 同为 `59.29%`，所以 SD 不能被干净归因于真实 preference labels；这是单 seed、226 test pairs 的快速诊断，不是显著性或 reward sufficiency 证明。

### 问题 2：哪个最强 / 最弱？

按 Test Accuracy，DC-AE 最强（`62.83%`），FLUX 最弱（`57.96%`）。这一排序只适用于当前固定 representation、reader、split 和 seed。

### 问题 3：shuffle control 是否接近随机？

FLUX `51.33%` 与 DC-AE `49.56%` 落在预设 `[45%,55%]` 随机带内；SD `59.29%` 未通过该 control gate。SD 的 real 与 shuffle accuracy 恰好相同，因此不能把 SD real result 干净归因于真实 train preference labels。

### 问题 4：是否足以进入 cross-VAE canonicalization？

**当前不足。** 虽然三个 real readers 都超过 55%，但 SD shuffle control 不接近随机。O1 因此支持“clean latent 中存在值得继续诊断的直接可读 preference signal”这一有限观察，却不足以支持 Reward information 已可被可靠 canonicalize，更不证明跨 VAE shared alignment。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本次实验到此停止，不自动运行 O1-v1、额外 null seeds 或 cross-VAE canonicalization。若未来另行批准后继续，应先解释/复核 SD shuffle anomaly，再决定是否需要 lightweight spatial encoder；不应直接升级为 DiT、Shared U 或大型 cross-VAE 实验。

## Sources

- [来源快照](../source-snapshots/latentatlas-o1-independent-clean-latent-oracle-smoke.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-o1-independent-clean-latent-oracle-smoke.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
