> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# D59 均值与空间变化互换的冻结选择实验

## 1. Date

2026-10-18。真实执行、回收与独立复算完成。

## 2. Purpose

D58已知均值与空间变化都改善坐标；本项直接检验哪一部分保持冻结DiNa赢家，以区别单一分量充分与联合依赖。研究缺口是Anchor所学修正到实际选择的机制链。

## 3. Code Version / Commit

工作分支`codex/latentatlas-d44-affine-gate`，未提交；实际专用源码`code-r3`由10文件SHA封存，未覆盖历史目录。配置SHA`aa305bde2ba7d402e3079ffd789b0ebf7a3af86ec2020611e7dea3215a6a88aa`。代码审查（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/d59-execution/independent-code-review.md`）。

## 4. Dataset / Input

原D44四对八图、Cosmos Clean→SD3.5；历史已消费DEV，原两流、u=.4/.1。P0=初始化特征FIT64 OLS；P1=学习后特征同规则OLS。参考Native及端点评分复用原D44/D56，真实生成NoisyState另立合同。

## 5. Parameters

逐图逐通道空间平均M；PM=P0+M(P1−P0)，PV=P1−M(P1−P0)。FP64→FP32一次→RNE BF16，16臂封存在评分前。Native绝对分差≥.125；方法绝对分差≤.0625近零。4次技术复现全部字段精确通过；14份确定性噪声重建精确匹配历史SHA，另2份复用，无新流。没有拟合或Reward训练信息。

## 6. Command

主控`d59-execution/run-stage.py`分stage运行config/cpu/readiness/gpu并固定revision r3；remote入口`code-r3/supervise.py`，原始命令、配置与不可重复claim见launch receipts。结果使用封存`analyze.py`及主控独立标准库`independent-result-check.py`复算。历史运行不可直接重放；新实验须使用新预算和身份。

## 7. Results

| 条件 | P0 | 均值PM | 变化PV | 完整P1 |
|---|---|---|---|---|
| u=.4，4个合格案例 | 2正确/2反向 | 2正确/2反向 | 1正确/3反向 | 4正确 |
| u=.1，3个合格案例 | 1近零/2反向 | 1正确/1近零/1反向 | 3反向 | 2近零/1反向 |

弱条件另1个Native不合格。PM保留aa/e58，PV修复900且损坏aa/e58；32d0ce83主条件PM/PV均反向、完整P1正确。完整分差、逐流值、实际赢家图像见主控报告（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/spatial-swap-result-d59.md`）。

DiNa68=4技术+64科学，嵌套骨干68包含其中，LOAD1；其他模型前向/拟合/训练0。GPU472.181秒，CPU构造1.886秒；94文件12.98MB全部回收，137预约全部完成，六组冻结状态匹配，最终锁空闲。主控从原始分数以精确有理数复算，240字段一致。

## 8. Analysis

本次两单一组成均未保留全部4个主条件赢家。32d0ce83的修复依赖完整组合，90070ef0的变化项已足够；因此作用随案例而异。四端点J提供实际量化评分的可加性检验，仍需Anchor可计算的事前预测来形成核心机制。普通非线性配对回归为强竞争解释；本项不估人口胜率。

## 9. Problems

独立审查发现共享pipeline模块误拦截，已在模型调用前修复。R2真实CPU构造因零坐标的FP64抵消残差触发严格端点门；R3用预先生成的error-free减法高低项审核，PM/PV字节保持修复前16个独立SHA，原失败保留。主控原delta端点检查未覆盖m+v的问题亦已记录并补全。详见主控报告，不把测试通过等同于科学结论。

## 10. Next Steps

关闭原四对上的分解/比例搜索，不升级均值独占、空间独占或通用交互为核心创新。下一项先审查未按REC成功筛选的候选与普通强非线性基线的可用性，要求合法Anchor量能产生事前可推翻预测，再安排新的验证。当前无需GPU或服务器。

## 11. Sources

- `raw/projects/latentatlas/d59-spatial-swap-20261018-r1/final-snapshot/`，原件及recovery manifest。
- `docs/latentatlas-anchor-theory-2026-10-17/spatial-swap-result-d59.md`及`d59-execution/`全部执行/核验记录。
- [latentatlas-feature-readout-d56-20261018](latentatlas-feature-readout-d56-20261018.md)、`latentatlas-theory-map`、`latentatlas-research-decisions`、`latentatlas-paper-framework`。
