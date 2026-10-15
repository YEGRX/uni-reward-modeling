# Framework v4 奖励反馈后验恢复固定验证 Reward Feedback Posterior Recovery

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

Research gap：同一最终偏好风险如何组合优化/参考/迁移/统计误差；条件矩匹配阶如何影响反馈任务；错误校准law是否留下迁移地板；偶数probe及未知截距的信息边界。A/C为主干，B仅接入条件通道迁移，无新方法线或网络。

## Config

[历史配置摘要](../../configs/experiments/latent-reward-channels-paper-framework-v4-validation.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

有限clean(U,J)与source(A,L)，显式Q/R生成单输出原joint；r2/r3/r1固定格。CAL四条件单元、两校准law/n16/128，各128块、seed42051009，所有方法同块；512块共147456数学样本。AUD两独立Binomial、全129²计数。真实资产只引用已有资格，不重新全库审计。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

| Formula / comparison | Predicted / observed / error | Status |
|---|---|---|
| F4/19–23/26 COMP | 四风险6.91866e-7/2.81318e-7/1.59163e-6/5.35388e-7均在界内；posterior重构≤1.11e-16；优化gap1.0082185e-4对应直接目标差 | SUPPORTED_IN_SPECIFIED_MODEL |
| 错误KL相加 | p(.3,.7)、v(.08,−.04)：双步KL .00623314 > 两倍单步 .00307139 | REFUTED_BY_COUNTEREXAMPLE，仅错误三角式非F22 |
| F16–18/27–36 ORDER | η.3 r2/r3风险6.9186556928e-7/1.3780732060e-9，低阶条件矩相同；F35误差≤2.6e-20；70位固定比值接近正系数 | SUPPORTED_IN_SPECIFIED_MODEL，非一般渐近证明 |
| F13充分非必要控制 | 完整jointKL .09151622，utility posterior差5.55e-17 | 固定任务比完整kernel相等更弱 |
| CAL错误law n128 | pool7.4979891e-7、MLE7.2184354e-7，精确迁移参考6.9186557e-7 | 有限观察与非零地板相容，不由两n证明极限 |
| CAL正确law n128 | pool7.0187870e-8、同信息MLE3.4256092e-8；配对差3.5931777e-8，SE6.1761118e-9 | 强baseline优势保留，不同law分栏 |
| F38–40 AUD | 偶数和式投影=MLE，误差1.92e-15；强probe风险1.3699047e-6仍劣不修复6.9186557e-7，弱/correct-baseline负格保留 | SUPPORTED_IN_SPECIFIED_MODEL |
| 未知c边界 | (.4,0)与(.3826766543,.12)相同probe却target pair差.00454534475；g=eta时任务差2.22e-16 | 已知c假设撤销为ASSUMPTION_FAILED；控制支持信息边界 |

512个CAL MLE解最大gap1.0767e-13（阈值1e-9），78端点解合法；AUD gap≤1.18e-16。321保存核验PASS，不称321个独立实验。

完整报告与三图（外部来源定位：`../../scripts/latent-reward-channels/outputs/paper-framework-v4-validation-20261009/report.md`）；CAL逐块配对（外部来源定位：`../../scripts/latent-reward-channels/outputs/paper-framework-v4-validation-20261009/calibration-paired.csv`）；CAL MLE gap（外部来源定位：`../../scripts/latent-reward-channels/outputs/paper-framework-v4-validation-20261009/calibration-MLE.csv`）；AUD全计数（外部来源定位：`../../scripts/latent-reward-channels/outputs/paper-framework-v4-validation-20261009/audit-counts.csv`）。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

同一实际Y law的root-osc误差上界允许相关与抵消；优化扰动增加KL却降低pair风险，不是风险加性分解。增加错误校准law样本不能自动提供部署条件law；正确law信息与同信息MLE的优势需分开。偶数probe需要已知截距，任务可识别性弱于参数可识别性；原source接口合法域与参数盒/复合核范围分别报告。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

固定四项已完成，不新增方法/参数搜索或获取新真实观测。ChatGPT维护理论修订与一般证明。两个n和三个高精度点不称极限/minimax证明或fresh视觉确认；不自动执行64次forward。

新增wall **1.972862417秒**、CPU **1.870084秒**；累计wall **263.579702167秒**。COMP+CAL .019092秒、ORDER+AUD .085402秒、shared1.868369秒，15秒及6/4/5内；失败和恢复纳账，旧累计不重置。0GPU/远端/付费/真实forward/图像/特征/训练。无需服务器，未核查旧服务器状态。

相关：`latent-reward-channels`（原wiki关联）；[latent-reward-channels-system-v3-validation](latent-reward-channels-system-v3-validation.md)；[latent-reward-channels-core-v2-validation](latent-reward-channels-core-v2-validation.md)。

## Sources

- [来源快照](../source-snapshots/latent-reward-channels-paper-framework-v4-validation.txt)，原页面定位 `wiki-store/wiki/experiments/latent-reward-channels-paper-framework-v4-validation.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
