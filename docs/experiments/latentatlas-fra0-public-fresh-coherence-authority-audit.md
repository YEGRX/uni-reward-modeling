# LatentAtlas FRA-0 Public Fresh Human-Coherence Authority Audit — 完整实验报告

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

### 2.1 研究背景

LatentAtlas 的 U4-A 系列已经在历史 development cohort 上得到 reward-free 的 correct-pairing specificity 信号，但它不能回答 frozen Reward Head 在 fresh human-coherence authority 上是否仍具有功能特异性。既有 [latentatlas-c1r-fresh-authority-audit](latentatlas-c1r-fresh-authority-audit.md) 又证明，G0.1 当前快照的全部 56,074 个有有效方向的 pair 已被历史实验消费，无法再充当新的 confirmatory authority。

因此，FRA-0 的任务不是训练或评价模型，而是先回答一个权限问题：公开数据中是否存在一套来源可复现、标签语义匹配、方向可证明、与 G0.1 图像和 prompt 隔离，并可冻结为 A1/A2/A3 三个 lockbox 的 fresh human-coherence authority。

### 2.2 核心研究问题

对四个预先固定的 Rapidata 候选，依次判断：

1. 能否把数据卡、schema、全部 official Parquet inventory 和固定语义样本绑定到 immutable 40-hex revision？
2. 标注问题是否属于 `MATCHED_COHERENCE` 或 `NEAR_MATCHED_COHERENCE`？
3. `image1/image2`、原始 option 顺序和 vote encoding 的关系是否有 revision-bound 证据，从而能安全推导 Reward-positive 方向？
4. 通过方向门后，是否能证明与 G0.1 无 exact image overlap、无 pHash≤4 near duplicate，并构造 prompt-disjoint pool？
5. 通过 hygiene 后，确定性分组和哈希分配能否满足 A1/A2/A3 的最小 pair/image 数？

### 2.3 冻结终态

FRA-0 只允许三种 global terminal status：

| 终态 | 精确含义 |
|---|---|
| `FRESH_AUTHORITY_READY` | 至少一个候选完成全源审计并形成可验证的 selected pool、authority groups 和 A1/A2/A3 lockboxes。 |
| `NO_SUITABLE_PUBLIC_FRESH_COHERENCE_AUTHORITY` | 所有固定候选都获得结论性结果，但没有候选通过全部 eligibility/engineering gates。 |
| `DATASET_PROVENANCE_FAILURE` | 至少一个仍可能合格的候选因来源、下载、schema 或全源处理不完整而无法下结论；缺失证据不能被伪装成科学 rejection。 |

### 2.4 范围与禁止事项

FRA-0 仅允许 CPU、网络、本地存储、hashing、strict JSON、Pillow、PyArrow 和 pHash 等 authority infrastructure。生产入口禁止触达 VAE、latent encoding、Torch training、Reward Reader/checkpoint、C0/C1/C2/G/O/U 系列 evaluation 或任何 model-performance metric。

所以，本实验无论得到哪一种 terminal status，都不直接评价 shared latent structure、candidate `U`、Reward transfer 或 unseen-VAE onboarding。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-fra0-public-fresh-coherence-authority-audit.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

### 4.1 历史 G0.1 authority

- 数据集：`Rapidata/human-coherence-preferences-images`
- Revision：`72c0ebefc7ef3bebe22643fc709a6e94c22b5b02`
- Source split：`train`
- Official shards：53
- Source rows：63,748
- Usable oriented pairs：56,074
- Ties：7,673
- Aggregate/detailed mismatch：1
- Unique images：6,632
- Sealed run：`LatentAtlas-runs/20260813T004136Z-40a2a17-f84d373a-reward-data-preflight`
- 本地 Parquet：`owner-home/Documents/LatentAtlas-data/rapidata-human-coherence`

G0.1 在本实验中只作为历史 authority 与 overlap baseline，不被修改，也不重新训练任何模型。

### 4.2 四个固定公开候选

