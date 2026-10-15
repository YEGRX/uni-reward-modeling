# LatentAtlas U4-A6-PROB Distributional Consensus-U

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

比较 Point、diagonal Gaussian 与 conditional Flow 三种 reward-free consensus representation，回答：distributional U 能否在保持 correspondence retrieval 的同时改善分布评分，以及更复杂的 Flow 是否相对简单 Gaussian 提供注册的新增价值。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u4a6prob-distributional-consensus-u.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- 冻结 P4096 fold 0：3,276 fit identities、820 evaluation identities。
- 输入为三 VAE paired representations；correct 与固定 null/control 共享注册 stream bindings。
- Flow shuffled control 只打乱 condition，保留 base noise 与 target，以检验真正的 condition dependence。
- 不访问 H1105、Reward、validation/test、fresh authority、网络或 CUDA。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

冻结分类：**`DISTRIBUTIONAL_U_FEASIBLE_BUT_FLOW_NOT_NECESSARY`**。

| System | cNRMSE | R@1 | MRR | Energy | Calibration error |
|---|---:|---:|---:|---:|---:|
| Point | 0.419571 | 0.998374 | 0.998950 | 1.559275 | 0.818595 |
| Gaussian | 0.485829 | 0.994715 | 0.996622 | 0.154735 | 0.174047 |
| Flow | 0.437064 | 0.989837 | 0.993776 | 1.689232 | 0.055758 |
| Flow shuffled | 1.304822 | 0.000000 | 0.007175 | 5.532565 | 0.409118 |

关键 lower-bound gates：

- Gaussian vs null specificity=`(0.354501, 0.026423, 0.017669)`，通过。
- Gaussian vs Point retrieval lower=`(-0.006504, -0.004225)`，通过 noninferiority；relative energy gain lower=`0.899367`，通过 added-value。
- Flow vs shuffled：energy degradation lower=`0.691115`、MRR degradation lower=`0.984158`，证明 Flow 确实依赖 condition。
- Flow vs Point relative energy gain lower=`-0.092358`，未提供注册新增价值。
- Flow vs Gaussian relative energy gain lower=`-10.026466`；虽然 calibration error 更低，但仍未通过 primary added-value rule。

Gaussian 与 Flow 均非塌缩、全部 64 dimensions active；Flow 也通过 diversity 与 condition-dependence gate。

Decision SHA-256：`a3cea01e978d10f4a2b37a188fa8b8acce54a598f525ad49bb1d7f1a64080850`。Inventory SHA-256：`50aa10424e93e53834e8825156a9e3f9128a44278a09919b2d158fe4c1f0f668`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

Gaussian 是本批次最有希望的新候选：它几乎保持 Point 的 retrieval，同时将 energy score 从 `1.559275` 降到 `0.154735`。这说明在当前 development fold 中，对 uncertainty 做简单参数化比只用 point representation 有明确注册价值。

Flow 的 shuffled control 表明它不是忽略条件的伪 Flow；它确实学到了 conditional distribution。但复杂度没有转化为更好的 primary energy score，所以当前没有理由优先 Flow。

这不证明 Gaussian 普遍最优，也不证明 Flow 在更大数据、不同 objective 或 fresh distribution 上永远无用。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本批次 hard stop，不自动扩展 Flow 或新增 sweep。若以后获得独立批准与 fresh functional authority，simple Gaussian 是更合理的预冻结候选；这只是 suggested-only direction，不构成当前实验的一部分。

全程 CPU-only；GPU 服务器不需要开启。

## Sources

- [来源快照](../source-snapshots/latentatlas-u4a6prob-distributional-consensus-u.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u4a6prob-distributional-consensus-u.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
