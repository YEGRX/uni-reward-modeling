# LatentAtlas 投稿实验证据补全 Submission Evidence

归档日期：2026-10-10；证据层级：主要最终报告＋历史页面。

## Experiment

围绕实际28页中文稿建立由合理baseline、真实输出和有效评价支撑的贡献证据。先复用合法缓存，再固定最小REC对照，不因Q32导数资格失败停止无关REC。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-submission-evidence-20261009.json)，不是可派发GPU任务。

**输入与范围：** 原NEW_EVAL56与DEV28缓存；CPU同Anchor ridge/SVD基线

DEV28：252图、1008对、4流4032逐流判断；已开发消费。NEW56：504图、2016对、4流8064；与旧adapter组互斥，但父pool已用于source qualification。独立内容单位分别28/56个完整connected groups，不是流或pair数。

E2：同原FIT64/VAL64；Cosmos同图T0、DC-AE同图T1。新ridge/SVD拟合不查Reward、不用目标偏好标签。数据用途、源/目标、模型与缓存身份见资产合同表。

## Result

**当前归档分类：** `CPU_BASELINES_FITTED_REWARD_NOT_RUN`

Cosmos ridge/SVD VAL NMSE0.228049708/0.444343958；DC-AE0.326515707/1.062346963。



## Conclusion

仅CPU拟合/坐标评价；新基线Reward评分与新增确认未运行。本报告旧Q32进度已由独立前向审计覆盖，历史原文保留。

完整指标、区间、成本和原失败见下方最终报告。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

优先只运行Cosmos两冻结基线真实任务评分：16,128科学+16技术DiNa、28唯一prompt、GPU硬上限90分钟；训练/反向/VAE0，不采购。新增范围审批已提出一次，尚待回复；旧权限未覆盖它。现有Q32聊天不重复启动、不终止。DC-AE部署资格和后续32,256评分另列计划。

若只有一轮有限计算，这项合理REC对照最可能改变方法贡献判断。随后仅在主张需要时补关键Anchor/初始化重复、事前预测、新独立完整组及公平部署成本，不默认全交叉。

相关页面：`latentatlas`（原wiki关联）、[latentatlas-dina-unseen-encoder-fixed-recipe-portability](latentatlas-dina-unseen-encoder-fixed-recipe-portability.md)、[latentatlas-dina-dcae-strong-anchor64-vs256-fixed2k-newgroups](latentatlas-dina-dcae-strong-anchor64-vs256-fixed2k-newgroups.md)、[latentatlas-dcae-q32-lowcost-main8](latentatlas-dcae-q32-lowcost-main8.md)、[latentatlas-dina-dcae-fixed-strong-bridge-2k](latentatlas-dina-dcae-fixed-strong-bridge-2k.md)。

## Sources

- [来源快照](../source-snapshots/latentatlas-submission-evidence-20261009.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-submission-evidence-20261009.md`。
- [最终原报告文本](../reports/latentatlas-submission-evidence-20261009-final.txt)：路径仅为来源定位；其中历史状态以最终段落/追加回执为准。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。

本报告旧MAIN8零评分描述属于历史，后续已由[独立前向审计](latentatlas-frozen-candidate-forward-audit.md)完成；ridge/SVD新任务评分仍未由本记录证实。
