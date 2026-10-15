# LatentAtlas RPJ1 Reward Projector Development Experiment

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

RPJ1 检验两件事：

1. 在 SD、FLUX、DCAE 三个已知 VAE 上，per-VAE shallow Reward Projector 能否支持一套共享 Reward Reader（one shared Reward model）。
2. 只有 Gate 1 合格时，才继续检验 reward-free Anchor registration 能否把冻结的 source Reward system 注册到留出的 target VAE。

本实验是 `latentatlas`（原wiki关联） 的 TRAIN/DEV-only development evidence，不使用 official TEST。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-rpj1-reward-projector-dev.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- Frozen HPDv3 TRAIN subdivision 与 official DEV。
- 已封存的 SD / FLUX / DCAE representation cache。
- 已封存的 authoritative 6144D text cache。
- Native DEV reference 仅用于冻结的对照比较。
- Official TEST orientation / forward / metrics：`0 / 0 / 0`。
- Anchor target Reward-label access：`0`。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

| Method | Macro Acc | BT-NLL | SD Acc | FLUX Acc | DCAE Acc |
|---|---:|---:|---:|---:|---:|
| DIRECT_SHARED | 0.627267 | 0.623737 | 0.613000 | 0.626000 | 0.642800 |
| PROJECTOR_SHARED | 0.630333 | 0.619715 | 0.609600 | 0.641200 | 0.640200 |

Gate 1 controls：

- Representation specificity: `PASS`
- Prompt over latent-only: `FAIL`
- Wrong-prompt specificity: `PASS`
- Direction balance: `PASS`
- Three-seed robustness: `PASS`
- Projector noncollapse: `FAIL`
- Incremental-value interpretation: `ONE_SHARED_REWARD_SUPPORTED_BUT_PROJECTOR_NOT_NECESSARY`

最终分类：

- Gate 1: `GATE1_PROJECTOR_SHARED_REWARD_NOT_SUPPORTED`
- Gate 2: `GATE2_NOT_RUN_SOURCE_REWARD_SYSTEM_UNQUALIFIED`
- Recommendation: `STOP_REWARD_PROJECTOR_GATE2_ON_THIS_AUTHORITY_AND_DIAGNOSE_GATE1_FAILURE`

Verifier 与封存：

- Disk-only scientific verifier: `PASS`
- Verifier receipt SHA256: `eb681a18f548aad5700238e1c7955be138ca78d714ef4c1d956d7ae90e133d1f`
- Result seal: `COMPLETED`
- Result seal SHA256: `bab045dd5a7e035df52a87b39764481747c8c8dc0f8ff935356659972387401b`

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

这个结果支持“已知三类 VAE 的冻结 latent 中存在可由一套直接共享 Reward Reader 读取的开发性信号”，但不支持“当前 shallow Projector 是必要且合格的共享 Reward 接口”。虽然 Projector 的宏观 Accuracy/BT-NLL 点估计略优于 Direct，共享 Projector 没有通过 prompt incremental 和 noncollapse 两个资格门槛，因此不能把微小点估计优势归因成 Projector 的有效增益。

Gate 2 被预注册条件正确阻断。因此，本实验没有检验 Anchor 是否能实现 reward-free target registration，也没有产生 unseen-VAE、zero-shot 或 canonical-U 证据。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

先做 Gate 1 failure localization：确定 noncollapse 失败来自 Projector parameterization、normalization、shared-reader shortcut，还是 prompt 与 latent 的增量信息不足。不得在同一 development authority 上通过改阈值或反复选择来“救活” Gate 1；若提出新 Projector，应冻结新协议并使用新的验证边界。

## Sources

- [来源快照](../source-snapshots/latentatlas-rpj1-reward-projector-dev.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-rpj1-reward-projector-dev.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
