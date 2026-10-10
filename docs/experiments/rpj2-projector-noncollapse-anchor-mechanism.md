# RPJ2 Projector Noncollapse and Anchor Mechanism

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在不读取 official TEST、不向 Anchor target 暴露 Reward labels 的条件下，回答两个机制问题：

1. RPJ1 的 Projector noncollapse gate 失败是否意味着真实 functional collapse？
2. correct same-image Anchor 能否把 pseudo-unseen held-out VAE 注册进冻结 Reward system？

本实验承接 [latentatlas-rpj1-reward-projector-dev](latentatlas-rpj1-reward-projector-dev.md)，但不改写其 sealed classification。

## Config

[历史配置摘要](../../configs/experiments/rpj2-projector-noncollapse-anchor-mechanism.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- 冻结 SD / FLUX / DCAE representation cache。
- 冻结 authoritative text cache。
- RPJ1 predecessor、Projector checkpoints 与同图 Anchor correspondence。
- 三个 known-VAE pseudo-unseen held-out episodes；每次用另外两个 family 构造 source Reward system。
- 内部 mechanism lockbox 只消费一次；不是 official TEST。

Authority counters：

- official TEST orientation / forward / rows loaded：`0 / 0 / 0`
- Anchor target Reward-label access：`0`
- mechanism lockbox orientation access：`1`
- network / RGB access：`0 / 0`

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### Q1：Projector 是否真实塌缩？

结论：`NO MATERIAL FUNCTIONAL COLLAPSE`。

- RPJ1 原 gate 的唯一失败项是 FLUX / seed 20260827 的 `effective_rank=9.288071` 未满足严格 `>16`。
- RPJ2 重新诊断得到 sample-variance ratio=`0.104484–0.249591`、effective-rank ratio=`1.009527–1.429366`、token-variance ratio=`0.120765–0.262363`、active dimensions=`1.0`。
- 所有 representation shuffle diagnostics 都保留 image-specific signal。
- 更准确的机制是 `FULL_RANK_FULLY_ACTIVE_AMPLITUDE_AND_TOKEN_VARIANCE_COMPRESSION`，即幅度与 token variance 压缩，不是真正样本信息塌缩。
- 冻结分类器没有这一组合，因此机器标签仍保留为 `PROJECTOR_FUNCTIONAL_NONCOLLAPSE_INDETERMINATE`；RPJ1 结论不被回写。

### Q2：Reward-free Anchor registration 是否成立？

结论：`NOT SUPPORTED`，全局分类为 `ANCHOR_REWARD_FREE_REGISTRATION_NOT_SUPPORTED_UNDER_TESTED_PROTOCOL`。

| Target | NoReg Acc/NLL | SUP Acc/NLL | Anchor Acc/NLL | rho Acc | rho NLL | episode |
|---|---|---|---|---:|---:|---|
| SD | `.484698/.711870` | `.584458/.649966` | `.574707/.655127` | `.902256` | `.916632` | `ANCHOR_PARTIAL` |
| FLUX | `.505701/.698411` | `.598860/.643174` | `.594059/.648034` | `.948470` | `.912014` | `ANCHOR_PARTIAL` |
| DCAE | `.518602/.691465` | `.617162/.635709` | `.598110/.646351` | `.806697` | `.809138` | `ANCHOR_PARTIAL` |

- 三个 supervised oracle 都 adaptable。
- correct Anchor 的 interface correspondence 对 five permutations 全部通过；R@1=`1.0`，permutation R@1 约 `.0125–.0167`。
- correct Anchor 的 Reward point estimate 对 NoReg 和 five permutations 都为正，wrong-prompt controls 也通过。
- 但三个 target 的 representation-specificity controls 全部失败，因此三个 episode 都只能是 `ANCHOR_PARTIAL`，不能升级成 reward-free registration support。
- DEV exact-path preflight 曾对三 target 都是 `ANCHOR_STRONG_PASS`，而一次性 lockbox 全变为 `ANCHOR_PARTIAL`；这说明 preflight optimism 没有跨越到冻结 lockbox，而不是可以忽略的随机小波动。

### Terminal verification

- Disk-only scientific verifier：`PASS`。
- Completed-seal replay：`PASS`。
- Inventory：`251` files，`634,000,245` bytes，tree SHA256=`193a5e69c4df5cb3747eae4ff5367807359df300853d1d08976e5a51441ac66f`。
- Verifier receipt SHA256=`23500174204b9c14392c96a73676ac9850cb5f80c1f2cfb05a4241304edf3d47`。
- Result seal SHA256=`53632b65bd44525e23257767e17cd5abd1c8dc3641ee98388a85b5adb5a80b23`，status=`COMPLETED`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

当前证据把两个问题分开了：

1. RPJ1 Projector 不是“信息全没了”；它仍全秩、全维活跃并保留 image-specific signal。原 noncollapse threshold 对这种 amplitude/token-variance compression 过于粗糙。
2. “几何上能正确对齐”不等于“Reward 因果上使用了正确 target representation”。Anchor 在 interface、NoReg improvement、permutation 与 prompt controls 上都表现良好，但 representation specificity 失败，说明 Reward improvement 不能严格归因到正确 target representation。
3. SUP 全过而 Anchor 只 partial，排除了“held-out family 根本不可适配”这一解释；更可能的缺口位于 reward-free registration objective、target representation usage 或 source-to-target functional interface。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

冻结建议：`DIAGNOSE_TARGET_FAMILY_GAP`。

下一实验应保持 TRAIN/DEV-only，并专门区分：

- correct target representation 是否被 Reward path 实际使用；
- interface correspondence 很强但 representation-specific Reward control 失败的原因；
- source Reward system、target stem 与 Anchor objective 中哪一段造成 functional attribution gap。

不得在本 lockbox 上改阈值、继续 architecture/seed sweep 或重复访问；也不能把 `ANCHOR_PARTIAL` 写成 registration 成功。

## Sources

- [来源快照](../source-snapshots/rpj2-projector-noncollapse-anchor-mechanism.txt)，原页面定位 `wiki-store/wiki/experiments/rpj2-projector-noncollapse-anchor-mechanism.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
