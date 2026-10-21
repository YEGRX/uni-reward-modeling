> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# R17 A2 等机会续训与冻结DiNa比较

## 1. Date
2026-10-14。

## 2. Purpose
用户已选择“等机会延长A2至收敛（推荐）”。从三组实际terminal1000继续，保留原模型、数据、loss、AdamW状态、sampler/RNG与原LR曲线，解决原收敛HOLD后完成已有权限下的两候选冻结DiNa比较。

## 3. Code Version / Commit
独立worktree `scripts/latentatlas-r17-a2-continuation-20261014`，branch `codex/r17-a2-convergence`，continuation commit `0fab4fd21d49197db1d749c326a5135511bfce3d`，含scoring当前HEAD `2faaef5fc019efbfa3de0e1be2c8db2f52dd5ac4`；spec canonical SHA `cb524cb1743e3bc162aa023acd552ccddfc494bbbac80e38b0e6d1e4b2779e97`。85pins，原80代码固定项逐字节保留。

## 4. Dataset / Input
原Cosmos FIT64/VAL64和原256paired payload、FIT-only variance与三A2 terminal1000权重。原DEV28/Native/REC不参与续训。

## 5. Parameters
三LR .0001/.0003/.001，B32、micro1、原坐标损失；从1001继续原500warmup/12000cosine，不reset。各500步为共同cohort，额外可选1500/2000/...；原500/1000历史保留。滚动六点50步间隔交给原≤1%gain/≤2%range/≤5%drift/≤1.25RECVAL与逐图BF16门，不放宽。只有同一cohort三组全部通过才停；原schedule定义域12000末仍未过则HOLD，不发明新的LR曲线。

## 6. Command
冻结continuation_transport→remoteCPU完整data/terminal预检→前台owned GPU worker。共享GPUlock、Linuxparentdeath、600s无账本进展watchdog，无总wall上限。额外恢复预测角色与全部update/VAL/shadow事前计费。

## 7. Results
**A2续训、两候选完整DiNa评分与独立CPU复算全部完成。** 三LR在1500/2000尚未共同合格，2500首次全部通过原阈值；selected LR .001 / 2500，VAL NMSE **0.09568115434376523**，checkpoint SHA `0a2a83368d59d265d1269128ad2d0344b09cfca3ab508a34c86a8fd90c2e31e7`。A1保持原LR .005 / 360 / SHA2432f111…不变。

新增4500次update、144000训练forward/同数backward；worker **1458.679943154秒（24.31分钟）**，Reward0。9398行账本、4698reserve/commit对、18PT/486tensor/85pins、AdamW/sampler/RNG连续性独立CPU审计PASS。原六trial29.47分钟及1000步HOLD均保留。

评分manifest canonical `b3a4db904c64fd0ab9424ef6a9127d25195782e8f5346918035bc3f58d0618c9`，29pins/41CPUtests。实际stage `r17-continued-dina-scoring-20261014-114112`：完整技术PASS，1008pair/16128R-side评分完成，worker8057.015955698s（其中科学6494.500894940s）。全stage技术+科学实际18658R/18660backbone。522文件与505参考资产SHA通过；全部6效应独立复算精确一致，1016坐标数值通过。

| 方法 | Native agreement | Margin MSE | RMSE / MAE | Human Accuracy | VAL NMSE | DEV NMSE | 参数 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Native | 100% | 0 | 0 / 0 | 72.8175% | — | — | — |
| REC1000 | 93.4109% | 0.233816244 | 0.483545 / 0.367952 | 72.6190% | 0.107318542 | 0.120299（R15） | 39,056 |
| A1 V26-MLP-LFM adapted | 92.1480% | 0.346610274 | 0.588736 / 0.446291 | 72.2966% | 0.207817544 | 0.245252281 | 2,128 |
| A2 MatchedSpatial GELU | 94.7487% | 0.158372698 | 0.397961 / 0.310818 | 72.6190% | 0.095681154 | 0.100681590 | 40,216 |

主REC−A2 agreement −1.337834pp，校正CI[−3.202407,+.012513]；MSE效应E−.192365，CI[−.302202,−.064927]；Human差0pp，CI[−2.058532,+1.959325]。A2 MSE可靠更好，但预冻双功能/Human判决均未决，实践等效未建立。

## 8. Analysis
保留原六trial29.47min与A2原1000HOLD。新延长cost单列，同Anchor信息不等于同1000-update compute。主统计仍RECvsA2/RECvsA1、6effects、28groups、四流不可拆。DEV28仍开发域；原论文benchmark和完整FFM+Task仍NOT_RUN。

## 9. Problems
评分前台SSH连接中断后，只读确认原同一进程继续并完整结束；stage returncode0、watchdog正常、无剩余计算进程，未重启或重复评分，原exit255与恢复收据保留。

前台首个长stdin帧等待；两个同长度CPUprobe通过，根因未确定。计划停止stalled reader时fresh-root guard发现阶段已出现而拒绝，未发kill、未重启或重复训练；原同一spec/进程继续。全过程记录，不称传输成功为模型结果。

## 10. Next Steps
本次已完成。GPU服务器可以关闭，后续无需服务器。论文应弱化REC独立性能优势，保留充分训练A2强接口；新独立connected groups和合法同架构FFM是后续研究缺口，不在本任务自动追加。

## 11. Sources
Source: `raw/projects/latentatlas/r17-a2-convergence-and-dina-20261014/`，actualrun `r17-a2-continuation-20261014-111732/`；direct-user-A2-continuation-authority.json；execution-spec-A2-continuation-r1.json；independent-continuation-code-review/；原六trial `raw/projects/latentatlas/r17-tier-a-12h-20261014/`。
相关：`latentatlas-r17-tier-a-formal-completion`、`R17_TIER_A_TRAINING_QUALIFICATION`、`R17_PUBLISHED_BASELINE_REAL_RESULTS`、`R17_TRAINING_AND_SCORING_EXECUTION_SPEC`。
