# LatentAtlas 冻结候选前向独立验证 Frozen Candidate Forward Audit

归档日期：2026-10-10；证据层级：主要最终报告＋历史页面。

## Experiment

新协议实际评价旧MICRO保存的四个固定候选，检查超出FIT的效用、A32/C32对照、坐标保护及事后风险分解。这不是恢复旧R1.1；原 `LOCAL_METHOD_NUMERICALLY_UNQUALIFIED`、FD比1.0865105197485838>0.20与全部原门槛保留。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-frozen-candidate-forward-audit.json)，不是可派发GPU任务。

**输入与范围：** VAL8面板768条件；MAIN8固定8组288对72图，新增6,912 pair-specific条件

原VAL8固定面板，每臂128条件，总768；坐标64图。原MAIN8固定8完整组、288物理pair、4噪声stream；三个新臂必须6912个pair-specific条件，不按图去重。合法N/G/BASE复用。VAL未用于32维theta拟合，但曾被S256训练诊断及本轮行动门控使用，不是项目级独立测试。

## Result

**当前归档分类：** `MAIN8_TRADEOFF_OR_DETERIORATION`

VAL中心风险点值下降9.3826%，普通95%跨0；MAIN8 Q32对G分差MSE较BASE增加44.7618%。



## Conclusion

独立新协议；原FD失败不改写。A/C误差点值更低；QA调整区间未决，QC次级未校正区间支持C；人类Accuracy差异未决。

完整指标、区间、成本和原失败见下方最终报告。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本轮实际执行与交付完成，最终状态 `MAIN8_TRADEOFF_OR_DETERIORATION`。不启动下一研究线、不扩到56组。原局部导数仍不合格；论文级独立确认、完整56组、跨分布推广、U必要性、P32的MAIN8效果和优于所有旧方法未验证。八组区间未决不表示等效。

相关：[latentatlas-dcae-q32-lowcost-main8](latentatlas-dcae-q32-lowcost-main8.md)、`latentatlas`（原wiki关联）。

## Sources

- [来源快照](../source-snapshots/latentatlas-frozen-candidate-forward-audit.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-frozen-candidate-forward-audit.md`。
- [最终原报告文本](../reports/latentatlas-frozen-candidate-forward-audit-final.txt)：路径仅为来源定位；其中历史状态以最终段落/追加回执为准。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
