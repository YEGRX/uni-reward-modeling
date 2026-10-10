# Core v2 有限转移与完整MLE固定验证 Finite Transfer and Full MLE

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

Research gap：T2/T4复核后有限风险转移与全半径条件是否得到正确的数值输入；相同条件样本和公开参数类下完整MLE与池化正值反馈（Pooled Positive Feedback, PPF）有何有限差异。不是新网络或真实视觉收益验证。

## Config

[历史配置摘要](../../configs/experiments/latent-reward-channels-core-v2-validation.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

有限U±1、Z(-.8,-.4,.4,.8)，原始pstar(u)p(z|u)Q联合表；四(u,s)条件clean residual单元。Proof n1全256序列；baseline四格各64数学重复。模型类/参考同权限，不给数值矩、true参数、target prior或target labels。真实缓存仅引用已有资格，不新增审计/分箱/反推posterior。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

| Formula / comparison | Predicted / observed / numerical error | Status |
|---|---|---|
| V2-14/16、B1/B2 | 四输入合法，pz最小.1875；mu=(.4+.96xi+.96tau u)s；参考不含参数，误差≤1.11e-16 | SUPPORTED_IN_SPECIFIED_MODEL |
| V2-B7 | theta导数/eta²绝对值.05916145–.05922405 ≥.04；tau/eta .14789759–.14806020 ≥.09；缩放双路径误差≤3.17e-13 | SUPPORTED_IN_SPECIFIED_MODEL，仅18点 |
| V2-C1/22 | 独立PMF得LR二阶乘积；误差≤1.11e-15；期望Fisher=n diag(160,64,64)，非样本Hessian | SUPPORTED_IN_SPECIFIED_MODEL |
| V2-18/13 | n1全256样本adaptive=pool；四采样方法转移下界0，reference下界1.668899032e-9、risk1.570565607e-7；pool risk1.864524468e-7更差 | SUPPORTED_IN_SPECIFIED_MODEL；零界非安全证书 |
| 主同权限n128/tau1/64 | adaptive1.573517544e-7、fullMLE2.198129748e-8；配对差+1.353704570e-7、SE5.365633086e-9 | MLE更好，保留强baseline优势 |
| 必要控制 | 两个tau0固定格pool风险低于完整MLE，但reference更强；额外known-tau0 MLE单列。n16/tau1/64差仅约1SE；四格观察到pool/adaptive完全相同 | 不重复计方法胜利，不预设提分 |

121核验行全达容差，不计作121独立研究实验。256 full/128 restricted MLE最大gap分别3.172612883e-9/2.356762533e-9，全部数值合格，268边界解保留。保存joint重算风险最大误差2.29e-16；配对均值/SE误差0。

一页主结论、证据附录及两张PNG/PDF图（外部来源定位：`../../scripts/latent-reward-channels/outputs/core-v2-validation-20261009/report.md`）；逐块风险（外部来源定位：`../../scripts/latent-reward-channels/outputs/core-v2-validation-20261009/baseline-draws.csv`）；MLE参数/gap（外部来源定位：`../../scripts/latent-reward-channels/outputs/core-v2-validation-20261009/MLE-solutions.csv`）。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

相同数据/model-class权限下，完整MLE在偏离结构主格更强；两个精确结构固定格与tau方向估计噪声解释一致，但不证明一般渐近率。保守adaptive在这四格未启用阈值，不能称其适应机制已被识别。固定合法半径范围内n128两解析率表达完全重合；仅省略常数的理论示意，非实际NLL或全半径证明。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本轮执行任务完成。eta.1没有未知eta0(C0)证书；有限输入不能证明T2/T4一般minimax与ICML新颖性。理论修订/一般证明由ChatGPT维护，不自动补旧closure、扩大n或真实前向。

新增测得wall **1.975608375秒**、CPU **1.683989000秒**；继承累计wall **259.936272416秒**。Proof4/baseline6/shared5及总15内，proof+baseline计旧C、shared计旧shared；保留R3.6保守扣账，不重置。0GPU/远端/付费/真实前向/特征/网络训练；64forward未执行。后续无服务器需求，未核查旧服务器状态。

相关：`latent-reward-channels`（原wiki关联）；[latent-reward-channels-r36-structural-statistical-repair](latent-reward-channels-r36-structural-statistical-repair.md)；[latent-reward-channels-r35-task-sensitive-validation](latent-reward-channels-r35-task-sensitive-validation.md)。

## Sources

- [来源快照](../source-snapshots/latent-reward-channels-core-v2-validation.txt)，原页面定位 `wiki-store/wiki/experiments/latent-reward-channels-core-v2-validation.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
