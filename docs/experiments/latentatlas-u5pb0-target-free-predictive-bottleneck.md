# LatentAtlas U5-PB0 Target-Free Predictive Bottleneck

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在复用 P4096、known-VAE、reward-free 的 development protocol 中，检验：

1. SD+FLUX product space 是否能无 target Reward label 地预测 DCAE latent；
2. 预测能力是否依赖正确 identity pairing；
3. direct predictor 的信息能否压缩进固定 `U[16,128]` bottleneck；
4. bottleneck 失败时能否区分 optimization failure、collapse 与 compactness failure。

该实验承接 [latentatlas-u4a4-reward-free-p4096-crossfit-correspondence-specificity](latentatlas-u4a4-reward-free-p4096-crossfit-correspondence-specificity.md) 与 [latentatlas-cvjdd0-cross-vae-joint-denoising-anomaly](latentatlas-cvjdd0-cross-vae-joint-denoising-anomaly.md)。它不使用早期 K64 RGB Anchor bank、relative-Anchor coordinates、H、Reward Head、RGB 或 fresh authority，但使用 P4096 中同 identity 的 SD/FLUX/DCAE matched latent correspondence，不能称为 unpaired 或广义的 anchor-free learning。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u5pb0-target-free-predictive-bottleneck.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Authority：P4096 development authority，fold 0。
- Train / validation / evaluation：`2868 / 408 / 820` identities。
- Source：SD `[4,64,64]` + FLUX `[16,64,64]`。
- Target：DCAE `[32,16,16]`。
- `target-free` 仅指 DCAE 内容不进入 forward input；DCAE latent 仍作为监督 loss target，因此不是无监督学习。
- Train-only per-view/per-channel normalization。
- Five deterministic pairing nulls。
- Identity-grouped common-stream bootstrap：5,000 replicates，seed=`2026082502`。
- Reward、Reward Head、orientation、H/H-bar、V708、G0.1 validation/test、NF mapping、RGB、network access counters 全部为 0。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 Final decision

```text
PRODUCT_SPACE_PREDICTIVE_ONLY
```

冻结的唯一下一步：

```text
保留 direct product-space model
```

### 7.2 Main metrics

| Condition | MSE | NRMSE | EV point | EV 95% interval | Cosine | R@1 | MRR |
|---|---:|---:|---:|---:|---:|---:|---:|
| B0 | 0.987446 | 0.995209 | 0.000000 | — | 0.137448 | 0.001220 | 0.008887 |
| B3 correct | 0.290828 | 0.540102 | 0.705474 | [0.702260, 0.708736] | 0.841990 | 1.000000 | 1.000000 |
| M1 correct | 0.724445 | 0.852433 | 0.266344 | [0.259180, 0.274046] | 0.523081 | 0.958537 | 0.975122 |

B3：

- Gate A=`PASS`。
- Worst null=`flux_wrong`，MSE=`0.632146`。
- Worst-pairing-gain=`1.173605 [1.150261,1.197748]`。
- Macro balanced AUROC=`0.999399 [0.999024,0.999707]`。
- Correct prediction 对全部五个 null 具有强 pairing specificity。

M1：

- EV lower >0，pairing gate=`PASS`，U noncollapse=`PASS`。
- Worst-pairing-gain=`0.320901 [0.309006,0.333060]`。
- Macro balanced AUROC=`0.907900 [0.899212,0.916659]`。
- Compact deficit=`1.490972 [1.467986,1.514329]`，远高于注册上限 `0.05`，因此 compact gate=`FAIL`。

### 7.3 U diagnostics

- feature variance=`0.491862`
- active fraction=`1.0`
- effective rank=`19.768419`
- sample-mean variance=`0.058206`
- permuted-U change=`0.530834 [0.525292,0.536638]`
- prediction change=`0.567797 [0.553596,0.582024]`
- constant-U advantage=`0.278044 [0.270869,0.285714]`

这些指标排除简单 collapse/complete-ignore，但不能把当前 U 升级为 canonical 或 universal U。

逐样本 change/advantage 区间由本地 5,000 次 bootstrap 重算；feature variance、active fraction、effective rank 与 sample-mean variance 是 MPS worker-attested aggregates，因没有持久化逐样本 U tensor 而未从 raw U 独立重建。五个 permutation 是冻结 comparative controls，不是 permutation-test p-value。

### 7.4 Integrity

- Completed verifier：`VERIFIED`
- Registered path count：26
- Inventory SHA-256：`3009c7b48b4d2f8799c6d17d36722d06f92e95982bd04d48ff09701c422038c3`
- Result seal SHA-256：`9e906076dfc15ba852db09332523f294bded7241838debcc1dc19cb1b8bd66ff`
- B3 selected checkpoint：`ae4b275b9f6dd1925ae802d3b5c7dbbfaef7304a2cfaea4f0a4b5da86ca8f03b`
- M1 selected checkpoint：`af2e25ae197f3d5b5ac975a06757d2cc596e60c1760c5b1026e1e0e9051779b2`
- Focused/adjacent regression after verifier repair：`173 passed`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 8.1 证明了什么

1. 在当前 reused-P4096、known-VAE development scope 内，SD+FLUX product space 含有强 target-free DCAE predictive information。
2. 该信息依赖正确 cross-VAE identity pairing，而不是只依赖 marginal mean。
3. M1 的 U 不是简单坍缩或完全被 decoder 忽略。
4. 在相近参数量、同训练预算与当前 `16×128` 参数化下，M1 没有在 5% 非劣范围内保留 B3 的预测质量。

### 8.2 不证明什么

- 不证明 universal/canonical U 不存在。
- 不否定所有 bottleneck architecture、capacity、loss 或 optimization。
- 不证明 Reward transfer、Reward sufficiency、fresh replication、unseen-VAE onboarding 或 cross-distribution generalization。
- 不构成 Anchor onboarding evidence；本实验没有使用早期 K64 RGB Anchor bank/relative-Anchor coordinates，但使用了 dense matched identities，不能外推到低成本或 unpaired onboarding。
- 不证明 Apple MPS 与未完成的 CUDA attempt 数值等价。
- 不解决 [latentatlas-u4b1-284-exploratory-fresh-functional-specificity](latentatlas-u4b1-284-exploratory-fresh-functional-specificity.md) 的 `SOURCE_H_INADEQUATE`。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

唯一冻结动作是：**保留 direct product-space model**。停止把本次 M1 当作已通过的 compact predictive-U；本页面不自动授权其他 target direction、seed、fold、Reward、fresh 或 architecture rescue 实验。

## Sources

- [来源快照](../source-snapshots/latentatlas-u5pb0-target-free-predictive-bottleneck.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u5pb0-target-free-predictive-bottleneck.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
