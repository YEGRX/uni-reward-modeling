# Latent Reward Channels R3.1：固定任务边界验证

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

ChatGPT维护给定理论；Codex独立核验有限模型预测、真实缓存假设与最小反例。Research gap：观测噪声如何改变clean效用差、接口任务作用和pair probability；不恢复完整clean分布，也不把toy当视觉确认。

## Config

[历史配置摘要](../../configs/experiments/latent-reward-channels-r31-task-boundaries.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

A：两点计数与27序列二维支持；B：二元source、连续合法U与两任务；C：16联合状态。真实只读为旧train32固定outer0 fit24/eval8，A M3/t1与M4、C categorical与固定一致性.1。旧val/test不选模，开发数据不fresh。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

- A：U无偏但J1系数−1/18，中点凸性失败；cap/clip期望偏差1/24与.0234375。有理数误差0，A-N14/18方差枚举误差≤4.441e−16。
- B：全部连续确定性最优MSE=.09025141459110135；全随机核=.07834166666666667，差−.01190974792443468。ell1/2无优势、ell3起出现；高信息两者0；scalar随机额外损失.06。
- C：主格相对最强B-only校准NLL下降.0076221229809127，真实I=.0077531760693810。artifact格NLL下降6.14509e−6而I=0；全部固定误差达标。

上述为SUPPORTED_IN_SPECIFIED_MODEL，没有给定假设内理论反例。有限数值支持不替代一般证明/新颖性审查。3个边界QP点的严格合法部署资格不足，高信息点一阶残差还超预设容差，保留4行NUMERICALLY_INDETERMINATE。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

A说明凸处理会改变部署风险，而非新方法提分。B排除弱确定性NN解释，优势依赖固定非凸二任务与内部调用预算。C明确区分prediction gain和beyond-calibration information，校准伪改善是错误信息解释的最小反例。

真实A描述风险可读但未获独立覆盖证书；B原生几何NOT_IDENTIFIABLE_WITH_CURRENT_ASSETS；C只读两head训练anchor/epoch不匹配，方法归因ASSUMPTION_FAILED，均值NLL差+.00464515。缺reverse及匹配nuisance资产，不伪造；条件矩可观测但OBSERVABLE_BUT_UNCERTIFIED。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

Possible improvement仅为观测需求：如果只取得一个成组真实观测，优先固定prompt四候选的独立K16噪声块（64次冻结LRM前向），用于区分同内容MC与稳定相对残差，不能证明跨prompt泛化。需要另行授权新前向/特征与资源，本轮不自动获取。理论修改继续交ChatGPT。

## Sources

- [来源快照](../source-snapshots/latent-reward-channels-r31-task-boundaries.txt)，原页面定位 `wiki-store/wiki/experiments/latent-reward-channels-r31-task-boundaries.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
