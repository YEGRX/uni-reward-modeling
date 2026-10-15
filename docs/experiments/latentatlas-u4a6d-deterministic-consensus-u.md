# LatentAtlas U4-A6-D Deterministic Consensus-U

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

检验能否仅用同一 identity 的三 VAE paired latent，学习一个不接收 VAE identity 的 deterministic consensus U，并同时满足：correct-over-null specificity、非塌缩、接近 chance-free retrieval、弱 VAE 可识别性，以及相对冻结 arithmetic reference baseline 的 noninferiority/material gain。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u4a6d-deterministic-consensus-u.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- 冻结 P4096 的 fold 0：3,276 fit identities、820 evaluation identities。
- 输入为 SD、FLUX、DCAE 三个注册 view 的 paired latent representation。
- Correct 与固定 null 使用相同 init、batch schedule 与训练预算。
- 不访问 H1105、Reward、validation/test、fresh authority、网络或 CUDA。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### Original attempt: operationally invalid

原实验完成训练后，在 terminal certificate serialization 时仍把 transient `checkpoint_bytes` 送入 recursive canonical JSON conversion，触发 `ValueError: U4-A6-D document contains a noncanonical value`。它只有 durable receipt 与 `operational_failure.json`，没有保存 metrics 或 scientific decision。

D2 唯一修复是在 canonical conversion 前移除 transient bytes；architecture、data、random streams、loss、optimization、metrics、thresholds 与 decision precedence 均不变。

### D2 verified result

冻结分类：**`DETERMINISTIC_CONSENSUS_U_NOT_CORRESPONDENCE_SPECIFIC`**。

但这个 fallback 名称对本次实际门控具有误导性：

- Specificity lower bounds `(relative cNRMSE, R@1, MRR)=(0.158261, 0.150000, 0.124974)`，全部通过。
- Noncollapse 通过：variance mass=`16.550848`，effective rank=`37.521936`，64 active dimensions。
- Worst-view R@1=`0.895122`，lower=`0.876829`，远高于 chance `1/820`。
- VAE probe balanced accuracy=`0.421545 <= 0.433333`，通过。
- Architecture、matched streams 与 training integrity 全部通过。
- 相对 arithmetic baseline，R@1/MRR point gap=`-0.065854/-0.048732`，lower=`-0.087805/-0.064485`，未达到 `-0.02` noninferiority threshold。
- Failure reasons 只有 `noninferiority`。

Decision SHA-256：`8a079465076677c760eeca590313694ec69d2e197e567cfce385a605b6863fe4`。Inventory SHA-256：`9b806e59bec63d4ab5bdaaf3303dd2ca04402862d6686da362282183b0d6e55e`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

准确表述应是：

> 当前 learned deterministic consensus 非塌缩并含 correct-pairing-specific structure，但相对简单 arithmetic reference baseline 的检索质量下降超过注册容忍度。

因此本实验否定的是当前 deterministic construction 在冻结 feasibility rule 下的竞争力，而不是所有 deterministic consensus U，也不是 correspondence specificity 本身。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本实验 hard stop。不要继续在相同 authority 上调 deterministic architecture。若以后另行批准，只能把它作为一个失败的当前构造对照，而不能当作 deterministic U 的一般不可能性证明。

本实验和归档均为 CPU-only；GPU 服务器无需开启。

## Sources

- [来源快照](../source-snapshots/latentatlas-u4a6d-deterministic-consensus-u.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u4a6d-deterministic-consensus-u.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
