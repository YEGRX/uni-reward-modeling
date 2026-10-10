# LatentAtlas U5-PROJ0-R2 Frozen-B3 Structural Projector

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在 `development-only / adaptive / reward-free / known-VAE` 条件下，检验是否必须先压缩出显式共享 `U`，还是可以让每个 source VAE 的独立 Projector 直接复原冻结 B3 的 source interfaces，再交给同一个 frozen downstream。

实验比较两条训练路径：

1. `P_SUP_*`：使用 target-side structural supervision 的上限参照；
2. `P_ANCHOR_*`：只依赖正确的跨 VAE teacher registration，并与五个 training permutation nulls 比较。

它承接 [latentatlas-u5pb0-target-free-predictive-bottleneck](latentatlas-u5pb0-target-free-predictive-bottleneck.md) 与 [latentatlas-u5pb1-predictive-u-capacity-spatial-topology](latentatlas-u5pb1-predictive-u-capacity-spatial-topology.md)：PB1 的显式 compact `U` 尚未进入 B3 的 5% envelope，本实验改问“模块化 per-VAE Projector 是否可以直接接入 frozen B3 structural interface”。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u5-proj0-frozen-b3-structural-projector.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- P4096 fold-0：train/validation/evaluation=`2868/408/820` matched identities。
- Source views：SD 与 FLUX；target view：DCAE。
- Source structural tokens：每个 source 为 `[64,128]`。
- Target interface：冻结 B3 的 source-interface cutpoint 与 frozen downstream。
- Normalization：train-only、per-view、per-channel。
- Evaluation：820 identities，5,000 次 common-stream bootstrap，seed=`2026082502`，central 90% interval indices=`249/4749`。
- 五个固定 training permutation nulls 与五个 evaluation pairing nulls。
- 不读取 Reward、Reward Head、RGB、H/H-bar、private orientation、新 VAE 或网络。

这里的 `Anchor` 指 same-identity cross-VAE registration / dense matched onboarding，不是早期 K64 RGB relative-anchor 坐标；因此不能称 unpaired、低成本 onboarding 或 unseen-VAE 实验。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### Final decision

```text
VERIFIED
ANCHOR_REGISTERED_PROJECTOR_STRUCTURALLY_SUFFICIENT
SUP=shallow_strict
ANCHOR=strict
SOURCE_DEPENDENCE_ESTABLISHED
TRAINING_PAIRING_SPECIFIC
EXPLICIT_U_NOT_REQUIRED_FOR_KNOWN_VAE_FROZEN_B3_INTERFACE
FRESH_AUTHORITY_REPLICATE_BEFORE_BROADER_CLAIMS
```

### Main structural metrics

Original B3 validation replay normalized MSE=`0.2881973982`。

| Arm | P/P MSE ↓ | joint deficit（90% CI） | Anchor-vs-SUP deficit（90% CI） | eval macro AUROC | noncollapse |
|---|---:|---:|---:|---:|---|
| P_SUP_SHALLOW | 0.288238 | -0.008839 `[-0.010056,-0.007642]` | N/A | 0.999461 | PASS |
| P_SUP_STRONG | 0.344627 | 0.185067 `[0.182559,0.187500]` | N/A | 0.987654 | PASS |
| P_ANCHOR_SHALLOW | 0.290836 | 0.000095 `[0.000083,0.000107]` | 0.009014 `[0.007792,0.010253]` | 0.999396 | PASS |
| P_ANCHOR_STRONG | **0.290829** | **0.000070** `[0.000056,0.000084]` | **-0.156107** `[-0.157836,-0.154320]` | 0.999398 | PASS |

`P_SUP_STRONG` 没有达到 strict joint gate，但 `P_SUP_SHALLOW` 达到；Anchor shallow/strong 均达到 strict structural gate。决策因此是 `SUP=shallow_strict` 与 `ANCHOR=strict`，不是“所有架构都 strict”。

### Registration specificity

