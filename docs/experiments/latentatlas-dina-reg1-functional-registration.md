# DINA-REG1 FLUX功能配准准备

归档日期：2026-10-10；证据层级：历史页面快照，未全量重新审计。

## Experiment

在SRC0已qualified的source-matched任务上，比较64 FIT+64 VAL独立captioned anchors下REC与FUNC是否能复用Frozen DiNa；target preference labels=0。SHIFT0外部结果不构成阻塞条件。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-dina-reg1-functional-registration.json)，不是可派发GPU任务。

**输入与范围：** 以原页面输入、统计口径与原冻结合同为准。

固定COCO val2017 bank2026080901的64 FIT和2026080902的64 VAL已于02:27通过CPU资产准入。官方caption ZIP252907541字节完整取得，按最小annotation ID选caption；128原图原SHA/尺寸通过，与完整HPDv3 4133来源路径的byte/RGB重叠均0。preflight SHA `daa0f44d27f09795437a2a763bcc0f4d870e4cf99d71f8cca506ab4e90d970fc`，敏感数据读取与GPU前向均0。03:30仅复用该回执物化训练清单，删除preference_labels:null；不重新下载或更换成员。

已找到既有FLUX.1-schnell VAE文件与model-bundle，revision741f7c3ce8b383c54771c7003378a50191e9efe9；权重预期SHA f5b59a26851551b67ae1fe58d32e76486e1e812def4696a4bea97f16604d40a3，167666902字节。config已按预期SHA在远端核验；权重04:16完整167,666,902字节已在远端校验预期SHA，传输结束；不得复用历史latent。旧bundle的MPS环境只是来源记录，新实验继续远端CUDA环境。

## Result

**当前归档分类：** `WIKI_SNAPSHOT_NOT_REAUDITED`

历史记录已导入；请结合该页结果与失败记录，不将实施或资格状态视为方法收益。

2026-09-22 09:15：三组训练均完成1000步，恢复任务exit0；已远端独立核验所有检查点链/各自VAL选点、冻结authority、七模型状态与实际新config，确认仅跳过已完成REC一次且其全部文件未变。唯一PostFit-r1任务于09:14:27启动，09:16:41实际评估子进程已进入模型加载与新进程准入，评分0/1008，不能称评估完成。接下来沿用冻结评估器及两次远端CPU回放，最终仍需本地portable复核。

补充资格新外层SHA `ad631da1…`，独立CPU回执 `d50bb54a…`；实际新parity `3aae86d1…`。缓存和原spec/正式科学代码未改；原失败保留。恢复前由冻结spec独立派生REC authority，原_resume验证500/1000与barrier；完整零步FUNC目录移入恢复attempt保留，原REC所有字节不变。

最新训练设置下FUNC测速23.9649秒/有效更新，两组剩余更新部分约13.31小时，尚不包含初始化、VAL、checkpoint、评估和回放，不能当总剩余时间承诺。

### 历史执行记录（下述运行中状态已过时）
23:01最新覆盖：旧chain-r1退出1，运行4692.95秒；REC终点检查点SHA `10967713eef97ce1521c78822e947d9aec36046da32a58ae91a236f564a07d2d`，远端CPU检查点核验回执SHA `fb32a6501b2a4579aac7093445e35be5b119cd4c144ec82a1e2d0c64fb1bf1fa`。核验范围为已保存绑定、两份payload、receipt链、模型历史barrier和last-progress；恢复前还需和独立冻结authority对照。FUNC在第一training_loss内、反传和optimizer之前失败，没有FUNC checkpoint或成功更新，故不重训REC。

补充后端资格任务 `LatentAtlas-REG1-Pilot-BackendQualification-r1` 于22:59:04启动，23:01模型加载中。外部启动器在Python前设置 `CUBLAS_WORKSPACE_CONFIG=:4096:8`，在runtime前设置冻结训练内核原有deterministic与TF32开关，调用未修改的v2资格入口，重新实际验证完整parity、8组缓存等价和固定短测速。配置SHA `1c255d417d9129ed9dbf898c3d955132f684e7cddd652dfc2c5f037827f169cd`。独立审查和远端CPU语法/绑定预检通过，实际GPU资格尚未完成；不修改已冻结科学参数、旧失败或旧资格绑定。

20:53现场：同一chain与fits进程仍在运行、无退出标记；新进程legacy与t=.4调用计数已记录，当前parity回执SHA `e5f4847901492c4d5531b1aa9d8ff1932c9468cf603e12e7a5e0fc19d243e11c`，首组REC的fit-bindings已发布，尚无checkpoint和精确更新计数。不以单次GPU利用率推断持续吞吐。只读代码检查另外记录了训练内核与测速入口的deterministic/TF32显式设置差异；当前没有对应运行错误，保持现有进程，若后续实际失败再保存证据并做工程恢复。

