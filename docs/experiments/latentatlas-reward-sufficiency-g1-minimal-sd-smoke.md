# LatentAtlas G1 Minimal SD Reward-Sufficiency Smoke

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在 [latentatlas-reward-data-preflight-g01](latentatlas-reward-data-preflight-g01.md) 已冻结可用数据契约后，为尽快取得一个真实结果，执行最小单 SD-VAE 工程闭环。目标不是检验三 VAE 跨域迁移，而是验证真实 GPU 编码、anchor-relative relation、Reward Head 训练、checkpoint-before-test 的调用/事件顺序、held-out 评价和终端封存能否从头到尾工作。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-reward-sufficiency-g1-minimal-sd-smoke.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Upstream authority: [latentatlas-reward-data-preflight-g01](latentatlas-reward-data-preflight-g01.md) 的权威 G0.1 run。
- G0.1 artifact-inventory SHA-256: `1258096302a7da7147d159431b1eb53e8e141d39a1887b6847d7469c6775ef37`
- G1 input-authority SHA-256: `7a4b08ec587f82f6f844a267af9f0ecb6aee641da91e5ae5acea44f3daf78842`
- Smoke input manifest/archive SHA-256: `4524714684561f83255a4f7147e867f06a9ed0e2b316fefd67c7550292f5587e` / `7a1db7eab994152b515e0542909c5b7ffde5d1e611841f4fb9826931ca27ddd4`
- Pairs: train/validation/test = `256/64/64`，合计 `384`。
- Unique reward images: `713`；frozen Anchors: `64`。
- Test set covers `25` image-connected components。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 Engineering outcome

运行状态为 **PASS（仅限工程闭环）**。事件顺序记录为：start → pair selection → feature-cache seal → checkpoint-then-target evaluation → terminal complete。Checkpoint 成功按 relation-cache hash 重开，完整运行随后通过独立 `audit_completed_run`。

| Metric | Observed value |
|---|---:|
| Source-validation macro BT NLL | `0.679867` |
| Held-out test accuracy | `0.5625` (`36/64`) |
| Held-out test BT NLL | `0.661298` |
| Test margin mean | `0.073384` |
| Test margin population std | `0.183128` |
| Test ROC AUC | `undefined / null` |

Accuracy 的 exact binomial test（null `p=0.5`）为：one-sided `p=0.190866`，two-sided `p=0.381733`；Wilson 95% interval 为 `[44.09%, 67.71%]`。因此 `56.25%` **没有显著高于随机水平**。BT NLL 比零 margin 的 `ln(2)≈0.693147` 低 `0.031850`，同样只作描述性观察。

Validation macro BT NLL 按 epoch 单调下降：`0.691995 → 0.685395 → 0.679867`，第三轮被选中。由于第三轮也是冻结上限，不能声称已经收敛。

ROC AUC 为空不是被隐藏的失败：输入 pair 已统一为 preferred/rejected 顺序，评价标签恒为 `1`，单类别下 ROC AUC 没有定义。Accuracy 和 BT NLL 仍能描述 preferred margin 的方向与大小，但不应与常规双类分类 AUC 混用。

### 7.2 Runtime and sealed identities

- RTX 4090 end-to-end approximately `56 s`；其中 SD latent encoding `36.87 s`。
- PyTorch cache manifest 记录 peak CUDA allocated `3,440,614,400` bytes（约 `3.20 GiB`）；外部约 `4.95 GB` 仅为非精确观测。
- Latent/relation cache SHA-256: `20deae7e...0776df` / `34445c47...a3101c`。
- Checkpoint artifact/model SHA-256: `7829597d...becda` / `c463e9a0...511e1`。
- Run inventory/events-prefix SHA-256: `96ceccdc...2c921` / `b5e23553...40a91`。
- 完整 transport archive: `23,460,403` bytes，SHA-256 `9b5c3435...219c`。
- Production audit: PASS，`0 Critical`。CPU 从 sealed relation cache 与 reopened checkpoint 精确重算，复现 `36/64` accuracy、NLL 与 margin mean/std。
- Train/validation/test 的 pair、image、component overlaps 均为 `0`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

这次最小实验已经回答工程问题：真实 SD-VAE 图像可在冻结输入 authority 下编码为 clean latents；64-anchor global-cosine relation 能被封存和重开；source-train scaler 与 MLP 能训练并用 validation 选择 checkpoint；test-label closure 在 checkpoint 封存/重开之后调用；最终结果、cache 和 checkpoint 能组成可审计的闭环。

但这里的 target isolation 不是 formal 级别：cropped manifest 中的 test-label 字段在训练前已经随文件整体解析进进程内存，只是 closure 到 checkpoint 后才真正取出。这证明了逻辑调用/事件顺序，**不证明 strict physical oracle isolation**，formal G1 不可沿用此数据打开方式。

数值上，64 个 test pairs 的 accuracy 为 `56.25%`，BT NLL 为 `0.6613`，比无信息 margin=0 的 `ln(2)≈0.6931` 略低；但 exact binomial test 不显著，Wilson interval 也包含 `50%`。这只是一项描述性 smoke observation。样本小、只跑一个 seed 和一个 VAE，且 selected epoch 正好等于三轮上限，因此不能据此估计稳定效应、收敛程度、跨 VAE 泛化或 reward transfer。

Research gap：预注册 G1 真正要回答的是跨 VAE target transfer，并要求 SD+FLUX→DC-AE 等 source/target 条件、三类 VAE、多个 seeds、controls、bootstrap 和正式 gate。本 smoke 没有覆盖这些问题。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

1. 将本结果仅作为真实 CUDA/数据/cache/checkpoint/target-isolation 路径的工程证据。
2. 若继续正式路线，先完成并独立审查预注册的 `G1_SMOKE_V1`（SD+FLUX→DC-AE），不得从本结果自动生成 formal permission。
3. Formal G1 必须在训练前将 target labels 置于不可访问的独立物理 authority/handle，不能只依赖 closure 调用顺序。
4. Formal G1 前需重新确认 GPU 启动边界，并执行完整三 VAE、多 seed、baseline/control/bootstrap 条件矩阵。
5. 下一阶段若只做归档、审查和报告则为 CPU only；不需要 GPU。

## Sources

- [来源快照](../source-snapshots/latentatlas-reward-sufficiency-g1-minimal-sd-smoke.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-reward-sufficiency-g1-minimal-sd-smoke.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
