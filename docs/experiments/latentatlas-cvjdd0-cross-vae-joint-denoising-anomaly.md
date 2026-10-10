# LatentAtlas CVJD-D0 Cross-VAE Joint Latent Denoising and Correspondence Anomaly Pilot

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在不读取 Reward label、不使用 Anchor/Bridge/candidate-U 坐标、不引入 fresh authority 的条件下，检验一个共享条件扩散去噪器是否能利用正确 matched cross-VAE conditions：

1. 改善 held-out identity latent 的去噪；
2. 稳定胜过五个 correspondence permutation nulls；
3. 将错误跨 VAE 配对识别为 anomaly。

该实验是 [latentatlas-u4a4-reward-free-p4096-crossfit-correspondence-specificity](latentatlas-u4a4-reward-free-p4096-crossfit-correspondence-specificity.md) 之后的新机制诊断：U4-A4 证明 P4096 上的 discriminative mapping 能保留 correct-over-null 信号；CVJD-D0 问的是联合生成式去噪目标是否会自发利用同一信号。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-cvjdd0-cross-vae-joint-denoising-anomaly.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Authority: 复用 P4096 development authority，fold 0。
- Fit/evaluation identities: `3276/820`，identity-disjoint。
- SD posterior-mode latent: `[4,64,64]`。
- FLUX posterior-mode latent: `[16,64,64]`。
- DCAE posterior-mode latent: `[32,16,16]`。
- Fit-only per-view/per-channel normalization；无 clipping。
- Evaluation timestep: `100/300/500/700`；每个 timestep 4 个冻结 noise draws。
- Five deterministic evaluation permutation nulls。
- 2,000 次 identity-grouped percentile bootstrap。
- Reward、H1105、fresh/test authority、network 等禁止访问计数均为 0。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 Headline

`JOINT_DENOISING_COLLAPSED_OR_IGNORES_CONDITION`

本次实际不是输出数值坍缩：Gate F 通过。更准确的语义是，当前 C 模型只学到极弱的 cross-VAE condition/correspondence 依赖，且 predicted-clean 还不如 noisy-copy baseline，因此落入冻结的 `collapsed-or-ignores-condition` 优先级分类。

### 7.2 Registered gates

| Gate | Result | Evidence |
|---|---|---|
| A Optimization adequacy | PASS | 3/3 models 完成 20k，有限，6 checkpoints 完整，terminal loss < early loss |
| B Joint value | FAIL | macro gain=`0.008887 [0.008701,0.009066]` < registered lower `0.02` |
| C Correspondence specificity | FAIL | five null lower 均 >0，但 worst macro lower=`1.550691e-5` ≪ `0.01` |
| D Anomaly discrimination | FAIL | AUROC 约 `0.5004`，FPR@95TPR=`0.95` |
| E Condition dependence | FAIL | correct-vs-shuffle 差异极小，predicted-clean NRMSE 劣于 noisy copy |
| F Noncollapse | PASS | 三 view variance/rank/active/noise-diversity/retrieval 不退化 |

### 7.3 Joint over marginal

| View | Relative gain point | 95% interval |
|---|---:|---:|
| SD | 0.005597 | [0.005499, 0.005691] |
| FLUX | 0.003647 | [0.003612, 0.003683] |
| DCAE | 0.017418 | [0.016912, 0.017915] |
| Macro | 0.008887 | [0.008701, 0.009066] |

C 相对 M 的改善在三 view 均为正，DCAE 最大，但 macro 只约 0.89%，未达 registered added-value gate。

### 7.4 Correct versus permutation nulls

- Five macro gap points: `1.92e-5–2.15e-5`。
- Five macro 95% lowers: `1.55e-5–1.78e-5`。
- Worst macro lower: `1.550691e-5`，约为注册 `0.01` 效应门槛的 `1/645`。

方向上存在极弱的 correct-over-null signal，但量级远不足以称 correspondence-specific。

### 7.5 Anomaly metrics

- AUROC=`0.500438 [0.500540,0.500778]`。
- AUPRC=`0.833781 [0.833438,0.834510]`；chance=`0.833333`。
- FPR@95TPR=`0.950000 [0.946341,0.951220]`。

当前 anomaly score 几乎无法区分 correct 与置换 correspondence。

### 7.6 Condition dependence and noncollapse

- C correct/shuffle loss=`0.7060607913/0.7060758201`，差值仅 `1.50e-5`。
- Prediction change=`3.6669e-5`，repeat error=`0`。
- Predicted-clean/noisy-copy NRMSE=`0.779382/0.767461`：C 比 copy baseline 更差。
- N correct-advantage lower=`-1.1654e-5`，没有复制 C 的 correct shortcut。
- SD/FLUX/DCAE active fraction 均为 `1.0`，noise diversity=`0.4011/0.6747/0.1414`。
- Retrieval R@1/MRR 均为 `1/1`，但 target noisy input 本身已携带 identity，不能单独归因 cross-VAE condition。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 8.1 本实验最强的否定是什么？

它否定的是当前这个具体构造：在 target noisy latent 已经高度预测 target clean latent 时，常规共享 `epsilon` denoising objective 不会自发地学到足够强的 identity-specific cross-VAE condition usage。

它不否定 shared structure 本身。U4-A4 已在另一 discriminative cross-fit mapping 上提供较强的 correct-over-null development evidence；CVJD-D0 说明该信号没有在当前 denoising setup 中转化为实质功能价值。

### 8.2 为什么不能只看正的 lower bound？

Joint gain 和 five-null gap 的 lower 确实都为正，但预注册门槛同时要求效应量达到可用程度。当 sample size 较大时，很小的系统差异也可以有正 lower；本次 `~2e-5` 的 permutation gap 即属于这种情况。

### 8.3 Deterministic posterior-mode 限制

输入 clean latent 是 posterior `mode()`，所以研究对象是确定性 latent 在 identities 之间的经验分布，而不是每个 identity 的多峰 posterior。Noise diversity 非零，本次不标记 `CONDITIONAL_DISTRIBUTION_EFFECTIVELY_DETERMINISTIC`；这也不能证明学到了有意义的多模态条件分布。

### 8.4 证据边界

可以说：当前 shared denoiser 能优化、不坍缩，其他 VAE conditions 有小幅正向改善，correct pairing 也有极弱方向信号；但当前 objective 被 target noisy self-signal 主导，未建立实质条件依赖。

不可以说：Universal U/canonical coordinates 不存在，Diffusion 劣于 Flow，Reward transfer 失败，unseen-VAE onboarding 失败，或 P4096 结果可泛化到新分布。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

CVJD-D0 到此 hard stop，未创建或执行 Rectified Flow、CrossFlow、LDDBM、第二 fold/seed、larger model、posterior resampling、Reward、fresh/unseen-VAE 或 architecture rescue。

若未来另行批准，最有信息量的下一问题是预注册一个排除 target noisy-copy shortcut 的 condition-necessity protocol，再判断 cross-VAE conditions 是否有实质性信息。该页面只保留建议，不授权后续实验。

## Sources

- [来源快照](../source-snapshots/latentatlas-cvjdd0-cross-vae-joint-denoising-anomaly.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-cvjdd0-cross-vae-joint-denoising-anomaly.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
