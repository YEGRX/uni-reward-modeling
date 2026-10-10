# GFI0 + GFI1 组内冻结 Critic 与少量 Anchor 功能注册

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

先检验组内冻结潜空间裁判（Frozen Latent Critic）能否在当前外部偏好数据上成立，再检验少量无偏好标签的 Anchor 能否支持跨 VAE Reward 复用。研究缺口（research gap）是：坐标重建与 Reward 功能恢复是否必须同步改善。该问题尚未得到本次实验结果。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-gfi1-group-frozen-interface-registration.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

计划使用 DIAG 643、EXTERNAL 2619；future reserve 12455 保持封闭。以上为协议规定规模，本轮没有读取其行或偏好方向。计划 Anchor 为 128 张有 caption、无偏好标签的原始 RGB，64 FIT + 64 VAL；尚未选择或准入，不能默认复用 DINA 候选。

已读组内匿名稿正文 9 页、补充材料 7 页。全文 URL/代码发布表述、链接注释与内嵌附件检查均未找到组内仓库或权重入口。补充材料的公开 checkpoint 指 SD3.5 基础模型。只能确认当前稿件未提供入口，不能推断作者没有在其他地方开源。本轮未做外网检索。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

用户协议 §8 的来源准入门槛触发。代码仓库/冻结代码包、训练后的 Critic checkpoint 均未取得；用户确认不在本地，并表示会向组内索取。

GFI0、REC、FUNC、bootstrap 和全部科学结论均 NOT_RUN。来源预检 receipt 为 PASS，仅验证 38 个文件、论文源文件摘要与停止原因，不是科学 verifier 或结果重放。归档包含源目录的 40 个文件及一份归档索引。

本轮偏好行/方向、future、old TEST、Anchor 偏好标签、实验 RGB、模型 forward、正式 fits、网络访问均为 0。没有访问模型权重；PDF 渲染属于文档核查。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

未取得指定裁判是材料缺失，不是 Critic 资格失败，也不能支持或否定少量 Anchor 的功能注册。历史 RRV1 自训 reader 与论文 SD3.5 block 18 Critic 不同，不可代用。[latentatlas-rgen1-reward-external-generalization](latentatlas-rgen1-reward-external-generalization.md) 的封存结论不因本次预检改变；[latentatlas-dina1-external-frozen-reward-functional-registration](latentatlas-dina1-external-frozen-reward-functional-registration.md) 保持原阻塞状态。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

收到材料后核对来源、权重摘要和推理语义，再完成数据准入与规格冻结，才进入 GFI0。可能改进（possible improvement）目前只保留协议中的功能对齐比较，不据未运行的结果新增方法或 sweep。

当前无需 GPU 或服务器；远端运行状态未核实。进入实际 GPU 阶段前再提醒开机。

相关项目：`latentatlas`（原wiki关联）。

## Sources

- [来源快照](../source-snapshots/latentatlas-gfi1-group-frozen-interface-registration.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-gfi1-group-frozen-interface-registration.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
