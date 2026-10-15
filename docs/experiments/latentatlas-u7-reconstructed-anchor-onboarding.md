# U7 True-Unseen Reconstructed-Anchor Onboarding

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

检验两件严格分离的事情：

1. 仅用 `RECONSTRUCTED_ANCHOR` 证据，能否为真正未见 target VAE 建立稳定 canonical-U registration；
2. registration 成立后，显式 U 能否在 fresh human-preference authority 上产生可归因 Reward-readable onboarding signal。

本实验承接 [rpj3-anchor-reward-instance-specificity-localization](rpj3-anchor-reward-instance-specificity-localization.md)，但使用全新的 fresh dataset split；它不读取或重放 RRV1 official TEST。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u7-reconstructed-anchor-onboarding.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Fresh preference rows：20,818。
- `SOURCE_DEV=5,202`，`LOCKBOX=15,616`。
- Unique images：62,421。
- 数据与 RPJ4 共享同一个 pinned Hugging Face snapshot 和 image spool；U7 使用 verified hardlinks，没有创建第二份约 22 GB RGB 数据。
- Fresh visual、authoritative text、visual-score、text-score caches 均先 label-blind materialize 和 seal，再进入 authority。
- Reconstructed training anchors：128 张；证据类固定为 `RECONSTRUCTED_ANCHOR`，不冒充 original HPDv3 RGB anchors。

Authority ledger：

- target Reward label access during registration：`0`
- fresh SOURCE_DEV orientation：`1`
- fresh LOCKBOX orientation：`0`
- old official TEST：`0`

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 Registration：PASS

- `18/18` fits 完成 12,000 updates。
- `18/18` optimization adequate。
- `18/18` selected reload PASS。
- Runtime=`1,664.2225 s`。
- Classification=`TRUE_UNSEEN_CANONICAL_U_REGISTRATION_ESTABLISHED`。
- Correct retrieval R1（三 seed）=`0.890625 / 0.812500 / 0.875000`；permutation 接近 0。
- Training registry SHA256=`20c42bec653b4d8918e581de69cee2702e8c1d2d92d8d52a62ede79aea2cc4f3`。
- Qualification SHA256=`95155041554a41b97480ba89122f5723b48aa681071ce95d76bb2ead20665cef`。

### 7.2 Fresh SOURCE_DEV：FAIL-CLOSED

Terminal source status：`FRESH_AUTHORITY_SOURCE_U_REWARD_UNQUALIFIED`。

| Seed | Accuracy | BT-NLL | Readability | PAIR_RO | GLOBAL_SD | Wrong Prompt | Direction | Noncollapse |
|---|---:|---:|---|---|---|---|---|---|
| 20260827 | 0.508993 | 0.702276 | FAIL | FAIL | FAIL | FAIL | PASS | PASS |
| 20260828 | 0.509460 | 0.706396 | FAIL | FAIL | FAIL | FAIL | PASS | PASS |
| 20260829 | 0.518103 | 0.700264 | FAIL | FAIL | FAIL | FAIL | PASS | PASS |

`three_seed_robustness=false`。输出非塌缩、方向正确，但主读取门和 image/prompt-specific attribution controls 没有联合通过。

### 7.3 Frozen answers

- Q1 registration：在 reconstructed-anchor claim ceiling 下成立。
- Q2 explicit-U onboarding value：`EXPLICIT_U_ONBOARDING_VALUE_INDETERMINATE`。
- LOCKBOX：未授权、未打开。
- Completed U7 classification：未产生；不能从 source failure 推断 lockbox outcome。

### 7.4 Source-stage terminal verification

- Remote/local source tree：112 files、63,311,719 bytes，tree SHA256=`56479e1fa9eba1c41da790e8843419cf04afba68507e1cd0a79e47a8883338a4`。
- Local visual / visual-score / text-score / authoritative-text disk-only replay：全部 `PASS`，model forwards=`0`。
- Evidence inventory：22 records，SHA256=`b854476dd03012bf25b4f27461c2e8b460cd2ced0d573c0d6f49e8939d261c60`。
- Source-stage evidence seal SHA256=`3ec9d4df51c084d1f0cc8afa09550e9f6eda4b5ce1fd8c415e0486f8571d2f7c`。
- Local verification receipt=`PASS`，SHA256=`f0a32149c29272c28e46eaabd29028ecdba79be1923fdb9c158bcd0b7f4d6269`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

U7 最重要的结果是把“几何 registration”与“Reward-readable onboarding”分开：前者可以在 reconstructed anchors 上稳定成立，后者在 fresh source authority 上没有通过。也就是说，retrieval/cosine/MSE 对齐不是 Reward compatibility 的充分条件。

该结果不能被描述为完整 U7 terminal classification，因为 protocol 合法地阻止了 LOCKBOX。正式 `finalize_u7.py` / `verify_u7.py` 要求 source 与 lockbox 都各消费一次；在 source failure 后运行它们会违反冻结 authority contract。因此本实验发布 source-stage fail-closed evidence seal，并对所有已产生 caches 做 disk-only replay。

## Possible Conflict / 待确认冲突

2026-09-06 [latentatlas-rgen1-reward-external-generalization](latentatlas-rgen1-reward-external-generalization.md) 对同一数据集做跨实验无标签身份审计：U7 SOURCE_DEV=5,202，RPJ4 SOURCE_DEV=4,164，交集=1,003；U7 LOCKBOX 的 15,616 行中有 3,161 行曾作为 RPJ4 SOURCE_DEV 被消费。因此本页 historical `LOCKBOX orientation=0` 只适用于 U7 自己的 split/access ledger，不能解释为跨 RPJ4/U7 的全局 untouched。原报告、模型与结果保持封存。RGEN1最初在冻结前暂停，随后按用户批准amendment重新定义authority并完成：测试路线BROAD FAIL、fresh native固定协议FAIL、RGB两面PASS；最终定位和限制见[latentatlas-rgen1-reward-external-generalization](latentatlas-rgen1-reward-external-generalization.md)。Future reserve 12,455行方向访问仍为0。

Source: 本页 §11 原 U7 source-stage report 与 `raw/experiments/latentatlas/rgen1-preflight-2026-09-06/input_read_ledger.json` 绑定的双方 split/identity/access receipts；重算结果见 `raw/experiments/latentatlas/rgen1-preflight-2026-09-06/authority_identity_audit.json`。

追加 Source: `raw/experiments/latentatlas/rgen1-final-2026-09-06/RGEN1_FINAL_REPORT.md`、`result_seal.json`；批准范围修订见`raw/experiments/latentatlas/rgen1-authority-freeze-2026-09-06/approved-authority-amendment.txt`。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

冻结本次 source-stage negative result，不在已消费 SOURCE_DEV 上调模型、阈值或挑 seed。下一实验应新建独立 identity，在新的 TRAIN/DEV-only surface 上定位“registration 成立但 Reward attribution 失败”的机制，例如 prompt-conditioning interface、Reward objective 或 representation-to-score coupling；只有重新冻结后才能申请新的 fresh authority。

## Sources

- [来源快照](../source-snapshots/latentatlas-u7-reconstructed-anchor-onboarding.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u7-reconstructed-anchor-onboarding.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
