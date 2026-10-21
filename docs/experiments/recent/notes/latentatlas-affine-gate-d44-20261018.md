> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# D44：完整仿射接口的冻结选择解释淘汰

## 1. Date

2026-10-18。当前状态：**CPU/GPU执行、资产回收、主控审计及独立原始分数复算完成。** 事前判据为 `RETAIN_FITTED_PROCEDURE_DIFFERENCE_ONLY`。GPU阶段结束，后续本地理论工作无需服务器。

## 2. Purpose

R15中REC在同一DiNa合同下修复了旧pointwise和reflect Spatial5接口的一些候选反选。D17证明REC覆盖含边界bias的完整2448参数仿射类，旧Spatial5与它并不嵌套。本次补上这个强普通对照，检验这些案例能否由完整仿射拟合解释，再决定理论应研究什么剩余现象。

## 3. Code Version / Commit

分支 `codex/latentatlas-d44-affine-gate`，未提交；保留已有修改。实现位于 `scripts/latentatlas-affine-gate-d44-20261018/`；执行源SHA见 `docs/latentatlas-anchor-theory-2026-10-17/d44-execution/root-implementation-review-v2.json`。方案与roster保持封存身份。

## 4. Dataset / Input

Cosmos原FIT64/VAL64同图Clean配对，SD3.5 T0已缩放teacher，FIT通道方差沿用原R3数值。固定4组/4对/8图来自已反复消费的DEV，按原前两流Native/REC同向、两旧线性接口反向选择；与FIT/VAL无交集。各图保留原latent网格。研究源是同图Clean；DiNa的u=.4/.1加噪条件不等同真实生成器Noisy State。

## 5. Parameters

完整3×3 zero-padding仿射：144源特征、8个边界mask、截距，共2448系数。FIT-only逐图等权统计；λ∈{0,.001}，仅VAL坐标NMSE选点。部署FP32物理matmul+bias后一次BF16转换。对照Native T0、REC1000、正式A2/.001/2500；A2有历史额外训练/搜索暴露。

固定两个评分条件与每图原前两流种子，共用各方法epsilon。主端点为两流均值候选选择与分差误差。方法margin绝对值≤.0625记近零，Native绝对值<.125记低信号。仿射4例全恢复则停止用这些案例主张非线性必要；至少2例仍严格反向且REC正确只保留拟合程序差异；其余未决。条件依赖另报，不估总体成功率。

## 6. Command

主控按封存配置一次启动；命令、配置与PID见原始 `gpu-launch-intent.json`。GPU限制1800秒，DiNa≤136，REC/A2各≤12，文本≤12；VAE、生成、训练为0。CPU上限45分钟/8线程/8GiB、仿射预测≤144。不自动重试。

## 7. Results

CPU：FIT访问64、VAL预测128、科学仿射预测8，总136。λ0的VAL NMSE为0.12350105068122784；λ.001为0.12358348639744852；按预设规则选择λ0。152个中心化设计方向数值满秩、截断0，最小特征值4.5412e−6。选定文件SHA `78bb08840b805accb99b66d0622de46d3fada62d088acbba43e94deb99963f02`。

冻结DiNa的两流平均候选margin如下，定义为左图分数减右图分数。“正确”指与Native同向。

| Pair前缀 | u | Native | 完整仿射L | REC1000 | A2 |
|---|---:|---:|---:|---:|---:|
| aa0c08c7ac48 | .4 | −.250000 | +.640625 反向 | −.203125 正确 | +.125000 反向 |
| 32d0ce8391c8 | .4 | +.531250 | −.562500 反向 | +.281250 正确 | +.562500 正确 |
| e58f945b016c | .4 | +1.031250 | −1.000000 反向 | +.625000 正确 | +.546875 正确 |
| 90070ef0157b | .4 | −.625000 | +.156250 反向 | −.437500 正确 | −.578125 正确 |
| aa0c08c7ac48 | .1 | −.265625 | +.625000 反向 | −.031250 近零 | −.031250 近零 |
| 32d0ce8391c8 | .1 | +.062500 低信号 | −.437500 不判 | −.031250 不判 | .000000 不判 |
| e58f945b016c | .1 | +.375000 | −.906250 反向 | −.062500 近零 | .000000 近零 |
| 90070ef0157b | .1 | −.234375 | +.578125 反向 | +.125000 反向 | +.093750 反向 |

