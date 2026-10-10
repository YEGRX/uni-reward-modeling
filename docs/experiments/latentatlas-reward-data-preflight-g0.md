# LatentAtlas Experiment G0 Reward Data Preflight

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在任何 Reward Head 或跨 VAE reward transfer 训练前，对公开真人图像偏好数据执行 CPU-only、fail-closed 的数据预检。核心问题是：数据来源、真人标签、图像字节、去重、image/prompt-disjoint split 和冻结 Anchor Banks 是否足以支持后续 `latentatlas`（原wiki关联） Experiment G1。

本阶段只审计数据，不检验 reward sufficiency，也不产生训练结果。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-reward-data-preflight-g0.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Dataset: `Rapidata/human-coherence-preferences-images`
- Frozen revision: `72c0ebefc7ef3bebe22643fc709a6e94c22b5b02`
- 53/53 Parquet shards
- 17,836,409,651 compressed bytes
- 63,748 pair rows
- Official task: two-image human preference for visual coherence, naturalness, and fewer visible generation glitches
- Prompt visibility in the annotation interface remains uncertain

下载后逐分片验证了官方 LFS SHA-256。非正式 sample 覆盖 53/53 shards、每 shard 128 行，共 6,784 行，所有 sample schema/image/coverage checks 通过。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### Formal gate

| Field | Result |
| --- | --- |
| Status | **Fail** |
| Failed stage | `rows` |
| Source row | `15,579` |
| Shard / local row | `train-00012-of-00053.parquet` / `1,143` |
| Aggregate counts | `(26, 26)` |
| Detailed counts | `(0, 26)` |
| Error | `formal detailed vote count mismatch with aggregate votes` |
| G1 decision | **May not begin** |
| Elapsed before fail | 约 20 秒 |

该行的 26 个 detailed votes 全部唯一映射到 image 2，而 aggregate columns 把它记录为 26/26 tie。

### Full-dataset read-only semantics audit

| Check | Result |
| --- | ---: |
| Rows parsed | 63,748 |
| Individual detailed votes | 1,144,093 |
| Aggregate/detailed exact agreement | 63,747 |
| Mismatch rows | **1** |
| Unknown/ambiguous vote target | 0 |
| Repeated ordered/unordered pair | 0 |
| Unique image paths | 6,632 |

这说明失败不是普遍字段误解，而是冻结 revision 中唯一一条可定位的数据不一致。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 这个 Fail 说明什么

G0 证明了当前冻结数据版本不能在既定的零容忍数据完整性协议下直接授权 G1。Fail 是审计系统正常工作：它阻止一条 aggregate 与逐票记录冲突的样本静默进入训练和评估。

### 这个 Fail 不说明什么

- 不说明 anchor-relative representation 没有 reward information。
- 不说明 Reward Head 训练失败，因为训练根本没有开始。
- 不说明跨 VAE reward transfer 不可行。
- 不说明整个 Rapidata 数据集不可用；63,747/63,748 行在该 invariant 上一致。
- 不允许把唯一异常静默删除后继续，因为那会违反冻结 protocol。

### 标签语义证据

官方 pinned card 明确数据是 human coherence votes，但未精确定义 aggregate columns 与 `detailed_results` 的内部路径别名。对官方 artifact 的全量只读审计显示：除唯一异常外，aggregate left/right counts 与逐票 left/right counts 完全一致；所有逐票目标都能唯一映射到 pair 两侧。因此最可信解释是 pair-local vote counts，而不是 image-global score/rank。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

当前必须先与导师/用户确认新的数据裁决，不能直接启动 G1。可讨论的三个选项：

1. **保持冻结 Fail**：把 G0 作为数据质量发现，暂不继续 G1。
2. **修订 protocol 后排除唯一异常行**：预先公开 row 15,579 的排除规则，重新版本化设计和配置，再从头运行 G0。
3. **修订 label source 为 detailed votes**：所有 63,748 行都从逐票记录重算左右 counts，aggregate 只做交叉检查；唯一冲突仍必须显式标记/排除或采用预先批准的优先级规则。

选项 2/3 都是新的实验协议，需要新的设计审查和明确批准，不能作为本次 Fail 的“修复后续跑”。

若决定重跑，推荐优先讨论选项 2：制定与具体赢家无关的通用 QC 规则，排除所有 aggregate/detailed mismatch，并把排除数、source index、artifact hash 写入正式产物。这比整体更换标签来源改动更小；但它仍然改变了此前“任一不一致即全局 Fail”的冻结裁决。

## Sources

- [来源快照](../source-snapshots/latentatlas-reward-data-preflight-g0.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-reward-data-preflight-g0.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
