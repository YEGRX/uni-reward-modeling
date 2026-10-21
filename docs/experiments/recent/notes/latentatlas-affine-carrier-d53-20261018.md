> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# D53 仿射投影与冻结 Reward 选择

## 1. Date

2026-10-18。实际执行与主控独立复算完成。

## 2. Purpose

区分REC成功能否保存在其仿射部分。D44已知原四对中普通仿射L失效、REC成功；固定FIT64拟合REC输出的全仿射投影Q，直接测其RM赢家。

## 3. Code Version / Commit

当前分支codex/latentatlas-d44-affine-gate，专用未提交代码scripts/latentatlas-affine-carrier-d53-20261018/；源SHA清单在报告。不修改历史D44代码/原始结果。34项远端人工测试及独立代码审阅通过。

## 4. Dataset / Input

原Cosmos→SD3.5同图Clean FIT64、原已消费DEV4对8图；同一冻结DiNa，u=.4/.1，各2噪声流。同图参考Native决定为端点。不是独立测试或原生生成Noisy State实验。

## 5. Parameters

Q为3×3共享全仿射153特征×16输出，逐图等权、固定原mean/scale、λ0、rcond1e−10、rank152。FP64求解、物理FP32部署后BF16。Native门0.125，方法近零门0.0625，主条件u=.4。

## 6. Command

严格先supervise.py --phase 1，再fit_q.py --execute一次，主控矩阵核验并封存Q，最后supervise.py --phase 2。实际配置、命令及SHA见执行计划（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/d53-execution/implementation-plan.md`）及回执；不要重跑已消费的一次性阶段。

## 7. Results

主条件REC4/4保持，Q4/4严格反向；弱条件3个合格对中Q3反向，REC2近零1反向。Q解释FIT上P的96.864%加权中心化变化。七个合格pair×condition中，P−Q端点增益均指向Native；弱条件增益不足以形成可靠正确分差。

实际REC66、DiNa36、CPU拟合1、Q预测8；GPU860.5486s/1200s。文本/VAE/A2/生成/训练均0。GPU锁释放、最后利用率0%。

## 8. Analysis

指定仿射投影删除的部分对四次选择有真实作用。下一理论主线研究Anchor怎样学到功能相关的非仿射输出，以及冻结条件如何改变其过边界幅度。普通非线性回归仍为主要baseline；本结果不选择特定新网络。完整分差、公式、证据范围与原创性判断见主控结果报告（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/affine-carrier-result-d53.md`）。

## 9. Problems

审查阶段修复冻结均值复现守卫；后台元数据进程因WSL生命周期中断，0模型调用，之后保持远程连接完成全部阶段。独立矩阵核验是导出统计检查，不是原FIT重新拟合。开发案例和重复噪声的相关性保持。

## 10. Next Steps

D54聚焦一个可检验的Anchor-only理论条件，要求能区别普通非线性回归解释，避免把有向增益恒等式作为创新。此后同类固定小预算定位按用户授权自主执行。相关：`latentatlas`、`latentatlas-theory-map`、`latentatlas-research-decisions`、[latentatlas-affine-gate-d44-20261018](latentatlas-affine-gate-d44-20261018.md)。

## 11. Sources

- raw/projects/latentatlas/d53-affine-carrier-20261018-r1/recovery-manifest.json（192项绑定）。
- docs/latentatlas-anchor-theory-2026-10-17/d53-execution/independent-result-review.json（主控有理数分差及账本复算）。
- docs/latentatlas-anchor-theory-2026-10-17/d53-execution/cpu-root-numerical-review.json（矩阵、截距、部署载荷）。
- docs/latentatlas-anchor-theory-2026-10-17/d53-execution/root-coordinate-analysis.json（FIT/DEV输出差统计）。
- docs/latentatlas-anchor-theory-2026-10-17/affine-carrier-proposal-d53.md（批准及后续自主授权）。
