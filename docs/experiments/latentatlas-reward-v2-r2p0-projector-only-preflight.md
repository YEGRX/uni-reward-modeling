# LatentAtlas Reward V2 R2P-0：Projector-Only Frozen Reward Interface 设计与预检

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

本阶段只冻结并验证一个条件式强基线：如果未来 R0/R1 产生合格且 sealed 的 RGB-text Reward oracle，能否在不训练 Reward components 的前提下，用每个 VAE 独立的 Projector 将 native latent 映射到冻结 Reward interface。

R2P-0 不是 Projector 实验结果。它不训练 Projector、不生成 R2P latent cache、不读取 Projector DEV、不 decode RGB、不读取 LOCKBOX，也不使用 MPS/GPU/AutoDL/network。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-reward-v2-r2p0-projector-only-preflight.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

R2P-0 只读取两份显式 legacy metadata 文件，不读取它们指向的 image order、tensor 或模型文件：

- Legacy seal：382 bytes，SHA-256=`c0c64931d62eb3ac0eaa056a931a2f5647892d18532abfec084ef1c0be952499`
- Legacy provenance：2,432 bytes，SHA-256=`3be5c5f8120159efc86aa849d4cf1af1b143fe054a0718b683bf84a0ff65c2b1`
- Seal image count=`14,918`，DCAE materialization count=`0`
- 分类：`LEGACY_FULL_AUTHORITY_CACHE`
- `training_eligible=false`，`benchmark_eligible=false`
- 证据边界：只有 sealed count、scope 与 provenance linkage，没有 row-level identity replay

未来 R2P-1 必须重新建立 split-scoped cache：TRAIN=`4,059 pairs / 8,118 images`，DEV=`900 pairs / 1,800 images`，LOCKBOX identities/RGB/latents=`0/0/0`。当前没有 materialize 该 cache。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

- `r2p0_preflight/` 精确包含 17 个普通文件：14 个 static protocol JSON、audit、verifier receipt 与 deterministic report；没有 `runs/`、latent、checkpoint、score、RGB 或模型 payload。
- Pinned independent verifier：`PASS / git_anchor / git_anchor_commit=dd63e1d…3837`
- R2P-0 focused regression：`94 passed`
- R0/R1 predecessor regression：`87 passed`
- 所有访问计数：Projector training、cache materialization、decode、Projector DEV、LOCKBOX、MPS、GPU、AutoDL、network 均为 `0`

当前 R0/R1 的真实 sealed 分类仍是：

```text
VALID / FALLBACK_RGB_ORACLE / INCONCLUSIVE_WEAK_ORACLE / ACQUIRE_FROZEN_VLM_ORACLE
```

它不满足 R2P-1 所要求的 `VLM_ORACLE + OIP_RGBTEXT_AUTHORITY_OBSERVABLE + PROPOSE_R2_RAW_LATENT_CEILING`，因此 execution gate 必须保持 blocked。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

### 能说明什么

- 条件式 R2P 协议、architecture、budget、controls、statistics、ratio、decode、MPS 与 artifact inventory 已冻结。
- CPU-only publisher/verifier 能 fail closed 地约束 exact repo root、clean predecessor、legacy metadata、17-file membership、canonical JSON、receipt、blocked command 与 pinned Git tree。
- Legacy 14,918-image full-authority cache 不能被误当成 TRAIN/DEV scoped training cache或 benchmark cache。

### 不能说明什么

- 没有合格 R0/R1 oracle，不能执行或解释 R2P-1。
- 没有训练任何 Strong/Shallow/P-SUP/P-ANCHOR/PERM Projector，因此没有 optimization、noncollapse、Reward retention 或 architecture comparison 结果。
- 没有证明 native latent 的 Reward ceiling、shared U 是否必要、Reward transfer、fresh confirmation、cross-distribution generalization 或 unseen-VAE onboarding。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

当前 hard stop。只有 R0/R1 产生合格且 sealed 的 oracle classification、result seal 与 independent verifier receipt，并另行获得用户明确授权后，才允许进入 R2P-1。

若 R0/R1 最终没有 qualified oracle：

```text
BLOCKED_NO_QUALIFIED_R0R1_ORACLE
```

随后终止 R2P，不得临时替换 backbone/oracle 并沿用同一正式实验身份。

当前下一阶段不需要 GPU 或服务器。

## Sources

- [来源快照](../source-snapshots/latentatlas-reward-v2-r2p0-projector-only-preflight.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-reward-v2-r2p0-projector-only-preflight.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
