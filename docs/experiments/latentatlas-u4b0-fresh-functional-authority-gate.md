# LatentAtlas U4-B0 Fresh Functional Authority Gate

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

U4-B0 的目标不是评估 Reward transfer，而是回答一个更早的门控问题：能否从公开、历史不重叠、方向完整的 fresh coherence 数据中，封存一套可供后续功能实验消费的 authority。

本次链路为：

```text
Rapidata/svg-benchmark pinned snapshot
→ FRA-SVG0 strict fresh pool
→ U4-B0 label-blind selection + orientation seal
→ B1 sample-sufficiency gate
```

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u4b0-fresh-functional-authority-gate.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- 数据集：`Rapidata/svg-benchmark`
- 固定 revision：`bbb5fde7d01c82bad242fd555a9ed2a2fad38b06`
- 本地 snapshot：80 files，`42,761,735,974` bytes，309,955 physical rows。
- FRA-SVG0 完整分类：
  - retained strict-fresh rows：284
  - missing coherence question：120,141
  - exact ties：4
  - encoded self-pairs：143
  - identical decoded RGB：758
  - conflicting duplicate rows：80,964
  - duplicate nonrepresentative rows：107,665
- 对 G0.1、U4 P4096、U4 H1105 的历史 overlap 在全部登记维度上均为 0。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 FRA-SVG0

- 独立 verifier verdict：`PASS`
- candidate state：`FRA_SVG0_AUTHORITY_CANDIDATE_READY`
- strict pool：284
- historical overlap rows：0
- 禁止访问计数：network、G0.1 forbidden columns、U4 forbidden artifacts、H1105 metrics 全为 0。

### 7.2 U4-B0

- 正式分类：`FRESH_FUNCTIONAL_AUTHORITY_CANDIDATE_SEALED`
- independent verifier：`PASS`
- completed paths：20/20
- authority seal：`b7c1b94ca6b73e235bb3cfcad771c616aea811e42452ff498d429580f688f642`
- inventory：`a40524e33d4630fab916609d5b80c6c3109fece01f80d04bae3137ceda4391d9`
- 14 个登记 overlap dimensions 的 count 全为 0。
- orientation materialization 恰好 1 次；selection、public candidate、historical registry 与 authority builder 也都满足冻结计数。
- GPU、网络、Reward checkpoint、latent/model output、H1105 metric、row-level orientation persistence 等禁止计数全为 0。

### 7.3 U4-B1 preformal gate

- 本机 Apple MPS exact-model smoke：`PASS`
- label-blind provider：284 pairs、568 unique images、284 components。
- runtime evidence：`U4B1_LOCAL_MPS_RUNTIME_EVIDENCE_READY`
- 最终 preformal status：`BLOCKED_INSUFFICIENT_FRESH_AUTHORITY`
- 原因：pair count `284 < 300`；image count `568 >= 300` 已通过。
- B1 formal config、infrastructure binding、formal root 与 private compute root 均未创建。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 8.1 结果证明了什么

1. 已得到一套 revision-bound、方向完整、历史登记维度零重叠的 public fresh functional authority candidate。
2. U4-B0 已把 284 条 eligible rows 的选择、coverage、orientation、provenance 与单次消费边界正式封存。
3. 过去的 `NO_FRESH_CONFIRMATORY_AUTHORITY` 已被推进为“fresh authority 已存在，但当前 B1 样本门槛不足 16 pairs”。

### 8.2 结果不证明什么

- 不证明 frozen Reward Head 在 fresh 数据上有效。
- 不证明 Reward transfer、canonical U、unseen-VAE onboarding 或跨分布泛化。
- 不证明 284 pairs 统计上一定不足；它只是不满足预先冻结的 300-pair B1 门槛。
- B1 的 blocker 是 preformal sample-sufficiency gate，不是模型负结果。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

当时有两条互斥路线：

1. **Confirmatory-first**：新增至少 16 条、最好留有排除余量的独立 fresh eligible pairs，构造新的 union authority，使原 B1 的 300-pair gate 原样通过。
2. **Speed-first diagnostic**：建立独立命名的 `B1-284` exploratory amendment，把 minimum pair count 冻结为 284；结果只能称 development diagnostic，不能冒充原 B1 confirmatory result。

项目随后选择并单独冻结了第 2 条路线。B1-284 已得到 `INDETERMINATE / SOURCE_H_INADEQUATE`，详见 [latentatlas-u4b1-284-exploratory-fresh-functional-specificity](latentatlas-u4b1-284-exploratory-fresh-functional-specificity.md)；该结果没有修改原 B1，也不能把 B0 SEALED 写成 Reward-transfer PASS。

## Sources

- [来源快照](../source-snapshots/latentatlas-u4b0-fresh-functional-authority-gate.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u4b0-fresh-functional-authority-gate.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
