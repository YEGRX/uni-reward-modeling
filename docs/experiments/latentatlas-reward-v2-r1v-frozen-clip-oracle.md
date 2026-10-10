# LatentAtlas Reward V2 R1V：Proper Frozen CLIP Oracle Qualification

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

前序 [latentatlas-reward-v2-r0r1-oip-authority-oracle](latentatlas-reward-v2-r0r1-oip-authority-oracle.md) 只能使用 DINO fallback 与 historical hashed prompt，得到 `INCONCLUSIVE_WEAK_ORACLE / ACQUIRE_FROZEN_VLM_ORACLE`。R1V 保持同一 OIP TRAIN→DEV authority、候选家族、controls 与 gates，改用 exact frozen CLIP image/text tower，回答：

1. proper VLM 能否建立绝对的 RGB 或 RGB×prompt observability；
2. correct image/prompt 是否稳定胜过五个 registered nulls；
3. M1 是否同时胜过 generator prior、historical hashed prompt-only 与 VLM text-only shortcuts；
4. 信号是否在 FLUX-preferred 与 SD-preferred 两个方向都成立；
5. 是否足以创建 frozen Reward interface 并解锁 R2P-1。

它只评估 Reward measurement/control oracle candidate，不评估 LatentAtlas 的 native-latent 方法。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-reward-v2-r1v-frozen-clip-oracle.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- OIP TRAIN/DEV/LOCKBOX pairs：`4,059 / 900 / 2,500`。
- DEV：900 pairs，561 connected groups；统计使用 common group bootstrap。
- TRAIN/DEV RGB images：`8,118 / 1,800`；CLIP prompt rows：`4,059 / 900`。
- LOCKBOX image/pair cache：`0 / 0`。
- LOCKBOX orientation/RGB/embedding/prompt access：全部为 `0`。
- Public registry rows read：`7,459`。
- H、U、native VAE latents、Bridge、DCAE、Projector 均未访问；R2/R2P 未执行。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 Registered candidates

| Candidate | DEV Accuracy | 90% CI | BT-NLL | 90% CI | FLUX-pref Acc | SD-pref Acc |
|---|---:|---:|---:|---:|---:|---:|
| C0 Generator Prior | 0.526667 | [0.498346, 0.554705] | 0.691763 | [0.689261, 0.694289] | 0.000000 | 1.000000 |
| C1-HASH Historical Prompt-Only | 0.553333 | [0.525275, 0.581006] | 0.681495 | [0.673422, 0.689734] | 0.406103 | 0.685654 |
| C1-VLM Text-Only | 0.566667 | [0.538547, 0.594350] | 0.676074 | [0.665994, 0.686296] | 0.464789 | 0.658228 |
| C2-VLM RGB-Only | 0.567778 | [0.539823, 0.595676] | 0.677535 | [0.671342, 0.683788] | 0.417840 | 0.702532 |
| M1-VLM RGB×Prompt Diagonal | 0.567778 | [0.539823, 0.595676] | 0.677520 | [0.671325, 0.683773] | 0.417840 | 0.702532 |

Zero-shot CLIP cosine 只作 diagnostic，不用于 gate 或 selection：Accuracy/BT-NLL=`0.548889/0.690304`。

### 7.2 Shortcut comparisons

M1 相对 C0 同时通过 Accuracy 与 BT-NLL improvement：

- `ΔAccuracy=0.041111`，one-sided 95% lower=`0.007901`；
- `ΔNLL=0.014243`，one-sided 95% lower=`0.008249`。

但 M1 没有超过两个 prompt shortcuts：

- vs C1-HASH：`ΔAccuracy=0.014444`，lower=`-0.020906`；`ΔNLL=0.003975`，lower=`-0.004560`；
- vs C1-VLM：`ΔAccuracy=0.001111`，lower=`-0.032880`；`ΔNLL=-0.001446`，lower=`-0.011654`。

因此 `m1_shortcuts=false`。C2 也有同样的 shortcut failure。

### 7.3 Image/prompt specificity 与 incremental control

- C2 image-specificity 的 five-null worst improvement：point=`0.021041`，one-sided 95% lower=`0.008166`，PASS。
- M1 image-specificity：point=`0.021057`，lower=`0.008185`，PASS。
- M1 prompt-specificity：point=`0.000010768`，lower=`0.000002845`，PASS。
- M1 相对 C2 的 prompt incremental：`ΔAccuracy=0.000000`；`ΔNLL=0.000014991`，lower=`0.000009954`。由于 Accuracy 没有增量，registered joint gate 为 `prompt_incremental_observable=false`。

