> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# LRM-R1：真实 FLUX 终态的四路径冻结 Reward 实验

2026-10-21。实际执行完成：4 Prompt × 2 Seed × 2 DiNa 评分流 × 4 路径，共 **64 次科学评分、16 次技术评分**；新增生成和训练均为 0。

**核心结果：REC 直接接入与强 Affine 均保留四组均分后的 Best-of-2 选择，Affine 还保留全部八个逐流排序。** REC 的逐流排序保留 7/8；所有接口路径的分数相对完整 T1 均向下偏移。正式决定为 `AFFINE_SUFFICIENT_IN_PILOT`，具体限定与投入判断见 [最终决定](lrm-r1-decision.md)。

## 1. 问题与数据

检验既有 Anchor-only 接口能否对真实 FLUX.1-dev 终态复用完全冻结 DiNa。候选取历史 SOURCE manifest 全八项，四个 Prompt 固定如下，每组 source seed 为 2026101601 / 2026101602：

- **dev-01**：A documentary street photograph of a small bakery on a rainy morning, warm light in the window, two parked bicycles, wet cobblestones reflecting the storefront, no readable text.
- **dev-02**：A close-up editorial photograph of a potter shaping a clay bowl on a wheel, both hands clearly visible, soft side light, a quiet studio with simple shelves in the background.
- **dev-03**：A studio photograph of a red cube to the left of a blue sphere and a yellow cone behind them, all resting on a matte gray table, clear geometric shapes and soft shadows.
- **dev-04**：A still life photograph of a transparent glass pitcher half filled with water beside a folded green linen cloth and a brushed steel spoon, natural window light, subtle reflections.

这是 **HISTORICAL DEVELOPMENT DIAGNOSTIC**。四组已消费 DEV 是统计单位，重复评分流用于检查噪声稳定性。完整候选 ID、Prompt SHA、终态和 PNG SHA 见 身份审查（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_R1_REAL_INTERFACE_QUALIFICATION/asset-contract-sol.md`） 与 评分前协议（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_R1_REAL_INTERFACE_QUALIFICATION/LRM_R1_PRE_SCORE_PROTOCOL.md`）。无排除、无新增候选、无按本轮结果挑选。

FLUX.1-dev revision `3de623fc3c33e44ffbe2bad470d0f45bccf2eb21`，原生成 28 步、1024²、guidance 3.5、true CFG 1、max sequence 512。模型、VAE、scheduler 及生成参数来自原冻结配置。本轮用真实 decoder 输入重放，全 8 图像素和 PNG SHA 与原图一致。

## 2. 方法和评分合同

| 路径 | 输入到冻结 DiNa 的参考坐标 | 作用 |
|---|---|---|
| A | `E_r(D_s(q_gen))` | 当前生成 PNG 的完整 T1 参考 |
| B | `P_REC(q_gen)` | 正式 REC5000 直接接入 |
| C | `P_REC(E_s(D_s(q_gen)))` | 源 VAE posterior mode 重编码诊断 |
| D | `P_Affine(q_gen)` | 正式 k5/λ=.001 Spatial Affine |

REC checkpoint SHA `801c8d5868b63ea486c057a47dfdff17ebf230ec481f974a066e6f2f1a61ef47`；Affine NPZ SHA `e49ff18ba382941f783dbe5febfebf3f9e77503f25ee20cca94a66ea34403734`。均固定原 D73 选择，不重训、不重新选模。训练保持 Anchor-only；本轮 RM 全部用于技术核验和评价。

DiNa-LRM-SD35M-12layers 使用原完整 admission、冻结 backbone/sole rm_lora/reward head/text encoders、tap [4,8,12]。状态摘要 `e52a78d353aac07520db04a3fe398f830f6460259488c858153d67224829a424`。实际 σ=0.4002932608127594、t=400.29327392578125，BF16 raw score。各路径的条件、实际 noise tensor 和混合后输入均逐 SHA 核验；DiNa 用自己的 SD3.5 文本编码，不使用 FLUX embedding。

