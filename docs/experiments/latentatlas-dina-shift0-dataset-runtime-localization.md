# DINA-SHIFT0 数据与运行协议诊断

归档日期：2026-10-10；证据层级：主要最终报告＋历史页面。

## Experiment

在SRC0源域qualified之后，以同一冻结DiNa checkpoint、PAPER_T04运行时、预处理及评分实现评估历史已消费EXTERNAL2619。区分dataset/task shift与runtime差异，不训练Reward、不把跨数据集泛化变为主线。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-dina-shift0-dataset-runtime-localization.json)，不是可派发GPU任务。

**输入与范围：** 2,619外部对 / PAPER_T04

仅旧DINA0 sealed surfaces/external/rows.json：2619行、5238图像身份；远端逐文件验证全部2,242,589,552字节，长度和SHA一致。未读取retired future12455或old TEST。

## Result

**当前归档分类：** `SOURCE_TO_EXTERNAL_PREFERENCE_TRANSFER_FAILURE_SUPPORTED`

外部Accuracy 51.3860%；中央90% [49.8814%,52.8888%]。



## Conclusion

保留外部迁移失败；不据此判定标签错误或所有DiNa无效。

完整指标、区间、成本和原失败见下方最终报告。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

SRC0及SHIFT0已完成；继续按原协议准备REG1的数据清单、固定规格和§63算力准入。在Anchor FIT only上先做20 warmup、50 REC及50 FUNC前后向步骤的成本评估，再估算16 fits；不得跳过准入直接正式训练。SHIFT0 external表现不阻塞REG1。表示配准与target Reward reuse尚无结果。当前为CPU准备阶段，GPU可释放；下个GPU阶段仍须按协议准入。

相关：`latentatlas`（原wiki关联）、[latentatlas-dina-src0-source-domain-parity](latentatlas-dina-src0-source-domain-parity.md)、[latentatlas-dina0-r1-native-qualification](latentatlas-dina0-r1-native-qualification.md)。

## Sources

- [来源快照](../source-snapshots/latentatlas-dina-shift0-dataset-runtime-localization.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-dina-shift0-dataset-runtime-localization.md`。
- [最终原报告文本](../reports/latentatlas-dina-shift0-dataset-runtime-localization-final.txt)：路径仅为来源定位；其中历史状态以最终段落/追加回执为准。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
