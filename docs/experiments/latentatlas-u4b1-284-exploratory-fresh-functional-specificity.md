# LatentAtlas U4-B1-284 Exploratory Fresh Functional Specificity

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在不修改原始 confirmatory U4-B1 的前提下，建立独立命名的 `B1-284` exploratory amendment，使用当前已封存的 284 对 fresh authority 回答：冻结 N-family DCAE→H mapping 与冻结 U0 Reward Head 是否同时具有绝对功能信号和 correct-pairing functional specificity。

该实验是 development-only、exploratory、non-confirmatory。它不恢复原 U4-B1 的 300-pair 门槛，也不能冒充原 U4-B1 confirmatory result。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-u4b1-284-exploratory-fresh-functional-specificity.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Authority：U4-B0 `FRESH_FUNCTIONAL_AUTHORITY_CANDIDATE_SEALED`
- Fresh pairs：284
- Unique images：568
- Connected components：284
- Effective component count：284.0
- Provider：原 B1 label-blind provider，seal=`d9d1c0f3c439b4dd12d8befa36da5edef62f9d2cc78a22d71f3344644b1ca7a0`
- Model bundle manifest：`d42641c49fc8233fe7f28c0d4182b4c635792d3ee844f14f3f44fe51fd535d`
- MPS smoke receipt file SHA：`ae8e71bff4182bb8b7f0c59b76d43eaf71ba84627ffb73e67a70f386540b368c`

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 Operational validity

- Completed-tree verifier：`PASS`
- Postformal verifier 精确冻结：production commit=`b8e4c4ee…`、raw config SHA=`0776395e…8fac`、MPS infrastructure binding=`c0fc7dbb…4f4e`。
- Scientific decision：`INDETERMINATE`
- Reason：`SOURCE_H_INADEQUATE`
- Exact public paths：23/23
- Inventory SHA：`9b4aa2a9adb984d5123fcfa38b33e8411fcbec1a0dab025eb2e9c651dfe8ea48`
- 14 个 validity flags 全为 true。
- Orientation open 恰好 1 次，发生在 prelabel score seal 后；network、training、post-orientation GPU、adaptive change 与 private per-item public persistence 均为 0。
- Postformal regression：U4-B1=`280 passed`；全仓=`3079 passed`；独立 verifier 继续返回相同 inventory 与 `INDETERMINATE`。

### 7.2 Aggregate functional metrics

| Condition | Accuracy point | Bootstrap interval | BT-NLL point | Bootstrap interval |
|---|---:|---:|---:|---:|
| `SOURCE_SD` | 0.514085 | [0.464789, 0.563380] | 0.709960 | [0.694164, 0.726029] |
| `SOURCE_FLUX` | 0.492958 | [0.443662, 0.542254] | 0.719656 | [0.698280, 0.741537] |
| `SOURCE_H` | 0.500000 | [0.450704, 0.549296] | 0.714304 | [0.696925, 0.732001] |
| N/correct 三 seed 中位数 | 0.514085 | [0.468310, 0.559859] | 0.718515 | [0.696708, 0.740210] |

Registered correct-over-all-null summaries：

- `G_acc point=-0.014085`，interval=`[-0.088028, 0.017606]`
- `G_nll point=-0.026631`，interval=`[-0.048816, -0.005511]`
- 所有 source、correct 与 permutation conditions 均未 collapse。

正的 `G_nll` 才表示 correct 的 BT-NLL 优于全部 null；本次为负。上述方向性结果只作描述，不改变 `SOURCE_H_INADEQUATE` 的 precedence。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 8.1 结果证明了什么

1. 284-pair amendment 的 authority、sample gate、模型、checkpoint、receipt、seal、access boundary 与聚合统计均有效，实验不是工程失败或 invalid run。
2. 在这套 exact frozen head/reference/protocol 下，`SOURCE_H` 直接 source-control 没有通过绝对可读性 gate：Accuracy 为随机点估计，BT-NLL 也差于 `log(2)`。
3. 因 DCAE mapping 的目标正是该 H arithmetic chart，SOURCE_H 失败意味着当前 cross-domain head/reference 不足以归因 DCAE mapping。当前最先暴露的瓶颈在 mapping 之前的 source-head/reference adequacy gate。
4. 描述性地，N/correct 接近随机且没有胜过五个 permutation null；但在 SOURCE_H 不 adequate 时，不能把它升级为“正确 correspondence mapping 已被 fresh 数据否定”。

### 8.2 结果不证明什么

- 不证明 H、SD、FLUX 或 DCAE latent 普遍不含 Reward 信息。
- 不证明所有 frozen/new Reward Head 都会失败，也不唯一定位为 head、reference、cohort shift 或 Reward semantics 中的某一个原因。
- 不证明 N mapping 本质不可达，不否定 U4-A4/U4-BD1 在历史 development cohort 上的结构/功能 specificity 结果。
- 不证明 canonical `U` 不存在、unseen-VAE onboarding 不可能或 cross-distribution transfer 普遍失败。
- 不构成原始 300-pair U4-B1 confirmatory PASS/FAIL；原 U4-B1 从未正式运行。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

下一步不应优先再换 Bridge 或 mapping architecture，而应先定位 `SOURCE_H_INADEQUATE`：

1. **最快的 development diagnostic**：设计 `B1-D0 Frozen-Head / Reference Adequacy Localization`，在已有 development authority 上固定比较 H/SD/FLUX 的 raw margin、scale/calibration、head checkpoint 与 Reward-semantics compatibility；只用于选定一个冻结修复候选，不宣称 fresh confirmation。
2. **最终 fresh gate**：取得新的、未消费的 fresh authority 后，先做 direct `SOURCE_H` adequacy gate；只有 H 通过，才重新进入 DCAE correct-vs-permutation mapping specificity。

不能重开本次 one-shot orientation，也不能根据本次 fresh metrics 在同一 authority 上调 head、threshold、mapping 或 calibration。

## Sources

- [来源快照](../source-snapshots/latentatlas-u4b1-284-exploratory-fresh-functional-specificity.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-u4b1-284-exploratory-fresh-functional-specificity.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
