# LatentAtlas RRV1 Frozen Latent Reward Readout

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在冻结 SD、FLUX、DCAE 与 current spatial U（S64-W）表示、冻结 prompt stack 和匹配轻量 Reward Reader family 下，用 HPDv3 external human preferences 正式判断：当前 U 是否保留可控、可归因的 Reward-readable information，以及相对 frozen native reference 的 Reward retention。

本页承接 [latentatlas-rrv1-cache-preflight](latentatlas-rrv1-cache-preflight.md)，并记录一次原始 TEST crash 与唯一获批 recovery。最终结果必须标记为 `RRV1_FORMAL_TEST_RECOVERY_AFTER_CONSUMED_AUTHORITY`，不能写成 pristine one-shot TEST。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-rrv1-frozen-latent-reward-readout.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Dataset：`MizzenAI/HPDv3@5ac4b5b5f2ef42c4613dec612473170b131552db`。
- TRAIN / DEV / TEST preference pairs：50,007 / 5,000 / 5,004。
- Cached images：53,271。
- Frozen representations：SD、FLUX、DCAE、S64-W。
- Text cache：CLIP-L + CLIP-G + authoritative Google T5-XXL，10,922×6,144。
- Formal readers：4 representations × 3 reader kinds × 3 seeds = 36 fits。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

最终分类：

```text
CURRENT_SPATIAL_U_NOT_REWARD_READABLE
```

冻结建议：

```text
STOP_CURRENT_U_REWARD_PATH_AND_REDESIGN_REWARD_COMPATIBLE_U
```

Primary prompt-conditioned Reader 的三-seed aggregate：

| Representation | Accuracy | BT-NLL |
|---|---:|---:|
| SD | 0.531375 | 0.704470 |
| FLUX | 0.585731 | 0.674222 |
| DCAE native reference | **0.609113** | **0.662478** |
| S64-W current U | 0.584532 | 0.681136 |

- S64-W vs native Accuracy deficit=`2.458 pp`，one-sided upper95=`4.077 pp`。
- BT-NLL gap=`0.018658`，relative gap=`0.028164`，upper95=`0.043081`。
- Reward Retention=`0.391645`，90% CI=`[0.065194, 0.675322]`。
- Seed robustness=`3/3 PASS`，direction balance=`PASS`。
- Representation specificity=`FAIL`：correct representation 未稳定胜过五个 shuffled-representation nulls。
- Prompt conditioning=`FAIL`：`U+prompt` 未显著胜过 U latent-only，wrong-prompt gate 也失败。
- Shallow diagnostic=`NONLINEAR_REWARD_READOUT_REQUIRED_UNDER_TESTED_FAMILY`。
- Structural/Reward relation=`STRUCTURAL_REWARD_RELATION_INCONCLUSIVE`。

Disk-only verifier 复核 1,860 个 paths、76/76 margin records，未训练、无网络，完整 scientific replay=`PASS`。Inventory=`3a23632a…b8ce0`，result seal=`8c395d76…c09`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

S64-W 的 Accuracy 高于 0.5，说明 current U 含有一定 preference-decodable information；但正式问题不只是“能否读出一点信号”，还要求 correct representation 和 correct prompt 在注册 controls 下具有特异性。后两项失败，所以不能把信号归因于预期的 spatial-U Reward geometry。

DCAE 是当前冻结条件下最强 native Reward reference。S64-W 保留了部分 Reward signal，但 retention 区间宽，而且结构恢复与 Reward gap 的关系仍不确定。应停止继续在同一 U 上堆 Reader/registration capacity，转向 Reward-compatible U objective。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

在 TRAIN/DEV-only authority 上设计 Reward-compatible U，至少同时保留 native DCAE ceiling、representation shuffle、wrong prompt 与 latent-only 四类 control。只能用 TRAIN/DEV 冻结一个候选，然后申请真正新的 external/fresh authority；不得复用本次 RRV1 TEST。

## Sources

- [来源快照](../source-snapshots/latentatlas-rrv1-frozen-latent-reward-readout.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-rrv1-frozen-latent-reward-readout.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