下表中的 rows、shards 与 bytes 是 FRA0-R 在 metadata barrier 冻结的 repository-level 快照，不是完成 full payload audit 后的 usable pair 数。

| 顺序 | Candidate | Immutable revision | Metadata rows | Shards | Download bytes | License |
|---:|---|---|---:|---:|---:|---|
| 1 | `Rapidata/Seedream-3_t2i_human_preference` | `a9cd84d2a93e82954fe69bd3097b53c48f51a486` | 60,030 | 101 | 26,668,535,842 | `cdla-permissive-2.0` |
| 2 | `Rapidata/Recraft-v3-24-7-25_t2i_human_preference` | `d7d47aab05cf8fcb5427e278d8817b9dbd65eafb` | 65,931 | 122 | 30,707,148,812 | `cdla-permissive-2.0` |
| 3 | `Rapidata/HunyuanImage-2.1_t2i_human_preference` | `c8a2675e752d9e4c0036f4be4e4d933e07f4c1c6` | 44,848 | 91 | 35,283,001,534 | `cdla-permissive-2.0` |
| 4 | `Rapidata/Flux-2-pro_t2i_human_preference` | `ef2e83f43b41897a8e1a40dd8a5dac209d164c79` | 44,857 | 69 | 28,906,555,375 | `cdla-permissive-2.0` |

四个候选合计登记 215,666 metadata rows 和约 121.6 GB encoded payload。由于 recovery 在 pre-payload orientation gate 得到结论性 rejection，这些大 payload 没有被下载。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 首次正式运行：metadata provenance fail-closed

首次运行 terminal status：`DATASET_PROVENANCE_FAILURE`。

| Sequence | Stage | Status | 解释 |
|---:|---|---|---|
| 0 | `production_preflight` | `SEALED_PASS` | 生产 commit、config、环境与入口边界通过。 |
| 1 | `candidate_revision_freeze` | `SEALED_INCOMPLETE` | 前三候选完整 resolved；Flux 取得 revision 后 metadata contract 未完成。 |
| 2 | `metadata_semantic_audit` | `NOT_RUN_GLOBAL_STOP` | 四候选共同 barrier 未通过。 |
| 3 | `old_authority_index` | `NOT_RUN_GLOBAL_STOP` | 未重放 G0.1 index。 |
| 4–7 | 四个 `candidate_full_audit` | `NOT_RUN_GLOBAL_STOP` | 无候选进入 full payload。 |
| 8 | `selected_pool_freeze` | `NOT_RUN_GLOBAL_STOP` | 无 selected pool。 |
| 9 | `authority_group_freeze` | `NOT_RUN_GLOBAL_STOP` | 无 authority groups。 |
| 10 | `lockbox_orientation_seal` | `NOT_RUN_GLOBAL_STOP` | 无 lockboxes。 |
| 11 | `cross_artifact_audit` | `SEALED_PASS` | 状态、文件树与交叉引用自洽。 |
| 12 | `terminal_seal` | `SEALED_PASS` | 失败结果本身被完整封存。 |

Flux-2-pro 已取得 revision `ef2e83f43b41897a8e1a40dd8a5dac209d164c79`，但在读取 `data/train-00009-of-00069.parquet` 的 metadata 时出现 Hugging Face DNS/SSL/connect failure。执行控制台观察到重试耗尽；sealed manifest 的最小公开 failure projection 只保留：

- `resolution_status=METADATA_FAILED`
- `failure_reason=METADATA_CONTRACT_FAILED`
- `evidence_projection={"error_class":"ConnectError"}`
- failure evidence SHA-256：`ac1ed78df272675c957e5dbf6ae84d6ed56d47004f13d0248f87901c5b395038`

因此，本次 `NA` 表示未运行，而不是 0：rows、usable pairs、exact/near overlap、POOL_A/B/C、prompt overlap、authority groups 与 lockboxes 都没有正式结果。前三个候选也不能因 Flux 的操作性失败而被称为通过或拒绝。

