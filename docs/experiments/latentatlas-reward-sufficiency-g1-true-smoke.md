# LatentAtlas G1 三 VAE Reward-Sufficiency Engineering Smoke

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

用 SD-VAE 与 FLUX VAE 的 source preference 训练 global-cosine MLP Reward Head，在物理分离的本地 target oracle 上比较 DC-AE correct Anchor 与 frozen wrong-Anchor control。该 smoke 首先验证三 VAE、cache、checkpoint、score、oracle、terminal seal 和 signed review 能否形成真实闭环，再观察最小 target 指标。上游 authority 见 [latentatlas-reward-data-preflight-g01](latentatlas-reward-data-preflight-g01.md)；早期单 VAE 工程路径见 [latentatlas-reward-sufficiency-g1-minimal-sd-smoke](latentatlas-reward-sufficiency-g1-minimal-sd-smoke.md)。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-reward-sufficiency-g1-true-smoke.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

- G0.1 artifact inventory: `1258096302a7da7147d159431b1eb53e8e141d39a1887b6847d7469c6775ef37`
- Input projection: `dd2363bec4b253cd7157ff5cf849a76022abe0113aa9cf0ee056c202c404fdbc`
- Label-free GPU projection: `77ecc5e12f90ef0b27ad70a82013f2bf2250896deb15f397e60d23c2b70313ba`
- Bundle manifest: `459022e0bed200d48d521797a7ae5ebfb40a93dbeba2840e61ab8c70cf453477`
- Bundle: `713` reward images + `64` Anchors，`contains_target_labels=false`
- Pairs train/validation/test: `256/64/64`
- GPU bundle held source orientations for train/validation but zero target-test orientations. Target labels remained on the local Mac until score sealing completed.

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

| Metric | Correct Anchor | Wrong Anchor | Correct − Wrong |
|---|---:|---:|---:|
| Accuracy | `34/64 = 0.53125` | `38/64 = 0.59375` | `-0.0625` |
| BT-NLL | `0.6836315958408619` | `0.6454089804235803` | `+0.0382226154` |
| Mean oriented margin | `0.02285032856` | `0.12653181233` | `-0.103681484` |

**直接结论：wrong Anchor 在本次 64-pair smoke 的 accuracy、BT-NLL 和 mean margin 上都更好。** 因此没有观察到预期的 correct-Anchor advantage。这是一个负向的探索性观察，不是“已证明不存在 reward signal”。

### 7.1 Terminal seal and review

- Terminal event: `complete / smoke / pass`
- Artifact inventory: `10db073311ae497c7fa685e459b2c55af2de48ab1595c9cd0d60f1838197900b`
- Pre-terminal events prefix: `099a76ec034708e245f9c6abd0faec6d5ed0e8c3c1030056368684792d5f2cc0`
- Typed oracle result: `c310d2aa029507cabd97a548373d82a4f32fdc673a645fd14548cae941f1494f`
- Independent exact recomputation: `Critical=0`, `Important=0`
- Audit projection: `e8cdb125f7b82c0cc944e007d766c20e604f147dc65c7d2dd2f786126d613f6c`
- Signed review receipt: `6afd5b6415aba265de537cdc28d2be9a31a835f2c06ce1b8641d1fb2319da916`
- Reviewed gate: `f83c8001042cbbd5faa9811e915d864ff6363d06edd5c634382e8858a04d0a9e`
- SSH signature verification: Good

### 7.2 Same-commit successor evidence

`f342b9c` successor smoke 精确复现 correct / wrong Anchor accuracy=`0.53125 / 0.59375` 与 BT-NLL=`0.683631595840862 / 0.6454089804235803`。其 review receipt 绑定：

- Artifact inventory: `27b891d3c1c1297bcbf29f4c1f3b4749a3dba5f03d4d4aad687505395a281a1c`
- Audit projection: `2ba378faac83fa54f62eca3f1a8aa8dd8c557dea61e019aeed762e2018c74960`
- Oracle result: `a8e188362c2c1549bb98e0afdabb9273aef74edf8098bdbca40b29d4bb57c1de`
- Review decision: `approve`

该 successor 只证明 formal commit 上的工程 wiring 与权限链通过；它不把 64-pair smoke metrics 变成 formal gate。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

工程边界已成立：GPU 端仅持有 label-free bundle；SD、FLUX 和 DC-AE 完成真实 CUDA 编码；source-only labels 用于 scaler / MLP 训练和 validation；checkpoint 及 correct/wrong score 先封存；本地 target provider 对 exact 64-pair batch 只打开一次；oracle metrics 被纳入 terminal seal。独立审计从 sealed tensors / checkpoint / scores 精确重算两个条件，结果一致且无 Critical / Important findings；签名 review 也绑定了 exact run projection。

这次 `f6b737a` run 替代了旧 `c0cdba3.../b3114bf` candidate 作为当前权威 engineering record。旧 candidate 的 raw-Parquet 主机污染与 oracle 未进 terminal seal 问题是历史 incident，不再描述新 run。

科学上仍应保守：只有一个 Anchor seed、一个 training seed、三个 epochs 和 64 个 target pairs；而且 wrong control 的表现更好。需要独立 formal design 的多 seed、完整 baselines/controls 与统计 gate，才能评估稳定 reward transfer。

后续 formal G1 已在 commit `f342b9c` 上完成 terminal seal，正式 decision=`no`、subtype=`control_failure`。该结果还记录了独立科学审计 `Critical=0, Important=1` 的 shuffle-validation 真实标签选择通道；详见 [latentatlas-reward-sufficiency-g1-formal](latentatlas-reward-sufficiency-g1-formal.md)。不得把本 smoke 的工程 `pass` 与 formal 科学 gate 混为一谈。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

1. 保留原始 `f6b737a` 与同 commit successor `f342b9c` 作为 engineering provenance，不将 smoke metrics 冒充 formal result。
2. Formal G1 已完成完整 condition/control/bootstrap 矩阵与 terminal seal；正式解释转到 [latentatlas-reward-sufficiency-g1-formal](latentatlas-reward-sufficiency-g1-formal.md)。
3. 后续若修订 shuffle control，应产生新的预注册 run，不覆盖 smoke 或已封存 formal run。
4. 继续保留 wrong Anchor 在 smoke 中更好的负向先验记录。

## Sources

- [来源快照](../source-snapshots/latentatlas-reward-sufficiency-g1-true-smoke.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-reward-sufficiency-g1-true-smoke.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
