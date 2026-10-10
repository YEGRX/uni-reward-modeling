# LatentAtlas Experiment G0.1 Reward Data Preflight

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在 [latentatlas-reward-data-preflight-g0](latentatlas-reward-data-preflight-g0.md) 因唯一 aggregate/detailed vote mismatch 按原冻结协议 fail-closed 后，用单独版本化、已批准的 G0.1 amendment 重跑完整 CPU-only 门禁。目标是验证：公开真人 pairwise preference 数据能否在明确排除该异常行后，形成可复现、image/prompt-disjoint 且与冻结 Anchor Banks 无重叠的 G1 输入。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-reward-data-preflight-g01.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Dataset: `Rapidata/human-coherence-preferences-images`
- Frozen revision: `72c0ebefc7ef3bebe22643fc709a6e94c22b5b02`
- Official Parquet shards: `53/53`
- Rows: `63,748`
- Unique decoded images: `6,632`
- Unique normalized prompts: `282`
- Task evidence: genuine human two-image coherence preference；公开 card 说明参与者比较两张图，但**未说明标注者是否看到 text prompt**。
- License recorded by the frozen card contract: `cdla-permissive-2.0`

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 Authority result

G0.1 判定 **PASS（仅限数据预检范围）**。八项顶层检查全部为 `pass`：predecessor、schemas、hashes、vote reconciliation、images、split、anchors 和 independent official-Parquet replay。

终端事件为 `complete / run / pass`：

- Pre-terminal events prefix SHA-256: `0567f92f15b94ef8e3b9fe4a7964211055e6377d8364f39b896731447bd48a2f`
- Artifact inventory SHA-256: `1258096302a7da7147d159431b1eb53e8e141d39a1887b6847d7469c6775ef37`
- Terminal seal 写入后的完整 `events.jsonl` SHA-256: `9faaba7f001a2f2690fd172cb0f0193ae01e4a67a45d80d7df03a907dce06f7f`

inventory 中绑定的是写 seal 前的 events prefix，完整文件随后多出 terminal event，因此两个 events hash 不同是协议预期，不是损坏。

### 7.2 Vote reconciliation

| 项目 | 数量 |
|---|---:|
| 审计行 | 63,748 |
| aggregate/detailed 完全一致 | 63,747 |
| mismatch | 1 |
| unknown / ambiguous / malformed | 0 / 0 / 0 |
| fatal opposite-winner mismatch | 0 |
| exact ties | 7,673 |
| 最终 usable non-tie pairs | 56,074 |

唯一 mismatch 仍是 source row `15,579`：aggregate `[26,26]`，detailed `[0,26]`。G0.1 不改写标签，而是按批准协议将该行排除；privacy-safe mismatch ID 为 `e846df34fa6f9b0112be779e51f1f6151ac2811fe0a06bc8adefc041a2dba6eb`。

### 7.3 Image/prompt-disjoint split

| Split | Components | Images | All rows | Usable pairs | Ties | Other exclusion |
|---|---:|---:|---:|---:|---:|---:|
| train | 218 | 5,201 | 50,957 | 44,839 | 6,117 | 1 |
| validation | 32 | 708 | 6,323 | 5,593 | 730 | 0 |
| test | 32 | 723 | 6,468 | 5,642 | 826 | 0 |

Train/validation/test 之间的 image IDs、pair IDs、prompt IDs 和 source-row indices 交集全部为空。总计 `282` 个 image-connected components 被整体分配，避免同一图像通过不同 pair 跨 split 泄漏。

### 7.4 Anchor audit

- Frozen Anchor images: `192`（3 × 64）
- Reward images: `6,632`
- Reward/Anchor overlap: `0`
- Cross-bank decoded Anchor duplicates: `0`
- Status: `pass`

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

G0.1 说明：经过公开、版本化的异常处理修订后，这个 Rapidata 冻结版本可以形成可复现、真人标注、无已检测 split 泄漏且与 Anchor 数据隔离的 pairwise preference 输入。因此，**CPU-side G1 实现、验证和非正式 smoke 可以继续**。

它不说明 Reward Head 有效，也不说明 reward 能跨 VAE transfer。当前没有训练 checkpoint、formal reward metric 或 G1 result；formal G1 GPU execution 仍未开始。

Research gap：需要 G1 才能回答 anchor-relative representation 是否保留 reward-relevant discrimination，以及跨 VAE 的泛化是否超过 raw-latent / image-space 等 baseline。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

1. 继续 G1 的 CPU-side 实现、单元测试、数据加载验证与 non-formal smoke。
2. 在正式 G1 GPU execution 即将开始前，再单独通知用户开 GPU。
3. G1 正式报告需包含 baseline、held-out metrics、VAE family 分层、方向性和失败案例，避免把 data-preflight Pass 写成 reward-sufficiency 证据。

当前下一阶段为 CPU only；不需要租用 GPU 服务器。

## Sources

- [来源快照](../source-snapshots/latentatlas-reward-data-preflight-g01.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-reward-data-preflight-g01.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
