> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# LatentAtlas Noisy-State Clean-Anchor 复用最小 Pilot

## 1. Date

2026-10-15。研究ID：`LATENTATLAS_NOISY_ANCHOR_REUSE_MINIMAL_PILOT`。当前结果为continuation r2/r5，真实完成A/B/C。

## 2. Purpose

检验原64张同图Clean Anchor训练的FLUX REC，能否复用到源noisy-state的clean预测，再接入完全冻结DiNa。Research gap限定为这一接口复用；不研究新网络或通用跨生成器value function。

## 3. Code Version / Commit

执行root：`/opt/latentatlas/noisy-anchor-reuse-pilot-20261015-r2`；r5 spec SHA `9d760fd715d236b7208d742cdd6d42d1d1ae44706415742448f58b3dfe6dedee`。独立保存源码文件SHA及r2至r5历史版本，不以本地未提交工作树冒充运行commit。原REC SHA `10967713eef97ce1521c78822e947d9aec36046da32a58ae91a236f564a07d2d`。新训练0，所有原权重冻结。

## 4. Dataset / Input

A/B固定DEV28 SHA排序前两个完整connected groups：18图、72pair、stream0。它们已消费，只能用于探索。C为两个事前固定且不重叠DEV的新prompt×两个source seed，4张1024图。不是随机独立确认集。

## 5. Parameters

FLUX.1-dev官方revision `3de623fc3c33e44ffbe2bad470d0f45bccf2eb21`，BF16、guidance3.5、trueCFG1。A采用50步sigma列表就近选.10/.35；C原生默认28步，实际sigma .10472089797/.34484893084，分别index27/24。DiNa reference sigma .4002932608127594，在Projector之后注噪，始终区别source sigma。原FIT64 target variance固定；source variance未取得，source NMSE不定义。

## 6. Command

完整包解压后，在已有NumPy的Python环境离线执行：

```text
python raw/projects/latentatlas/noisy-anchor-reuse-minimal-pilot-20261015/continuation-r2/verify-saved-evidence-r5.py
```

独立525项复算的运行参数见六报告入口README；仅读取工件，不调用模型、GPU或网络。实际GPU启动器、配置、日志和计费账本全部留存。

## 7. Results

**`A_B_C_TRAJECTORY_PILOT`：实际完成，不表示科学机制确认。**

| 层 | 真实结果 | 边界 |
|---|---|---|
| A坐标 | Clean NMSE .164775261；低/中 .170030283/.193422461，raw MSE分别+3.22%/+18.10% | 18图，低档资源门通过，不是通用误差保证 |
| B冻结Reward | Clean/低/中均67/72=93.055556%；margin MSE .643039280/.651340061/.619004991 | 低档0排序变化；中档2个tie变化、0严格翻转；仅2组 |
| C真实轨迹 | 茶壶prompt所有FLUX路径与Native同向；石桥prompt所有路径反向 | 石桥原Clean已反序，noisy没有相对Clean新增翻转 |

C Native两margin为−.3125/+.34375；Clean为−.84375/−.21875；低档为−.75/−.25；中档为−.78125/−.3125。完整20分数、4图、16项target坐标指标均交付，未回选。

A444与B144个字段独立复算差0；C525/525项通过；855份远端原件SHA全匹配。离线总核验378项最大差1.1920928955078125e−7。独立复算不重推模型分数。

## 8. Analysis

baseline是原Clean、Native、direct noisy及生成终态/RGB重编码。人工加噪结果提供有限复用信号；真实生成已暴露原Clean的Native保真边界，不能仅归因于noisy。低sigma点是最后Euler步，接近final受更新公式约束；中点仅提前3步。普通margin鲁棒性、denoising质量与局部连续性仍是竞争解释。未评价Human Accuracy、跨源混池或生成加速。

## 9. Problems

完整生成资产缺口已恢复；原Schnell标签VAE与dev真实权重SHA相同，语义配置一致。r4卸载技术失败1次完整保留，r5同权重全CUDA修复，未改科学预算。当前仅最小DiNa重放资格通过，完整legacy parity未执行。少量CPU/GPU逆变换舍入差异如实记录，主指标使用实际BF16输入。仅2组、2prompt，不计算确认性CI或宣称等效。

### Possible Conflict / 待确认冲突

旧r1报告的`STOPPED_TECHNICAL_QUALIFICATION`和A/B/C `NOT_RUN`是资产未齐时的历史截面。用户随后要求继续寻找，本continuation实际恢复并执行，故当前状态更新为已完成；旧原报告与57文件停止包全部保留，不静默改写。两者不代表同一时点的相互矛盾结果。

## 10. Next Steps

本轮完成，不追加训练或Reward调用。Possible improvement是先在真正独立新内容上确认原Clean生成域保真及F5终态/往返边界，再决定是否值得扩展更早的真实轨迹；不能仅因工程成功就扩大noisy机制主张。GPU阶段已结束，服务器可以关闭；后续复核只需本地CPU，当前电源状态未核验。

相关：`latentatlas`、`latentatlas-cross-encoder-consistency-results`、[latentatlas-r17-a2-convergence-and-dina](latentatlas-r17-a2-convergence-and-dina.md)。

## 11. Sources

- 当前最终报告（原件定位：`wiki/deliverables/latentatlas-noisy-anchor-reuse-minimal-pilot-20261015-continuation-r2/FINAL_PILOT_DECISION.md`）
- 完整原始证据索引（原件定位：`wiki/deliverables/latentatlas-noisy-anchor-reuse-minimal-pilot-20261015-continuation-r2/SOURCE_INDEX.md`）
- 当前完整结果包（原件定位：`wiki/deliverables/latentatlas-noisy-anchor-reuse-minimal-pilot-20261015-completed-r5.zip`）
- 历史r1停止报告（原件定位：`wiki/deliverables/latentatlas-noisy-anchor-reuse-minimal-pilot-20261015/FINAL_PILOT_DECISION.md`）
- 原用户附件副本：`raw/projects/latentatlas/noisy-anchor-reuse-minimal-pilot-20261015/user-request-original.txt`
- 当前原件：`raw/projects/latentatlas/noisy-anchor-reuse-minimal-pilot-20261015/continuation-r2/`
