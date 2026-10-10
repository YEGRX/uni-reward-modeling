# 冻结 Projector 机制审计与第二评分函数复用

归档日期：2026-10-10；证据层级：主要最终报告＋历史页面。

## Experiment

阶段A审计总体准确率相近是否掩盖逐样本判断、坐标表示和DiNa内部功能差异；阶段B测试同一冻结Projector经SD3.5 decoder接入固定PickScore。研究缺口（research gap）是任务兼容是否延伸到一个新的读取函数，而非寻找新的通用架构。新增训练0。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-frozen-projector-mechanism-and-readout.json)，不是可派发GPU任务。

**输入与范围：** 开发集1,008对 / 28组；DiNa四流；PickScore独立口径

只使用旧Pilot已消费1008对、28完整关联组、252图像身份；A3/A4为事前固定32对子集。原图278条别名保留。单训练种子、单打乱对照，没有新增科学样本。

caption经明确amendment允许的一次metadata-only全源字节扫描提取，只物化白名单1008条pair_id/prompt。后续只读封存derived文件，未重新打开14400行来源、retired future12455或old TEST；不能宣称其余源文件字节零访问。

## Result

**当前归档分类：** `REUSE_INCONCLUSIVE`

统一DiNa REC/FUNC 72.793%/72.470%；PickScore REC/FUNC 64.58%/63.69%，复用均INCONCLUSIVE。



## Conclusion

PickScore是decoder→RGB路径。原B收尾exit1/cleanup NOT_PROVEN保留；后续CPU证据接受不改写原退出。

完整指标、区间、成本和原失败见下方最终报告。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本轮实验结束，不启动下一实验或旧16组。整理和验收已交付，每小时定时检查已删除；已向共享任务仅通报资源可用，不授权其他任务自行恢复。其他任务仍须遵守其用户的明确开始指令和共享锁。

## Sources

- [来源快照](../source-snapshots/latentatlas-frozen-projector-mechanism-and-readout.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-frozen-projector-mechanism-and-readout.md`。
- [最终原报告文本](../reports/latentatlas-frozen-projector-mechanism-and-readout-final.txt)：路径仅为来源定位；其中历史状态以最终段落/追加回执为准。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