20:32执行状态：冻结spec SHA `09c649688ab2981949b3816d8901a5d44b5fb44e64d9afc5491f3ebaf65ce532`，不可变代码b24aef0，链配置SHA `0bbcc3a91f2f033e5c351ce7f64367caaf3c61df418dd9b4e29252af98db98eb`。唯一任务 `LatentAtlas-REG1-Pilot-Chain-r1` 已运行，phase fits、无退出；尚未看到实际更新，不能称训练完成。下文旧DRAFT或尚未启动描述只保留为历史状态。

20:28最新覆盖：r2实际8组等价检查全部完成；REC/FUNC分别10 warmup+50 measured、有效batch32，当前进程真实legacy+t04 parity通过，七模型状态不变。独立远端CPU核验256 payload和435 nested producer bindings及输出链通过。summary SHA `16de3666a4df7611419b9ece22cbea693ab8fd5de84a025569df7384d5748ef5`，独立回执SHA `f589ddbaf3026b597bfceeb00463872a343b80c8b06b423201a3f61fa2b53902`。这是工程资格，不是配准或Reward复用结果；旧r1失败不改写。

实际缓存路径REC每更新3.8349秒，FUNC19.5137秒；本次三组1000步仅更新部分估42862.28秒，即约11.91小时。结合尚未实测的正式VAL、评估和回放，用户沟通采用18–24小时的暂定安排，非保证完成时间；须按实际训练吞吐更新。不能拿不同时间的REC测速比较声称统一加速倍数。

最新工程状态：r2部署版本2d8fe51与已批准HEAD b24aef0的生产代码字节相同；配置SHA `fbac9ee773ca7f5f492695c3ab072c5faeb9d5c9c77802005708ca3e40545138`。任务 `LatentAtlas-REG1-Pilot-CachedEngineering-r2` 独占运行，尚无实际成功回执或新测速。三组训练、固定样本评估、两次独立CPU回放的代码与控制流程已完成独立审查；完整pilot spec仍待实际r2成功后绑定冻结。以下组件和失败记录作为历史保留。

小实验当前只完成组件验证：缓存目标14focused/156回归、训练内核16、入口18、七模型guard13、源行导出10、portable证据41项远端CPU测试。独立审查已关闭缓存入口的实际代码路径绑定缺口；三fit入口的工程凭证与嵌套缓存复核缺口已由d985291修复，38项CPU测试及独立复审通过。实际cached loss/gradient已尝试并在梯度逐位比较处失败；新测速及3fit尚未执行。独立工程入口d882dfd实际运行后在首例梯度逐位比较处停止（exit1），配置SHA3a5122a62334e195dd202a391eb8f4c0187922e82a5ef2f573f5a436b3341e67；没有正式训练。

静态阅读官方代码定位U_FUNC候选：`runtime.model.reward_head.agg_visual`输出（reward_head.py:282），作为visual_out交给attn1（:320）。处于layer FiLM/projection/fusion之后、cross-attention及其RMSNorm之前；来源接口声明[B,N,width]，真实benchmark已验证[1,1200,1536] BF16、attn1实际消费该tensor、score exact invariance和projector非零有限梯度。无需凭记忆退回raw H4/H8/H12；fallback尚未选用。

组件证据：合同独立原文数值与真实草案校验58 passed（8.61s）；缓存修正producer provenance与新进程parity分离、实际BF16/eval/frozen/device检查、禁止CPU测试通道进入CUDA后23 passed（5.56s）；算力准入修正临时计算图驻留与OOM/完整性失败优先级后17 passed（1.75s）。这些是远端合成/组件检查，不能替代真实模型准入。

资产证据：原r1下载失败已保留；r2恢复任务已完成，Anchor资格回执已校验回传。FLUX config已验证，权重传输由远端offset与独占锁控制；较大数据块曾超时，缩为64KiB并在每次不确定写入后重新查询offset。所有新数据下载仍在远端；本机仅传既有合法VAE文件。

## Conclusion

仅文档归档，本次未重验原数据、模型或所有终点；原文的数学例/工程检查/科学结果需分别阅读。

源域qualification和SHIFT0诊断均已完成；representation/interface registration与target Reward reuse仍无结果。源码定位、资产存在、动态FUNC接口、GPU成本和科学结论必须分开。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

检查唯一FUNCRecovery-r1的进程、调用计数、checkpoint和退出状态，不读取中间Accuracy、不重复启动。完成时独立验证三组terminal记录与各自VAL选择、skipped_completed_fits=1、原REC逐文件SHA保持及当前进程资格；不能仅凭exit0宣布完成。

随后使用原standalone evaluator及固定1008对/28组，评价保留原backend，不自动继承训练开关；两次独立远端CPU回放后，核验portable信任根并完成最终授权本地回放，封存交付后删除自动检查。不重启旧fresh-only链，不扩为原16组。

相关：`latentatlas`（原wiki关联）、[latentatlas-dina-src0-source-domain-parity](latentatlas-dina-src0-source-domain-parity.md)、[latentatlas-dina-shift0-dataset-runtime-localization](latentatlas-dina-shift0-dataset-runtime-localization.md)。

## Sources

- [来源快照](../source-snapshots/latentatlas-dina-reg1-functional-registration.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-dina-reg1-functional-registration.md`。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
