# LatentAtlas DINA0 + DINA1：外部冻结 Reward 与功能注册预检

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

[latentatlas-rgen1-reward-external-generalization](latentatlas-rgen1-reward-external-generalization.md)之后，改用外部成熟Frozen Latent Reward作为裁判，把“裁判本身是否可读偏好”和“不同VAE能否复用裁判”分开检验。DINA0先验证原生SD3.5→DiNa；只有通过才进入DINA1。

DINA1比较同一小Projector的完整latent重建目标（REC）与冻结DiNa内部H4/H8/H12匹配目标（FUNC）。research gap是：复用Reward是否必须恢复完整reference latent coordinates，还是少量same-image anchors就能恢复所需function。

不是新U、true-unseen、fresh preference confirmation或通用Reward结论。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-dina1-external-frozen-reward-functional-registration.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

计划仅用consumed DIAG643 strict rows和RPJ4-only EXTERNAL2619 strict rows。本轮两个surface的orientation访问都为0。future reserve12455 rows、oldofficialTEST仍禁止读取。

已核实COCO val2017原始RGB两组64候选：文件SHA/尺寸/解码/FITVAL去重通过；没有preference labels。查询128个候选自身bytehash在全局图片目录中的路径，均不存在。但完整目录覆盖证明尚缺，因此这还不是已通过资格的Anchor bank。

旧6632-image overlap证据不能证明与完整20818-row新authority不重叠。可接受U7已有raw-byte identity，不额外要求decoded-RGB；仍需完整namespace的coverage/nonmembership证明。不会临时读取future索引来补证。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

| 检查 | 本轮结果 |
|---|---|
| 官方代码/config审计 | scoped22文件Gitblob与SHA核验通过，3版本已pin；模型权重未下载 |
| 原始RGB候选 | 128当前payload核验通过；完整authority不重叠尚未证明 |
| 合成测试/基线 | 51新预检测试+9继承authority测试=60PASS |
| preflight磁盘核验 | PASS，77文件+4代码绑定；只验证预检记录 |
| DINA0原生资格/DIAG/EXTERNALAcc | NOT_RUN |
| SD/FLUX/DCAE REC/FUNC、null、bootstrap | NOT_RUN |
| full reconstruction是否不必要 | 未评价，不能支持或否定 |

访问：oldTEST/DIAG/EXTERNAL/futurerow/futureorientation/anchorpreflabel/projectortrainlabel/formalfit全0。RGB128；network45次逻辑操作含失败重试；DiNa model-repo card/config4次，weights0；modelforward0。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

这是一项数据准入证明缺口，不是DiNa失败，也不是FUNC失败。用户要求在第一次DINA0评分前把DINA1 spec及anchor manifests一起冻结，因此不能先看裁判表现再补证明。`latentatlas`（原wiki关联）与RGEN1历史证据不因本次预检改变。

若将来FUNC Reward不劣于REC但q_MSE<1.25，只能说复用成功、重建必要性未定；不能把FUNC得分好直接当作full reconstruction unnecessary。REC只是同浅Projector的重建目标baseline，不是12-block Latent Bridge复现。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

先取得满足零future访问边界的既有覆盖/非成员证明，再完成完整科学spec、正式实现与FIT-only smoke。随后按DINA0 gate条件执行DINA1，不能自行改目标救结果。

FUNC计划20736000个student conditions，必须实测CUDA吞吐再安排租用。估计条件时长0.1/0.5/1秒会对应24/120/240天，仅作为成本敏感性，不是速度预测。显存规划约24–48GiB的1024 FUNC microbatch1方案也未实测，不能保证4090适用。

当前仅CPU/证据工作，无需租用GPU；远端开关状态未核实。相关：`latentatlas`（原wiki关联）、[latentatlas-rgen1-reward-external-generalization](latentatlas-rgen1-reward-external-generalization.md)、[rpj4-true-unseen-sd35-anchor-confirmation](rpj4-true-unseen-sd35-anchor-confirmation.md)、[latentatlas-u7-reconstructed-anchor-onboarding](latentatlas-u7-reconstructed-anchor-onboarding.md)。

## Sources

- [来源快照](../source-snapshots/latentatlas-dina1-external-frozen-reward-functional-registration.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-dina1-external-frozen-reward-functional-registration.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
