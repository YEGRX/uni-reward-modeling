# DC-AE 同源 Anchor 64→256、固定2000更新与新评价组

归档日期：2026-10-10；证据层级：主要最终报告＋历史页面。

## Experiment

实验身份：DINA_DCAE_STRONG_ANCHOR64_VS256_FIXED2K_NEWGROUPS_PILOT_R1。
固定当前 Strong Bridge、T1、初始化、W0和2000更新日程，只把同源FIT64嵌套扩为FIT256，检验新组上的坐标误差、偏好Accuracy和T1排序保真是否共同改善。Research gap是数据支持的作用尚未区分；本轮不是U必要性检验。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-dina-dcae-strong-anchor64-vs256-fixed2k-newgroups.json)，不是可派发GPU任务。

**输入与范围：** NEW_EVAL56：2,016对 / 56组 / 504图 / 4流

原Anchor父pool确认是COCO val2017，5000张图；原256抽样与FIT/VAL银行随机过程已远端CPU精确复现。新增192图按用户固定hash排序，排除旧256开发图、VAL及HPDv3原图/RGB身份。FIT256=原FIT64+192，原VAL64不变。
新评价从372个合格组按预定hash选56个完整组，504图、2016对。四臂共64512个逻辑评分条件。所有候选来自已有source qualification消费过的来源pool；只与已知adapter开发组互斥，不能称项目全局fresh。未知预训练重叠保留。
输入seal：f5924cb348b0955aad5a65763b7edbe5354e7e016567fcea43f39d993fe9843d。

## Result

**当前归档分类：** `ANCHOR_EXPANSION_JOINT_GAIN_SUPPORTED`

S64→S256：NMSE下降29.1081%；Accuracy68.5392%→69.9529%；G一致率85.8771%→88.6930%。



## Conclusion

单嵌套Anchor draw和初始化，固定2K更新；三端点调整区间通过，near-native未成立，来源pool已被source资格消费。

完整指标、区间、成本和原失败见下方最终报告。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本轮固定任务已完成并停止，唯一下一步建议（未执行）：预注册独立的新增Anchor抽样复现，保持结构、T1、loss及2000更新不变，以检查本次收益对抽样的稳健性。不追加任何当前实验的臂、seed、步数或模型。

最终报告、独立本地回放及seal/readback已通过，128条已有来源路径和相关页面链接已回读核对；监控latentatlas-anchor256随后由应用工具实际删除（deleteStatus=deleted）。本轮无剩余执行项。

相关：`latentatlas`（原wiki关联）、[latentatlas-dina-dcae-fixed-strong-bridge-2k](latentatlas-dina-dcae-fixed-strong-bridge-2k.md)、[latentatlas-dina-dcae-strong-bridge-eval-domain-t1-localization](latentatlas-dina-dcae-strong-bridge-eval-domain-t1-localization.md)。

## Sources

- [来源快照](../source-snapshots/latentatlas-dina-dcae-strong-anchor64-vs256-fixed2k-newgroups.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-dina-dcae-strong-anchor64-vs256-fixed2k-newgroups.md`。
- [最终原报告文本](../reports/latentatlas-dina-dcae-strong-anchor64-vs256-fixed2k-newgroups-final.txt)：路径仅为来源定位；其中历史状态以最终段落/追加回执为准。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