A 参考编码为每图固定种子的 posterior sample；C 源编码为 posterior mode。D_s 包括 RGB8 后处理及 PNG，四路共用同一候选身份。当前 A 新计算，不用旧 T0 分数充当 T1。评分前封存协议 SHA `5555e124ba5f855ed8553973f3112445bd07048e762cad8090af4e7cbb3893a1`，之后又在首次 RM 前封存条件与实际 GPU 噪声张量。详见 合同验证（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_R1_REAL_INTERFACE_QUALIFICATION/LATENT_CONTRACT_VERIFICATION.md`）。

## 3. 主要结果

相对 A，单候选误差为 M−A，margin 固定为较小 seed 减较大 seed；选择按两流均分。各 Prompt 等权。下表单图误差使用每方法 16 个观测，margin 使用 8 个流内分差，推断单位仍为四组。

| 路径 | Score MAE | Score RMSE | Score bias | Margin MSE | Margin bias | Native agreement | Best-of-2 记分 | Native regret |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| B REC 原生终态 | 1.218750 | 1.389747 | -1.218750 | 0.107910 | -0.140625 | 87.5% | 100.0% | 0.000000 |
| C REC 源重编码诊断 | 1.308594 | 1.515383 | -1.308594 | 0.108643 | -0.148438 | 87.5% | 87.5% | 0.000000 |
| D 强 Spatial Affine | 1.294922 | 1.376043 | -1.294922 | 0.106323 | 0.136719 | 100.0% | 100.0% | 0.000000 |

B 与 D 的实际均分选择均 4/4 匹配 A。C 有 3 组严格保序、1 组精确平局；按预先固定的“接口平局半分”规则为 87.5%。C 的实际 tie-break 选择 seed 较小者，在本轮碰巧也是 A 赢家，故实际选择匹配也是 4/4、regret 为 0。不能把这个平局称为四组严格保序。

本协议没有已验证的 T1 MAE 或准确率通过阈值；以上是描述性结果。正式 `AFFINE_SUFFICIENT_IN_PILOT` 表示强 Affine 已复现当前候选选择，没有观察到 REC 额外收益，范围是这四组及固定两流，不是总体等效检验。

## 4. 每组均分、分差和案例

| Prompt | A 分差 | B 分差 | C 分差 | D 分差 | A / B / C / D 的实际 seed 选择 |
|---|---:|---:|---:|---:|---|
| dev-01 | 0.140625 | 0.281250 | 0.281250 | 0.281250 | 2026101601/2026101601/2026101601/2026101601 |
| dev-02 | -0.218750 | -0.515625 | -0.484375 | -0.484375 | 2026101602/2026101602/2026101602/2026101602 |
| dev-03 | 0.562500 | 0.031250 | 0.000000 | 1.125000 | 2026101601/2026101601/2026101601/2026101601 |
| dev-04 | -0.250000 | -0.125000 | -0.156250 | -0.140625 | 2026101602/2026101602/2026101602/2026101602 |

- **dev-01，雨中面包店**：四路均选 seed1601；A 在流1分差为 .0625，触发预声明近零提示，主评价仍使用精确 tie 规则。
- **dev-02，陶工**：四路均选 seed1602；接口负分差约为 A 的两倍，选择方向保持、margin 幅度改变。
- **dev-03，几何物体**：A 两流分差均 .5625；B 为 .1875 / −.125，均分只剩 .03125；C 为 .125 / −.125，均分精确为 0；D 两流均 1.125。REC 在流1反转发生于非近零的 A 分差，重新编码没有修复，强 Affine 两流保持。该组是主要功能不稳定案例。
- **dev-04，静物**：四路均选 seed1602，接口的负分差幅度比 A 小。B/C 的输入变化没有改变实际组选择。

## 5. 全部实际原始分数

| Prompt | source seed | 评分流 | A 完整 T1 | B REC | C 重编码 REC | D Affine |
|---|---:|---:|---:|---:|---:|---:|
| dev-01 | 2026101601 | 0 | -3.90625 | -4.40625 | -4.43750 | -4.68750 |
| dev-01 | 2026101601 | 1 | -4.00000 | -4.46875 | -4.43750 | -4.71875 |
| dev-01 | 2026101602 | 0 | -4.12500 | -4.75000 | -4.75000 | -5.03125 |
| dev-01 | 2026101602 | 1 | -4.06250 | -4.68750 | -4.68750 | -4.93750 |
| dev-02 | 2026101601 | 0 | -4.18750 | -5.43750 | -5.59375 | -5.65625 |
| dev-02 | 2026101601 | 1 | -4.12500 | -5.56250 | -5.68750 | -5.78125 |
| dev-02 | 2026101602 | 0 | -4.03125 | -5.00000 | -5.18750 | -5.21875 |
| dev-02 | 2026101602 | 1 | -3.84375 | -4.96875 | -5.12500 | -5.25000 |
| dev-03 | 2026101601 | 0 | -8.50000 | -11.00000 | -11.25000 | -10.12500 |
| dev-03 | 2026101601 | 1 | -8.43750 | -11.00000 | -11.25000 | -10.12500 |
| dev-03 | 2026101602 | 0 | -9.06250 | -11.18750 | -11.37500 | -11.25000 |
| dev-03 | 2026101602 | 1 | -9.00000 | -10.87500 | -11.12500 | -11.25000 |
| dev-04 | 2026101601 | 0 | -6.06250 | -6.84375 | -6.81250 | -6.93750 |
| dev-04 | 2026101601 | 1 | -6.00000 | -6.81250 | -6.81250 | -7.00000 |
| dev-04 | 2026101602 | 0 | -5.75000 | -6.68750 | -6.62500 | -6.81250 |
| dev-04 | 2026101602 | 1 | -5.81250 | -6.71875 | -6.68750 | -6.84375 |

原始长表：FOUR_PATH_SCORE_LEDGER.jsonl（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_R1_REAL_INTERFACE_QUALIFICATION/FOUR_PATH_SCORE_LEDGER.jsonl`）；宽表：[FOUR_PATH_RESULTS.csv](../tables/lrm-r1-four-path-results.csv)，16 个候选×流记录，每行四路径，附候选/PNG/Prompt、clean、噪声、noisy-input 与 score tensor 身份。

