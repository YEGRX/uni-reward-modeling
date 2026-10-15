# Strong Bridge 评价域 T1 坐标诊断

归档日期：2026-10-10；证据层级：主要最终报告＋历史页面。

## Experiment

research gap：冻结S2000的T1坐标误差改善是否从Anchor传递到固定评价域，及其与已有模型排序变化的关系。baseline为B2000小P0，metrics为normalized MSE、平均loss之比、paired group bootstrap；无新训练或Reward。前序 [latentatlas-dina-dcae-fixed-strong-bridge-2k](latentatlas-dina-dcae-fixed-strong-bridge-2k.md)，项目 `latentatlas`（原wiki关联）。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-dina-dcae-strong-bridge-eval-domain-t1-localization.json)，不是可派发GPU任务。

**输入与范围：** 既有开发评价252图；零新Reward评分

固定252唯一图像、1008物理对、28connected groups；与64FIT/64VAL不相交。只读复用原DC-AE latent、既有T1 sample/cache、B2000/S2000、FIT-only T0方差W0；payload/tensor/seed/route/hash已核。B40080、S889424参数，两个既定结构并非matched capacity。来源层确实解析已消费DEV中含人工标签的旧文件；分析manifest与模型margin表无人工偏好或correctness字段。历史R1访问范围unknown。

## Result

**当前归档分类：** `EVAL_T1_CHANGE_INCONCLUSIVE`

B/S EVAL T1 NMSE0.309154/0.310404；相对下降−0.405%，95%约[−2.732%,1.994%]。



## Conclusion

FIT下降35.92%不外推EVAL坐标；没有新Accuracy或U必要性结果。

完整指标、区间、成本和原失败见下方最终报告。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

实验已完成，停止，不启动新实验。唯一后续建议（不执行）：在独立固定评价集上控制其他条件，只操纵Anchor覆盖以检验坐标泛化贡献；不能预先保证有效。当前无GPU或远端计算需求，服务器可关闭。

## Sources

- [来源快照](../source-snapshots/latentatlas-dina-dcae-strong-bridge-eval-domain-t1-localization.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-dina-dcae-strong-bridge-eval-domain-t1-localization.md`。
- [最终原报告文本](../reports/latentatlas-dina-dcae-strong-bridge-eval-domain-t1-localization-final.txt)：路径仅为来源定位；其中历史状态以最终段落/追加回执为准。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
