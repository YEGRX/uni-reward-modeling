> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# FLUX × Cosmos 跨编码器Reward一致性：DEV28

## 1. Date
2026-10-14启动，2026-10-15收口。

## 2. Purpose
检验同图Anchor训练出的独立接口，在不同VAE候选同池比较时能否无需额外Reward校准而共享冻结评分标尺。用户确认该应用场景存在；最终选择本轮只做完整DEV探索，新组另做。

## 3. Code Version / Commit
独立子仓库 `scripts/latentatlas-r17-cross-encoder-20261014`，branch `codex/cross-encoder-reward-consistency`。原R17训练/scoring代码不修改。主code/设计在第一次混合结果前封存，见raw `code-before-mixed-score-analysis-r1.json`；最终Git/SHA随交付。

## 4. Dataset / Input
原DEV28，1008pair/252images/28connected groups/4streams；共4032相关判断，Native0共33，agreement分母3999。Native+FLUX旧逐侧score与Cosmos旧REC/NoReg/Perm1逐侧score经identity/runtime/teacher/noise审核通过，全部CPU重组。

## 5. Parameters
FF/FC/CF/CC；Native tie排除、studenttie半失配。Delta=(dFC+dCF−dFF−dCC)/2。100000整组PCG64 seed2026101407。校准为两折14/14 group crossfit的mean offset和positive affine OLS，不用Human标签，额外Reward分数信息单列。

## 6. Command
在子仓库目录运行全部 `python -m unittest discover -s tests -v`。实际分析：`python scripts/latentatlas-r17-cross-encoder-20261014/run_analysis.py --inputs raw/projects/latentatlas/r17-cross-encoder-consistency-20261014/inputs/input-manifest-r1.json --output <fresh-output>`。只需CPU与NumPy；输出必须新路径，不覆盖旧raw。

## 7. Results
FF91.6854%、FC88.9597%、CF88.9972%、CC93.4109%。Delta3.5696pp，95%CI[2.5487,4.6738]pp，upper95=4.4864pp。3546个双单路严格正确判断中371个混合反转，条件10.4625%。常数offset crossfit Delta .8252pp（削减76.88%），正仿射 .8627pp；校准无正式CI，不称通过2pp风险认证。

Cosmos NoReg/Perm1的Delta25.6814/25.5564pp，同时它们CC仅59.6774/59.4274%，不是机制隔离对照。NoReg为固定初始化Projector；Perm1真实评分CP500，不能误用terminal1000。

15项单元测试PASS；独立50767项检查/492数值叶PASS，maxabs3.55e−15。所有新增Projector训练/GPU/Reward/VAE调用均0。服务器不需要继续运行。

## 8. Analysis
within-encoder保序不足以保证混合候选可直接评分。约77%额外失配可由简单offset诊断消除，当前更支持工程失效边界与校准解释，未支持自动共同标尺的新核心数学机制。DEV为已消费开发域；校准读取额外Reward信息，即使新增调用为0也不是原R0方法。

## 9. Problems
现有source400全部SRC0已消费，Oct2新组也已消费。远端两个registry/access原文件SHA与本地历史记录一致。没有把旧NEWGROUPS当未消费数据；原teacher tensor并未在本轮重新完整rehash，只继承已核验历史运行与hash-bound代码证据。

## 10. Next Steps
当前DEV任务完成。按用户明确选择，独立新组确认 `DEFERRED_BY_USER/NOT_RUN`。不下载新数据，不启动GPU。若日后确认，需要真新组与冻结模型/校准/统计、独立CAL以及新runtime资格。

## 11. Sources
Source: `raw/projects/latentatlas/r17-cross-encoder-consistency-20261014/`。主要原工件/哈希见`source-index.md`；结果`dev28-analysis-r1/result.json`；身份`independent-assets/`；独立统计`independent-statistics/report.json`；新组暴露`independent-fresh-groups/`及远端收据。
相关：`latentatlas-cross-encoder-consistency-results`、`latentatlas-cross-encoder-consistency-protocol`、`R17_PUBLISHED_BASELINE_REAL_RESULTS`、`latentatlas`。
