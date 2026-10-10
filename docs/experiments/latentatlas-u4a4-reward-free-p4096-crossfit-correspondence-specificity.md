# LatentAtlas U4-A4 Reward-Free P4096 Cross-Fit Correspondence Specificity

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

U4-A4 是 U4-A3 之后唯一一次 `development-only / adaptive follow-up / non-confirmatory / reward-free / reused nonfresh evaluation cohort / CPU-only` 的 P4096 cross-fit correspondence specificity audit。Run identity 为 `U4A4_DEV_REWARD_FREE_P4096_CROSSFIT_CORRESPONDENCE_SPECIFICITY`。

它只回答一个有限问题：用注册的 P4096 source rows 训练时，若 target pairing 是 correct canonical target 或五个冻结 whole-row permutation null，参数量匹配的 flat affine family F 与 invariant nonlinear family N 能否在 identity-disjoint、但历史上已经暴露的 H1105 development cohort 上表现出稳定的 correct-over-all-nulls advantage。

这不是 Reward 实验，也不是 fresh holdout、independent test、confirmatory authority 或 generalization experiment。它不能建立 canonical U、universal U、Reward transfer、unseen-VAE transfer、真实部署能力，也不能把 H1105 称为 unseen/fresh/test cohort。

相关页面：`latentatlas`（原wiki关联）、[latentatlas-u4a3-reward-free-k64-parameterization-factorization](latentatlas-u4a3-reward-free-k64-parameterization-factorization.md)、`representation-alignment`（原wiki关联）、`latent-space`（原wiki关联）。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u4a4-reward-free-p4096-crossfit-correspondence-specificity.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Population algorithm：`sha256_rank_split_seed_2026082201`；T=`5201`、P4096=`4096`、H1105=`1105`。
- Population proof：P4096 与 H1105 disjoint，且二者 union 等于 T。
- P4096 source：标准化 DCAE tokens，`float32 [4096,32,16]`；target：raw SD/FLUX barycenter，`float32 [4096,64]`。
- H1105 evaluation：source `float32 [1105,32,16]`，correct canonical barycenter target `[1105,64]`；全 24 个 artifacts 使用同一 original-order correct H1105 gallery，query `i` 的 positive index 固定为 `i`。
- DCAE normalization：`(-0.41792598366737366, 2.2100250720977783, 1e-6)`，不从 H1105 重新估计。
- Pairings：`correct` 加 `perm_01..perm_05`；五个 null 是 seeds `2026082202..2026082206` 的 single-cycle whole-row derangements，全部 bijective、fixed points=`0`、target-row multiset 与 correct 完全相同。
- 只用 P4096 拟合；H1105 只在 fit seal 之后由 one-shot private evaluator 打开一次。本次 P/H identity-disjoint，但 H1105 已在历史 U4-A 流程中暴露，因此不能解释成新鲜泛化证据。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 Frozen classification

正式分类：**`CROSS_FAMILY_CORRECT_PAIRING_ADVANTAGE_ON_HISTORIC_DEV_COHORT`**。

Safe claim：在当前注册协议中，P4096-trained F 与 N 都在历史已暴露的 H1105 development cohort 上对 correct pairing 产生了 robust correct-over-all-nulls advantage。它是 development-only、adaptive、non-confirmatory、reward-free 证据，不是 fresh holdout 或 generalization evidence。

### 7.2 F 的 P4096 train summary

F 的 shared SVD design shape 为 `[4096,513]`，numerical rank=`513`，effective condition number=`124.854808`，cutoff=`6.672854e-10`。六个解析 artifacts 全部 finite；normal-equation 与 row-space relative residual 都约为 `1e-15`。

| Pairing | Global Charbonnier | NRMSE | R@1 | MRR | Mean cosine | Relative fit residual |
|---|---:|---:|---:|---:|---:|---:|
| correct | 0.639248 | 0.199769 | 0.426758 | 0.528332 | 0.982769 | 0.199769 |
| perm_01 | 0.915929 | 0.286233 | 0.001465 | 0.008440 | 0.963834 | 0.286233 |
| perm_02 | 0.917105 | 0.286601 | 0.003174 | 0.009106 | 0.963751 | 0.286601 |
| perm_03 | 0.916300 | 0.286349 | 0.002686 | 0.009722 | 0.963818 | 0.286349 |
| perm_04 | 0.917179 | 0.286624 | 0.001221 | 0.006746 | 0.963728 | 0.286624 |
| perm_05 | 0.915767 | 0.286183 | 0.001465 | 0.008592 | 0.963902 | 0.286183 |

### 7.3 N 的 P4096 train summary 与 adequacy

每个 cell 均为 10,000 updates / 640,000 presentations，finite、terminal reload/hash 一致且 parameter delta norm `>0`。下表为同一 pairing 的三个 seed range。

