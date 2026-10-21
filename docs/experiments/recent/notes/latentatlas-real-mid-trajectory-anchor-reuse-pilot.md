> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# LatentAtlas 真实生成中段 Clean-Anchor 复用 Pilot

## 1. Date

2026-10-15。先完成缺失缓存审计r1，用户批准端点校验重放后执行r2；历史r1报告与ZIP保留不覆盖。研究ID：`LATENTATLAS_REAL_MID_TRAJECTORY_ANCHOR_REUSE_PILOT`。

## 2. Purpose

检验原64 Clean FIT训练的FLUX REC，在真实生成完成14次、剩14次更新时，是否保持完全冻结DiNa对同轨迹终态的排序。Research gap是真中段相对终态的接口复用，baseline为Native U、RGB重编码Clean C、原生终态H与原k24/k27；不将本分支等同于跨生成器统一价值排序。

## 3. Code Version / Commit

独立代码`/opt/latentatlas/real-mid-trajectory-anchor-reuse-approved-20261015-r2/code/58cf0594bbfb454a`，content SHA `58cf0594bbfb454aff826493519ebd5917b6e28c5f65a2ea016590ed85bb18b7`；封存spec-r2 SHA `1582549f7f596a2fa38cb32d3382352bee3e7c98903ba2c2d9a04af11d7c40c3`。原源模型、REC与DiNa身份不变；12执行文件、47原运行时源文件和所有模型/数据SHA见成本JSON。原r5和初审r1原件保留。

## 4. Dataset / Input

同一茶壶/石桥prompt，各原source seeds2026101501、2026101502，原4张1024生成图。DiNa scoring noise seed依次2026101511/12/13/14；旧20分数仅复用。reference VAE posterior seeds为另一组，见D63身份核查（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/noisy-anchor-assets-d63.md`）§4（2026-10-18澄清原“reference seed”歧义）。新轨迹4份全28步state/velocity，新REC预测4份；图像未重选，未增加新图。

## 5. Parameters

k14是pre-step，14次更新已完成，14次未完成；源sigma14=.7595109343528748。原28步、guidance3.5、true CFG1、BF16/CUDA协议不变。reference DiNa tau请求.4，实际sigma=.4002932608127594。FP32 clean预测后按原scale.3611/shift.1159转换→BF16原REC→canonical noise→全冻结DiNa。

本次新的独立授权允许源科学112+技术1、完整原轨迹重放4、REC4、DiNa科学4+技术2、文本root≤18；VAE/源文本/训练/校准均0。source阶段墙钟≤2700秒，Reward≤600秒，失败不退还。

## 6. Command

解压完整证据包后，已有NumPy的环境运行；输出目录须全新：

```text
python raw/projects/latentatlas/real-mid-trajectory-anchor-reuse-approved-20261015-r2/recompute-midpoint-results.py --output-dir fresh-independent-recomputation
```

该脚本只读实际缓存和原始账本，不导入Torch、不联网、不调用模型。

## 7. Results

状态：MIDPOINT_REAL_FUNCTIONAL_PILOT_COMPLETED。已取得四图重放的真实k14，旧端点全字节匹配。新增REC4、DiNa科学4/技术2；源误差为k24的6.96–7.68倍。相对H新增反转0/2、平局0；Native失配1/2已存在于Clean。暂不足以决定训练noise-aware接口，仅两pair探索。

| prompt | Native U margin | 原Clean C | 原生终态H | 新真实中段M14 | 相对H新增严格反转 |
|---|---:|---:|---:|---:|---|
| P1 | -0.312500000 | -0.843750000 | -0.750000000 | -0.843750000 | False |
| P2 | +0.343750000 | -0.218750000 | -0.250000000 | -0.312500000 | False |

- 四图旧k24/k27 state/velocity与final packed latent共20项字节一致；原P1-S1技术速度同样一致。真实k14确实取得。
- 本地与远端35/35 CPU测试、独立代码与分析审查通过；最终537/537项独立验收通过。
- 实际新调用：{'FLUX_C_TECH': 1, 'GENERATION_START': 4, 'FLUX_C_SCIENCE': 112, 'REC_FORWARD': 4, 'DINA_TEXT': 12, 'DINA_TECH': 2, 'DINA_C_SCIENCE': 4}。所有调用completed，失败/未完成0；无训练、VAE或校准。

## 8. Analysis

### 2026-10-18 D63：完整轨迹的离线漂移筛查

预声明与独立复算（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/noisy-anchor-decision-d63.md`）仅使用上述四份原轨迹，固定k14，以过去两次速度估计未来关于sigma的仿射变化。四图修正后/原源MSE依次2.342016、2.614852、3.068526、2.161756，未通过全部≤0.5的事前门，停止该候选。方向cosine仅0.232–0.314；实际更新残差相对范数1.3%–2.1%。全27个非初始时点的恒等式闭合为0；k14 FP32估计与缓存逐字节一致，四个payload SHA吻合。

