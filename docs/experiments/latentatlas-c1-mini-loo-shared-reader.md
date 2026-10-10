# LatentAtlas C1-Mini Leave-One-VAE-Out Direct Shared Reward Reader

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在 [latentatlas-c0-mini-v1-direct-shared-reader](latentatlas-c0-mini-v1-direct-shared-reader.md) 已显示三个 seen VAE 可以由同一套 9,473 参数 reader 共同读取后，检验下一项最小 problem-identification 问题：只用两个 source VAE 的 Reward supervision 训练时，同一读取规则能否迁移到一个不提供 Reward-supervised latent、gradient 或 model-selection signal 的 held-out VAE family。

本实验运行且只运行三个 calibration-only leave-one-VAE-out（LOO）条件：SD+FLUX→DC-AE、SD+DC-AE→FLUX、FLUX+DC-AE→SD。目标 VAE 只用其 5,201 个 train-split image tokens 拟合固定 scalar mean/std，因此这是 **calibration-only unseen-VAE transfer**，不是 strict zero-shot。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-c1-mini-loo-shared-reader.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- 完全复用 [latentatlas-reward-data-preflight-g01](latentatlas-reward-data-preflight-g01.md) 与 C0 的冻结权威：train/validation/test=`44,839 / 5,593 / 5,642` pairs，unique images=`5,201 / 708 / 723`。
- Image、pair、prompt、source-row 跨 split 交集均为 0；split SHA-256=`83a96bcdeb2805e1743b4555c5a1366558612dc5033598c777295b3016ab64ea`。
- SD/FLUX/DC-AE latent shape=`[4,64,64] / [16,64,64] / [32,16,16]`；三份正式 cache 覆盖全部 6,632 reward images，额外 192 Anchor rows/VAE 不参与。
- 统一输入仍为每 channel 无参数池化到 `4×4` 后的 16 维 token；reader architecture、optimizer、超参数、seed 与 C0 完全相同。
- SD/FLUX/DC-AE 的 train-only scalar normalization mean/std=`0.372937/3.461009`、`-0.145613/2.136468`、`-0.417926/2.210025`。
- C1 只导入 hash-bound C0 family-level baseline，不导入 C0 test labels 或 per-example scores。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

| Held-out Target | Sources | Source Macro Acc | Source Macro NLL | Target Acc | Target NLL | C0 Full-Seen Acc | Acc Gap | Retention |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| SD | FLUX + DC-AE | 55.67% | 0.681528 | 53.51% | 0.698236 | 54.68% | -1.17 pp | 0.6188 |
| FLUX | SD + DC-AE | 55.84% | 0.684281 | 54.47% | 0.686796 | 55.07% | -0.60 pp | 0.7648 |
| DC-AE | SD + FLUX | 54.27% | 0.685610 | 52.46% | 0.691153 | 55.83% | -3.37 pp | 0.5768 |
| **Macro** | — | — | — | **53.48%** | **0.692062** | **55.19%** | **-1.71 pp** | — |

Target-minus-Full-Seen NLL gap：SD/FLUX/DC-AE=`+0.012897/+0.004690/+0.007138`；macro=`+0.008242`。Target-minus-C0-Independent accuracy gap=`-2.39/-0.07/-3.69 pp`。

三个 source macro 均满足 Accuracy > `0.5` 且 NLL < `log(2)`。Held-out FLUX 与 DC-AE 同时满足 Target Accuracy > `0.5` 且 NLL < `log(2)`；held-out SD 虽 accuracy 为 `0.5351`，但 NLL=`0.698236 > log(2)`。DC-AE 的 accuracy 相对 C0 Full-Seen 下降 `3.37 pp`。

预注册 smoke gate 判定为 **Case B — Seen Sharing Works, Unseen Transfer Degrades**：SD 触发 target NLL 退化条件，DC-AE 触发相对 Full-Seen accuracy drop 条件；FLUX 最接近 seen baseline。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 8.1 C0 的 seen sharing 是否等于 unseen-family transfer？

不等于。C0 的 Shared−Independent macro gap 只有 `-0.34 pp`，说明同一参数可共同读取已见过的三种 VAE；C1 在 leave-one-family-out 后，相对 C0 Full-Seen 的 macro accuracy drop 扩大到 `-1.71 pp`，并出现两个不同形式的 family degradation。问题更接近 unseen-VAE domain generalization / canonicalization，而不是 seen-domain 参数冲突。

### 8.2 是否完全失败？

也不是。三个 target accuracy 都高于 `0.5`，FLUX 与 DC-AE 的 BT-NLL 也低于 `log(2)`，且 retention=`0.58–0.76`。这说明两源规则仍有可迁移的 preliminary signal，但 family pattern 不足以支持 Case A。

### 8.3 Family asymmetry

FLUX 的 held-out accuracy 只比 C0 Full-Seen 低 `0.60 pp`，最稳定；DC-AE 的 accuracy drop 最大；SD 的 accuracy drop 不大，但概率排序的 BT-NLL 超过 chance NLL。Accuracy 与 calibration-sensitive NLL 给出了不同的失败形态，后续设计不能只看 accuracy。

### 8.4 Seal 与监督边界

三份 checkpoint、config/model/input/calibration/sample-count projections 均先冻结并重新验 hash，之后 C1-local authority 才开启一次 test orientations；九个 metric cells 对每个 run 都复用同一 checkpoint SHA，`test_label_open_count=1`。由于相同 preference orientation 同时定义 source 与 target 的任务，source validation 必然知道公共 pair labels；可执行保证是 seal 前不存在 **target latent × Reward label**、target validation metric、target gradient 或 target-dependent model selection，而不是声称目标 label bytes 在物理上不存在。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

C1-Mini 到此停止，不自动执行 strict no-calibration、VAE-ID、Anchor/Relation features、Minimal-U、DG baseline、extra seeds、null、bootstrap、architecture change 或 sweep。若另行立项，优先把 **unseen-VAE DG/canonicalization** 作为新问题独立预注册，并使用新的 confirmatory test authority；不得根据本次 test family pattern 调参或覆盖 sealed result。

## Sources

- [来源快照](../source-snapshots/latentatlas-c1-mini-loo-shared-reader.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-c1-mini-loo-shared-reader.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
