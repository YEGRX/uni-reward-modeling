# LatentAtlas U4-B1D1：OIP Source Reader Restoration

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

沿 [latentatlas-u4b1d0-source-head-reference-adequacy](latentatlas-u4b1d0-source-head-reference-adequacy.md) 的结论，使用此前未被 LatentAtlas 消费的 Open Image Preferences（OIP）大样本，先恢复 source/head/reference adequacy，再决定是否有资格进入 DCAE correct-vs-null：

```text
更大 OIP source-development authority
        ↓
只比较 R0 / R1 / R2 source readers
        ↓ eligible candidate only
冻结唯一 candidate
        ↓
同源、预承诺 LOCKBOX 的 SOURCE_H gate
        ↓ Pass only
另行执行 U4-B1D2 DCAE correct-vs-null
```

U4-B1D1 是 `adaptive development + same-source partition lockbox`，不是独立数据集确认。实际结果在 DEV selection 阶段停止，没有打开 LOCKBOX，也没有评价 DCAE。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u4b1d1-oip-source-reader-restoration.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Binarized source：`data-is-better-together/open-image-preferences-v1-binarized@421d9b4e11f22d576a15c14e38aaa4687748023f`
- Raw-vote source：`data-is-better-together/open-image-preferences-v1-results@532865f46c87d7ca33f6805b4c9c42f0a5a6b7c0`
- Retained pairs：`7,459`
- Unique images：`14,918`
- Connected prompt/base-ID/image groups：`4,671`
- Split：TRAIN=`4,059`、DEV=`900`、LOCKBOX=`2,500`
- Cross-split prompt/base-ID/image overlap：`0 / 0 / 0`
- 历史 authority exact encoded-byte image overlap：G0.1=`0`、P4096=`0`、H1105=`0`、FRA-SVG0=`0`

OIP 每一对都比较 FLUX.1-dev 与 SD3.5-large。其人类偏好语义混合了 prompt adherence 与 aesthetics；本实验 reader 不读取 prompt，因此结果不能解释为纯 coherence 或完整 prompt adherence。历史 overlap audit 只覆盖 exact encoded bytes，不能排除感知近重复、语义近重复或跨 authority prompt overlap。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 Generator-prior control

TRAIN-only generator prior 在 DEV 上为：

- Accuracy：`0.526667`
- BT-NLL：`0.691763`

这说明 OIP 中存在不可忽略的 generator identity shortcut；source reader 必须显著胜过该 baseline，不能只靠“总是偏好某个生成器”取得表面准确率。

### 7.2 Development candidates

| Candidate | H Accuracy [lower, upper] | H BT-NLL [lower, upper] | ΔAcc lower | ΔNLL lower | FLUX-win Acc | SD-win Acc | Eligible |
|---|---:|---:|---:|---:|---:|---:|---|
| `R0_FROZEN_U0_SHARED_H` | `0.507778 [0.479376,0.535754]` | `0.702748 [0.694378,0.711334]` | `-0.061471` | `-0.020170` | `0.544601` | `0.474684` | No |
| `R1_LINEAR_SHARED_H` | `0.503333 [0.475930,0.530454]` | `0.705298 [0.699117,0.711568]` | `-0.060674` | `-0.020023` | `0.474178` | `0.529536` | No |
| `R2_U0_MLP_SHARED_H` | `0.492222 [0.465423,0.519553]` | `0.714340 [0.705210,0.723615]` | `-0.071349` | `-0.031987` | `0.474178` | `0.508439` | No |

三个候选都没有通过 eligibility gate：

- R0 的 H Accuracy lower 未过 0.5、NLL point/upper 未低于 `log(2)`，且 SD-preferred stratum `<0.5`。
- R1 的 H Accuracy 与 NLL 均未过绝对门槛，FLUX-preferred stratum `<0.5`。
- R2 的 H Accuracy point `<0.5`、NLL 更差，FLUX-preferred stratum `<0.5`。
- 三者相对 generator prior 的 `ΔAccuracy lower` 与 `ΔNLL lower` 都为负。

### 7.3 Frozen decision

```text
classification                    = NO_SOURCE_READER_RESTORED
candidate                         = null
lockbox_orientation_access_count  = 0
dcae_materialization_count        = 0
dcae_mapping_materialization_count= 0
dcae_evaluation_count             = 0
```

因此，预备好的 U4-B1D2 没有获得执行授权；没有 DCAE scientific result。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 8.1 当前结果能说明什么

- 旧冻结 U0 head、固定线性 reader 与当前 U0-MLP reader，在 OIP 的 4,059-pair TRAIN → 900-pair DEV 条件下都没有恢复 H-compatible source adequacy。
- 相比 B1D0 的 284-pair SVG localization，本实验使用更大且此前未消费的 OIP source-development cohort，仍没有找到能同时通过 absolute、generator-prior 与双方向 gates 的候选。
- 失败不仅是“没超过随机”：三种候选都不能稳健超过 OIP 中很强的 generator-prior shortcut。
- 按冻结顺序在最早失败层停止，避免把 source-reader failure 错写成 DCAE mapping failure。

### 8.2 当前结果不能说明什么

- 不证明 SD/FLUX latent 不含任何人类偏好或 Reward 信息。
- 不否定 prompt-aware reader、显式分解 aesthetics/prompt adherence、不同 reference、不同 head capacity 或新的训练语义。
- 不构成独立数据集 fresh confirmation；LOCKBOX 甚至没有打开。
- 不评价 DCAE correct-vs-null、Reward transfer、canonical/universal `U`、unseen-VAE onboarding 或跨分布泛化。
- OIP 的 mixed semantics 加上 reader 无 prompt 输入，使负结果可能来自 task/observation mismatch，而不只是 representation inadequacy。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

1. U4-B1D2 保持封存，不执行 DCAE encoding 或 correct-vs-null。
2. 下一轮优先处理 semantics/observability：把 prompt-aware 与纯视觉 aesthetics-only 问题分开，先建立 source-only ceiling。
3. 在 development authority 上冻结唯一新的 source candidate 后，再使用未消费 authority 或预承诺 lockbox 做 `SOURCE_H` gate。
4. 只有 `SOURCE_H` 通过 absolute、generator-prior 与方向 gates，才解锁 U4-B1D2。

本轮 source encoding 已由本机 Apple MPS 完成；当前后续分析与报告为 CPU-only，不需要租用 GPU 服务器。

## Sources

- [来源快照](../source-snapshots/latentatlas-u4b1d1-oip-source-reader-restoration.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u4b1d1-oip-source-reader-restoration.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
