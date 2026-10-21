# 近期实验详细记录：原编号、报告与结果表

更新：2026-10-21。首次阅读请从[首页的完整实验讲解](../../../README.md#experiments)进入：Anchor → REC评分 → baseline → 真实用途与Noisy实验。本页保留原编号、技术设置和逐项证据，方便查表与追溯。[原87条历史索引](../index.md) · [新增来源与文件指纹](source_manifest.json)。

本页汇总已完成工作，新增16份研究记录、11份主要报告和4份原结果CSV。原87条目录、统计表和资产清单保持历史身份。本次入仓只整理文档，没有重新训练或评分；早期准备快照中的 `NOT_RUN` 以相应阶段和日期理解，后续真实完成结果另列。

## 一、主要进展与真实生成实验

<a id="d73"></a>
### D73：同 Anchor 的强基线与直接前作比较（10月19–20日）

每来源64 FIT + 64 VAL，坐标监督与选模，冻结同一 DiNa；评价为已消费DEV28：252图、1008物理pair、4流，Native非tie分母3999。两个来源共享评价图，分别推断。Interposer为同Anchor、batch/损失等合同下的适配对照，不是原发布大数据训练完整复现；相同更新与搜索机会不等于相同FLOPs。

| 方法 | FLUX Native agreement | FLUX margin MSE | Cosmos Native agreement | Cosmos margin MSE |
| --- | ---: | ---: | ---: | ---: |
| 强空间 Affine | 91.5854% | .472092 | 90.0850% | .470821 |
| Interposer-MSE | 90.5351% | 1.072784 | 92.2731% | .296914 |
| Interposer-cycle | 86.5716% | 1.844546 | 92.6732% | .349111 |
| REC | **94.7237%** | **.298031** | **94.6362%** | **.147559** |
| A2 | 92.8607% | .315073 | 94.8737% | .156197 |

REC相对强Affine的agreement与margin MSE改善有原调整区间支持；对Interposer的结论随来源和指标不同，REC–A2的两主端点比较仍未分辨。人类偏好增益不由高agreement自动推出。原报告保留每一比较的区间和选择规则。

[FLUX主要报告](reports/d73-flux.md) · [Cosmos主要报告](reports/d73-cosmos.md) · [完整阶段记录](notes/latentatlas-c-baseline-d73-20261019.md)

<a id="r1"></a>
### LRM-R1：真实 FLUX 终态能否复用冻结 DiNa（10月21日）

4个已消费Prompt、每个2候选，8张真实FLUX图；每候选2条固定参考噪声。比较完整图像T1参考、REC直接终态、源图重编码REC和强Affine，沿用正式接口，无新增训练或生成。

| 路径 | Native逐流agreement | 均分Best-of-2 | Score MAE | Margin MSE |
| --- | ---: | --- | ---: | ---: |
| REC直接终态 | 7/8 | 4/4 | 1.218750 | .107910 |
| 重编码REC | 7/8 | 3严格同选＋1精确tie | 1.308594 | .108643 |
| 强Affine直接终态 | 8/8 | 4/4 | 1.294922 | .106323 |

正式判断：`AFFINE_SUFFICIENT_IN_PILOT`。普通Affine已覆盖本轮均分选择，REC未显示专属增量。绝对分数偏移与组内排序分开评价；统计单位是4个Prompt，不是8个流比较。

[真实实验报告](reports/lrm-r1-results.md) · [正式决定](reports/lrm-r1-decision.md) · [16行逐候选/流的四路径原表](tables/lrm-r1-four-path-results.csv) · [研究记录](notes/latentatlas-lrm-r1-real-interface-qualification-20261021.md)

<a id="r2"></a>
### LRM-R2：被复用的 Reward 在目标分布上是否有效（10月21日）

只读取R1同八图的16条原生DiNa分数与8条历史PickScore，恢复身份和预处理、独立复算，无新模型调用。

| Prompt | DiNa两流均分差 | PickScore分差 | 同选 |
| --- | ---: | ---: | --- |
| dev-01 | .140625 | −.460210800171 | 否 |
| dev-02 | −.218750 | .001127243042 | 否 |
| dev-03 | .562500 | .015584945679 | 是 |
| dev-04 | −.250000 | .484071731567 | 否 |

严格同选1/4，无精确tie；三组分歧中DiNa原两流均同向。没有同图人类偏好标签，PickScore也不是人类真值。`GO_REWARD_VALIDITY_CONFIRMATION`表示报告建议先做新目标内容盲评，**本轮没有执行该后续任务**。

[有效性分析](reports/lrm-r2-validity.md) · [科研决定](reports/lrm-r2-decision.md) · [四组原比较表](tables/lrm-r2-reward-comparison.csv) · [研究记录](notes/latentatlas-lrm-r2-reward-validity-audit-20261021.md)

<a id="n1"></a>
### LRM-N1：原 Clean 接口对真实 Noisy State 的迁移（10月21日）

R1前两个历史Prompt、4条原生轨迹，在原28步调度接续缓存，捕获k23/k26，共8个真实状态；四个终态逐位匹配历史候选。REC、强Affine和完整DiNa固定，无本轮训练。源sigma与DiNa reference sigma分开，直接raw-noisy路径不额外二次加噪。

| 路径 | k23同即时/终态参考 | k26同即时/终态参考 | Final regret（中/后） |
| --- | --- | --- | --- |
| 完整当前估计图像参考 A | 2/2 | 2/2 | 0 / 0 |
| 当前clean estimate → REC B | **2/2** | **2/2** | **0 / 0** |
| raw noisy → REC C | 2/2 | 1/2 | 0 / .09375 |
| raw noisy → Affine D | 1严格同选＋1tie，半分.75 | 1/2 | .03515625 / .1640625 |

正式判断：`CLEAN_ESTIMATE_BRIDGE_ONLY`。B在两个已观察流中均保持方向，C后期dev-02反向、D后期dev-01反向。中期C的margin MSE反而低于B，不能把B保序写成所有数值指标占优。两Prompt和重复时点不支持总体迁移率；Final仍是冻结DiNa端点，人类效用问题沿用R2结论。端到端节省未测。

[完整结果及所有分差](reports/lrm-n1-results.md) · [输入与时间合同](reports/lrm-n1-contract.md) · [科研决定](reports/lrm-n1-decision.md) · [64行逻辑科学分数（56新＋8复用）](tables/lrm-n1-four-path-scores.csv) · [逐状态比较](tables/lrm-n1-per-state-comparison.csv) · [研究记录](notes/latentatlas-lrm-n1-real-noisy-transfer-20261021.md)

## 二、此前完成的检验与机制诊断

<a id="mixed"></a>
| 日期 / 阶段 | 做了什么、观察到什么 | 原记录 |
| --- | --- | --- |
| 10月14日 R17方法审计 | 区分LFM/FFM/TLT、原作与跨VAE适配；该阶段CPU准备不代表原benchmark完成 | [方法与预算记录](notes/latentatlas-r17-published-stitching-competition.md) |
| 10月14日 A2续训与冻结DiNa比较 | Cosmos A2 margin MSE .158373、REC1000 .233816；Human Accuracy相同，排序增益区间未决 | [完整记录](notes/latentatlas-r17-a2-convergence-and-dina.md) |
| 10月14–15日 DEV28混合评分 | FF/CC agreement 91.6854%/93.4109%；FC/CF 88.9597%/88.9972%。额外失配3.5696pp，95%CI[2.5487,4.6738]pp；offset两折交叉拟合降至.8252pp，无正式校准CI及新组确认 | [混合路径与校准](notes/latentatlas-cross-encoder-reward-consistency-dev28.md) |
| 10月15日人工噪声与最小轨迹Pilot | 2组18图72对，Clean/两噪声档均67/72；真实两Prompt四图中，石桥Clean原已反序 | [A/B/C记录](notes/latentatlas-noisy-anchor-reuse-minimal-pilot.md) |
| 10月15日真实中段补充；18日D63 | 原4轨迹恢复k14，相对终态新增反转0/2；原Clean失配保持。D63离线漂移修正未过事前源误差门，停止该候选 | [真实中段与漂移筛查](notes/latentatlas-real-mid-trajectory-anchor-reuse-pilot.md) |
| 10月16日联合决策与18日D60 | REC→A2有142次严格翻转，但human修复/损坏90/90；margin数值改善和人类正确性净增益分开 | [联合决策记录](notes/latentatlas-r17-real-decision-audit-20261016.md) |
| 10月16日多源Noisy V0 | 4个DEV Prompt、FLUX/SD1.5共16轨迹；普通ridge复现34/36匹配选择，mixed等于固定FLUX选择；SD1.5为1024部署，和常用512设置不同 | [多源真实轨迹记录](notes/latentatlas-multisource-noisy-v0-20261016.md) |
| 10月18日D44强仿射对照 | 补齐含边界bias的普通映射，区分特定拟合程序差别与“非线性必需” | [D44](notes/latentatlas-affine-gate-d44-20261018.md) |
| 10月18日D53仿射投影 | 指定投影解释96.864% FIT输出变化，却丢失四个筛选案例的主条件赢家；说明小坐标残差可有功能作用 | [D53](notes/latentatlas-affine-carrier-d53-20261018.md) |
| 10月18日D56/D58隐藏特征 | 学后特征OLS保留4个主条件赢家，初始化特征为2个；弱条件仍失败。D58做修正的均值/空间分解 | [D56/D58](notes/latentatlas-feature-readout-d56-20261018.md) |
| 10月18日D59组成互换 | 单独均值或空间变化项均未保留全部4个主条件赢家，作用随案例不同 | [D59](notes/latentatlas-spatial-swap-d59-20261018.md) |
| 10月20日D74少Anchor预测 | 16/32/64 FIT开发检验；坐标选择器在四个FLUX设置选错，未带来主要决策收益，正式NO_GO_PREDICTION | [结果](reports/d74-results.md)、[决定](reports/d74-decision.md)、[记录](notes/latentatlas-d74-few-anchor-functional-prediction-20261020.md) |

这些开发和筛选案例用于定位适用边界，不能替代方法冻结后的独立内容确认。原Q32、HPS及R18历史结果仍保留在[旧索引](../index.md)，没有因本次主线重排而删除。

## 三、工件与复核范围

- `notes/`：16份原研究页的可读导出，保留执行历史，跨仓原件引用改为定位文字。
- `reports/`：11份主要报告/决定/合同导出，重点覆盖D73、D74、LRM-R1/R2/N1。
- `tables/`：4份既有原结果CSV，逐字节保留；R1是16行四路径并列表，N1是64行方法逐分数表。
- `source_manifest.json`：逐文件原件定位、原SHA与导出SHA；Markdown仅净化个人路径/私有主机和迁移链接，原科学数值保留。

本仓提供这些小型记录与表格。原张量、模型、完整运行环境和全部科学回放依赖仍由原工件库管理；本次检查文件身份和文档，不重新调用模型或重验全部科学统计。
