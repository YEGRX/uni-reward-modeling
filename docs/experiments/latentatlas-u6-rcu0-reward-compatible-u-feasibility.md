# LatentAtlas U6-RCU0 Reward-Compatible U Feasibility

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在冻结 SD、FLUX、DCAE 单视图 latent 上，用同一组 canonicalizer / Reward reader 参数测试：当前构造能否形成一个可由同一 Reward reader 跨三个 VAE 读取的 reward-compatible U。

本实验是 [latentatlas-rrv1-frozen-latent-reward-readout](latentatlas-rrv1-frozen-latent-reward-readout.md) 之后的 TRAIN/DEV-only、adaptive、non-confirmatory follow-up；不读取或重放 RRV1 official TEST preference orientation。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u6-rcu0-reward-compatible-u-feasibility.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Sealed RRV1 TRAIN/DEV latent cache：SD、FLUX、DCAE。
- TRAIN/DEV-only authoritative text cache：CLIP-L + CLIP-G + Google T5-XXL，6,144-D。
- Native reference：RRV1 在 TEST 前由 DEV BT-NLL 选择的 DCAE prompt reader。
- TRAIN/DEV、TRAIN/hidden-TEST、DEV/hidden-TEST 的 row/image/pair overlap 均为 0。
- 发现 1 条 TRAIN/hidden-TEST prompt 文本重复；只记录文本重复，没有读取对应 TEST preference orientation。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

最终分类：

```text
NO_REWARD_COMPATIBLE_U_SIGNAL_UNDER_TESTED_PROTOCOL
```

冻结 decision/bootstrap 口径使用 primary seed `20260827`。原 compact 报告中的 D 数字是该 primary seed 的 point estimates，不是三-seed aggregate：

| Representation | Accuracy | BT-NLL | Margin SD |
|---|---:|---:|---:|
| SD | 0.618400 | 0.626804 | 0.628227 |
| FLUX | 0.635600 | 0.610268 | 0.739967 |
| DCAE | 0.644800 | 0.602421 | 0.748346 |
| RRV1 native DCAE | **0.650200** | 0.606691 | — |

A/B/C/D primary-seed prompt macro 结果：

| Arm | Macro Accuracy | Macro BT-NLL | 主要失败 gates |
|---|---:|---:|---|
| A `DIRECT_SHARED_MIN` | 0.629133 | 0.619239 | native Accuracy；prompt Accuracy/NLL increment |
| B `DIRECT_SHARED_PARAMMATCH` | 0.630267 | 0.613431 | native Accuracy；prompt Accuracy/NLL increment |
| C `RCU_BT_ONLY` | 0.632200 | 0.615368 | native Accuracy；representation Accuracy；prompt Accuracy/NLL increment |
| D `RCU_BT_SCORECONS` | **0.632933** | **0.613164** | native Accuracy；representation Accuracy；prompt Accuracy/NLL increment |

完整 A/B/C/D 的每个 VAE、三-seed均值、reader 对照、bootstrap lower95 和逐 arm 解释见：

`LatentAtlas-runs/U6_RCU0_ALL_ARMS_COMPLETE_REPORT_2026-08-29.md`

- 36/36 fits 完成 5,000 updates；36/36 optimization adequate；36/36 checkpoint reload PASS。
- Stable seeds=`3/3`，noncollapsed=`true`，direction balanced=`true`。
- D score-consistency variance=`0.042909`，低于 C 的 `0.061714`，该局部目标按预注册方向改善。
- Native non-inferiority 未关闭：最弱 family Accuracy lower95=`-0.018318`；BT-NLL lower95=`0.033199`；两者均要求 `>0`。
- 五个 representation shuffles 中，一项 Accuracy lower95=`-0.001537`，因此 `REPRESENTATION_ACCURACY_CONTROLS` 失败；五项 BT-NLL controls 均为正。
- 五个 wrong-prompt controls 的 Accuracy/BT-NLL lower95 均为正。
- Prompt 增量失败：prompt-vs-latent Accuracy lower95=`-0.024273`，BT-NLL lower95=`-0.025712`。
- Primary D 未通过 gates：`NATIVE_ACCURACY_GAP`、`REPRESENTATION_ACCURACY_CONTROLS`、`PROMPT_ACCURACY_INCREMENT`、`PROMPT_NLL_INCREMENT`。
- Official TEST orientation / rows / representation / forwards=`0 / 0 / 0 / 0`。
- Disk-only verifier=`PASS`，verified artifacts=`155`，inventory SHA256=`e576fb0fd293058584b48d81a17552eab4e6c866b5040fc77fc88a8a9dbff63b`，result seal SHA256=`381364b5bc807b42d77a0b7e74ff8b84a3d478aac7f12ff648d01eb4f22741d8`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

当前单视图 RCU 构造可以稳定训练，并在三个 VAE 上产生明显高于 chance 的 DEV preference signal；score-consistency 也降低了跨 VAE 分数方差。但正式结论由联合 gates 决定：最弱 family 未同时关闭 native Accuracy/NLL gap，correct representation 未在所有五个 shuffle 上通过 Accuracy specificity，prompt 也未相对 latent-only 提供稳定增量。因此，不能把当前表现称为已建立 reward-compatible U。

这个负结果只否定当前 frozen SD/FLUX/DCAE、当前单视图 tokenizer/canonicalizer、当前 reader/optimizer 与 RRV1 TRAIN/DEV authority 下的具体协议。它不否定所有 nonlinear/canonical/universal U，也不提供 unseen-VAE、target-free onboarding、fresh holdout、RGB 重编码、noise latent、Projector 或 product-space 证据。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

不再复用 RRV1 official TEST，也不把当前 development 结果升级为确认性结论。下一步若继续，应先在 TRAIN/DEV-only 范围定位四个失败 gate 中的主瓶颈：native Accuracy non-inferiority、representation Accuracy specificity、prompt Accuracy/NLL increment；冻结唯一修订候选后，再申请 genuinely fresh external authority。当前结果不自动授权继续架构、seed、fold 或 threshold sweep。

## Sources

- [来源快照](../source-snapshots/latentatlas-u6-rcu0-reward-compatible-u-feasibility.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u6-rcu0-reward-compatible-u-feasibility.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
