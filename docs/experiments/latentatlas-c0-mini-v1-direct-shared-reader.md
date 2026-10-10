# LatentAtlas C0-Mini-v1 Direct Shared Clean-Latent Reward Reader Diagnostic

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在 [latentatlas-o1-v1-lightweight-spatial-oracle](latentatlas-o1-v1-lightweight-spatial-oracle.md) 已给出三种 VAE 各自含有可读 Reward signal 的 preliminary evidence 后，隔离检验一个更小的问题：当 Independent 与 Shared 条件使用完全相同的 model-agnostic 输入接口和 9,473 参数 reader 时，参数完全共享是否本身造成 Reward readability 损失。

本实验只比较三份 Independent Same-Interface Readers 与一份看不到 VAE identity 的 Direct Shared Reader；不使用 Anchor、Relation、G1 feature、VAE-specific adapter/head、domain token、canonical `U`、预训练视觉模型、超参数 sweep 或 null 扩展。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-c0-mini-v1-direct-shared-reader.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- 冻结数据来自 [latentatlas-reward-data-preflight-g01](latentatlas-reward-data-preflight-g01.md)：`56,074` usable preference pairs、`6,632` reward images。
- Train/validation/test pairs=`44,839 / 5,593 / 5,642`；unique images=`5,201 / 708 / 723`。
- Image、pair、prompt、source-row 均跨 split disjoint；split SHA-256=`83a96bcdeb2805e1743b4555c5a1366558612dc5033598c777295b3016ab64ea`。
- SD/FLUX/DC-AE latent shape=`[4,64,64] / [16,64,64] / [32,16,16]`；三份正式 cache 均覆盖全部 reward images，另有的 `192` 个 Anchor rows 全部排除。
- 每个 channel 独立做 `AdaptiveAvgPool2d((4,4))` 的整数分块等价实现，再 flatten 为 16 维 token；因此三个 VAE 的统一接口分别为 `4/16/32 × 16` tokens。
- 每个 VAE 只用 5,201 张 unique train images 的全部 pooled values 拟合一个固定 population scalar mean/std；validation/test 不参与。SD/FLUX/DC-AE mean=`0.372937/-0.145613/-0.417926`，std=`3.461009/2.136468/2.210025`。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

| VAE | Independent Acc | Shared Acc | Acc Gap | Independent NLL | Shared NLL | NLL Gap |
|---|---:|---:|---:|---:|---:|---:|
| SD | 55.90% | 54.68% | -1.22 pp | 0.683931 | 0.685340 | +0.001408 |
| FLUX | 54.54% | 55.07% | +0.53 pp | 0.684835 | 0.682106 | -0.002729 |
| DC-AE | 56.15% | 55.83% | -0.32 pp | 0.679810 | 0.684015 | +0.004204 |
| **Macro** | **55.53%** | **55.19%** | **-0.34 pp** | **0.682859** | **0.683820** | **+0.000961** |

机器精度的 Independent/Shared macro accuracy=`0.555300/0.551932`，accuracy gap=`-0.003368`；对应 macro NLL gap=`+0.000961`。

Best epoch / validation NLL：SD=`3 / 0.682376`，FLUX=`1 / 0.687101`，DC-AE=`5 / 0.685316`，Shared=`1 / 0.688983`；实际训练 epoch 数分别为 `8/6/10/6`。

四个 9,473 参数 checkpoint 均在 test 前冻结并校验 SHA-256；同一份 Shared checkpoint 被用于 SD/FLUX/DC-AE 三次 family-wise test。所有 `checkpoint_frozen` events 都早于唯一 `test_labels_opened` event，`test_label_open_count=1`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 8.1 Same-interface Independent readers 是否保留基本可读性？

三者 test accuracy 均高于 pairwise chance `0.5`，BT-NLL 均低于 `log(2)`。结合 O1-v1 的 repaired-null 3/3 preliminary positive，可把统一 coarse-token interface 视为保留了弱但一致的 Reward readability。这里没有为 C0 新增 null distribution，因此不能把这句话升级为正式显著性结论。

### 8.2 参数完全共享是否造成明显损失？

没有观察到。Shared macro accuracy 只比 Independent 低 `0.003368`（`0.34` percentage points），远小于预注册 Case A 的“约 2 pp”描述边界；三个 family gap 为 `-1.22/+0.53/-0.32 pp`，没有任何单一 VAE collapse。Macro NLL 仅恶化 `0.000961`。

### 8.3 Gate

正式报告按预注册 smoke gate 归为 **Case A — Jointly Readable**：当前 simple model-agnostic reader 下，heterogeneous VAE latent 中的 Reward information 已经能够被同一套参数共同读取。该结论是 preliminary problem-identification evidence，不是统计显著性证明，也不证明 unseen-VAE generalization 或 universal Reward sufficiency。

### 8.4 对 canonical `U` 的含义

C0 没有提供“参数共享导致明显 readability loss”的证据，因此当前没有理由仅基于这一问题启动 Minimal Reward-Supervised Canonical `U`。这不证明任何 U 永远无用，只表示本轮定义的 canonicalization problem 未被检测到。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

C0-Mini-v1 到此停止。不执行 VAE-ID、LOO、Minimal-U、architecture change、hyperparameter sweep 或额外 null。若未来另行立项，必须提出与本结果不同的新科学问题并重新预注册，不能根据本次 test 调参或覆盖 sealed result。

## Sources

- [来源快照](../source-snapshots/latentatlas-c0-mini-v1-direct-shared-reader.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-c0-mini-v1-direct-shared-reader.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
