# LatentAtlas FRA0-R Provenance Recovery

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在不覆盖 [latentatlas-fra0-public-fresh-coherence-authority-audit](latentatlas-fra0-public-fresh-coherence-authority-audit.md) 历史封存的前提下，修复 FRA-0 在固定 Hugging Face revision 后形成 metadata 时遇到暂态 `httpx.ConnectError` 就立即终止的问题，并以新的 run root 重做一次完整候选门禁。本阶段只审计公开 fresh human-coherence authority，不训练模型、不编码 latent、不读取 Reward evaluation。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-fra0r-provenance-recovery.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- 历史 G0.1 authority：`LatentAtlas-runs/20260813T004136Z-40a2a17-f84d373a-reward-data-preflight`
- G0.1 本地数据：`owner-home/Documents/LatentAtlas-data/rapidata-human-coherence`
- `Rapidata/Seedream-3_t2i_human_preference`：`a9cd84d2a93e82954fe69bd3097b53c48f51a486`
- `Rapidata/Recraft-v3-24-7-25_t2i_human_preference`：`d7d47aab05cf8fcb5427e278d8817b9dbd65eafb`
- `Rapidata/HunyuanImage-2.1_t2i_human_preference`：`c8a2675e752d9e4c0036f4be4e4d933e07f4c1c6`
- `Rapidata/Flux-2-pro_t2i_human_preference`：`ef2e83f43b41897a8e1a40dd8a5dac209d164c79`

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

- Terminal status：`NO_SUITABLE_PUBLIC_FRESH_COHERENCE_AUTHORITY`。
- 旧 attempt 的 `DATASET_PROVENANCE_FAILURE` 目录与 seal 保持不变；本次 Stage 0 production preflight、Stage 1 candidate revision freeze、Stage 2 metadata semantic audit、Stage 3 old-authority index 与 cross-artifact audit 均为 `SEALED_PASS`，说明先前网络 provenance blocker 已解除。
- 四个候选均被正式分类为 `NEAR_MATCHED_COHERENCE`，但 revision-bound `side_order_evidence.status=UNPROVEN`，理由为 `NO_REVISION_BOUND_SIDE_ORDER_DOCUMENT_REGISTERED`。
- 每个候选的 3 个固定样本均为 `encoding_unresolved_samples=3`、`usable_oriented_samples=0`，因此四个 candidate full audit 均为 `SEALED_REJECTED / AMBIGUOUS_COHERENCE_ORIENTATION`。
- 没有 selected public authority：`selected_public_artifact_sha256=null`；没有 lockbox：`selected_lockbox_sha256={}`。后续 pool/group/lockbox 阶段按 global stop 未运行。
- 候选 payload 均未下载；formal result tree 只有约 4.8 MB，staging 为空。
- Recovery tests：FRA-0 `612 passed`；全仓 `2332 passed in 590.22s`。独立结果重放复算 39 个文件、36 个 inventory members、13 个连续事件与 terminal self-hash，全部通过；提交后 `audit_terminal_run` 再次通过且工作树干净。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

本次结果证明两件事：第一，原 FRA-0 的暂态 metadata 网络失败已被一个保留固定 revision、有限次数且 fail-closed 的恢复路径解决；第二，在当前冻结协议和四个公开候选版本中，没有候选具备可验证的左右侧序/方向权威，因此无法构造 fresh Reward-positive pair authority。

本次结果不证明这些数据集没有有用的 coherence 标签，也不证明其 vote encoding 实际方向错误；它只证明当前注册材料不能把公开 pair 的左右位置可靠映射到“哪张图更少 glitch / Reward 更高”。本次也不产生 canonical U、Reward transfer、unseen-VAE onboarding、fresh holdout 或模型性能结论。

### FRA0-SO public evidence probe（2026-08-24）

- Rapidata SDK 固定 commit `8a9e23be9b3ff2d57b4674eaa94853a29abd99a0` 说明通用 Compare result 的 `winner_index` 中 `0/1` 分别表示第一/第二 option，`votedFor` 是标注者选择的 option，`summedUserScoresRatios` 是可靠度加权比例。
- SDK 当前固定 commit `1611566d04247847c51f1b5fde6cea7e201f69eb` 再次把 `0/1` 定义为 ordered option list 的 first/second asset。
- Rapidata 官方 `svg-benchmark` 固定 commit `bbb5fde7d01c82bad242fd555a9ed2a2fad38b06` 明确：`weighted_results_image{1,2}_coherence` 是选择对应图片的 trust-weighted raw vote share；数值越高表示被判断为 glitches 更多、coherence 更差，并称该存储方式与其他 Rapidata preference datasets 一致。
- 这些材料形成一致的第一方通用语义，但仍没有将四个目标 revision 的 exporter 明确绑定为 `option 0/1 → image1/image2`，也没有公开其 Parquet exporter commit。故正式 side-order gate 继续为 `UNPROVEN`；只能把现有映射记为非正式 operational hypothesis，不能据此开启 fresh U4-B0。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

- U4-B0 仍不能启动，因为 frozen Reward Head 所需的 fresh functional authority 与 lockbox 尚未形成。
- 下一步只应做 bounded side-order authority acquisition：取得并冻结可绑定到上述具体 revision 的官方 schema/dataset-generation code/document，或由用户提供新的、来源可核验且 image/prompt-disjoint 的本地候选 authority。
- 最小第一方确认需明确四项：`image1/image2` 与原始 option 0/1 的映射、UI 随机换边后 exporter 是否恢复原始顺序、`votedFor` 文件标识到图片列的映射、生成四个固定 revision 所用 exporter/code identity。
- 未取得新证据前，不以相同四候选原样重跑，不下载 26–35 GB payload，不猜测 orientation，也不启动 Reward、latent 或 GPU 实验。

## Sources

- [来源快照](../source-snapshots/latentatlas-fra0r-provenance-recovery.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-fra0r-provenance-recovery.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
