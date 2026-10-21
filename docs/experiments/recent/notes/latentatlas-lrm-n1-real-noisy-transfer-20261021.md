> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# LatentAtlas LRM-N1 真实Noisy-State冻结奖励迁移

## 1. Date

2026-10-21 13:49 Asia/Shanghai；真实实验完成并停止。

## 2. Purpose

已有Clean Anchor训练的REC/Affine能否直接处理FLUX真实中间状态并保留冻结DiNa的即时与终态选择？将raw noisy路径和当前clean estimate路径分开。

## 3. Code Version / Commit

分支codex/latentatlas-d44-affine-gate，保护原未提交修改，无新commit。原两项工程失败在raw保留；正式接续code-r3与source/prepare/score-spec绑定全部源码和权重SHA。

## 4. Dataset / Input

R1历史dev-01/dev-02，seed2026101601/1602，4条真实原轨迹。用实际保存的k21接续21–27，捕获k23/k26共8状态；4个终态逐位复现原生成候选。2个Prompt为统计单位，属于已消费DEV。

## 5. Parameters

原FLUX.1-dev，1024²/28step/guidance3.5/BF16；源σ=.4070784152/.1954545975；DiNa合法实际σ=.4002932608/.2001733035，两时间分开。正式REC和强Affine不训练，DiNa六项state冻结。A完整当前图桥、B当前估计REC、C raw noisy REC、D raw noisy Affine；Final为真正终态的对应时间T1。A/B/Final两流，C/D单确定性。

## 6. Command

真实运行由`control.py`按source_r3/prepare/score三个spec与1500/900/1200秒上限执行。日常复算只运行`analyze.py`和`independent_recompute.py`，不自动重启模型。完整命令与SHA见下方复现入口。

## 7. Results

正式 **CLEAN_ESTIMATE_BRIDGE_ONLY**。

| 路径 | k23同即时/Final | k26同即时/Final | Final regret（中/后） |
|---|---|---|---|
| 完整即时A | 2/2 | 2/2 | 0 / 0 |
| 当前估计REC B | 2/2 | 2/2 | 0 / 0 |
| 直接REC C | 2/2 | 1/2 | 0 / .09375 |
| 直接Affine D | 1严格+1tie，半分.75 | 1/2 | .03515625 / .1640625 |

B的两个流在四个相关单元均同向。C后期dev02反向；D中期dev01平局、后期dev01反向。C中期MAE5.9765625但margin MSE .06640625（优于B .166015625）；后期MAE缩至1.578125仍反向，不能只按分数接近判断功能。

新增DiNa64=56science+8tech，复用8Final；source实际30前向，原完整轨迹恢复4、完整新生成0，另一次中断generation start。源decode9/ref encode9、REC18/Affine9，训练/文本/人类评价0。含加载/失败的GPU阶段监督墙钟1983.474110秒；不是kernel计时或部署收益。

## 8. Analysis

当前估计桥支持本pilot早期选择保真，raw noisy的零训练直接迁移尚不稳定。A本身保留Final选择，因此这四轨迹不能简单解释为中间状态完全无终态信息。输入尺度差、训练支持域、噪声法则和函数敏感性仍是竞争解释，未做因果分离。Final仍是DiNa目标，R2人类有效性缺口保持。

## 9. Problems

root关键词计数门失败0 forward/334.615秒；日志Path拼接失败1技术+1生成science/371.406秒；原件与消耗保留。源坐标CPU BF16 scalar加法与CUDA有≤.0009765625差异，明确CUDA opmath后16项全等，实际输入未变。186资产/64input/64score SHA核验，40数组与两实现64汇总数值通过。

## 10. Next Steps

本轮停止，不新增noisy mapper、理论、D74、独立扩样、人类标注或成本benchmark。若另行推进，应以当前估计桥为强对照，并先解决当前任务所需的有效性/噪声合同问题；本轮未执行下一阶段。GPU结束且资产已回收，服务器可关闭，当前电源未知。

## 11. Sources

- `raw/projects/latentatlas/lrm-n1-20261021/user-request.txt`。
- `raw/projects/latentatlas/lrm-n1-20261021/completed-n1/`与逐资产recovery-manifest。
- [结果](../reports/lrm-n1-results.md)、[正式决定](../reports/lrm-n1-decision.md)、复现（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_N1_REAL_NOISY_TRANSFER/REPRODUCIBILITY/README.md`）。
- `latentatlas`、[latentatlas-lrm-r1-real-interface-qualification-20261021](latentatlas-lrm-r1-real-interface-qualification-20261021.md)、[latentatlas-lrm-r2-reward-validity-audit-20261021](latentatlas-lrm-r2-reward-validity-audit-20261021.md)、`latentatlas-research-decisions`。
