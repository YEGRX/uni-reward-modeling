# LatentAtlas U4-BD1 冻结 Reward Head 函数保持诊断

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

U4-BD1 检查的是：已有 F（flat affine）与 N（invariant nonlinear）映射能否在历史 V708 cohort 上，保持一个**精确冻结的 U0 Reward Head** 的输出数值与排序。

冻结 source reference 为：

\[
s_{ref}=R_{U0}\left(\frac{B_{sd}(\operatorname{normalize}_{sd}(z_{sd}))+B_{flux}(\operatorname{normalize}_{flux}(z_{flux}))}{2}\right)
\]

实验比较 correct mapping 与五个 permutation null、matched no-fit initial-state control、constant-reference control。它没有训练或微调 Reward Head，也没有打开任何新的 Reward labels、preferences、margins、orientations 或 prompt text。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u4bd1-frozen-head-function-preservation.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Cohort：历史已暴露的 V708 validation cohort，共 `708` 个 identity。
- Cohort 状态：`fresh=false`，`historically_exposed=true`。
- Ordered identity commitment：`525b4521049856de12249b80d5d7e62428f1592adbe157721a1d0401a4a05bf6`。
- 没有重开 H1105 或 P4096，也没有访问 test data 或 fresh authority。
- 冻结 Reward Head architecture：`Linear(64,64) -> GELU -> Dropout(0.1) -> Linear(64,1)`，共 `4,225` parameters。
- Reward Head file SHA-256：`f8096c49afcec03d7f80228d82c925710931f805d53d5c057882ffb6c1e032cb`。
- Reward Head state SHA-256：`b45076296c57cd720c784c548cab99f4d1fad70f1e44150fdc05377da417c3ea`。
- Head 以 CPU `float32`、`eval`、frozen、dropout disabled 方式执行；指标聚合使用 `float64`。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 Frozen classification

最终分类：

`INVARIANT_NONLINEAR_REGISTERED_FROZEN_HEAD_FUNCTION_SPECIFICITY_ONLY`

这里的 gap 为 control error 减 correct error；因此正值表示 correct mapping 更接近冻结 reference。注册判定同时要求 point gap 与 5% lower bound 严格为正。

| Family | Control | Metric | Point gap | 5% lower bound | Gate |
|---|---|---:|---:|---:|---|
| F | five nulls | value | `0.41899547090574396` | `0.3660657145383268` | Pass |
| F | five nulls | order | `0.10034689861135915` | `0.07734053897234483` | Pass |
| F | no-fit | value | `0.4691349667414384` | `0.41716154264805416` | Pass |
| F | no-fit | order | `-0.020128259498308487` | `-0.03478756075486916` | Fail |
| F | constant | value | `-0.0614016701443858` | `-0.1108815811505659` | Fail |
| F | constant | order | `-0.020128259498308487` | `-0.03478756075486916` | Fail |
| N | five nulls | value | `0.8479262515099083` | `0.7868014274287389` | Pass |
| N | five nulls | order | `0.1782910147902455` | `0.15954709674630776` | Pass |
| N | no-fit | value | `0.6624385023127112` | `0.5979867512647268` | Pass |
| N | no-fit | order | `0.16029716936567615` | `0.14375979370833492` | Pass |
| N | constant | value | `0.2521483307214618` | `0.19078648241910612` | Pass |
| N | constant | order | `0.060655069159577885` | `0.04678434523264616` | Pass |

### 7.2 Family-level conclusion

- **N registered pass**：N 对 five nulls、matched no-fit initial states 和 constant reference 的 value/order point gaps 与 lower bounds 全部为正。
- **F registered fail**：F 虽对 five nulls 方向正确，且 no-fit value 通过，但 constant-control 的 value/order 均失败，no-fit order 也失败。因此 F 不能获得 registered frozen-head function-specificity 结论。
- 两族均有 `point_directional=true`，但只有 N 的 `registered_pass=true`。

### 7.3 Seal and verifier evidence

- Attempt receipt SHA-256：`a32bbfd81c31106cd280aa53adfb127fee8fde9728151147fed1cade1ee61a10`。
- Result seal SHA-256：`4ce23943e1befeac2700af4ab4f39fe4f501a2b1f4261775b0a71aaf99df772b`。
- Inventory file SHA-256：`55f027ae9c900f0197cb023747daed47eb8cbf002b1201bf970f6c5414166e3e`。
- `result_seal.json` 封存 18 个 artifacts；其后生成 self-excluding `inventory.json`，共记录 19 个 entries；正式根共 20 个 top-level paths。
- Audit status=`COMPLETED`，`attempt_consumed=true`，四项 validity gates 全部为 `true`。
- Disk-only verifier version=`U4BD1_COMPLETED_TREE_VERIFIER_V1`；它重算 aggregate arithmetic、gate、classification、seal 与 inventory，且不重开 per-identity forward values。
- Head/source/mapping parameter digests 前后完全一致，`parameter_digests_unchanged=true`。
- Reward labels/orientations/preferences/margins、head training/calibration/fine-tuning、mapping fit、H1105/P4096、test data、fresh authority、network、GPU/CUDA/MPS、original images、per-identity persistence 与 post-V708 adaptation 等 forbidden counters 全部为 `0`。
- 持久化产物只有 aggregate diagnostics；没有 per-ID scores、bootstrap contributions 或新 checkpoint。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 8.1 这项结果证明什么

在**同一个精确冻结的 U0 Reward Head**与**历史 V708 identities**上，N mapping family 对注册的 null、no-fit 和 constant controls 都表现出稳健的 value/order function preservation。相对 U4-A4 的 correspondence-specificity，U4-BD1 进一步表明 N 的正确映射不仅对应 identity pairing，还能较好保存这一特定冻结 head 的函数行为。

### 8.2 这项结果不证明什么

- 不证明该 Reward Head 的输出是正确的人类 Reward，也不证明 Reward accuracy 或 reward sufficiency。
- 不使用任何新 Reward labels，因此不是 fresh Reward confirmation。
- V708 是历史已暴露 cohort，因此不是 fresh holdout、cross-distribution 或 unseen-identity generalization。
- 只绑定一个 exact frozen head，因此不是跨 Reward Head transfer，更不是 canonical/universal U。
- 不检验 unseen-VAE transfer、低成本 onboarding、唯一坐标系或 downstream policy usefulness。
- N pass 不能推广成 F pass；F 明确未通过 constant control 与 no-fit order gate。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

1. 将本结果作为 exact-head、historic-cohort 的 bounded diagnostic 保留，不在同一 V708 authority 上追加 architecture/seed/control sweep。
2. 若要检验 Reward transfer，必须先冻结新的独立 functional authority 与新 Reward Head/任务契约，不能复用本结果替代 fresh confirmation。
3. 若以后进入 unseen-VAE onboarding，应另行预注册新 VAE、身份隔离、模型绑定、controls 与 terminal seal；不得把 N 在 V708 的通过直接推广过去。
4. 当前归档与后续讨论不需要 GPU 或远程服务器。

## Sources

- [来源快照](../source-snapshots/latentatlas-u4bd1-frozen-head-function-preservation.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u4bd1-frozen-head-function-preservation.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
