# LatentAtlas C2-DEV Generic Domain Generalization Baseline Probe

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在不访问 G0.1 test authority 的条件下，比较 ERM、Risk Extrapolation（REx）和 Group Distributionally Robust Optimization（GroupDRO）能否改善 Direct Shared Reward Reader 的跨 VAE family 留一迁移。该实验是独立的 problem-identification probe，状态固定为 `development_only / exploratory / confirmatory=false`，不能替代被 C1-R fresh-authority gate 阻止的独立确认实验。

相关页面：`latentatlas`（原wiki关联）、[latentatlas-c0-mini-v1-direct-shared-reader](latentatlas-c0-mini-v1-direct-shared-reader.md)、[latentatlas-c1-mini-loo-shared-reader](latentatlas-c1-mini-loo-shared-reader.md)、[latentatlas-c1r-fresh-authority-audit](latentatlas-c1r-fresh-authority-audit.md)。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-c2-dev-generic-dg-baselines.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- 只使用 G0.1 TRAIN=`44,839` pairs / `5,201` images 和 VALIDATION=`5,593` pairs / `708` images。
- 三个 VAE family：SD、FLUX、DC-AE。
- 每个 LOO run 使用两个 source family 的 TRAIN labels/gradients 与 source VALIDATION NLL 选择 checkpoint；held-out target 只用 5,201 个 TRAIN-image tokens 拟合固定 scalar normalization。
- C2 没有 test label authority、test evaluator 或 test token view；authority audit 中 `test_orientation_access_count=0`、`test_metric_api_instantiated=false`。
- 九个 checkpoint 与全部 projection 先封存并验证，之后才一次性读取 validation orientation；`target_dev_labels_open_count=1`。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 Target development macro

| Method | Target Macro Accuracy | Target Macro NLL | Accuracy vs ERM | NLL vs ERM |
|---|---:|---:|---:|---:|
| ERM | 0.536385 | 0.704045 | 0.000000 | 0.000000 |
| REx | 0.532809 | 0.702883 | -0.003576 | -0.001162 |
| GroupDRO | 0.535968 | 0.702787 | -0.000417 | -0.001258 |

Accuracy 改善为正，NLL 改善为负。ERM 的 Accuracy 最高，GroupDRO 的 NLL 最低；两种 DG 方法都略降 NLL，但都没有提升 macro Accuracy。

### 7.2 Held-out family

| Held-out | ERM Acc / NLL | REx Acc / NLL | GroupDRO Acc / NLL |
|---|---:|---:|---:|
| DC-AE | 0.516360 / 0.693085 | 0.518148 / 0.694349 | 0.523869 / 0.691804 |
| FLUX | 0.552298 / 0.688933 | 0.555695 / 0.688836 | 0.556767 / 0.687012 |
| SD | 0.540497 / 0.730117 | 0.524584 / 0.725466 | 0.527266 / 0.729545 |

- REx 仅在 FLUX 同时满足 `DeltaAcc>0` 与 `DeltaNLL<0`。
- GroupDRO 在 FLUX 和 DC-AE 同时改善，但 held-out SD Accuracy 相对 ERM 下降约 `1.32 pp`。
- ERM macro source→target Accuracy gap 为负、NLL gap 为正，复现了基本 development LOO degradation trend。
- REx 的 macro absolute Accuracy gap 比 ERM增加 `0.005870`，absolute NLL gap减少 `0.000737`。
- GroupDRO 的 macro absolute Accuracy/NLL gap 分别变化 `+0.001013/+0.000079`，没有 jointly reduce generalization gap。

### 7.3 Frozen classification

结论：**`DG_RESULT_MIXED`**。

- 不满足 `GENERIC_DG_PROMISING`：两种 DG 方法的 macro Accuracy delta 均未达到 `+1.0 pp`。
- 不满足 `NO_CLEAR_GENERIC_DG_GAIN`：GroupDRO 具有 macro NLL 改善，且至少两个 family 的 NLL delta 非正，因此落入 Accuracy/NLL disagreement 与 family asymmetry 的 mixed 区域。
- 注册建议：先做 mechanism analysis，再选择后续实验；不得自动启动 canonical U、额外 DG method、更多 seed、test evaluation 或 architecture change。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

1. 简单 generic DG objective 没有形成跨三 family 一致的 macro Accuracy 增益，说明 C1 暴露的 unseen-family transfer degradation 不能仅靠 REx/GroupDRO 直接解释或解决。
2. GroupDRO 在 FLUX/DC-AE 上出现同向改善，但 SD 明显退化；这更像 family-specific optimization trade-off，而不是已建立的 universal DG gain。
3. NLL 与 Accuracy 分歧说明概率校准/排序边界可能发生不同变化。后续机制分析应检查 source validation disparity、held-out SD 的 score distribution 和 GroupDRO q 轨迹，但不能在当前 validation 结果上继续调参后冒充确认性证据。
4. C2 与 C1-R 的角色不同：C1-R 要求新的 image-disjoint confirmatory authority，而 C2 明确复用既有 TRAIN/VALIDATION 做 development-only baseline。C2 的 mixed 结果不能解除 C1-R blocker，也不能升级 C1 Case B。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

1. 先进行只读 mechanism analysis，重点比较 held-out SD 与其他 family 的 source-domain loss disparity、score calibration、selected epoch 和 GroupDRO q trajectory。
2. 若要确认跨 VAE DG 效果，仍需人工提供或批准新的 image-disjoint Reward authority，并重新预注册 confirmatory protocol。
3. 不自动启动 Minimal-U、canonicalization、额外 DG methods/seeds、test evaluation、dataset 抓取或 architecture sweep。
4. 当前与下一步均为 CPU-only / 文档分析；若租用 GPU 仍在运行，可以关闭。

## Sources

- [来源快照](../source-snapshots/latentatlas-c2-dev-generic-dg-baselines.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-c2-dev-generic-dg-baselines.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
