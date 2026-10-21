> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# R17 真实联合决策审计

## 1. Date

2026-10-16。新报告接收后的缓存复算；不是重新训练或新评分。

## 2. Purpose

为什么需要：新包只根据边缘汇总证明“必然发生一些决策改变”，缺少实际REC/A2/Native联合行，不能回答改善来自哪些事件。当前工作区有真实分数，因此直接补齐，区分坐标/数值改善、选择改变与人工正确性净增益。

## 3. Code Version / Commit

新分析代码 `docs/latentatlas-real-decision-audit-2026-10-16/joint-audit/run_audit.py`；另行精确算术核验 `verify_independent.py`。文件SHA见同目录 `output-sha256.json`。根知识库main无提交；未改历史实验脚本。主控从原始三个分数文件重新算关键计数/MSE，结果 `primary-acceptance.json`。

## 4. Dataset / Input

Cosmos CI8x8 Clean T0，252图、28组、1008物理pair、4重复噪声流，共4032行；DEV已消费。REC1000与A2 .001/2500正式checkpoint，Native3999非tie行。三份原分数SHA分别 a231c595…48be4、5965a8d7…8ff4a、b09292c7…a1a9e；完整值及每侧图像/seed/原评分manifest在identity-and-verification.json。A2侧顺序由原producer代码SHA绑定，不仅看列名猜测。

## 5. Parameters

保留历史四流和pair-occurrence。human以严格正确计，student tie非正确；Native agreement在Native非tie上student tie记0.5。MSE所有4032行。事后整组bootstrap20000次，seed2026101602。比例控制每次留出完整1组、另27组拟合正系数，REC/A2等额外Native信息预算。

## 6. Command

已有NumPy解释器运行joint-audit/run_audit.py，再Python3运行verify_independent.py。仅CPU，主分析0.116秒/RSS94MB，独立核验约0.216秒/49MB。0训练/模型前向/DiNa/GPU调用。主控直接原始分数复算另有回执。

## 7. Results

| 对象 | 实际结果 |
|---|---:|
| human修复 / 损坏 | 90 / 90 |
| REC→A2严格翻转 / tie转换 / 同三态 | 142 / 69 / 3821 |
| Native严格修复 / 损坏 | 89 / 47 |
| 同三态行贡献的净margin MSE改善 | 90.9991% |
| REC / A2 margin MSE | 0.233816243819 / 0.158372698330 |
| 等信息LOO正比例后REC / A2 MSE | 0.224363781925 / 0.157715715844 |
| REC四流中双向符号pair | 80 / 1008 |

正负贡献全部保留，见event-contributions.csv及native-margin-contributions.csv。比例控制不改变符号/选择；其改善依赖缓存Reward标签，不能声称是原无Reward方法。

### 2026-10-18 D60增量：完整开发组的Native选择损失

完整报告（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/functional-risk-decision-d60.md`）从原6份输入复算6臂：全28组REC/A2平均Native regret=.0190039741/.0129261320，Pointwise=.0411108108、Spatial5=.0498959980、V26=.0269252232。整组排除D44所属4组后，REC/A2=.0176818283/.0116399129。24原指标匹配，24,192个方法×pair×流的损失以两公式精确一致。

Native regret取最优Native分数减接口所选侧Native分数，接口tie按均匀选择期望，另存确定tie版本。本次计算前固定该开发描述量，原主指标保持；Human Accuracy原均值均72.619%，联合功能判决仍未决。28组和剩余24组均已消费，每流pair选择不等于九候选共同池选择。主复算CPU.787秒；0模型/拟合/GPU/SSH。A2/V26的504输出SHA与1016项既有独立坐标复算另有资产回执。

## 8. Analysis

新包确定性下界strict flip≥19、human repair=damage≥10正确但较松；真实联合行现在给出142和90。修正“仅数字变了、选择完全没变”的过强表述：确实有选择更替，但净人工正确数仍为0。约91%的净数值改善来自决策未变化行，说明margin fidelity与人工选择收益需要单独评价。

这不证明A2与REC等效，也不证明所有更强Projector无用。原六效应同时区间仍用于原正式比较；本次未校正描述性区间不能取代它。训练预算不等、共享拟合历史、反复消费DEV不因group留出控制消失。当前最强替代解释仍包含普通回归和margin效应，不能直接认定特殊共享几何。

## 9. Problems

包的原工作环境缺Native/A2不等于当前资产缺失。包内27-cell优化见证是NOT_REAL_ROWS，不能当真实联合样本。本次65项SHA通过，14个整数见证全部等式及目标值精确回代，但未安装SciPy、未独立重优化全部极值。

## 10. Next Steps

已补完该包的核心联合数据缺口；不以继续事后分箱阻挡系统工作。按用户升级要求，推进真实多来源Noisy V0、混合选择和完整英文内部稿。此审计可支撑论文“数值保真不自动转化为人工正确性收益”的有限域经验论断，不能填补真实生成效用或成本表。

相关：`latentatlas-current-evidence-map`、`latentatlas-theory-map`、`latentatlas-research-decisions`、`latentatlas-paper-framework`。

## 11. Sources

- 新原包：`raw/notes/latentatlas/real-decision-audit-2026-10-16/`（原ZIP SHA a3df22239c57cf4b3168b500db39b27ce975cc8799b96a6410548386f57e38d3）。5份根主文+README已全文读；嵌套代码按问题核查。
- 实际完整审计：`docs/latentatlas-real-decision-audit-2026-10-16/joint-audit/REPORT.md`。
- 主控直接复算：`docs/latentatlas-real-decision-audit-2026-10-16/primary-acceptance.json`。
- 原正式统计：`raw/projects/latentatlas/r17-a2-convergence-and-dina-20261014/final-fixed-analysis/`。
- 原始REC、Native、A2路径和完整SHA：joint-audit/identity-and-verification.json。
