> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# LatentAtlas-LRM-R2：真实FLUX目标分布上的Reward有效性审计

## 1. Date

2026-10-21。状态：**本地历史资产审计、独立复算和图像诊断完成；停止**。主决策：`GO_REWARD_VALIDITY_CONFIRMATION`，下一实验只建议未执行。

## 2. Purpose

区分接口Reward Fidelity、参考Reward Validity与真实任务Utility。直接恢复R1完整T1和同八图PickScore，回答1/4同选是否属实、三组分歧的边界/噪声性质，以及是否值得先投入人类有效性确认。

Research gap：目标FLUX真实生成分布上的人类偏好证据缺失；baseline：原PickScore代理、同池uniform、R1强Affine；metrics：组内分差/严格同向/原两流稳定性、描述性proxy选择差。Possible improvement限一项新组盲评，不设计或训练方法。

## 3. Code Version / Commit

本轮独立新代码：`scripts/latentatlas-lrm-r2-20261021/{restore_compare,root_recompute,recover_contract,make_inspection_sheets,make_scored_sheets}.py`。

既有分数SHA：T1原科学账本 `05d8b0d328ffb3766e23086e344a5b4e7479da9092107042eb49adb685f40a44`；PickScore raw `a0569a8d1d535a992299f21d86a4ecd25178db94209d3caa256b96c6cf5c5b43`。本轮不改原R1/C稿/历史raw。

## 4. Dataset / Input

固定dev-01…04各两seed2026101601/1602，8张1024²真实FLUX.1-dev原PNG和8份终态全部重核SHA；24个原标量=DiNa T1 A16条＋PickScore8条。旧表8条SD15明确排除。四Prompt已消费，等级HISTORICAL_DEVELOPMENT_DIAGNOSTIC。

原生成与两RM模型/checkpoint、Prompt、实际posterior/noise seed、原文件记录索引/哈希及预处理见正式资产报告和`restored-candidates.json`。没有其它同八图HPS或人类标签在本轮限定范围恢复。

## 5. Parameters

严格沿R1两流算术mean，side0−side1，较大为优；无变号/尺度拟合/新流。DiNa σ=.4002932608127594，t=400.29327392578125，固定同图参考posterior sample。PickScore为原FP32 scaled cosine，单次science，无噪声方差估计；exact tie=0，DiNa原.0625警戒只描述，不剔除。

补齐历史processor配置和两份Transformers v4.51.3源码，实际SHA均匹配原pin；由配置和默认得到224 BICUBIC resize/center crop/1÷255/原mean/std。用原patch恢复七份r3源文件并逐SHA匹配，未执行历史模型代码。模型权重身份依据原冻结回执，没有远端加载。

## 6. Command

项目根执行：

```sh
python3 scripts/latentatlas-lrm-r2-20261021/restore_compare.py
python3 scripts/latentatlas-lrm-r2-20261021/root_recompute.py
python3 scripts/latentatlas-lrm-r2-20261021/recover_contract.py
python3 -m unittest discover -s scripts/latentatlas-lrm-r2-20261021/tests -v
```

图像对照使用已有Pillow CPU环境，原1024²全图像素逐位保持，文字在图外。主控实际看完全部8图；非盲视觉诊断没有当成人类标签。

## 7. Results

| Prompt | T1 Δ（1601−1602） | PickScore Δ | 选择是否同向 | T1两流Δ |
|---|---:|---:|---|---|
| dev-01 | .140625 | −.460210800171 | 否 | .21875 / .0625 |
| dev-02 | −.218750 | .001127243042 | 否 | −.15625 / −.28125 |
| dev-03 | .562500 | .015584945679 | 是 | .5625 / .5625 |
| dev-04 | −.250000 | .484071731567 | 否 | −.3125 / −.1875 |

严格同选1/4，无精确tie；三组分歧的完整T1两流均同向。dev-02最小P分差仍相差591 FP32 ULP，不能删除为浮点平局；没有其人类偏好/抗扰动阈值。PickScore原技术repeat只一图dev-01 seed1602，两次及science一致，其余七图不据此称已重复。

T1所选图的PickScore相对同池uniform均值−.116228103638；R1 B/D同选，因此其同池代理结果逐组相同。这个量不是人类utility。R1强Affine8/8逐流、4/4均分选择保持，不隐藏普通映射竞争结果。

主控Fraction与Sol计算56比较字段完全相等，五项边界测试通过；完整图像与评分见病例报告。没有从四组估计总体准确率或显著劣于随机。

## 8. Analysis

面包店两图均有可读BAKERY，违反no-readable-text；静物组左布平折、右布卷起；几何组左圆锥遮挡蓝球，与behind-both要求存在缺口；陶工两图均显示双手与碗。它们提供可观察诊断对象，不能自动变成人类偏好标签。两模型的偏好维度/输入信息、近边界和目标偏好误差仍是竞争解释。

原文核查确认DiNa论文默认t=.4；官方另有静态图u=.1示例，不能据此标R1非法或在四组后重新择t。R1同t两流均分也不同于跨时刻token ensemble。

## 9. Problems

Reward validity继续未建立：没有同图人类标签，旧代理仅一图有技术repeat；两个分歧组的较大原分差不是校准置信度。当前有效性审计不能宣称DiNa/FLUX普遍失效或PickScore真值正确。原始资产、统计实现与视觉事实的来源分开。

## 10. Next Steps

唯一主决策为GO_REWARD_VALIDITY_CONFIRMATION：先做新目标FLUX候选的事前冻结人类盲评，再判断portability质量/成本实验。报告提出24新Prompt×2候选、5评审/组的有界筛查，只是建议，未获得本轮执行授权、没有启动。原C Clean结果保留；不改主稿、不训练、不扩可靠性新路线。

本轮新增模型/RM/VAE/接口/生成/训练/GPU/SSH/人工评价调用全部0，服务器不需要，电源状态未知。

相关：`latentatlas`、[latentatlas-lrm-r1-real-interface-qualification-20261021](latentatlas-lrm-r1-real-interface-qualification-20261021.md)、`latentatlas-research-decisions`、`latentatlas-takeover-reading-ledger`。

## 11. Sources

- [正式决定](../reports/lrm-r2-decision.md)。
- 完整资产（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_R2_REWARD_VALIDITY_AUDIT/R2_ASSET_AUDIT.md`）。
- 四组原图与分数（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_R2_REWARD_VALIDITY_AUDIT/R2_CASE_STUDIES.md`）、[CSV](../tables/lrm-r2-reward-comparison.csv)。
- [有效性](../reports/lrm-r2-validity.md)、论文意义（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_R2_REWARD_VALIDITY_AUDIT/R2_LRM_RESEARCH_IMPLICATIONS.md`）。
- `raw/projects/latentatlas/lrm-r2-20261021/user-request.txt`与同级公开小配置/源码恢复记录。
