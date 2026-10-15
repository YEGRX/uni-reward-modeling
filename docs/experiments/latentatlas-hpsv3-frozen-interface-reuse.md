# HPSv3 冻结接口复用与加载恢复

归档日期：2026-10-10；证据层级：主要最终报告＋历史页面。

## Experiment

检验冻结FLUX/Cosmos REC经共同SD3.5 decoder、量化Q和HPSv3后能否保留参考效用。已按用户续接授权完成原范围，结果为`CORE_COMPLETE_WITH_CONTROL_GAP`。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-hpsv3-frozen-interface-reuse.json)，不是可派发GPU任务。

**输入与范围：** 已消费1,008对 / 28组 / 252图；统一新机六臂1,512分数

固定已消费1008对/28关联组/252图，不是新held-out。O/N在新机重新评分原504个输入并验收；旧机504个修复分数保留为历史，不混入当前主比较；FLUX复用252份旧clean缓存；三Cosmos臂生成756份clean后共同解码。caption只读derived1008；未重新打开14400/future12455/External/oldTEST。历史metadata-only全源字节扫描及仅白名单物化的事实保留。

## Result

**当前归档分类：** `RETENTION_INCONCLUSIVE`

O/N/FLUX REC/Cosmos REC Accuracy76.091/75.298/73.413/74.702%；两REC保持判据未决。



## Conclusion

HPS正确加载已恢复，旧失效结果撤回；decoder-mediated；F_NOREG协议不兼容缺席，不称七臂完整。

完整指标、区间、成本和原失败见下方最终报告。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本轮完成，不启动下一实验。正确HPS入口已可按使用指南复用；最终报告明确两接口的具体结论与限制。续接自动检查hpsv3已在父协调方最终读回后实际删除；删除回执见同次归档的 `AUTOMATION_DELETION.json`。相关：`latentatlas`（原wiki关联）、`latentatlas-current-evidence-map`（原wiki关联）。

## Sources

- [来源快照](../source-snapshots/latentatlas-hpsv3-frozen-interface-reuse.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-hpsv3-frozen-interface-reuse.md`。
- [最终原报告文本](../reports/latentatlas-hpsv3-frozen-interface-reuse-final.txt)：路径仅为来源定位；其中历史状态以最终段落/追加回执为准。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
