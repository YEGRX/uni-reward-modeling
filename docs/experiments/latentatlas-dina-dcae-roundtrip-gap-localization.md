# DC-AE 注册缺口定位：解码—重编码参照实验

归档日期：2026-10-10；证据层级：主要最终报告＋历史页面。

## Experiment

在相同 DC-AE latent 上，对比当前小 Projector 与“匹配 decoder → RGB → 原 SD3.5 encoder → 冻结 DiNa”固定替代路径，判断所测 Reward 行为缺口是否可由更完整的可实现接入路径缩小。此路径不是信息论上限。关联 [latentatlas-dina-vae2-dcae-recipe-portability](latentatlas-dina-vae2-dcae-recipe-portability.md)、[latentatlas-dina-reg1-functional-registration](latentatlas-dina-reg1-functional-registration.md)、`latentatlas`（原wiki关联）。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-dina-dcae-roundtrip-gap-localization.json)，不是可派发GPU任务。

**输入与范围：** 开发集1,008对 / 28组 / 4流；252图

旧 HPDv3 已消费开发集，固定 1,008 对、28 个完整关联组、4 流、252 个原图 byte 身份。旧 Native、DC-AE Projector、FLUX Projector 三臂只读封存评分；新增 DC-AE、FLUX、SD3.5 self round-trip。零目标偏好训练、零新增参数拟合。

## Result

**当前归档分类：** `BETTER_FEASIBLE_PATH_DEMONSTRATED`

DC-AE round-trip72.54%，旧Projector64.16%；Native一致率97.47%。



## Conclusion

decoder→RGB→source encoder新增预训练模块与计算，不是信息论上限或纯容量因果证明。

完整指标、区间、成本和原失败见下方最终报告。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本轮已封存并停止自动检查；不触发 FUNC、旧 16 fits 或其他实验。外推与原因分解须另立且预先固定的研究设计。

## Sources

- [来源快照](../source-snapshots/latentatlas-dina-dcae-roundtrip-gap-localization.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-dina-dcae-roundtrip-gap-localization.md`。
- [最终原报告文本](../reports/latentatlas-dina-dcae-roundtrip-gap-localization-final.txt)：路径仅为来源定位；其中历史状态以最终段落/追加回执为准。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
