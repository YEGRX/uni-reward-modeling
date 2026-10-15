# LatentAtlas Reward V2 R0/R1：OIP Authority Audit + RGB-Text Oracle

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

本实验只回答：OIP 的 TRAIN→DEV human-preference authority，在拥有完整 RGB 与 prompt 信息时，是否存在超越 generator/prompt shortcuts、依赖正确 image/prompt 配对的可学习信号。

RGB oracle 只是 `task observability ceiling / control`，不是 LatentAtlas 最终方法。最终方法仍冻结为：

```text
z_m -> U_m -> R_shared(U_m, p)
```

本实验不使用历史 H、candidate U、Bridge、旧 U0 Reward Head 或 DCAE mapping，也不编码任何新 VAE latent。

此前 U4-B/H 系列统一保留为 `ARCHIVED_HISTORICAL_DIAGNOSTIC_LINE`，不删除也不改写，但不再是 Reward V2 的科学依赖；拟议的 `U4-B1D1P2` 未执行并标记为 `SUPERSEDED_BY_REWARD_V2`。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-reward-v2-r0r1-oip-authority-oracle.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- OIP split：TRAIN=`4,059`，DEV=`900`，LOCKBOX=`2,500`；按 connected groups 隔离，`group_disjoint=true`。
- DEV：900 pairs，561 groups；统计以 group bootstrap 为单位。
- TRAIN/DEV exact RGB bytes：共读取 `8,118 + 1,800 = 9,918` 张图像。
- Public registry metadata rows：`7,459`。Prompt Parquet 存在 label-blind mixed-row-group physical scan，但没有把 LOCKBOX prompt 行发射、建模或纳入统计。
- LOCKBOX orientation/RGB/model-output/statistics access 全为 `0`；`lockbox_prompt_rows_emitted/modelled/in_statistics=0/0/0`。
- Authority public-pairs SHA-256：`fb390a90b0af132193d032eccfea658557989291d2665ef95295d52259430224`。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

1. Generator prior 不可忽略：overall Accuracy=`0.526667`，且 FLUX/SD 两方向完全分裂为 `0/1`。
2. Prompt-only 是当前最强 shortcut：Accuracy/BT-NLL=`0.553333/0.681495`，但 FLUX-preferred Accuracy 只有 `0.406103`，仍不是方向稳健的完整 authority oracle。
3. 当前只找到 exact historical DINO fallback；它没有语言编码器，prompt 侧只能沿用历史 hashed feature，因此证据强度不足。
4. C2 虽有 Accuracy=`0.536667` 的正点估计，但 NLL upper、双方向与 five-null image-specificity 均失败，不能称已建立 image-specific preference signal。
5. M1 没有超过 prompt-only，也没有超过 C0/C2；correct RGB 与 correct prompt 都未稳定胜过各自 nulls。
6. OIP 当前究竟包含 image-only preference、prompt-conditioned preference，还是主要是 generator/prompt shortcut，使用这个 fallback oracle无法作出可靠裁决。
7. 因此分类必须是 `INCONCLUSIVE_WEAK_ORACLE`。该分类不能淘汰 OIP，也不授权进入 R2 raw/native latent ceilings。
8. 唯一冻结下一步是先获得并冻结一个 proper vision-language backbone，再以同一 R0/R1 合同重新资格审查；不能根据本结果扩大 DINO、改变 gates 或转去扫 latent readers。

### 能说明什么

- 本次正式流程、authority join、TRAIN→DEV、RGB bytes、projection、control、bootstrap、seal 与独立 replay 均操作有效。
- 在精确 DINO+historical-hashed-prompt fallback 下，C2/M1 没有形成可归因的 image/prompt-pairing specificity；prompt-only shortcut 的点估计更强。
- 旧 H/U/Bridge/DCAE 线不是本结论的依赖项。

### 不能说明什么

- 不能说明 OIP 本身没有 image-specific human preference signal；proper VLM oracle 尚未测试。
- 不能把 OIP 定性为已被 prompt/generator shortcut 淘汰；Case E 对 weak fallback 的阴性结果有明确保护。
- 不能说明 native SD/FLUX/DCAE latents 不保留 Reward 信息。
- 不能说明 shared U、cross-VAE Reward Head、Reward transfer、calibration、fresh confirmation 或跨分布泛化成立或失败。
- OIP 仍是 mixed pairwise preference authority，不能把它窄化为纯 aesthetics、纯 coherence 或纯 prompt alignment。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

- 本机和服务器均没有已缓存且可哈希绑定的 compatible VLM，只能采用冻结的 DINO fallback。
- Transformers 5.14 将 ImageNet mean/std 返回为 tuple；实现已用测试驱动方式只规范化 tuple/list 表示，不改变任何数值或预处理语义。
- DINO 没有 text tower，C1/M1 的 prompt 侧仍是 historical hashed features；这正是最终分类必须降级为 `INCONCLUSIVE_WEAK_ORACLE` 的原因。
- OIP 固定包含 FLUX-vs-SD generator confound；C0 与 direction-stratified metrics 证明必须继续保留 generator shortcut control。
- 本实验是 adaptive development-only；DEV 已消费，不能作为 fresh confirmatory authority。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

- `latentatlas`（原wiki关联）
- [latentatlas-u4b1d1-oip-source-reader-restoration](latentatlas-u4b1d1-oip-source-reader-restoration.md)
- [latentatlas-u4b1d1p-oip-prompt-observability](latentatlas-u4b1d1p-oip-prompt-observability.md)
- `multimodal-learning`（原wiki关联）
- `dino`（原wiki关联）
- `clip`（原wiki关联）
- `latent-space`（原wiki关联）
- `variational-autoencoder`（原wiki关联）

## Sources

- [来源快照](../source-snapshots/latentatlas-reward-v2-r0r1-oip-authority-oracle.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-reward-v2-r0r1-oip-authority-oracle.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
