# LatentAtlas U5-PB1R1 Residual Information Localization

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

承接 [latentatlas-u5pb1-predictive-u-capacity-spatial-topology](latentatlas-u5pb1-predictive-u-capacity-spatial-topology.md)，在不训练新 U 的前提下，用 frozen B3 与最佳 spatial predictive-U `S64-W` 定位剩余约 31.4% predictive gap：它更像 local/frequency detail、source complementarity，还是 distributed/static bottleneck limitation。

本实验是 `adaptive / development-only / reused-P4096 / known-VAE / single-fold / non-confirmatory / reward-free`。Validation 408 是 primary classification authority；Evaluation 820 只允许 secondary descriptive replay。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u5pb1r1-residual-information-localization.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Reused P4096 fold-0 transport：train/validation/evaluation=`2868/408/820` identities。
- Source：SD `[4,64,64]` + FLUX `[16,64,64]`；target：train-normalized DCAE `[32,16,16]`。
- Frozen checkpoints：B3、S64-W primary；Q128、Q64-W secondary。
- B3/S64-W conditions：correct、sd_wrong、flux_wrong、factorial_both_wrong；Q128/Q64-W 只做 correct。
- Five null definitions 与 2×2 factorial commitment 均在任何 forward 前冻结。
- Reward、Reward Head、RGB、H/H-bar、network access 均为 0。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### Validation primary

```text
B3 MSE = 0.288197414090
S64-W MSE = 0.378931647824
absolute gap = 0.090734233734
95% CI = [0.087909618832, 0.093694700235]
relative point deficit = 31.4834%
```

| Evidence | Point / CI | Formal status |
|---|---|---|
| Channel top-8/32 | `0.317721 [0.315135,0.320845]` | `NEGATIVE` |
| Patch top-26/256 | `0.133791 [0.131971,0.139650]` | `NEGATIVE` |
| High frequency | `0.349824 [0.345412,0.354192]` | 单独未过 gate |
| Mid+high frequency | `0.827552 [0.820041,0.834740]` | `FREQUENCY=POSITIVE` |
| Gram relative gap | `0.375544 [0.359924,0.391308]` | close=`false` |
| SD source component | magnitude positive，association incomplete | `INDETERMINATE` |
| FLUX source component | magnitude positive，association incomplete | `INDETERMINATE` |
| Standard interaction | `-0.173677 [-0.187467,-0.160319]` | `NEGATIVE` |

Low/mid/high excess fractions=`17.2448% / 47.7729% / 34.9824%`。Spatial center gap=`0.112013`、border=`0.083641`，但 top-patch gate 明确为负。B3/S64-W Gram normalized errors=`0.417681/0.574538`。

Final Validation decision：

```text
RESIDUAL_LOCALIZATION_INCONCLUSIVE
DO_NOT_SELECT_NEW_ARCHITECTURE
NOT_SUPPORTED_WITHIN_5_PERCENT
```

### Evaluation incident

Evaluation durable access=`1` 已消费；production loader 错把 PB1 training-registry hash schema 用于 PB0 transport manifest。两者对 dtype/shape 的序列化分别是 `float32 + compact JSON shape` 与 `torch.float32 + Python tuple shape`，相同 tensor bytes 得到不同 digest。运行在 `evaluation/sd tensor drift` 停止，Evaluation forward=`0`、arithmetic replay=`0`、completion receipt=`0`。

整个 attempt 保持 `EVALUATION_OPEN`；不是 `FINALIZED`、不是 `VERIFIED`，没有 inventory/result seal/verifier pair。Commit `d1eca17…` 只修复未来 authority，不回写本次 attempt。

### Verification

- Production preflight：`248 passed, 1 skipped`。
- Strict Validation-only replay：`PASSED`；408 rows、12 keys、`rtol=1e-4`、`atol=1e-6`。
- Future-fix tests：runtime=`13 passed`；PB1R1 focused=`59 passed, 1 skipped`。
- Final branch full repository：`2993 passed, 1 skipped in 801.80s`；唯一 skip 是 controller-only real Validation smoke。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

结果的关键不是“找到了唯一残差类型”，而是排除了一个过早的架构选择：频率信号确实偏 mid/high，但 channel 和 patch 并不集中，因此不能把下一步直接定为 multiscale/local U；SD/FLUX sensitivity magnitude 较强，却未稳定关联 high-residual identities，因此也不能直接转 shared/private；Gram 仍未 close，但现有 gate 又不足以单独证明 iterative/distributed mechanism。

Q128 secondary comparison显示 S64-W 相对 Q128 消除了 `55.0952%` 的 B3 gap，并把 Gram signed gap 从 `0.405488` 降到 `0.156857`（减少 `61.3164%`）。这进一步支持 [latentatlas-u5pb1-predictive-u-capacity-spatial-topology](latentatlas-u5pb1-predictive-u-capacity-spatial-topology.md) 的“Spatial Read matters”机制解释，但没有定位 Spatial Read 尚未保留的唯一信息结构。

本次证明范围仅限 frozen B3/S64-W、reused-P4096、known-VAE、single-fold Validation。它不证明 fresh confirmation、Evaluation replication、canonical U、Reward transfer、unseen-VAE、multi-seed/fold 或全局最优架构。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

当前 hard stop：`DO_NOT_SELECT_NEW_ARCHITECTURE`。不训练 local/multiscale、shared/private 或 iterative communication U。

若未来继续，只允许先冻结新的 run identity 与已修正 PB0 transport-hash protocol；再取得真正新的 Evaluation authority，执行一次 secondary descriptive replay。不能 resume 或 retry 已消费 attempt，不能让新 Evaluation 修改这次 Validation classification，也不能因为 incident 自动开新 U。

当前与下一步 protocol/report 工作不需要租用 GPU；本地服务器在线状态未在本页核验。

## Sources

- [来源快照](../source-snapshots/latentatlas-u5pb1r1-residual-information-localization.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u5pb1r1-residual-information-localization.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