这是新计算的源坐标诊断，复用旧图而无新模型/RM结果；原中段功能结论保持。主控以独立BF16解码及直接Euler求和复算，最大指标差4.45e−16以下。计算合计1.426秒，0拟合/模型/GPU/SSH。下一步不调此候选的窗口或幅度；原生轨迹Anchor监督继续按当前输入—终点target的信息合同研究。关联：`latentatlas-theory-map`、`latentatlas-research-decisions`。

### 2026-10-15 原实验分析

两pair仅是已消费开发实例，不能估计总体一致率或统计显著性/等效性。source终态预测MSE、P输出漂移、reference MSE与NMSE、实际分数/margin全附；source和reference坐标误差不可跨尺度比较。reference NMSE复用原FIT64逐通道target方差，不在当前图上重新拟合。

逐side及逐pair保留`M−U=(M−H)+(H−C)+(C−U)`和平方展开交叉项；这是描述性分解，不识别三个独立因果机制。石桥C/H原已与Native反序，不能将原错误归因于中段。平局独立于新增严格反转和恢复Native严格方向。

## 9. Problems

初审确有缺失k14缓存，只有原k24/k27；获明确授权后才完整重放，并以旧端点字节门恢复同图身份。执行前修复字节门、必要资产封存和局部函数覆盖问题；首次CPU-only版本检查拒绝与CPU舍入oracle差异记录均保留。实际GPU原模型调用没有因这些问题失败。完整legacy parity仍未执行，只有本次两H精确重放的有限运行时资格。

## 10. Next Steps

本轮完成后停止。Possible improvement需要由实际中段现象决定，当前4图2pair不足以决定新noise-aware Projector训练，未开展新训练或新增其他噪声档位。不能宣称跨VAE真实noisy-state统一评分、跨生成器共同排序或新普适理论。

GPU阶段已结束，当前后续仅本地CPU，服务器可以关闭。相关：`latentatlas`、[latentatlas-noisy-anchor-reuse-minimal-pilot](latentatlas-noisy-anchor-reuse-minimal-pilot.md)。

## 11. Sources

- MIDPOINT_MECHANISM_ASSESSMENT.md（原件定位：`wiki/deliverables/latentatlas-real-mid-trajectory-anchor-reuse-completed-20261015-r2/MIDPOINT_MECHANISM_ASSESSMENT.md`）
- MIDPOINT_ASSET_AUDIT.md（原件定位：`wiki/deliverables/latentatlas-real-mid-trajectory-anchor-reuse-completed-20261015-r2/MIDPOINT_ASSET_AUDIT.md`）
- MIDPOINT_COORDINATE_DIAGNOSTICS.md（原件定位：`wiki/deliverables/latentatlas-real-mid-trajectory-anchor-reuse-completed-20261015-r2/MIDPOINT_COORDINATE_DIAGNOSTICS.md`）
- MIDPOINT_FROZEN_REWARD_RESULTS.md（原件定位：`wiki/deliverables/latentatlas-real-mid-trajectory-anchor-reuse-completed-20261015-r2/MIDPOINT_FROZEN_REWARD_RESULTS.md`）
- MIDPOINT_COST_AND_INTEGRITY.json（原件定位：`wiki/deliverables/latentatlas-real-mid-trajectory-anchor-reuse-completed-20261015-r2/MIDPOINT_COST_AND_INTEGRITY.json`）
- SOURCE_INDEX.md（原件定位：`wiki/deliverables/latentatlas-real-mid-trajectory-anchor-reuse-completed-20261015-r2/SOURCE_INDEX.md`）
- 原始新结果与源码：`raw/projects/latentatlas/real-mid-trajectory-anchor-reuse-approved-20261015-r2/`。
- 初审缺失证据和授权提议：`raw/projects/latentatlas/real-mid-trajectory-anchor-reuse-pilot-20261015-r1/`。
- 完整结果证据包（原件定位：`wiki/deliverables/latentatlas-real-mid-trajectory-anchor-reuse-completed-20261015-r2.zip`）。
