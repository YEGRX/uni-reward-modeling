# LatentAtlas U4-A2 Reward-Free Train-Closure Localization

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

U4-A2 是一个 `development-only / adaptive follow-up / non-confirmatory` 的 CPU-only 诊断实验。它只检查 U4-A 冻结训练对应关系

`standardized DCAE token representation z -> raw SD/FLUX barycenter H`

在有限 train population 上，能否被当前 Bridge、直接坐标目标或预注册容量 oracle 闭合。它不打开 Reward、H1105、validation/test、fresh authority 或 held-out structure，也不评价 canonical target validity、Reward transfer、unseen-VAE generalization、low-cost onboarding、structural generalization 或 LatentAtlas 全局命题。

相关页面：`latentatlas`（原wiki关联）。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u4a2-reward-free-train-closure-localization.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Population：从 5,201 个 train identities 按冻结 split seed `2026082201` 排序得到 P64；`K8 subset K16 subset K64`，P64 commitment 为 `298de01620748320cc2f5c521448f806ac13ecd5c2e3db7c544f7aa5956c9707`。
- Input `z`：标准化 DCAE、CPU `float32`、shape `[K,32,16]`；标准化为 `(z_raw - (-0.41792598366737366)) / (2.2100250720977783 + 1e-6)`。
- Target `H`：raw SD/FLUX barycenter、CPU `float32`、shape `[K,64]`，定义为 `(SD_shared + FLUX_shared) / 2`，没有 L2 normalization 或新 H 定义。
- Pairing oracle 在 K8/K16/K64 上均为 R@1=`1.0`、MRR=`1.0`。
- Input-target consistency 为 `INPUT_TARGET_FUNCTIONAL`；没有 duplicate source/target group，也没有 conflicting source group。
- 只允许读取重建 train P64 所需的 manifest metadata；Reward、H1105、validation/test latent/output/metric/token/pair identity、CUDA、network 与 holdout materialization 计数均为 0。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 Frozen classification

正式分类：**`CURRENT_SYSTEM_TINY_SET_CLOSABLE`**。

Decision precedence 在 A robustly closes K8 时即命中该分类。它的准确含义是：当前 1,088 参数 Bridge 与原 U4-A objective 在 frozen observed K8 train set 上实现了注册的 terminal retrieval closure；它不等于 raw coordinates 已恢复，也不表示 K16/K64 已闭合。

Frozen closed cells：

- `A/k8/lr_1e-3`；
- `B/k8/lr_1e-3`；
- `B/k16/lr_1e-3`；
- `R/selected/k8/lr_1e-3`。

Secondary mechanism tag 为 `CLOSURE_ASSOCIATED_WITH_RANK_RECOVERY`。这是相关性标签，不是 rank recovery 的因果证明。

### 7.2 Per-seed terminal rows