## 6. 组级敏感性与数值状态

逐次留出一个 Prompt，保留三组重新计算：

| 方法 | Score MAE 范围 | Margin MSE 范围 | 逐流 agreement 范围 | 均分 Best-of-2 记分范围 | Regret |
|---|---:|---:|---:|---:|---:|
| B | 0.869792–1.440104 | 0.041667–0.138346 | 0.833333–1.000000 | 1.000000–1.000000 | 0 |
| C | 0.911458–1.559896 | 0.034180–0.141602 | 0.833333–1.000000 | 0.833333–1.000000 | 0 |
| D | 1.080729–1.453125 | 0.036296–0.135742 | 1.000000–1.000000 | 1.000000–1.000000 | 0 |

移除 dev-03 后，B/C 的逐流 agreement 都变为 100%，说明本次噪声反转集中在一组；其余留出情形为 5/6。D 保持 6/6。B/D 的均分组选择和 regret 在所有留出情形中保持。四组不足以估计总体效应，本轮不报告显著性、总体优势或统计等效。

64 个分数有限，无 NaN/Inf；A 无精确平局。C 在 dev-03 均分精确平局，B 的均分差 .03125 触发近零提示。所有已封存模型状态在前后完全一致。

## 7. 成本与核验

| 本轮新增操作 | 实际次数 | 说明 |
|---|---:|---|
| 真实生成 / 训练 | 0 / 0 | 复用原八候选 |
| 源 VAE decode / encode | 9 / 9 | 八候选加首候选重复技术检查 |
| 参考 VAE encode | 9 | 同上；固定种子重复一致 |
| REC / Affine | 18 / 9 | B、C 各八次加重复；Affine 为 CPU 部署 |
| DiNa 科学 / 技术 | 64 / 16 | 合计 80，达到预定硬上限后停止 |
| DiNa 文本编码器 root | 12 | 四 Prompt × 三编码器；技术资格条件复用原缓存 |
| 新外部 Reward | 0 | 只审计历史 PickScore |

单 GPU RTX4090D，准备监督用时 48.775s，评分监督用时 403.602s，共 452.377s；两阶段均正常退出。评分显存峰值 17572036608 bytes（16.365 GiB）。这些含模型加载、身份核验与诊断的实际阶段耗时，不构成路径间受控加速基准。

全部 70 文件已取回。主控另写 Fraction/NumPy 复算：27 个主指标、96 个留组指标一致；64 个实际 noisy 输入和64个分数 tensor SHA 匹配；六根冻结状态及实际80次 RM账本重核通过。坐标诊断采用保存数组先转高精度再差分，修正说明见 分析精度记录（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_R1_REAL_INTERFACE_QUALIFICATION/REPRODUCIBILITY/ANALYSIS_CORRECTION.md`）。19 项边界/统计测试覆盖实现，科学结论来自真实分数。

## 8. 使用范围与最终投入判断

当前证据支持这组真实终态上的同源候选选择复用。三条接口的绝对分数偏移、dev-03 的 REC 流间反转，以及 A 与历史 PickScore 仅 1/4 组同选，决定独立确认必须同时检查选择保真与 Reward 有效性。失败诊断（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_R1_REAL_INTERFACE_QUALIFICATION/FAILURE_DIAGNOSIS.md`）逐项给出可排除和未定解释。

本轮完成后停止。没有新网络、后续自动扩展、D74、论文改写或完整成本实验。原 CVPR 57 文件 SHA 全部保持。

## 原始证据

- `raw/projects/latentatlas/lrm-r1-20261021/completed-r1/{prepare-r1,score-r1}/`：全部真实数组、PNGs、条件、噪声、调用账本、回执。
- `raw/projects/latentatlas/lrm-r1-20261021/recovery-manifest-r1.json`：70 文件逐 SHA 和归档身份。
- `REPRODUCIBILITY/{functional-analysis,root-independent-audit,cached-diagnostics,resource-ledger}.json`。
- `LRM_R1_PRE_SCORE_PROTOCOL.md`、`pre-score-seal-r1.json`，保留原评分前字节。
