# ABC R3.6 结构统计修复固定验证 Structural Statistical Repair

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

Research gap：公共一阶残差结构能否在同样本上消除普通CR2的低阶估计噪声；真正已知矩如何改变正值积分信息权限；小额零probe能否改变任务不可识别性而保持同总预算。ChatGPT维护理论，Codex独立验证固定预测，不新增理论、网络或参数搜索。

## Config

[历史配置摘要](../../configs/experiments/latent-reward-channels-r36-structural-statistical-repair.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

R3.5原六条件单元NPZ，n16/n128各2048块seed350109，完整复用而不重新采样。另新增已批准四Z未知形状有限模型、偶阶正值积分状态与完整二项计数。均为finite/formula-style或数学MC；真实缓存资格只读继承，不能称视觉收益、fresh确认或ICML新颖性。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

| Probe | Prediction / observed / strong baseline | Status |
|---|---|---|
| E-AC36 | 原n16/eta.6：sampleCR2 .0001393903506、SR2 .000002275525474、prior .00003332609271；配对SR2−CR2=-.0001371148251，SE3.15242e-6。约束CR2=SR2只记一个身份；knownCR2/fullBayes更强 | SUPPORTED_IN_SPECIFIED_MODEL |
| E-A36 | A36-4系数.0842208705944392独立核对；n1 eta.01普通CR2 KL/eta²=.08424699099，SR2=.0000003368853690；有限余项单列 | SUPPORTED_IN_SPECIFIED_MODEL；非一般渐近证明 |
| E-C36 | 未知形状主n16/eta.6：PCV2.106467051e-6 vs同信息SR2 2.161225486e-6，配对差-5.47584e-8、SE1.78693e-8；eta.3差未超约1.3SE。不给theta/target prior | SUPPORTED_IN_SPECIFIED_MODEL；很小数学MC信号 |
| C controls | theta0 reference风险0，PCV2.214432612e-6更差；错误结构SR2/PCV约1.40/1.42e-5，劣于reference1.03e-5和raw3.49e-6；正确新均值PCV是额外权限 | 正确baseline支持；旧公共均值ASSUMPTION_FAILED，不是定理反例 |
| E-M36 | 精确已知矩的四格积分正值/无偏与方差界核验通过；同批经验均值PCV=rawMGF=1.1817618415159772；下界只检查指定输入 | SUPPORTED_IN_SPECIFIED_MODEL；不等于posterior无偏或独立minimax证明 |
| E-B36 | N192/Delta.12小额零probe .001293206612优均匀三probe .001575549183但逊两probe .001216597132；弱Delta.03 null .00008998712685最好。零probe区分旧不可识别对 | SUPPORTED_IN_SPECIFIED_MODEL；不等于完整内容核恢复 |

226核验行均达冻结容差，不计作226独立研究实验。保存posterior从原joint重算risk最大误差2.22e-16，raw矩/配对均值SE复核误差0；原始近零oracle负值保留。

单份完整报告、三张PNG/PDF图与底层CSV/NPZ（外部来源定位：`../../scripts/latent-reward-channels/outputs/r36-structural-statistical-repair-20261008/report.md`）；实际成本（外部来源定位：`../../scripts/latent-reward-channels/outputs/r36-structural-statistical-repair-20261008/source-and-cost.json`）。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

普通样本CR2的失败不是本模型所有校正都不可行：同数据保持公共结构可消除一阶噪声。但同结构CR2与SR2等价，不能重复算创新优势。已知数值矩、已知结构、经验矩三种权限分开；PCV的正值积分无截断地板不代表每个n每个参数都优于结构CR2。B新增probe改变识别合同，与有限预算是否提分分开。

知识仍围绕noisy latent reward反馈后的效用差、任务作用与偏好概率，不是高维clean分布恢复。历史真实A/B无优势、C旧gate未完成合格机制验证、旧No-Go不变。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本轮未发现满足完整假设的数值反例要求ChatGPT修订；预定错误结构和正确baseline保留。理论泛化、证明与新颖性仍由ChatGPT维护。最关键缺证是实际reward residual的合法公共一阶结构或解析条件矩资格，不自动获取或申请更大实验。可选AC36-4下界补充、B36-6/7渐近实验未执行。

测得新增wall **3.440691332秒**；加未计时解析失败的保守1秒，扣账 **4.440691332秒**，继承累计 **257.960664041秒**。各阶段3/8/6/8和总25秒内；旧预算未重置。0GPU/远端/付费/新真实图像特征/head训练，64前向未授权未执行。后续CPU或无服务器，未核查旧服务器状态。

相关：`latent-reward-channels`（原wiki关联）；[latent-reward-channels-r35-task-sensitive-validation](latent-reward-channels-r35-task-sensitive-validation.md)；[latent-reward-channels-r34-feedback-task-channel](latent-reward-channels-r34-feedback-task-channel.md)。

## Sources

- [来源快照](../source-snapshots/latent-reward-channels-r36-structural-statistical-repair.txt)，原页面定位 `wiki-store/wiki/experiments/latent-reward-channels-r36-structural-statistical-repair.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
