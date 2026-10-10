# RPJ4 True-Unseen SD3.5 Reconstructed-Anchor Confirmation

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

检验一个 operationally unseen 的 SD3.5 VAE，能否在 shared Reward、source checkpoints 与 target protocol 全部冻结、target preference labels=`0` 的条件下，仅用 same-image reconstructed anchors 建立 reward-free interface；随后按 `SOURCE_DEV → LOCKBOX` 的顺序，确认该 interface 是否保留 instance-specific Reward behavior。

本实验的最高证据等级固定为 `TRUE_UNSEEN_ONBOARDING_ON_RECONSTRUCTED_ANCHORS`。它不使用 original HPDv3 RGB anchors，也不能描述为 pristine RPJ4 或 universal VAE confirmation。

## Config

[历史配置摘要](../../configs/experiments/rpj4-true-unseen-sd35-anchor-confirmation.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Target VAE：`stabilityai/stable-diffusion-3.5-medium`，只使用 VAE。
- Fresh authority：`datapointai/text-2-image-dpo-human-preferences-full` 的 pinned snapshot。
- Fresh rows：20,818；SOURCE_DEV 选中 4,164 rows，其中 3,429 个有向 non-ties，735 ties 排除。
- Reconstructed anchors：128 张；由冻结 DCAE latent 经冻结 decoder 重建为 clamped FP16 RGB，再由 SD、FLUX、DCAE 与 SD3.5 对同一像素重新编码。
- Source latent/text caches、reconstructed-target cache 与 fresh-source cache 均在 authority 前封存，并通过 disk-only verifier。

Authority ledger：

- target training Reward-label access：`0`
- target training preference orientation access：`0`
- fresh SOURCE_DEV orientation access：`1`
- fresh LOCKBOX orientation access：`0`
- old official TEST access：`0`

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 Target interface：PASS

- 18×12,000 target fits 全部完成；18 receipts、18 selected checkpoints、0 interim checkpoints。
- Target training registry SHA256=`23f1f2b1225b9900fa1177e1ccdda207f10be581aec21b7dd7a276bd12990472`。
- Interface metrics SHA256=`c595324440e2450f4baae236a0ac920cb5cd83a07999a17bf27c65af97591817`，artifact status=`PASS`。

| Seed | Correct MSE | Permutation MSE macro | Correct R@1 | Permutation R@1 macro |
|---:|---:|---:|---:|---:|
| 20260827 | 0.00394252 | 0.01166841 | 1.000000 | 0.015625 |
| 20260828 | 0.00403790 | 0.01168367 | 1.000000 | 0.012500 |
| 20260829 | 0.00403065 | 0.01214970 | 1.000000 | 0.009375 |

这证明 frozen reconstructed-anchor interface 在该几何指标上可建立；它本身不证明 Reward compatibility。

### 7.2 Fresh SOURCE_DEV：FAIL-CLOSED

Terminal source status：`FRESH_AUTHORITY_SOURCE_REWARD_UNQUALIFIED`。

| Seed | Teacher | Accuracy | BT-NLL | Seed consistency |
|---:|---|---:|---:|---|
| 20260827 | dcae | 0.486439 | 0.724506 | FAIL |
| 20260828 | dcae | 0.504229 | 0.707090 | FAIL |
| 20260829 | dcae | 0.498104 | 0.716970 | FAIL |

- Aggregate Accuracy=`0.487022`，BT-NLL=`0.711464`。
- Accuracy-above-chance=`-0.012978 [-0.026945, 0.001312]`。
- NLL advantage over chance=`-0.018317 [-0.023339, -0.013330]`。
- Better-than-chance、`PAIR_RO`、`GLOBAL_SD`、wrong-prompt、direction-balance gates 均未通过；seed robustness=`0/3`。
- `fresh_source_qualification.json` SHA256=`ac86b56dee2660c10f58bf259cfdb90b0304ecfd2a30fa686a02e725cd1b349e`。

### 7.3 Frozen decision and verification

- Executive answer=`INDETERMINATE`。
- Final classification=`FRESH_AUTHORITY_SOURCE_REWARD_UNQUALIFIED`。
- Recommendation=`STOP_WITHOUT_OPENING_FRESH_LOCKBOX`。
- Decision SHA256=`032903ccf0951ee7d5efaec07b585f117b52ead85d6700cf579315af01a3aa26`。
- Scientific disk-only verifier=`PASS`；network/model-forward/training/old TEST 均为 `0`。
- Result seal SHA256=`c7cfa3443ba96d0d4f619cbfb2c2eac08a26781bd90e3628adb11dfa6073cd69`。
- Completed replay=`PASS`：64,603 files、42,933,254,755 bytes，model-forward/training/network/old TEST=`0/0/0/0`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

RPJ4 的关键结果是：reconstructed-anchor interface geometry 成立，但 frozen source Reward 在真正 fresh SOURCE_DEV 上不合格。由于 source control 是进入 LOCKBOX 的前置必要条件，target Reward readability、Anchor-vs-NoReg、Anchor-vs-permutations、Reward retention 以及 fresh LOCKBOX 的所有结论都保持 `NOT_EVALUATED`。

因此不能把结果解释为“SD3.5 onboarding Reward 失败”，也不能从几何 registration 成功推断 Reward-compatible onboarding 成功。当前唯一合法结论是：确认性问题在 source-control gate 处变为 `INDETERMINATE`。

## Possible Conflict / 待确认冲突

2026-09-06 [latentatlas-rgen1-reward-external-generalization](latentatlas-rgen1-reward-external-generalization.md) 核对出 RPJ4 与 U7 并非同一 SOURCE_DEV：本实验为 4,164 行，U7 为 5,202 行，交集仅 1,003 行。本页 source Acc/NLL 不能作为 U7 5,202 行上的 exact replay 目标。RPJ4 SOURCE_DEV 中有 3,161 行落在 U7 LOCKBOX，U7 SOURCE_DEV 中有 4,199 行落在 RPJ4 LOCKBOX；两次各自 LOCKBOX=0 的历史凭据不支持全局 untouched 声明。原报告、模型与结果保持封存。RGEN1最初在冻结前暂停，随后按用户批准amendment重新定义authority并完成：测试路线BROAD FAIL、fresh native固定协议FAIL、RGB两面PASS；最终定位和限制见[latentatlas-rgen1-reward-external-generalization](latentatlas-rgen1-reward-external-generalization.md)。Future reserve 12,455行方向访问仍为0。

Source: 本页 §11 原 RPJ4 report 与 `raw/experiments/latentatlas/rgen1-preflight-2026-09-06/input_read_ledger.json` 绑定的双方 split/identity/access receipts；重算结果见 `raw/experiments/latentatlas/rgen1-preflight-2026-09-06/authority_identity_audit.json`。

追加 Source: `raw/experiments/latentatlas/rgen1-final-2026-09-06/RGEN1_FINAL_REPORT.md`、`result_seal.json`；批准范围修订见`raw/experiments/latentatlas/rgen1-authority-freeze-2026-09-06/approved-authority-amendment.txt`。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本实验 hard stop。不得重放 SOURCE_DEV、打开当前 LOCKBOX、挑 seed、调 threshold，或把 interface PASS 升级为 Reward confirmation。若未来继续，应新建独立 TRAIN/DEV-only mechanism study，先定位 source Reward qualification 与 prompt/image-specific attribution 的失败原因；只有冻结新候选后，才能申请新的 genuinely fresh authority。

当前 GPU 阶段已经结束，后续报告与 Wiki 归档只需本地 CPU/磁盘。

## Sources

- [来源快照](../source-snapshots/rpj4-true-unseen-sd35-anchor-confirmation.txt)，原页面定位 `wiki-store/wiki/experiments/rpj4-true-unseen-sd35-anchor-confirmation.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
