# Latent Reward Channels 规格审计与冻结 MVP 实验

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

验证公式、梯度、噪声坐标、通道和泄漏，再判断冻结特征上的候选方法是否值得升级。执行成功、产物一致、统计效应与科学Go分开。

## Config

[历史配置摘要](../../configs/experiments/latent-reward-channels-initial-audit.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

CPU可解Gaussian/离散prior。真实D2：固定32/8/8 prompts×4 seeds、192张512图；test为完整留出背景/风景家族。A/B1使用sampler endpoint；B2用同PNG的两个VAE posterior.mode，scale .13025/.18215。A/C冻结D64特征，train K16、val/test K64。PickScore训练集标准化，ImageReward独立评价。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

- A0 clean optimum8.25、posterior optimizer clean6.0；机制错位成立，精确校正方差366。
- B0 2160记录含360 PSD不可行；独立补充证明均值/方差一致仍可有critic期望误差。
- C0 matched：35/35控制通过，44/50主拟合未收敛；无稳定categorical优势。A1共1960轨迹，group存在负结果。
- A2/A3：test group bias²点估计均未优于pointwise，无稳定独立效用改进；A4 No-Go。
- B1：已知affine校准缩小几何误差；不等于实际生成轨迹收益。B2：低噪声额外通道收益、高噪声canonical误差回退，任务效用不稳；B3 No-Go。
- C2：categorical较训练Gaussian/pairwise NLL更低，但相对p=.5无可靠优势，一致性没有稳定额外收益；扩大No-Go。
- 核心测试241通过；具体CI、逐prompt指标与补充诊断见最终报告，未把重叠测试数相加。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

Research gap仍在真实可学习性：精确oracle反例成立不保证有限数据学习方法有效。Metrics的estimand逐列区分；有限witness MMD²、posterior NLL与clean候选选择效用不互相替代。八prompt、单一heldout家族、C0未收敛、B2单seed/MC4限制推断；C2的真实feature posterior偏差无法由现有输入直接识别。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本轮停止。未启动A4/B3/扩大；下一阶段无GPU需求。新研究方向需另立协议，不用剩余预算自动扩展。参见`latent-reward-channels`（原wiki关联）。

## Sources

- [来源快照](../source-snapshots/latent-reward-channels-initial-audit.txt)，原页面定位 `wiki-store/wiki/experiments/latent-reward-channels-initial-audit.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
