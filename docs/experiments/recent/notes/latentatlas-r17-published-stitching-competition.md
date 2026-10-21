> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# LatentAtlas R17 公开Stitching复现与冻结Reward竞争

## 1. Date

2026-10-13，CPU准备收口；新GPU训练/科学评分NOT_RUN。

## 2. Purpose

先核验公开论文真实方法，再比较Cosmos64Anchor接口的功能保真与信息/计算成本；不默认REC优于公开方法。Research gap：现代stitching尚无同冻结DiNa的公平结果。

## 3. Code Version / Commit

独立新增`scripts/latentatlas-r17-stitching-20261013/`。未提交/覆盖原REC；17活动代码SHA由`execution-spec-r3-final.json`冻结，canonical ee9fdf611b39ab840ee92c5b861d616dc986f367104d2cbd1df9e5863c1ab6f8。旧campaign漂移被拒绝并保留。

## 4. Dataset / Input

Cosmos FIT64/VAL64 nativeT0原paired bank：256tensor真实SHA/BF16/shape/finite通过；与DEV252无图像身份交集。DEV1008pairs/28connectedgroups/4流为已消费开发域；新独立评价组缺失。128原caption和512anchor seeds身份恢复；新headquery cache缺。

## 5. Parameters

Baseline：N21-coordinate336params，V26LFM2128，sameMLPFFM-only2128；前两TierA coordinate，后者TierB读冻结R功能feature。3LR/方法，见冻结执行协议；原REC39056不重训。

## 6. Command

`train_campaign.py --spec .../execution-spec-r3-final.json --check-only`已运行CPU预检。新paid stage必须直接用户授权、Torch2.6/CUDA资格及独立技术门；未创建可冒用批准文件。测试命令与离线包使用方法见包README。

## 7. Results

43 CPU tests通过；真实pretrainedN21底座合成输入一次CPU原接口通过；Cosmos两个适配器各一次小批CPU通过；原RewardHead随机小配置FP32图通过。原benchmark、完整64训练、新DiNa scores/CI/cost为NOT_RUN。七份完整报告：

- `R17_CROSS_VAE_COMPARABILITY_AND_INFORMATION_BUDGET`：Tier信息、loss/容量/空间/计算公平性和资产。
- `R17_CVPR2026_STITCHING_REPRODUCTION`：LFM/FFM/Task/两阶段区别与DiNa最终query对应。
- `R17_ICML_PUBLISHED_METHOD_COMPETITION_ASSESSMENT`：十五审稿问题、竞争解释和投稿定位。
- `R17_NEURIPS2021_STITCHING_REPRODUCTION`：N21原接口/官方底座CPU与坐标架构适配。
- `R17_PUBLISHED_BASELINE_REAL_RESULTS`：历史R15实数与R17新NOT_RUN严格区分。
- `R17_PUBLISHED_STITCHING_METHOD_AUDIT`：原方法、代码状态、全设置出处和复现等级。
- `R17_TRAINING_AND_SCORING_EXECUTION_SPEC`：候选、训练/技术/科学预算、12端点与停止规则。

## 8. Analysis

Metrics：四stream per-pair margins，agreement/MSE与HumanAccuracy分开，28wholegroup bootstrap、12端点α.025。不能用CPU PASS作科学成功、单64规模作dataefficiency证明，不能把FFM-only称完整论文方法。

## 9. Problems

N21作者stitch源码未找到；V26官方repo仍README；原benchmark资源和合法Task labels缺。FFM需全根生产guard、真实BF16有限响应、512新feature及费用pilot。TierA仍需远端CUDA source-only/BN/checkpoint资格和ownedwatchdog，GPU权限尚无。

## 10. Next Steps

建议先批准有界TierA：6trial/max5400updates/R0/owned2小时上限；训练后资格与评分单独批准，两候选完整scorecap18686R（science16128）。FFM先补productiongate/pilot，不默认全量；若值得投稿，另新独立connectedgroups确认。Possible improvement：从纯坐标接口到功能特征监督的可量化Pareto，而非预设REC绝对最优。

## 11. Sources

Source: `raw/projects/latentatlas/r17-published-stitching-20261013/SOURCE_INDEX.md`及逐文件SHA表；两用户report原件SHA、两paper/supp/codecommit、原R14/R15资产；新CPU收据和独立review。相关 `latentatlas`、`R15_ICML_RESEARCH_DECISION`。
