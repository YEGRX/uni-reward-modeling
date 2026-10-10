# RGEN1 Reward 外部分布泛化定位

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

定位 [rpj4-true-unseen-sd35-anchor-confirmation](rpj4-true-unseen-sd35-anchor-confirmation.md) / [latentatlas-u7-reconstructed-anchor-onboarding](latentatlas-u7-reconstructed-anchor-onboarding.md) 的 source Reward failure：是 HPDv3 Reward 外部分布迁移、shared interface，还是当前 latent Reward 方案没有学到新偏好？Research gap 是 registration 成功并不保证 Reward readability。本轮是 adaptive diagnosis，不是全新 authority confirmation。

**核心结果：旧冻结路线在两块已消费诊断面均为 BROAD FAIL；fresh DCAE 在固定协议下 FAIL；固定 CLIP 加小型 head 在两面 PASS。问题被收窄到所测试 latent Reward formulation / representation，不能归咎于共享接口，也不能证明 DCAE 不含偏好信息。**

## Config

[历史配置摘要](../../configs/experiments/latentatlas-rgen1-reward-external-generalization.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

数据：`datapointai/text-2-image-dpo-human-preferences-full@0e757688c64ff6ee7c412e8b810cdbded2751dfc`；primary label：Overall Preference。

| 范围 | 原始行 | Strict preference | 用途 |
|---|---:|---:|---|
| FIT | 3,641 | 2,985 | 固定训练 |
| SELECT | 781 | 653 | 仅按 BT-NLL 选 checkpoint |
| DIAG | 780 | 643 | Adaptive development diagnostic 主判定 |
| RPJ4-only EXTERNAL | 3,161 | 2,619 | 历史已消费外部诊断，不参与训练/选择 |
| Future reserve | 12,455 | 不读取 | Globally unconsumed future reserve |

U7 开发池 5,202 行；RPJ4 SOURCE_DEV 4,164 行；交集 1,003；consumed union 8,363。独立身份图审计 20,818 行/20,785 组件，去连接后 future reserve 仍为 12,455，quarantine=0。已有行、图像、prompt、pair、组件交叉审计通过；缺 generator/group metadata，因此 clean 声称只覆盖可用身份字段与已记录消费历史。

原 U7 15,616 行 LOCKBOX 不能整体称 globally untouched。两个历史实验各自 LOCKBOX=0 的事实保留；跨实验 consumption union 单独记录。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

### 7.1 Frozen → DIAG

下列为 Acc/NLL；共享路线是三 VAE 宏平均，正式资格仍要求每个 family 通过。

| 模型 | Prompt | Latent-only | 状态 |
|---|---|---|---|
| Native SD | 51.48% / .6993 | 48.99% / .7052 | FAIL |
| Native FLUX | 46.97% / .7074 | 48.68% / .7161 | FAIL |
| Native DCAE | 47.28% / .7100 | 44.17% / .7414 | FAIL |
| Direct Shared | 48.11% / .7048 | 49.14% / .7185 | FAIL |
| Explicit U | 50.08% / .6987 | 49.09% / .7131 | FAIL |
| Projector | 48.11% / .7071 | 46.86% / .7276 | FAIL |

EXTERNAL也全部FAIL。Frozen failure scope：**BROAD**，不是仅共享路线失败。

### 7.2 Fresh DCAE 与 RGB

| 模型 | DIAG Acc/NLL | EXTERNAL Acc/NLL | 资格 |
|---|---|---|---|
| Fresh DCAE prompt | 50.54% / .6975 | 50.25% / .6983 | 两面FAIL |
| Fresh DCAE latent-only | 52.88% / .7590 | 53.42% / .7404 | 两面FAIL |
| Fixed CLIP + RGB head | 58.63% / .6640 | 58.04% / .6659 | 两面PASS |

RGB两面 readability、PAIR_RO、A/B direction、3seed全部PASS。DIAG Acc−.5 lower95=.053655；NLL−log2 upper95=−.016150。External对应为.064701和−.021001。

Prompt role：`PROMPT_CONDITIONING_NOT_ESTABLISHED`。Fresh DCAE的PAIR_RO与wrong-prompt均FAIL。没有预注册等价界限，不可由“不显著”推断image-dominated。

Fresh Direct / Projector / U：`NOT_RUN_BY_REGISTERED_GATE`；其可学习性仍不可判定。

### 7.3 最终判定与验证

- Classification：`LATENT_REWARD_FORMULATION_OR_REPRESENTATION_IS_PRIMARY_BOTTLENECK`（注册Case F）。
- Recommendation：`LATENT_REWARD_FORMULATION_DIAGNOSTIC`。
- 9次正式fit：native6+RGB3，均执行5,000步。82项测试PASS。
- 6块统计结果重放（每块20,000次）mismatch=0；2,629个结果/来源文件、202主规格绑定、自动decision与report一致性PASS；终态三件套复核PASS。
- Spec SHA：`399f2562150d2083b6b8dd136875c1f7cdda019987d4cdedfc386c0c9cb6f102`。
- Decision SHA：`159a4b68534cf4274337a552d59660fdc798a353d54cb8ac2168dba5a6ae594b`。
- Final result seal：`737562835ff85b11f729cae9fa6bf91674e0ac2c7bb40db70dc82b82fa088b36`。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

RGB PASS说明这两块已消费diagnostic surface存在可由固定CLIP+小head读取的视觉偏好信号。Native失败不是shared constraint独有现象，因此本轮不支持优先增大U/Projector或直接重做shared interface。

Case F只是收窄到当前latent Reward方案，**不能区分DCAE表示、reader/head formulation、优化设置、最早250步checkpoint选择，或其交互**。六个native的最佳eligible checkpoint均为250步，SELECT NLL仍劣于初始，`optimization_adequate=false`；RGB三seed均在500步最低且优于初始。协议枚举`NOT_LEARNABLE_BY_TESTED_LATENT_READER`只解释为固定协议未达到资格门槛，不是latent没有信息或任务不可学习。

旧HPDv3 Reward的外部分布失败已在测试范围内成立；但fresh native也FAIL，不能把“只要Multi-Authority训练即可解决”当成已证实结论。没有fresh shared成功证据，所有true-unseen target Reward、U/Projector优越、universal Reward与部署结论保持关闭。

## Possible Conflict / 待确认冲突

原§22/§25冲突已按用户批准amendment解决，四份authority文件在训练前封存。Overlap行绑定两份消费来源；首次消费先后缺可靠时间，标为不可确认，不伪造chronology。

RPJ4 sealed rowwise/metrics/nulls/bootstrap artifact replay mismatch=0，不重访raw orientation；其source teacher是RPJ2 Projector，不能等同本轮RRV1 native DCAE。U7指标/readability bootstrap重放通过，但缺null rowwise arrays的控制项仅summary/hash验证，不能声称完整exact control replay。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本轮已停止。下一实验应先用受控比较区分latent表示、reader/formulation与固定优化/检查点选择的影响；保持现有RGB正对照与authority边界，再单独冻结计划。**尚未启动任何下一实验，未打开未来reserve。**

GPU计算已结束；当前后续工作不需服务器，云服务器实际状态未检查。

## Sources

- [来源快照](../source-snapshots/latentatlas-rgen1-reward-external-generalization.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-rgen1-reward-external-generalization.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
