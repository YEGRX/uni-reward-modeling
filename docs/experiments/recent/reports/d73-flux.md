> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# D73 FLUX：匹配前作与强基线的功能比较

2026-10-20。状态：完整评分、原始账本核验及独立统计复算已完成；论文整合见当前稿及其审查回执。

## 结论及科学作用

**39,056 参数的 REC 在 FLUX 上相对共享空间仿射、Interposer-MSE 和 Interposer-cycle，都获得了可分辨的 Native agreement 与 margin MSE 收益。** 结合 [Cosmos 匹配比较](d73-cosmos.md)，这支持 C 论文的实用主张：在规定的少图配对适配预算内，小型空间接口能够改善同一个冻结奖励模型的功能保真度。

两来源共用同一批 252 图、28 prompt 组和 Native 分数，是两种源表示上的比较，不能按两个独立数据集或 56 个独立组计算证据。当前全部属于已消费开发域；独立实现的复算增强计算可信度，未提供新的独立样本。

## 数据、接口和信息合同

- 训练 FIT64、选模 VAL64，同图参考为 SD3.5 T0。总适配图像暴露为 128 图。FLUX 源为冻结 FLUX.1-schnell 的原始、未平移/缩放/打包的后验 mode，revision `741f7c3ce8b383c54771c7003378a50191e9efe9`。
- 原始 16 个训练 run 加四项一次性延长，每家族四学习率、相同有效 batch32、100 个坐标验证点。统一延长由事前晚期改善规则触发，5000 步后四家族均低于继续触发线，停止追加训练。
- 所有参数训练及本次 checkpoint 选择只读坐标；RM 训练、选模查询均为 0。评价保持完整 DiNa、条件与噪声合同冻结。坐标 VAL 是本次固定比较规则，不是未来接口选择的唯一合法标准。
- 评价 1008 物理 pair、4032 pair-stream；Native tie33，agreement 分母3999。半分学生 tie、Human tie错误，沿用原协议。
- 每来源单独使用预定的 10 方法对 × 2 主要端点比较族，50,000 次共同 PCG64 组 bootstrap，seed2026101902，分位数 .00125/.99875。未建立跨来源联合95%族；绝对 margin MSE 差承担推断，相对下降为描述量。

| 家族 | 学习率/正则 | checkpoint步 | VAL NMSE |
|---|---:|---:|---:|
| REC | .001 | 5000 | .1402612391 |
| A2 | .001 | 5000 | .1325024851 |
| Interposer-MSE | .001 | 4500 | .2033614123 |
| Interposer-cycle | .0003 | 5000 | .2134910619 |
| 空间 affine k5 | λ=.001 | 闭式拟合 | .1503772143 |

选中 artifact 与 SHA 见回收的 `score-assembly-flux-extension-r1/selection.json` 和 `score-spec.json`；spec SHA `3c025a5f32bc833e939b680edd6fb18b1a1924b781109680f8e83bd39ca70b2a`。Interposer 使用官方 commit `9344ddf53c3f4164a753f1ab30885ad99941a437` 的前向结构，MSE适配与保留双向L1/round-trip目标的cycle适配分列；同优化机会不表示同 FLOPs，也不是对其原发布大数据权重的复现。

## 实际结果

| 方法 | Native agreement % | margin MSE | Human Accuracy % | Native regret |
|---|---:|---:|---:|---:|
| 空间 affine | 91.5854 | .472092 | 72.8919 | .034427 |
| Interposer-MSE | 90.5351 | 1.072784 | 69.7173 | .052644 |
| Interposer-cycle | 86.5716 | 1.844546 | 69.3204 | .108710 |
| REC | **94.7237** | **.298031** | 72.6687 | .020301 |
| A2 | 92.8607 | .315073 | 72.6935 | .025676 |

以下方向均为 REC 减基线，区间为本来源20项主比较族调整区间：

| 比较 | agreement差 pp [区间] | margin MSE差 [区间] | 相对MSE下降 |
|---|---|---|---:|
| REC − affine | +3.1383 [.4254, 5.9078] | −.174061 [−.340912, −.033533] | 36.87% |
| REC − Interposer-MSE | +4.1885 [1.8417, 7.3235] | −.774753 [−1.952356, −.229972] | 72.22% |
| REC − Interposer-cycle | +8.1520 [3.9083, 12.9493] | −1.546515 [−2.708031, −.666970] | 83.84% |

A2 相对三基线的 margin MSE 均有可分辨改善；agreement 仅相对 cycle 可分辨。A2−REC 的 agreement差为 −1.8630 pp，区间 [−4.3770,.1379]；margin MSE差为 +.017042，区间 [−.057527,.109571]，两项均未分辨。因此不声称 REC 显著优于 A2，也不保留旧训练预算下 A2 必然更优的架构解释。