| Pairing | Terminal loss range | Terminal/initial range | NRMSE range | R@1 range | MRR range | Adequate seeds |
|---|---:|---:|---:|---:|---:|---:|
| correct | 0.567753–0.569622 | 0.176477–0.177577 | 0.177426–0.178010 | 0.400879–0.411377 | 0.489804–0.498522 | 3/3 |
| perm_01 | 0.959574–0.961145 | 0.298048–0.300475 | 0.299873–0.300364 | 0.000488–0.000732 | 0.003242–0.003536 | 3/3 |
| perm_02 | 0.959420–0.960612 | 0.298137–0.300131 | 0.299825–0.300197 | 0.000488–0.000488 | 0.002833–0.002940 | 3/3 |
| perm_03 | 0.959324–0.960997 | 0.297738–0.300040 | 0.299795–0.300318 | 0.000244–0.000488 | 0.002893–0.003149 | 3/3 |
| perm_04 | 0.959638–0.961237 | 0.298196–0.300003 | 0.299893–0.300393 | 0.000244–0.000732 | 0.003445–0.003578 | 3/3 |
| perm_05 | 0.959762–0.960224 | 0.297959–0.300041 | 0.299931–0.300076 | 0.000244–0.000244 | 0.002659–0.002803 | 3/3 |

N optimization adequacy=`PASS`：correct adequate seeds=`3/3`；每个 null 也都是 `3/3`；exact registry、same-seed bindings 与 terminal integrity 全部为 true，failure reasons 为空。

### 7.4 H1105 全部 24 个 aggregate metric rows

下表保留全部注册 aggregate metrics；显示值四舍五入，机器判定使用 `evaluation_summary.csv` 中未舍入的 float64 数值。

| Family | Pairing | Seed | NRMSE | RMSE | MSE | Cosine | R@1 | R@5 | MRR | Mean rank | Median rank | Eff. rank | Var. mass | Finite |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| F | correct | — | 0.225712 | 0.720134 | 0.518593 | 0.977590 | 0.363801 | 0.601810 | 0.471814 | 26.171 | 3.0 | 14.434 | 36.449 | true |
| F | perm_01 | — | 0.325956 | 1.039964 | 1.081525 | 0.952625 | 0.000905 | 0.007240 | 0.007549 | 544.453 | 529.0 | 20.867 | 9.111 | true |
| F | perm_02 | — | 0.326954 | 1.043149 | 1.088159 | 0.952144 | 0.000905 | 0.003620 | 0.007162 | 545.855 | 547.0 | 21.188 | 8.777 | true |
| F | perm_03 | — | 0.324653 | 1.035807 | 1.072895 | 0.952804 | 0.000905 | 0.004525 | 0.007569 | 545.660 | 555.0 | 21.469 | 8.830 | true |
| F | perm_04 | — | 0.325962 | 1.039984 | 1.081566 | 0.952561 | 0.000000 | 0.003620 | 0.006252 | 548.060 | 547.0 | 20.666 | 8.881 | true |
| F | perm_05 | — | 0.327414 | 1.044615 | 1.091220 | 0.952219 | 0.001810 

（其余历史细节见来源快照。）

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

1. U4-A3 只证明 K64 上 F/N 能同时插值 correct 与 null，不能证明 correspondence specificity。U4-A4 把拟合 population 扩到 P4096、在 identity-disjoint H1105 上 cross-fit 后，F 与 N 的 correct 都稳定胜过全部五个 null，且三项 registered lower-bound gates 同时通过；这建立了当前历史开发 cohort 内的 correspondence-specific signal。
2. 信号不是单一 architecture 偶然：parameter-matched F 与 N 都通过，故冻结 headline 是 cross-family advantage。N 的点估计更高，但 U4-A4 没有注册 F-vs-N model-selection gate，不能据此宣布 N 为最终架构。
3. Correct mapping 并非完美 coordinate recovery：F/N correct H NRMSE 约为 `0.226` / `0.186`，R@1 约为 `0.364` / `0.462–0.471`。因此本实验支持“正确配对具有可识别优势”，不等于 raw coordinate 已完全恢复或 universal canonical target 已证明。
4. Query bootstrap 只度量固定 H1105 cohort 上、固定 artifacts 下的 conditional query robustness。它不是 training-randomness CI、population-generalization CI 或显著性检验。
5. 结果把解释空间从“小样本纯 interpolation”推进到“大量配对、历史开发 cohort 上的 correct/null discrimination”，但仍没有跨越 Reward-free registered development audit 到 fresh functional confirmation 的证据边界。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

1. 当前执行 hard stop：不自动设计、创建或运行 U4-A5、U4-B、Reward、fresh holdout、larger K、新 VAE 或任何其他 follow-up。
2. 仅作为建议、并未执行：先进行 scientific review；如果之后有独立审批与真正未触碰的 authority，再冻结单一协议检验这种 structural correspondence specificity 是否能转化为 Reward functional specificity。不能复用当前 H1105 作为 fresh confirmation。
3. 不应依据本实验的 N 较高点估计直接做 architecture selection；若未来需要选择，必须另行冻结选择 authority 与 gate。
4. 正式运行和结果整理均为 CPU-only；GPU 未使用且无需租用服务器，若 GPU 实例仍开着可以关闭。

## Sources

- [来源快照](../source-snapshots/latentatlas-u4a4-reward-free-p4096-crossfit-correspondence-specificity.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u4a4-reward-free-p4096-crossfit-correspondence-specificity.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
