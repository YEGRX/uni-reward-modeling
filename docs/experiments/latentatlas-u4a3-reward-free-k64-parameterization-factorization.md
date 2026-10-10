# LatentAtlas U4-A3 Reward-Free K64 Parameterization Factorization

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

U4-A3 是 U4-A2 之后唯一一次 `development-only / adaptive follow-up / non-confirmatory / reward-free / observed-train K64` 的 CPU-only 参数化分解实验。Run identity 为 `U4A3_DEV_REWARD_FREE_K64_PARAMETERIZATION_FACTORIZATION`。

它只回答一个有限问题：在冻结的 observed-train K64 对应关系上，U4-A2 的 K64 未闭合更接近当前 Bridge/solver 的限制，还是更宽的 pooled affine、invariant nonlinear 或完全展开 affine 参数化也无法闭合。实验同时把 correct pairing 与五个冻结 permutation null 放进相同指标和 gate，避免把“能记住 64 个训练点”误写成“学到了 correspondence”。

本实验没有打开 Reward、H1105、fresh/formal authority、held-out structure、validation/test latent/cache row、validation/test metric/model output/pair identity/token、VAE identity lookup、CUDA 或 network。它不评价 Reward transfer、canonical target validity、unseen-VAE generalization、structural generalization 或真实部署能力。

相关页面：`latentatlas`（原wiki关联）、[latentatlas-u4a2-reward-free-train-closure-localization](latentatlas-u4a2-reward-free-train-closure-localization.md)、`representation-alignment`（原wiki关联）、`latent-space`（原wiki关联）。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u4a3-reward-free-k64-parameterization-factorization.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Population：沿用并重新验证 U4-A2 冻结的 observed-train K64 population；不创建 fresh 或 formal authority。
- Input：标准化 DCAE token representation，shape `[64,32,16]`。
- Correct target：raw SD/FLUX barycenter `H`，shape `[64,64]`，whole-row assignment 为 `T(g_i)=H(g_i)`。
- Null targets：五个冻结 cyclic offsets `1/7/13/29/37`，对应 `perm_01` 至 `perm_05`；candidate bank 保持 canonical H original order。
- Seeds：`20260823`、`20260824`、`20260825`。
- Authority chain：每个 O seed 的初始状态被 disk verifier 独立绑定到 U4-A2 predecessor checkpoint 的 `final_state_sha256`；predecessor 85-path Git tree 也被独立重放验证。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 Frozen classification

正式分类：**`INVARIANT_NONLINEAR_TRAIN_FIT_NOT_CORRESPONDENCE_DISCRIMINATIVE`**。

Safe claim：expanded invariant nonlinear finite K64 train fit 至少同时闭合了一个注册 null，因此不是 correspondence-discriminative。正式事实为 `f_all_interp=true`、`n_clean=false`、`n_nondisc=true`、`non_f_any_joint_close=true`、`p1_clean=false`、`p1_nondisc=false`。

### 7.2 O/P0/P1/F/N correct/null 表

| Condition | Correct pairing | 五个 null pairings | Summary rows | Joint-closing cells | 结论 |
|---|---:|---:|---:|---:|---|
| `O` current Bridge + L-BFGS rescue | `0/3` | 未注册 | 3 | 0 | 当前 Bridge 即使 rescue 也未闭合 K64 correct |
| `P0` pooled affine analytical | `0/1` | `0/5` | 6 | 0 | pooled affine 解析解对 correct/null 均不闭合 |
| `P1` pooled affine trainable | `0/3` | `0/15` | 18 | 0 | correct 与五组 null 的三 seeds 均不闭合 |
| `F` flat affine analytical | `1/1` | `5/5` | 6 | 6 | correct/null 全部精确插值，non-discriminative |
| `N` invariant nonlinear | `3/3` | `15/15` | 18 | 18 | correct/null 全部闭合，non-discriminative |
| **Total** | — | — | **51** | **24** | 只有 F 与 N 产生 closure |