u=.4的L恢复0/4，L反向且REC正确4/4，超过事前至少2例的继续阈值；A2正确3/4。u=.1的3例Native合格案例中，REC/A2各2例近零、1例反向，严格正确0例。四例等权分差MAE（含低信号例）：u=.4时L/REC/A2为1.19921875/.22265625/.234375；u=.1时为.87109375/.28125/.25。

实际使用DiNa136次（技术8＋科学128）、REC8次、A2 8次、文本12次（3个编码器各4次）；VAE、生成、训练均0。监督总墙钟510.178秒，低于1800秒上限；没有重试。303项预约全部成功完成，另列BACKBONE136为同一次DiNa评分的内部调用记录，不重复计为评分。GPU结果64文件、17,680,261字节回收SHA全部匹配，GPU进程查询为空。

主控核验与独立标准库实现均复算全部136条分数、40项历史逐值重放、8项冻结状态回执及文本指纹。4份文本缓存中的8个返回embedding张量额外逐字节重哈希；token/mask以重建回执与三份历史回执核对。独立审查未重新执行CUDA。CPU产物227项独立检查覆盖NPZ、VAL聚合和BF16输出身份，未重新拟合或从源输入重跑预测。

## 8. Analysis

完整仿射对照补齐了旧基线的模型类缺口；在这4例的原评分条件下，REC仍有真实选择增量。当前保留的是拟合程序差异：所选L失败不能排除整个仿射类，A2修复3例也使普通非线性回归、优化及正则化成为必要竞争解释。λ0设计条件数约6.87×10⁶；λ.001约3.11×10⁴而VAL略差，固定选模规则保持，未事后换λ追求Reward结果。

跨条件结果把理论目标具体化为候选对误差的条件响应。设Native margin为n_u，方法margin为m_u，e_u=m_u−n_u，则m_.1−m_.4=(n_.1−n_.4)+(e_.1−e_.4)。现有分数的精确有理数分解表明：aa例Native绝对margin略增，REC仍进入近零；e58例Native margin收缩与近零同时出现；900例Native margin变化和方法误差变化共同伴随反选。因此单独以“Native margin统一收缩”概括本轮现象不成立。该恒等式是有限bank记账，不作因果分解或新定理。

4例为事先按历史结果选出的已消费DEV；u=.1使用本轮固定同噪声bank，范围限于同图Clean接口的两种DiNa条件。`latentatlas-theory-map`与`latentatlas-paper-framework`据此区分功能差异、真实Noisy部署和核心创新。

## 9. Problems

原文本条件张量未取得，用户明确批准重建12根；每个prompt需精确匹配原8项指纹。独立代码审查发现跨输出目录重置调用计数，已修成固定授权唯一claim并复测。远端合成测试因同步落盘超30秒，保持会话连接后28项全过，127.803秒；无真实模型调用。不得把调试计为科学运行。

## 10. Next Steps

返回理论：研究合法坐标Anchor信息能否对同一个接口的多条件候选差分误差给出可估计、非循环的预测。与普通非线性共享回归、正则化及读出条件敏感性逐项比较。继续条件是得到超出既有工具的新可检验关系；若只将未知敏感度或已观测误差代入margin界，则停止该候选。本轮不扩样、不更改λ，不开启新模型调用。核心创新仍待建立，长期目标保持。

## 11. Sources

- `docs/latentatlas-anchor-theory-2026-10-17/contribution-discriminator-d44.md`
- 同目录 `affine-gate-roster-d44.json`、`affine-gate-review-d44.md`
- 同目录 `d44-execution/` 的授权、实现/独立复核、原条件指纹、进度与启动回执
- `raw/projects/latentatlas/d44-affine-gate-20261018-r1/`：CPU/GPU原始产物、封存配置、调用账本及回收清单
- GPU原始结果独立复算（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/d44-execution/gpu-independent-result-review.md`）
- 同执行目录 `score-analysis.json`、`root-execution-audit.json`、`condition-change-decomposition.json`、`cpu-independent-output-review.md`
- 主控理论取舍§38.5（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/theory-to-decision-mainline.md`）
- `latentatlas-research-decisions`、`latentatlas-current-evidence-map`
