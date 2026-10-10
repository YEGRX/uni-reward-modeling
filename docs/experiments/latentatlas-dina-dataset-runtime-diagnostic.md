# DiNa 数据任务与推理契约诊断

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

定位 DINA0 接近随机的原因。Research gap：区分数据标注错误、任务/分布迁移与官方推理设置差异。用户决定后续采用 DiNa，组内 Critic 缺失不再阻塞该路线。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-dina-dataset-runtime-diagnostic.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

历史 consumed DIAG643 + EXTERNAL2619；固定 datapointai revision `0e757688c64ff6ee7c412e8b810cdbded2751dfc` 的 README。没有读取 retired future、旧 official TEST 或 mixed raw parquet。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

Baseline/metrics：原K4 accuracy50.420%，反号49.580%；四个单次noise accuracy50.344%–50.477%。上游行身份与方向一致。86/2619在四次噪声中出现严格正负翻转，1178对四次均错；19对平均分差为零。输入清单6524图均512×512。DIAG投票权重与方向全部一致，按共识程度分组的准确率不单调。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

数据来源为参考图驱动的身份保持生成，full版等权且未筛选；DINA0只给提示词/候选图并评估Overall Preference。任务信息和分布不匹配是待验证假设，不能把Prompt Alignment定义套到Overall Preference。固定官方静态示例u=.1与论文默认t=.4不同；原实验不是论文主表复现。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

用户随后提供完整SRC0/SHIFT0/REG1新协议；当前来源准入状态见 [latentatlas-dina-src0-source-domain-parity](latentatlas-dina-src0-source-domain-parity.md)。新协议允许历史HPDv3 test用于development；用户进一步授权无法联系作者时自主解决。完整test与预处理已在读行前冻结，实际14,400对，图像下载中；论文精确绑定仍不确定。

Possible improvement：先固定 HPDv3 原图、checkpoint、t=.4和预处理，核查源域能力，再比较迁移。源域成功不能当作fresh外部泛化；旧DINA0 negative保持，不启动DINA1。

相关：`latentatlas`（原wiki关联）、[latentatlas-dina0-r1-native-qualification](latentatlas-dina0-r1-native-qualification.md)、[latentatlas-glc0-group-latent-critic-native-qualification](latentatlas-glc0-group-latent-critic-native-qualification.md)。

## Sources

- [来源快照](../source-snapshots/latentatlas-dina-dataset-runtime-diagnostic.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-dina-dataset-runtime-diagnostic.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
