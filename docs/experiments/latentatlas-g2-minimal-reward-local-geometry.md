# LatentAtlas G2-v0 Minimal Reward-Relevant Shared Local Geometry

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在不等待 formal G1、不训练 encoder / Reward Head / U 的前提下，检查 SD-VAE、FLUX-VAE、DC-AE 在各自 Anchor Relation space 中共同认可的局部邻居，是否比单 VAE 邻居或 matched Random 具有更小的 human-preference-derived RewardGap。该实验与 [latentatlas-reward-sufficiency-g1-true-smoke](latentatlas-reward-sufficiency-g1-true-smoke.md) 的 Reward Head、预测和指标完全解耦，只复用可独立解释的 clean latent / global-cosine relation cache。

核心问题：

\[
\text{Cross-VAE neighborhood consensus 越高}
\Rightarrow
\text{RewardGap 越小？}
\]

## Config

[历史配置摘要](../../configs/experiments/latentatlas-g2-minimal-reward-local-geometry.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Preference authority: [latentatlas-reward-data-preflight-g01](latentatlas-reward-data-preflight-g01.md) 的 `pair-manifest.jsonl`。
- 只保留两个 endpoint 都在三 VAE relation cache 的 usable comparisons：`999` pairs、`713` unique images。
- Split counts: train / validation / test = `605 / 168 / 226`。
- 三 VAE 对同一 `713` 张图完整覆盖；`missing_images=[]`。
- Clean latent shapes：SD `[4,64,64]`，FLUX `[16,64,64]`，DC-AE `[32,16,16]`。
- Relation shapes：三者均为 `[713,64]`。
- Frozen RGB Anchor Bank：seed `2026080901`，`64` anchors。
- Relation operator：`global_cosine`。

### Preference graph audit

RewardGap 只用 train labels 拟合：

- `605` train edges，`481` nodes；
- `149` connected components；
- largest component size=`11`；
- median component size=`2`；
- row-weighted isolated-pair fraction=`0.127273`；
- 因存在多个大于 2 的连通分量，且绝大多数 comparison rows 不属于 isolated-pair component，RewardGap gate 判定为 identifiable。

其中两个三图 component 构成严格循环偏好，每张图恰好一胜一负；BT 最优 utility 方差为 0。按 \((q-\mu)/(\sigma+\epsilon)\) 的协议，这两个 component 的标准化 utility 记为 0，并在 audit 中显式记录，未制造任意排序。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

| Consensus | N | Mean RewardGap | Median RewardGap | Mean 95% CI |
|---|---:|---:|---:|---:|
| C=3 | 102 | 1.325454 | 1.394935 | [1.176761, 1.487455] |
| C=2 | 79 | 1.320168 | 1.398234 | [1.132289, 1.520203] |
| C=1 | 132 | 1.300765 | 1.224155 | [1.125612, 1.465905] |
| Random | 181 | 1.337475 | 1.242970 | [1.204228, 1.473186] |

额外统计：

- `C≥2` mean=`1.323147`；
- `C=1` mean=`1.300765`；
- all-neighbor mean=`1.313708`；
- Random mean=`1.337475`；
- `C≥2 − C=1 = +0.022382`，即 consensus 邻居没有更接近；
- `C≥2 − Random = -0.014327`，差异很小；
- Spearman `(consensus, -RewardGap)=-0.001502`，95% CI=`[-0.085874, 0.082752]`。

按附件给出的点估计 decision gate，本次更接近 **Case B**：all-neighbor mean 略低于 Random，但 `C≥2` 没有优于 `C=1`。必须同时保留限定：四组 CI 大幅重叠，Spearman 几乎为 0，因此这是**弱 Case B pattern**，不是已检测到稳健的 single-VAE reward-local structure。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

最清楚的结论是：**cross-VAE consensus 没有产生 reward-similarity enhancement。** `C=3`、`C=2` 均没有比 `C=1` 更小的 RewardGap，相关系数也不支持“consensus 越高、gap 越低”。

all-neighbor 相对 matched Random 的 mean gap 仅低约 `0.02377`，而组内 bootstrap CI 很宽并高度重叠。因此不能把它升级为明确的 single-VAE geometry reward enrichment，更不能声称 Anchor Relation 已经 canonicalize Reward coordinate。

对 Minimal-U 的含义：如果继续，优先考虑 learned / task-aware canonicalization；不要直接使用当前 Anchor Relation 作为 canonical Reward coordinate。Relation 最多保留为 weak structural auxiliary，同时让 raw clean latent 与 Reward supervision 承担更主要角色。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

1. 按 G2-v0 停止条件，不自动启动 kNN Reward Prediction 或 G2-v1。
2. 若未来设计 Minimal-U，将 current Relation 视为 weak auxiliary / local structural hint，而不是 fixed Reward coordinate。
3. 若要确认 single-VAE neighbor 是否真的优于 Random，应另行预注册 component/query-aware inference 与更大 clean-latent coverage；不能在本 run 上追加 seed 或调 k 追求显著性。
4. 下一阶段不需要 GPU；只有真正开始新 VAE encoding 或训练时才应重新启动 GPU 服务器。

## Sources

- [来源快照](../source-snapshots/latentatlas-g2-minimal-reward-local-geometry.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-g2-minimal-reward-local-geometry.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
