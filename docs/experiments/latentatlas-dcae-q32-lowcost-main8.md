# LatentAtlas DCAE Q32 低成本 MAIN8 实验

归档日期：2026-10-10；证据层级：主要最终报告＋历史页面。

## Experiment

在固定S2562000、T1/W0、DiNa/PAPER_T04下，比较C32/A32/Q32，仅拟合各32维小参数。先M0/E0/E1/E2；只有固定行动、参考与可比性门槛全部通过才继续MAIN8。完整E3、EP和4K续训不在授权内。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-dcae-q32-lowcost-main8.json)，不是可派发GPU任务。

**输入与范围：** 固定S2562000、T1/W0、32维；MICRO原协议

原56组504图/2016对/4流历史缓存。固定hash MAIN8=8完整组、72图/288对；其6912条原请求的完整source/prompt/noise/receipt绑定已远端核。原FIT256、VAL64互斥；392份S256预测绑定，最小官方caption ID、T1/W0充分量和24面板已封存。实际任务FIT=64图、16面板×2流，共128条件。

## Result

**当前归档分类：** `LOCAL_METHOD_NUMERICALLY_UNQUALIFIED`

FD ratio1.0865105197485838>0.20失败；FIT LinErr0.12015720026795061<0.25不覆盖FD失败。



## Conclusion

原E2/MAIN8未运行；416科学、8技术、128次输入反向为该旧轮实际成本。保存四候选不是效用通过。

完整指标、区间、成本和原失败见下方最终报告。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本轮原始数值、独立CPU、可视化、MICRO/最终报告、raw/wiki/index/log及seal已交付。E2/MAIN8不再自动启动，不调步长/阈值/半径。任何后续数值响应研究需另行明确定义的新协议。下一阶段无本实验GPU计算；无需保持GPU为本实验运行，不停止其他任务。

相关：`latentatlas`（原wiki关联）。旧CPU阶段不可变报告是当时快照，不是当前缺口状态。

## Sources

- [来源快照](../source-snapshots/latentatlas-dcae-q32-lowcost-main8.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-dcae-q32-lowcost-main8.md`。
- [最终原报告文本](../reports/latentatlas-dcae-q32-lowcost-main8-final.txt)：路径仅为来源定位；其中历史状态以最终段落/追加回执为准。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。

后续另立[冻结候选前向审计](latentatlas-frozen-candidate-forward-audit.md)；其结果不改写本轮FD失败与未运行字段。
