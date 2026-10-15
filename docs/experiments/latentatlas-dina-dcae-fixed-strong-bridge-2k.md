# DC-AE 固定强 Bridge 函数类定位预实验

归档日期：2026-10-10；证据层级：主要最终报告＋历史页面。

## Experiment

只读旧 B2000（P0＋T1），固定 64 FIT/64 VAL Anchor、T1、前 2000 步日程与评分集，只把映射改为 12 个残差块的 S，检验函数类／归纳偏置变化的坐标与行为效应。结构同时改变参数量和计算量，因此不能单独归因于容量。相关背景：[latentatlas-dina-dcae-ab-budget-response-4k](latentatlas-dina-dcae-ab-budget-response-4k.md)、[latentatlas-dina-dcae-target-spatial-factorial](latentatlas-dina-dcae-target-spatial-factorial.md)。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-dina-dcae-fixed-strong-bridge-2k.json)，不是可派发GPU任务。

**输入与范围：** 开发集1,008对 / 28组 / 4流；64 FIT+64 VAL

64 FIT／64 VAL 互斥，并与当前 252 张开发评价图像无身份重叠；T1 固定目标、FIT-only W0，B 的前 2000 步学习率和 64,000 次抽样序列已按旧实际状态核对。评价 1008 对、28 个 connected groups、4 个 streams；旧 A/B/Native/G 逐行只读复用。旧 B 评价的 `clean=false`、外层 exit1、attempt uncertain 仍保留，其完整科学输出仅在原范围内获补充接受。缺失的 2026-09-28 Context Snapshot 不能作为已读来源；关键合同从冻结工件恢复。

## Result

**当前归档分类：** `JOINT_BEHAVIOR_GAIN_SUPPORTED_NOT_NEAR_NATIVE`

B→S Accuracy64.8562%→68.4276%，Native一致率77.7694%→83.9335%。



## Conclusion

参数40,080→889,424，结构与计算量共同变化；不是预算匹配基线或完整Latent Bridge复现。

完整指标、区间、成本和原失败见下方最终报告。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

用户2026-10-01另行授权的评价域坐标诊断见 [latentatlas-dina-dcae-strong-bridge-eval-domain-t1-localization](latentatlas-dina-dcae-strong-bridge-eval-domain-t1-localization.md)；该新 identity 当前BLOCKED，不改变本页前序封存结果。

本 identity 完成即停止。唯一后续建议是另行预注册同一评价图像上的 S/B 配对 T1 坐标诊断，先确定不读取偏好标签的目标来源；此处不执行。当前无 GPU 或远端服务器需求。

## Sources

- [来源快照](../source-snapshots/latentatlas-dina-dcae-fixed-strong-bridge-2k.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-dina-dcae-fixed-strong-bridge-2k.md`。
- [最终原报告文本](../reports/latentatlas-dina-dcae-fixed-strong-bridge-2k-final.txt)：路径仅为来源定位；其中历史状态以最终段落/追加回执为准。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