- Training correct-vs-five-permutations：Anchor shallow macro gain=`2.659518 [2.627223,2.691399]`，worst gain=`1.384759 [1.358724,1.411403]`；Anchor strong macro=`2.659612 [2.627311,2.691499]`，worst=`1.384820 [1.358785,1.411451]`；两者 `passed=true`。
- Evaluation correct-pairing：四个主 arms 全部 `passed=true`；Anchor shallow/strong macro gain=`3.631413/3.631942`，macro AUROC=`0.999396/0.999398`。
- 四个主 arms 的 SD/FLUX projected outputs 全部 active fraction=`1.0`，effective rank=`47.99–73.65`，noncollapse 全通过。
- Projector-vs-S64-W closure：Anchor shallow/strong=`0.999696/0.999778`，决策记录为 `PROJECTOR_INTERFACE_OUTPERFORMS_CURRENT_EXPLICIT_U`。

### Integrity

- Completed path count：`800`。
- Inventory SHA-256：`7e35a4cc7dac7d6c7d3d14f913a19f0320aefaa0e0e54f023af053ab7f03e7cf`。
- Result seal SHA-256：`0b264cec6064c202f1bba5803f5b7b2983499542bf467640b6919e44a8621c93`。
- Strict verifier：`VERIFIED / strict-forward`，9 arms，17 questions，training performed=`false`，verifier replay read=`1`。
- Authority counts：evaluation materialization=`1`、production read=`1`、strict verifier read=`1`、post-evaluation training=`0`。
- Forbidden counters：Reward/Reward Head/RGB/network/H-or-Hbar/private-orientation/new-VAE 全部为 `0`。
- Pre-run regression：U5=`200 passed`，PB1 compatibility=`169 passed`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

本实验给出了当前 U 系列最强的 Projector-only 正证据：在已知 SD/FLUX、同一 P4096 fold、冻结 B3 cutpoint/downstream 的范围内，正确跨 VAE registration 学出的 per-VAE Projector 可以把两个 source interfaces 恢复到足以维持 B3 downstream structural behavior 的程度。它不仅接近 B3，而且同时满足 correct-over-five-training-permutations、correct input pairing、noncollapse 与 optimization gates，因此不能用“模型坍缩”或“随便配对也一样”解释。

这也解释了 PB1 的一个关键分叉：当前显式 compact `U`（S64-W）不是唯一可行接口。对于 known-VAE frozen-B3 onboarding，可以让每个 VAE 用模块化 Projector 直接对齐目标接口，而不必先经过单个显式共享 `U`。这里的“explicit U not required”严格限定于该接口，不等于数学上证明 U 无用，更不等于 canonical U 不存在。

不能外推的部分：

- 没有 Reward 或 Reward Head，所以不证明学出的跨 VAE interface 能支持 Reward；
- 没有 unseen VAE，所以不证明新 VAE onboarding；
- 使用 reused-P4096 与同一 development authority，不是 fresh confirmation；
- 是 single fold / single seed，不证明跨 seed/fold 稳定；
- 使用 dense matched identities，不证明低 Anchor budget 或 unpaired registration；
- 不证明 fresh distribution、canonical U 或跨 frozen downstream/head transfer。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

注册建议是 `FRESH_AUTHORITY_REPLICATE_BEFORE_BROADER_CLAIMS`：先在独立 fresh authority 上原样复制已冻结的 Anchor Projector 协议，不再根据本次结果调 architecture、loss、seed 或 gate。只有 fresh structural replication 通过后，才适合另立 Reward-functional Projector 对比，检验 frozen Reward Head/Reward oracle 是否也能被保存。

当前实验已经 hard stop；不在同一 P4096 authority 上继续扫 Projector、增加 permutation、改变 threshold 或把结果升级为 Reward/canonical-U 结论。

## Sources

- [来源快照](../source-snapshots/latentatlas-u5-proj0-frozen-b3-structural-projector.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u5-proj0-frozen-b3-structural-projector.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
