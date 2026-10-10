# ABC R3.4 反馈与任务通道固定验证 Feedback and Task Channel Validation

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

Research gap：noisy reward优化后，即使新效用prior已知，within-utility likelihood变化是否仍令偏好posterior错误；reward probes能识别哪些任务核及需要多少统计信息。ChatGPT维护理论；Codex独立固定数值/机制检查，不扩网络。

## Config

[历史配置摘要](../../configs/experiments/latent-reward-channels-r34-feedback-task-channel.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

四状态有限joint、四Gaussian成分、三效用三输出冻结核、两probe二项计数。Exact enumeration / known-model / formula-style；不是视觉数据训练。原endpoint、双VAE和旧NPZ仅只读字段/资格检查。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

| 验证 | predicted / observed及baseline | 状态 |
|---|---|---|
| AC | V/UV同mean .537049567和总KL .043053014；posterior KL分别约0/.009634065。UV pair excess预测.002154038098144443、观测.002154038098144073；prior-only/最强Y1校准NLL .6807228824，repair/fulljoint oracle .6785688443 | SUPPORTED_IN_SPECIFIED_MODEL |
| G | 实际h条件均值-.5/-1.5/.5/1.5；GH40/80平均posterior KL .0083553129846/.0083553126976，差2.87e-10；mixture/formula logit误差≤1.14e-13 | SUPPORTED_IN_SPECIFIED_MODEL |
| B | 零probe marginals相同但核不同；三probe cond25.60154，核恢复误差8.88e-16。target0/.3 pair excess2.454e-8/2.950e-6，宽界.015122保留；完整内容差.2且utility核相同的控制保留 | SUPPORTED_IN_SPECIFIED_MODEL |
| S | 主格b.2/n64逆MSE .04982288378劣于零.04；合法投影/预定选择.02415184255；oracle0。42.0042%超出已知参数类，不等于非法Bernoulli核比例；clean-labeled另列不同权限 | SUPPORTED_IN_SPECIFIED_MODEL |

113核验达到固定容差，不是113独立实验；无本轮数值失败。近零负KL、不利逆格及保守风险界保留。没有满足完整假设的理论反例；有限点不证明渐近/连续完备性/整个minimax下界。

完整报告、底层CSV/JSON/NPZ及三张PNG/PDF主图（外部来源定位：`../../scripts/latent-reward-channels/outputs/r34-feedback-task-channel-20261008/report.md`）。实际成本（外部来源定位：`../../scripts/latent-reward-channels/outputs/r34-feedback-task-channel-20261008/source-and-cost.json`）。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

排除了本模型中仅用reward mean或total KL描述posterior危害的解释。Residual-aware等于known-joint oracle是公式验证，不是学习算法胜过oracle。奖励倾斜可识别utility条件作用而不能自动恢复整个content channel。有限计数逆的方差代价、参数类合法性和投影收益需分开。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本轮无需ChatGPT修订已限定公式。最值得新增的是冻结实际scorer/接口的reference与reward优化后同效用条件观测表，区分prior-only与within-utility变化；单孤立图像不够。本轮不获取、不采购，64新前向未授权未执行。旧No-Go和真实方法无优势、C旧gate未有效判别保持；后续无需GPU，未检查旧服务器状态。

相关：`latent-reward-channels`（原wiki关联）；[latent-reward-channels-r33-channel-structure](latent-reward-channels-r33-channel-structure.md)；[latent-reward-channels-r32-fixed-validation](latent-reward-channels-r32-fixed-validation.md)。

## Sources

- [来源快照](../source-snapshots/latent-reward-channels-r34-feedback-task-channel.txt)，原页面定位 `wiki-store/wiki/experiments/latent-reward-channels-r34-feedback-task-channel.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