表中 null 分母按实际 cell 计数：解析条件每个 pairing 1 cell，训练条件每个 pairing 3 seeds。F 和 N 都能拟合 correct，但也同样拟合所有注册 null，因此二者只证明有限 K64 train interpolation/capacity，不证明 correspondence specificity。

### 7.3 全部 24 个 joint-closing cells

- F（6）：`F/correct`、`F/perm_01`、`F/perm_02`、`F/perm_03`、`F/perm_04`、`F/perm_05`。
- N correct（3）：`N/correct/seed_20260823`、`N/correct/seed_20260824`、`N/correct/seed_20260825`。
- N null（15）：`N/perm_01..perm_05 × seed_20260823/20260824/20260825`，五个 null 的三个 seeds 全部闭合。

O、P0、P1 没有任何 joint-closing cell。F 的 exact affine witnesses 为 `6/6`；N 的 correct 与所有 null 都达到 joint closure，故 `N/F non-discriminative` 是本实验最关键的限制，而不是附带现象。

### 7.4 Seal and verification

- Canonical result tree：共 `142` 个 paths；`inventory.json` self-excluded registry 含 `141` entries。
- `summary.csv`：严格 `51` rows，SHA-256=`4eeaf200339b6fdf1bfadd4e3f6b8ff3457b199fba3a6d7d8fda45feb431bbed`。
- Trainable terminal checkpoints：`39`（O 3 + P1 18 + N 18）。
- Analytical certificates：`12`（P0 6 + F 6）。
- Inventory SHA-256：`dc917e69f94cac8bf31fcb13780990acbc9e747ccb145bcaebc0a6429bf751e4`。
- Decision SHA-256：`bdfbefb150b9f9dd3fadf95b8497796c8709c3197f3dbd175b3dba6d13ce9301`。
- Disk-only verifier：**PASS / `VERIFIED_COMPLETE`**；它仅使用 Python standard library，不导入 Torch 或 U4-A/U4-A2 authority/trainer。
- Audit：15 个 forbidden access counters 全部为 `0`，`formal_or_fresh_authority_materialization_count=0`，`holdout_materialization_count=0`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

1. U4-A2 的 B/K64 未闭合不能再被解释为“这 64 个 observed-train 对应点根本不存在可拟合映射”。F 与 N 已分别用展开 affine 和 invariant nonlinear 参数化闭合 correct pairing。
2. 但 F 对全部五个 null 同样精确插值，N 对 correct 与五个 null 的 18/18 cells 全部闭合。二者没有 correspondence discrimination，只展示有限样本记忆/插值能力。
3. O/P0/P1 对 correct 和已注册 null 都没有 closure，说明当前 Bridge、pooled affine 解析解与 pooled affine trainable path 的 K64 失败仍是一个真实的参数化/优化现象；它并不自动升级为 target 无效或 correspondence 不存在。
4. `N clean=false` 与 `N nondisc=true` 必须同时保留：N 的 correct fit 成功，但 null-control 失败，故 headline 不能写成 nonlinear success 或 correspondence recovery。
5. 本结果只缩小 U4-A2 的解释空间：K64 可被更高容量参数化插值，但当前证据没有找到既闭合 correct、又拒绝 permutation null 的模型族。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

1. 当前 hard stop；不自动启动新实验，不打开 Reward/H1105/held-out，不扩 K、模型或 null，也不创建 U4-A4/U4-B。
2. 建议先做 scientific review，下一份新设计若获批准，应把“correct 闭合且 permutation null 不闭合”作为首要判别目标，而不是继续增加纯 train interpolation capacity。
3. 一个可讨论但未执行的方向，是在新的冻结协议中加入 source-structure-preserving、complexity-matched 的 discrimination/cross-fit 约束，检验 inductive bias 是否能保留 correct correspondence 而拒绝 permutation null；这需要新的 authority 与审批，不能从本结果自动启动。
4. 结果阶段为 CPU-only；不需要 GPU 或租用服务器，若实例仍在运行可以关闭。

## Sources

- [来源快照](../source-snapshots/latentatlas-u4a3-reward-free-k64-parameterization-factorization.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u4a3-reward-free-k64-parameterization-factorization.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