| Cell | Seed | R@1 init→final | MRR init→final | Coordinate RMSE | Cosine | Rank init→final / target | Variance | Closed |
|---|---:|---:|---:|---:|---:|---:|---:|:---:|
| `A/k8/lr_1e-3` | 20260823 | 0.1250→1.0000 | 0.3772→1.0000 | 0.814841 | 0.964905 | 3.948→3.927 / 5.605 | 1.072899 | yes |
| `A/k8/lr_1e-3` | 20260824 | 0.2500→1.0000 | 0.4449→1.0000 | 1.024674 | 0.947318 | 3.849→3.278 / 5.605 | 1.472269 | yes |
| `A/k8/lr_1e-3` | 20260825 | 0.1250→1.0000 | 0.3844→1.0000 | 0.967015 | 0.952129 | 4.430→3.407 / 5.605 | 1.315185 | yes |
| `A/k16/lr_1e-3` | 20260823 | 0.1250→0.9375 | 0.2935→0.9583 | 1.020158 | 0.945819 | 5.321→4.069 / 10.382 | 1.098650 | no |
| `A/k16/lr_1e-3` | 20260824 | 0.0000→0.9375 | 0.2045→0.9583 | 1.058666 | 0.945521 | 5.562→4.067 / 10.382 | 1.162292 | no |
| `A/k16/lr_1e-3` | 20260825 | 0.1250→0.7500 | 0.2608→0.8177 | 1.056846 | 0.942775 | 5.829→4.091 / 10.382 | 1.106645 | no |
| `A/k64/lr_1e-3` | 20260823 | 0.0156→0.3125 | 0.0878→0.4811 | 0.972786 | 0.955425 | 7.503→7.709 / 17.614 | 0.675803 | no |
| `A/k64/lr_1e-3` | 20260824 | 0.0156→0.3750 | 0.0764→0.5015 | 0.979940 | 0.954506 | 7.871→7.815 / 17.614 | 0.700855 | no |
| `A/k64/lr_1e-3` | 20260825 | 0.0156→0.2969 | 0.0786→0.4564 | 0.981657 | 0.954435 | 8.701→7.401 / 17.614 | 0.704484 | no |
| `B/k8/lr_1e-3` | 20260823 | 0.1250→1.0000 | 0.3772→1.0000 | 0.000242 | 1.000000 | 3.948→5.605 / 5.605 | 0.759065 | yes |
| `B/k8/lr_1e-3` | 20260824 | 0.2500→1.0000 | 0.4449→1.0000 | 0.000207 | 1.000000 | 3.849→5.605 / 5.605 | 0.759052 | yes |
| `B/k8/lr_1e-3` | 20260825 | 0.1250→1.0000 | 0.3844→1.0000 | 0.000259 | 1.000000 | 4.430→5.605 / 5.605 | 0.759072 | yes |
| `B/k16/lr_1e-3` | 20260823 | 0.1250→1.0000 | 0.2935→1.0000 | 0.246285 | 0.997192 | 5.321→10.456 / 10.382 | 0.675619 | yes |
| `B/k16/lr_1e-3` | 20260824 | 0.0000→1.0000 | 0.2045→1.0000 | 0.240148 | 0.997367 | 5.562→10.559 / 10.382 | 0.679698 | yes |
| `B/k16/lr_1e-3` | 20260825 | 0.1250→1.0000 | 0.2608→1.0000 | 0.267401 | 0.996748 | 5.829→10.598 / 10.382 | 0.668032 | yes |
| `B/k64/lr_1e-3` | 20260823 | 0.0156→0.7188 | 0.0878→0.7992 | 0.692725 | 0.977603 | 7.503→15.477 / 17.614 | 0.556701 | no |
| `B/k64/lr_1e-3` | 20260824 | 0.0156→0.7188 | 0.0764→0.7973 | 0.693358 | 0.977534 | 7.871→15.707 / 17.614 | 0.560932 | no |
| `B/k64/lr_1e-3` | 20260825 | 0.0156→0.7031 | 0.0786→0.7847 | 0.692401 | 0.977558 | 8.701→15.537 / 17.614 | 0.565126 | no |
| `R/selected/k8/lr_1e-3` | 20260823 | 0.1250→1.0000 | 0.3772→1.0000 | 0.053925 | 0.999841 | 3.948→5.628 / 5.605 | 0.750458 | yes |
| `R/selected/k8/lr_1e-3` | 20260824 | 0.2500→1.0000 | 0.4449→1.0000 | 0.029659 | 0.999951 | 3.849→5.602 / 5.605 | 0.751198 | yes |
| `R/selected/k8/lr_1e-3` | 20260825 | 0.1250→1.0000 | 0.3844→1.0000 | 0.121360 | 0.999209 | 4.430→5.577 / 5.605 | 0.767469 | yes |

### 7.3 Preregistered NOT_RUN rows

| Cell | Seeds | Status / gate |
|---|---|---|
| `C/k8/lr_1e-3` | 20260823/24/25 | `NOT_RUN_B_TINY_K_CLOSED` |
| `C/k16/lr_1e-3` | 20260823/24

（其余历史细节见来源快照。）

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

1. 当前 U4-A Bridge/objective 不是“连最小 observed train set 都无法排序闭合”：A 在 K8 的 3/3 seeds 都达到 R@1=MRR=1.0，因此 headline 为 `CURRENT_SYSTEM_TINY_SET_CLOSABLE`。
2. A 的 K8 coordinate RMSE 仍为 `0.815–1.025`，final effective rank 也低于 target。这个结果只证明注册的 retrieval ordering closure，不能写成 raw coordinate recovery。
3. 把同一 Bridge 改为直接 coordinate objective 后，B 在 K8 达到近乎精确坐标拟合，并在 K16 的 3/3 seeds 达到 retrieval closure、显著恢复 effective rank；说明 objective 对小集合的坐标/结构恢复有实质影响。但由于 decision precedence 先命中 A/K8，本实验的正式分类不是 `OBJECTIVE_LIMITED`。
4. B/K64 仍只有 R@1≈`0.703–0.719`、MRR≈`0.785–0.799`，没有 closure。由于 C 被 gate 掉，这不能唯一归因于 capacity、optimization、canonical target 或 input reward completeness。
5. 预注册 objective restoration 选择 B/K8，并在 3/3 seeds 保持 retrieval closure；它是 secondary diagnostic，不改变 headline。
6. 这些都是 frozen observed train correspondence 上的 adaptive development evidence。它不能升级 U4-A predecessor，也不能支持 Reward 或 unseen-VAE 功能结论。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

1. 当前 hard stop，先进行科学复核，不自动启动后续实验。
2. 允许保留的方向性信号是：小集合表现具有明显 K 依赖，且 direct coordinate objective 在 K8/K16 明显优于原 objective；任何关于 K64 capacity/optimization 的进一步定位都需要新设计与新的 scientific approval。
3. 不自动启动 U4-A3、U4-B、FRA-0、Reward、FFT/cycle、更大 population 或新 H。U4-A predecessor 仍保持原 `OPTIMIZATION_OR_CAPACITY_LIMITED_INDETERMINATE`。
4. 当前实验阶段已经结束，后续仅为 CPU-only 结果复核；不需要 GPU 或租用服务器，若实例仍运行可以关闭。

## Sources

- [来源快照](../source-snapshots/latentatlas-u4a2-reward-free-train-closure-localization.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u4a2-reward-free-train-closure-localization.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
