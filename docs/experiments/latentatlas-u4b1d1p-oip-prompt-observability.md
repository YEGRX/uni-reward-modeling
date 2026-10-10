# LatentAtlas U4-B1D1P：OIP Prompt Observability Localization

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

沿 [latentatlas-u4b1d1-oip-source-reader-restoration](latentatlas-u4b1d1-oip-source-reader-restoration.md) 的 source-reader 失败继续做最小定位：在同一 OIP TRAIN/DEV authority 上比较 `H_ONLY`、`PROMPT_ONLY` 与 `JOINT=[H;prompt]`，判断先前结果是否主要来自 prompt 不可观察（prompt observability mismatch）。本实验是 adaptive development-only source localization；只有冻结 gate 通过才可能产生 source candidate，DCAE 不在本实验中评价。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u4b1d1p-oip-prompt-observability.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- OIP TRAIN pairs：`4,059`
- OIP DEV pairs：`900`，覆盖 `561` 个 groups
- 可绑定 prompt text：`7,459`
- LOCKBOX orientation access：`0`
- LOCKBOX label-blind prompt-text access：`2,500`

这里必须区分两种访问：LOCKBOX 的偏好方向标签完全未打开，但为检查 prompt sidecar 的完整性，读取了 `2,500` 条不含方向标签的 prompt text。因而不能写成“LOCKBOX 完全零访问”，也不能把该 pilot 当作 lockbox confirmation。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

| Condition | Accuracy [lower, upper] | BT-NLL [lower, upper] | FLUX-preferred Acc | SD-preferred Acc |
|---|---:|---:|---:|---:|
| `GENERATOR_PRIOR` | `0.526667 [0.498346,0.554705]` | `0.691763 [0.689261,0.694289]` | `0.000000` | `1.000000` |
| `H_ONLY` | `0.495556 [0.467849,0.523077]` | `0.706556 [0.698626,0.714550]` | `0.413146` | `0.569620` |
| `PROMPT_ONLY` | `0.553333 [0.525275,0.581006]` | `0.681495 [0.673422,0.689734]` | `0.406103` | `0.685654` |
| `JOINT` | `0.540000 [0.512623,0.567391]` | `0.698075 [0.686767,0.709557]` | `0.488263` | `0.586498` |

冻结 gates：

```text
h_only              = false
prompt_observability= false
joint_over_h        = false
joint_over_prompt   = false
```

`PROMPT_ONLY` 相对 generator prior 的 NLL improvement point/lower=`0.010267/0.002567`，Accuracy improvement point=`0.026667`，但其 lower=`-0.006623`，且 FLUX-preferred stratum Accuracy=`0.406103`。因此它只能记为 partial prompt-only descriptive signal，不能升级为注册的 prompt-observability PASS。

`JOINT` 相对 `H_ONLY` 的 Accuracy 与 NLL improvement lower 分别为 `0.018438` 与 `0.000743`，说明 prompt feature 给当前 H reader 增加了一些 development signal；但 `JOINT` 不胜 `PROMPT_ONLY`，其相对 prompt-only Accuracy improvement lower=`-0.039956`、NLL improvement lower=`-0.024024`，且未通过冻结 gate。

最终状态：

```text
classification                     = NO_PROMPT_OR_H_OBSERVABILITY_SIGNAL
source_reader_candidate_id         = null
lockbox_orientation_access_count   = 0
lockbox_prompt_text_access_count   = 2500
dcae_materialization_count         = 0
dcae_mapping_materialization_count = 0
dcae_evaluation_count              = 0
```

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 能说明什么

- 在当前 OIP development protocol 下，`PROMPT_ONLY` 确实出现了比 generator prior 更低 NLL 的局部描述性信号；prompt 不是完全无信息。
- `H_ONLY` 没有建立 source adequacy；加入 prompt 后的 `JOINT` 虽优于 H-only，却没有优于 prompt-only，因此当前 H 没有显示可靠增量价值。
- 按冻结 gate，三种可训练条件都不足以形成可冻结的 source reader candidate，最早 blocker 仍在 source task/observability/reader 层。

### 不能说明什么

- 不证明 prompt 完全无偏好信息；严格负分类与 prompt-only 的局部描述性信号可以同时成立。
- 不证明 SD/FLUX latent 没有 Reward 信息，也不否定更合适的 prompt encoder、image-prompt interaction、aesthetics-only authority 或不同 reader。
- 不评价 DCAE mapping，因此不是 DCAE correct-vs-null 失败。
- 不构成 Reward transfer、canonical/universal `U`、fresh lockbox confirmation、unseen-VAE onboarding 或跨分布泛化证据。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

1. DCAE/B1D2 继续封存；不得把本轮结果写成 DCAE failure。
2. 下一轮 source-only development 应优先区分：prompt-only generator preference、image-only aesthetics，以及显式 image-prompt interaction。
3. 只冻结一个在 development authority 上通过 absolute、generator-prior 与双方向 controls 的新候选。
4. 再用新的未消费 source authority 做 `SOURCE_H` gate；只有通过后才评价 DCAE correct-vs-null。

当前实验与归档均已结束；不需要租用 GPU。下一轮若仅复用已有 H/cache 并训练轻量 source readers，可 CPU-only；只有重新编码大型视觉/文本模型时才需要另行启动 GPU。

## Sources

- [来源快照](../source-snapshots/latentatlas-u4b1d1p-oip-prompt-observability.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u4b1d1p-oip-prompt-observability.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
