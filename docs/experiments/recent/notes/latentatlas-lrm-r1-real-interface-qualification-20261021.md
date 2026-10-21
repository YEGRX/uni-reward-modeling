> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# LatentAtlas-LRM-R1：真实 FLUX 终态冻结 Reward 接入资格

## 1. Date

2026-10-21。状态：**实际实验与复算完成，停止**。正式决定：`AFFINE_SUFFICIENT_IN_PILOT`。

## 2. Purpose

判断既有Anchor-only接口是否能对真实FLUX.1-dev原生终态复用冻结DiNa，区分输入合同问题、源重编码差异、T1目标变化和普通强映射的作用。

本轮是四个已消费历史DEV Prompt的资格诊断，不是独立确认；研究范围仅真实终态同源Best-of-2，无新训练、D74、可靠性新算法或论文改写。

## 3. Code Version / Commit

本轮源码：`scripts/latentatlas-lrm-r1-20261021/`。执行spec逐文件SHA锁定`common.py`、`prepare.py`、`score.py`及13份原D73依赖，未覆盖历史代码。

- 准备spec SHA：`b79fd4db83e833427962d13e6437e480e42d5ca9ee6f945529d94dbd4cacb93f`。
- 评分spec SHA：`0bceaa89dd7561f8c0c95a89a2d76dace051fc234a960d15f700493a11329d8d`。
- 评分前协议 SHA：`5555e124ba5f855ed8553973f3112445bd07048e762cad8090af4e7cbb3893a1`。
- 完整复现入口（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_R1_REAL_INTERFACE_QUALIFICATION/REPRODUCIBILITY/README.md`）。

## 4. Dataset / Input

历史SOURCE八候选：dev-01…dev-04，各source seed2026101601/2026101602；原PNG和terminal SHA全核。FLUX.1-dev revision `3de623fc3c33e44ffbe2bad470d0f45bccf2eb21`，28steps、1024²、guidance3.5。全部8图实际decoder replay像素/PNG SHA一致，无新增生成。

`final_native_u`是unpacked但仍scaled/shifted的BF16 u，真实q按原decoder BF16逐运算 `u/.3611+.1159` 得到。旧`generated_final/reencoded_clean`是REC1000输出，未混用。源dev VAE与D73 schnell VAE权重SHA实际相同，配置仅路径元数据不同。

## 5. Parameters

四路径：A完整生成图T1；B正式REC5000(q)；C同一REC(source posterior.mode重编码)；D正式k5/λ=.001 Spatial Affine(q)。REC SHA `801c8d5868b63ea486c057a47dfdff17ebf230ec481f974a066e6f2f1a61ef47`；Affine SHA `e49ff18ba382941f783dbe5febfebf3f9e77503f25ee20cca94a66ea34403734`。沿用64FIT/64VAL所选接口，无本轮重新选模。

同一冻结DiNa、SD3.5合法文本、σ=.4002932608127594、t=400.29327392578125、BF16 raw score；每候选2条按身份固定噪声，四路逐SHA匹配。A固定每PNG参考posterior sample seed，C源posterior.mode。技术16独立于科学64；历史T0技术分数不进入当前T1比较。

## 6. Command

实际单GPUprepare/score由持锁、父进程生存监督器执行，命令、退出码及耗时保存在原始`prepare-supervisor-r1.json`、`score-supervisor-r1.json`。无需依赖对话复原运行参数。

离线主评价器：`python3 scripts/latentatlas-lrm-r1-20261021/analyze.py --ledger <原始jsonl> --out <新json> --csv <新csv>`。独立复算`independent_audit.py`使用本地NumPy环境，不导入Torch或调用模型；`diagnose_cached.py`核留组与已有缓存。

## 7. Results

| 路径 | Score MAE | Score bias | Margin MSE | Native agreement | 均分Best-of-2 | Native regret |
|---|---:|---:|---:|---:|---|---:|
| B REC | 1.218750 | −1.218750 | .107910 | 7/8 | 4/4 | 0 |
| C 重编码REC | 1.308594 | −1.308594 | .108643 | 7/8 | 3严格保序+1精确tie，半分记为87.5% | 0（固定tie-break） |
| D Affine | 1.294922 | −1.294922 | .106323 | 8/8 | 4/4 | 0 |

主要不稳定案例dev-03：A两流margin均.5625，B为.1875/−.125，均分.03125；C为.125/−.125，均分0；D两流1.125。重编码未修复此反转。其余三组四路组选择一致。

q_cycle相对q_gen的逐图RMSE范围8.216%–20.344%，均值12.529%。REC直接/重编码到T1平均坐标MSE .099998337/.100892415，Affine .096102437；坐标统计由保存数组先升float64再差分。强Affine已解释本轮选择能力，未观察到REC专属增量。

本轮实际：DiNa科学64+技术16=80；文本12；源decode9/encode9、参考encode9；REC18、CPU Affine9；生成/训练/新外部Reward均0。准备/评分监督合计452.377秒，评分显存峰值16.365GiB。70文件取回，退出码0、无超时，六冻结根状态不变。

## 8. Analysis

主控Fraction/NumPy独立核27主指标、96留组指标、64个实际noisy输入SHA和64个score SHA，全部一致；Sol另用Fraction核相同统计并审全文。19项边界/统计测试通过。实际四Prompt是单位，两个流不计为八独立样本。无预先验证的T1功能数值阈值，决定仅描述本轮选择充分性，不称总体等效。

同图旧PickScore缓存8/8身份核验，与当前A同选1/4；外部代理不是人类真值，状态`REWARD_VALIDITY_NOT_ESTABLISHED`。接口保真与目标质量价值分开。

## 9. Problems

绝对分数均向下偏移，REC在一组中有流间反转。T0训练目标与当前生成图T1、图像域变化及参考sample的影响未独立分离。没有B失效/C恢复的模式，不能把源输入域偏移定为唯一原因。

准备脚本差分先发生于BF16；主控从原保存数组升float64重算并保留原诊断记录。该离线修正不改任何模型输出或分数，逐元素分解残差0，平方展开误差最大4.164e−17。完整说明见报告。

## 10. Next Steps

**本轮停止，无待续跑。** 值得进行有强Affine对照和目标质量依据的新组独立确认，当前不启动。原C论文Clean证据和D72支持定理保持，本轮不改稿、不扩理论、不训练新接口。服务器可关闭，电源状态未知。

相关：`latentatlas`、`latentatlas-research-decisions`、`latentatlas-theory-map`、[latentatlas-c-baseline-d73-20261019](latentatlas-c-baseline-d73-20261019.md)、[latentatlas-multisource-noisy-v0-20261016](latentatlas-multisource-noisy-v0-20261016.md)。

## 11. Sources

- [正式决定](../reports/lrm-r1-decision.md)。
- [真实实验与全部64分数](../reports/lrm-r1-results.md)。
- 失败诊断（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_R1_REAL_INTERFACE_QUALIFICATION/FAILURE_DIAGNOSIS.md`）。
- `raw/projects/latentatlas/lrm-r1-20261021/completed-r1/`及`recovery-manifest-r1.json`。
- `raw/projects/latentatlas/lrm-r1-20261021/user-request.txt`，本轮用户补充指令覆盖原规模及决定枚举。
