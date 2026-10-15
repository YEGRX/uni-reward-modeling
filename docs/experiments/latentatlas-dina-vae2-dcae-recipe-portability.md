# DC-AE 注册配方迁移预实验 DC-AE Recipe Portability Pilot

归档日期：2026-10-10；证据层级：主要最终报告＋历史页面。

## Experiment

检验已在FLUX上使用的固定REC配方，经必要接口移植后，能否让已知第二编码器DC-AE在零目标偏好训练标签下复用同一冻结DiNa Reward。检验配方迁移，不迁移FLUX Projector权重。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-dina-vae2-dcae-recipe-portability.json)，不是可派发GPU任务。

**输入与范围：** 开发集1,008对 / 28组 / 4流；64 FIT+64 VAL

固定64FIT/64VAL COCO anchors；HPDv3开发评价1008pairs/28完整关联组/4原噪声流。复用封存Native与FLUXREC，三新DC-AE臂共24192科学条件。目标偏好标签仅用于固定评价，不用于训练；禁用数据未新增消费。

## Result

**当前归档分类：** `REGISTRATION_GAIN_NOT_NEAR_NATIVE`

正确REC 64.162%，未训练43.06%，置换48.69%，Native72.817%。



## Conclusion

配准收益成立，不支持near-native。目标专属Projector有1000步训练，不是zero-shot。

完整指标、区间、成本和原失败见下方最终报告。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

**已停止：自动检查latentatlas-dc-ae已删除；没有下一实验授权。** 完整中文报告（外部来源定位：`LatentAtlas-runs/DINA_VAE2_DCAE_RECIPE_PORTABILITY_PILOT-20260924-R1/REPORT.md`）。相关项目`latentatlas`（原wiki关联）、历史[latentatlas-dina-reg1-functional-registration](latentatlas-dina-reg1-functional-registration.md)。

## Sources

- [来源快照](../source-snapshots/latentatlas-dina-vae2-dcae-recipe-portability.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-dina-vae2-dcae-recipe-portability.md`。
- [最终原报告文本](../reports/latentatlas-dina-vae2-dcae-recipe-portability-final.txt)：路径仅为来源定位；其中历史状态以最终段落/追加回执为准。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