REC/A2 相对 affine 的 Human Accuracy 差分别 −.2232/−.1984 pp，描述性95%区间均含0；相对两 Interposer 的 Human Accuracy 描述性区间为正。这不形成相对 affine 或 Native 的人类质量收益主张。全部10方法对、4端点与每组充分统计量保存在完整统计 JSON。

## 核查和实际计算量

原评分监督正常退出，5677.120秒，未超时；原运输回执正常结束。22份原字节文件共167,694,727字节已回收，SHA与大小均核验。全部 reserve/attempt/complete/commit 一致，无 pending；40320条科学查询与实际调用事件逐项对应。104次技术RM、1270次接口前向、1次runtime构造、新文本0；不重复把RM与backbone双根日志计为两次评分。

实际 runtime 权重、Native 重放、学生重复前向、冻结状态和28组条件的资格见 `flux-score-real-qualification-root-audit-r1.json`。本地独立复算另核 FLUX源证明、252份编码receipt、仅替换源字段的整份manifest等价性，以及1260预测条目与实际clean评分输入的身份链；未把元数据复核冒充再次读取未回收的张量payload。

主控使用冻结统计实现；Sol 6.1 从原始分数、Native方向和组身份独立编写索引抽样实现，未读取主控统计结果。主控读其实现，重新核284份输入SHA及5份生产统计输入SHA；**745数值、全部28组分子与分母完全一致，最大差0**。draw SHA `e5a3cc936ab81c08e156fde5c3cac641a1c79d2d29a57f9720a35904174d27c9`。独立CPU约1.23秒，模型/SSH/GPU调用0。

| 计量 | FLUX正式比较（含延长/资格） | Cosmos+FLUX正式比较合计 |
|---|---:|---:|
| 科学单图RM | 40320 | 80640 |
| 技术单图RM | 104 | 208 |
| 接口预测（含重复资格） | 1270 | 2540 |
| 新文本编码 | 0 | 72 |
| 新VAE编码 | 256 | 256 |
| 训练网络图次forward/backward（各） | 2400000 | 4800000 |
| optimizer更新 | 62500 | 125000 |
| VAL前向 | 25600 | 51200 |
| 神经训练监督时间 | 14.900小时 | 30.044小时 |
| 冻结评分监督时间 | 5677.120秒 | 11387.531秒 |

合计口径为两来源正式比较及其一次性延长，早期技术训练pilot和CPU affine拟合另记；不是项目所有历史调用总数。FLUX缓存另用233.519秒。数据取得、训练、选模和RM评价成本分开，不据这些时间宣称端到端部署加速。

## 决策与下一步

1. 结束本轮既定前作/强基线比较。小型 REC 可作为独立确认的主接口候选，A2与两适配Interposer保留完整对照，不再因已有开发结果扫新结构/学习率。
2. 论文主张限定为少图适配预算下的冻结功能收益。普通共享非线性回归仍是机制竞争解释；D72维持一个条件性支持定理，不从两来源结果推断新的Anchor几何或宽度因果机制。
3. 下一主要障碍是从已消费source400之外建立真正独立的确认组，先冻结方法、主要比较、信息预算和停止规则，再取得结果。当前结果用于选择REC主候选，是明确的开发阶段选择，需在确认账本登记。A/B不展开。
4. 全部原始评分数据已回收，后续写作和复算为本地工作；GPU服务器可关闭，实际电源状态未知。本轮比较整合验收后删除当前基线续作自动化，未将整篇论文或旧暂停理论目标标为完成。

## Sources

- 原始结果根：`raw/projects/latentatlas/c-baseline-d73-20261019/completed-flux-score-r1/`。
- 固定实验协议（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/d73-execution/protocol.md`）、最终评分账本审计（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/d73-execution/flux-score-completion-root-audit-r1.json`）、实际技术资格（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/d73-execution/flux-score-real-qualification-root-audit-r1.json`）。
- 原字节回收清单（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/d73-execution/flux-score-complete-transfer-1792480865.json`）。
- 冻结统计实现结果（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/d73-execution/flux-statistics-r1.json`）、独立复算及限域（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/d73-execution/flux-independent-recompute-r1.md`）、主控验收（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/d73-execution/flux-statistics-root-acceptance-r1.json`）。
- [Cosmos比较](d73-cosmos.md)、论文计划（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/c-paper-plan-d73.md`）、[latentatlas-c-baseline-d73-20261019](../notes/latentatlas-c-baseline-d73-20261019.md)、`latentatlas-paper-framework`。