### 7.2 FRA0-R：排除网络因素后的候选结论

FRA0-R terminal status：`NO_SUITABLE_PUBLIC_FRESH_COHERENCE_AUTHORITY`。

| Sequence | Stage | Status | 解释 |
|---:|---|---|---|
| 0 | `production_preflight` | `SEALED_PASS` | Recovery production 与权限边界通过。 |
| 1 | `candidate_revision_freeze` | `SEALED_PASS` | 四个 immutable revisions、cards、inventories、footers 与固定样本全部冻结。 |
| 2 | `metadata_semantic_audit` | `SEALED_PASS` | 四候选均识别为 near-matched coherence；统一方向合同已登记。 |
| 3 | `old_authority_index` | `SEALED_PASS` | G0.1 snapshot/index 完整重放。 |
| 4–7 | 四个 `candidate_full_audit` | `SEALED_REJECTED` | 均在 pre-payload orientation eligibility gate 结论性拒绝。 |
| 8 | `selected_pool_freeze` | `NOT_RUN_GLOBAL_STOP` | 无候选可进入 pool。 |
| 9 | `authority_group_freeze` | `NOT_RUN_GLOBAL_STOP` | 无 selected pool，故无 groups。 |
| 10 | `lockbox_orientation_seal` | `NOT_RUN_GLOBAL_STOP` | 无 authority lockboxes。 |
| 11 | `cross_artifact_audit` | `SEALED_PASS` | 结果树、事件链和选择缺失状态自洽。 |
| 12 | `terminal_seal` | `SEALED_PASS` | 结论性无合格候选结果被完整封存。 |

### 7.3 四候选结果矩阵

| Candidate | Semantic compatibility | Side-order evidence | Fixed samples | Usable oriented | Candidate status | Failure reason |
|---|---|---|---:|---:|---|---|
| Seedream-3 | `NEAR_MATCHED_COHERENCE` | `UNPROVEN` | 3/3 encoding unresolved | 0 | `REJECTED_CONCLUSIVE` | `AMBIGUOUS_COHERENCE_ORIENTATION` |
| Recraft-v3 | `NEAR_MATCHED_COHERENCE` | `UNPROVEN` | 3/3 encoding unresolved | 0 | `REJECTED_CONCLUSIVE` | `AMBIGUOUS_COHERENCE_ORIENTATION` |
| HunyuanImage-2.1 | `NEAR_MATCHED_COHERENCE` | `UNPROVEN` | 3/3 encoding unresolved | 0 | `REJECTED_CONCLUSIVE` | `AMBIGUOUS_COHERENCE_ORIENTATION` |
| Flux-2-pro | `NEAR_MATCHED_COHERENCE` | `UNPROVEN` | 3/3 encoding unresolved | 0 | `REJECTED_CONCLUSIVE` | `AMBIGUOUS_COHERENCE_ORIENTATION` |

四项 `side_order_evidence.rationale` 均为 `NO_REVISION_BOUND_SIDE_ORDER_DOCUMENT_REGISTERED`。这不是说数据卡没有说明 coherence 极性；数据卡已经说明问题选择“更多 glitches”的图片。真正缺失的是：对这四个具体 dataset revision，尚无被冻结的官方材料把 exporter 中的 op

（其余历史细节见来源快照。）

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 8.1 结果证明了什么

1. FRA-0 production pipeline 能够在公开来源证明不完整时 fail closed，并把缺失证据保持为 `NA`，而不是伪造成候选 rejection。
2. Recovery 证明首次 blocker 是暂态 metadata network/provenance 问题，而不是 Flux dataset 内容已被判定不合格。
3. 在相同 immutable revisions 和相同科学协议下，四个候选都具有 near-matched coherence 语义，但都缺少足以推导 Reward orientation 的 revision-bound side-order authority。
4. 因四个候选均在 eligibility 层获得结论性拒绝，global `NO_SUITABLE_PUBLIC_FRESH_COHERENCE_AUTHORITY` 在该冻结四候选合同下成立。
5. Authority system 的 capability isolation、事件链、条件文件树、terminal seal 和无 selected-authority 状态均可独立重放。