### 7.4 Frozen gate table

| Gate | C2 | M1 |
|---|---:|---:|
| Absolute observability | PASS | PASS |
| Beats all registered shortcuts | FAIL | FAIL |
| Image specificity | PASS | PASS |
| Prompt specificity | N/A | PASS |
| Both preference directions > 0.50 | FAIL | FAIL |
| Prompt incremental over C2 | N/A | FAIL |

M1/C2 的 FLUX-preferred Accuracy=`0.417840`，one-sided 95% lower=`0.374713`；SD-preferred Accuracy=`0.702532`，lower=`0.665323`。两方向明显不对称，因此不能把 overall positive point estimate 写成方向稳健的 Reward authority。

### 7.5 Corrected frozen decision

```text
validity_status       = VALID
oracle_type           = NO_QUALIFIED_ORACLE
authority_class       = OIP_RGBTEXT_SIGNAL_WEAK_NOT_QUALIFIED
recommended_next_step = STOP_NO_R2_R2P_U_UNLOCK
```

- `qualified_reward_oracle_interface.json`：未创建。
- `r2p_unlock_receipt.json`：未创建。
- R2P training：未执行。
- Completed verifier：`PASS / fit_calls=0`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 能说明什么

1. Proper frozen CLIP 相比 DINO fallback 确实恢复了更清晰的 weak signal：C2/M1 通过 absolute gate，并且 correct image 与 correct prompt 分别胜过 registered nulls。
2. 这个信号包含 pairing specificity；所以不能再写成“RGB/prompt 完全没有可检测信息”。
3. 但 M1 没有稳定超过 C1-HASH 或 C1-VLM，prompt 加入 C2 后 Accuracy 增量为 0；当前 signal 仍不能与 prompt/generator shortcuts 充分分离。
4. FLUX-preferred 与 SD-preferred 方向严重不对称，说明 overall Accuracy 不能代表双方向稳定性。
5. 最终只能称 `OIP_RGBTEXT_SIGNAL_WEAK_NOT_QUALIFIED`；proper VLM 消除了“fallback 太弱”这一部分不确定性，但没有把 OIP 资格审查推进到可解锁状态。

### 不能说明什么

- 不能说明 OIP 没有 image-specific 或 prompt-specific signal；两个 specificity controls 实际已通过。
- 不能说明 OIP 已成为 qualified Reward authority，也不能把 `NO_QUALIFIED_ORACLE` 误读为“没有使用 VLM”；它表示冻结的 VLM candidate 未通过资格门。
- 不能证明 prompt-semantic interaction 已成立；prompt-null specificity 通过，但相对 C2 的 registered incremental gate 失败。
- 不能证明 native SD/FLUX/DCAE latents、Projector、H、U、Bridge、Reward transfer、fresh confirmation 或 unseen-VAE generalization 成立或失败。
- Frozen CLIP 来自大规模互联网预训练；无法证明其 pretraining 与 OIP 的 prompt/semantic content 完全无重叠。
- 这是 adaptive development-only 结果，DEV 已被使用，不能作为 fresh confirmatory evidence。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

当前唯一正式动作是：

```text
STOP_NO_R2_R2P_U_UNLOCK
```

不执行 R2、R2P-1、U/native-latent、Projector、Bridge 或 DCAE 实验，也不在同一 DEV authority 上继续 backbone/head/architecture sweep。若 Reward V2 主线未来继续，应另行冻结新的 authority 问题、数据边界与 controls，而不能把本次 weak signal 升级为现成 Reward interface。

本机 MPS 编码阶段已经结束；当前归档与下一步方案设计均为 CPU-only / no server。租用 GPU 服务器不需要运行。

## Related Pages

- `latentatlas`（原wiki关联）
- [latentatlas-reward-v2-r0r1-oip-authority-oracle](latentatlas-reward-v2-r0r1-oip-authority-oracle.md)
- [latentatlas-reward-v2-r2p0-projector-only-preflight](latentatlas-reward-v2-r2p0-projector-only-preflight.md)
- `multimodal-learning`（原wiki关联）
- `clip`（原wiki关联）
- `vision-transformer`（原wiki关联）
- `embedding`（原wiki关联）
- `latent-space`（原wiki关联）
- `variational-autoencoder`（原wiki关联）

## Sources

- [来源快照](../source-snapshots/latentatlas-reward-v2-r1v-frozen-clip-oracle.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-reward-v2-r1v-frozen-clip-oracle.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