### 8.2 结果没有证明什么

本实验不证明：

- 四个 Rapidata 数据集没有有用的 coherence labels；
- 它们的真实 option/image mapping 错误；
- 所有公开数据都不可能形成 fresh authority；
- exact/near image overlap 或 prompt overlap 的数量为零；
- pool/lockbox 一定太小；
- Anchor、Bridge、candidate `H/U`、canonical U 或 shared latent structure 不成立；
- frozen Reward Head 不能 transfer；
- unseen-VAE onboarding 或 cross-distribution generalization 失败。

这里唯一被否定的是：**在冻结的四个候选 revisions 与当时已注册的公开证据下，无法合法地把 pair vote 转成 LatentAtlas Reward-positive orientation，因此不能构造 FRA-0 authority。**

### 8.3 为什么不能“根据字段名猜方向”

如果把 `weighted_results_image1_coherence` 直接解释为 image1 的原始 option vote，需要额外假设 exporter 保持了 option order、UI 换边后恢复原序、`votedFor` 与文件列映射稳定，以及四个 revisions 使用同一生成代码。任一假设错误都会系统性翻转部分或全部 Reward labels。

FRA-0 的作用正是阻止这类来源不明的标签进入后续 confirmatory experiment。方向证据缺失是 authority blocker，不是一个可以靠肉眼 spot-check 或多数统计修复的普通数据清洗问题。

### 8.4 与项目后续进展的关系

FRA0-R 是 2026-08-24 对这四个特定候选的历史结论。2026-08-25，项目通过不同来源与不同冻结协议完成 [latentatlas-u4b0-fresh-functional-authority-gate](latentatlas-u4b0-fresh-functional-authority-gate.md)：`Rapidata/svg-benchmark` 固定 revision 最终形成 284-pair/568-image fresh authority，U4-B0 独立 verifier=`PASS`。

这项后续进展说明“公开 fresh authority 不可能获得”从来不是 FRA-0 的结论；它也不回写或推翻 FRA-0。两者可以同时成立：

- FRA-0：原四个 t2i candidates 缺少 revision-bound side-order 证据，不能授权。
- FRA-SVG0/U4-B0：另一条具有完整方向合同的公开数据路线已经成功封存 fresh authority。

当前最新研究阻点已从“有没有 fresh authority”推进到“exact frozen head/reference 在 fresh H 上是否 adequate”，而不是继续重复 FRA-0 的四候选审计。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

### 10.1 对 FRA-0 历史路线的停止规则

- 不修改两个 sealed result tree。
- 不在没有新 revision-bound side-order authority 的情况下原样重跑四个候选。
- 不猜测 orientation，不依据字段名或样本外观补标签。
- 若未来必须重启该路线，只接受能够绑定到具体 revision 的官方 exporter code/schema/document，并使用新的 run identity。

### 10.2 当前项目行动

FRA-SVG0/U4-B0 已通过另一条路线形成 fresh authority，因此当前无需继续修复 FRA-0。后续研究应遵循 [latentatlas-u4b1-284-exploratory-fresh-functional-specificity](latentatlas-u4b1-284-exploratory-fresh-functional-specificity.md) 的边界，优先定位 frozen head/reference adequacy；任何最终 fresh confirmation 仍需新的未消费 authority，不能重复使用已经消费的 284 pairs。

### 10.3 资源状态

本报告与 FRA-0/FRA0-R 复验均为本地 CPU-only 文档和 hash 工作，不需要 GPU。当前无法核实是否有租用 GPU 服务器仍在运行；若有，可关闭。

## Sources

- [来源快照](../source-snapshots/latentatlas-fra0-public-fresh-coherence-authority-audit.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-fra0-public-fresh-coherence-authority-audit.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
