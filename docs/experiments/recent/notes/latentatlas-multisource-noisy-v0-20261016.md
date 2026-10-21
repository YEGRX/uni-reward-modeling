> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# LatentAtlas 多来源真实 Noisy V0 与终态选择

## 最新状态（2026-10-16）

**本轮V0闭环完成，非独立确认；未识别独特机制或明确的修复型V1。** 两源16条真实轨迹、48份当前状态、288个科学DiNa side、两方法72项选择与独立终态PickScore均完成，原文件已回收并核SHA。GPU阶段全部结束，后续文档/分析不需要服务器；服务器实际是否关机未由本页核实，若仍租用可关闭。

V0在两源各阶段的平均终态DiNa效用高于同池uniform，但普通ridge与V0在34/36个匹配决策上相同；两个差异重复同一个物理事件。所有mixed选择等于同方法/阶段固定FLUX选择，效用差0。PickScore不支持FLUX的平均选择增益，支持本轮SD15选择；不能因此认定某个评价器正确。

## 1. Date

2026-10-16。实验执行、原数组独立复算、完整成本核验完成。英文内部稿正文8页（含参考文献）、补充8页，已完成实质审查、修订、编译与逐页验收；状态为**DRAFT_COMPLETE / IDEA_VALIDATION_PARTIAL / SUBMISSION_NOT_READY**。当前结论见 `latentatlas-current-evidence-map`；写作边界见 `latentatlas-paper-framework`。

## 2. Purpose

历史Clean接入与四条FLUX轨迹不能回答跨生成器早期选择是否有用。本轮检验现有V0对两个非参考VAE生成器真实早/中/晚状态的合法评分，比较同pool均匀选择、固定单来源和普通空间共享映射。接口可执行、功能保真、终态效用与总成本分别判断，不预设共享几何或新算法成立。

## 3. Code Version / Commit

以原代码闭包和配置SHA为身份，旧失败不覆盖。SD15只复用已拥有模型资产，新建本项目4通道V0，不混入独立论文adapter或结论。

- FLUX SOURCE r2：`scripts/latentatlas-noisy-v0-20261016/r2/`，配置SHA `7ea322d97cdb15dc1a7e3a6683657fe3d52c1a506268facb09d81a374479b42e`。
- FLUX REWARD attempt1记录修复：配置 `45fdfbe356588088e2bc6b74e94fa22f7d4b24e5be432da4e9b2a11cb79b9131`，只改IO/部署血缘，随后加载期失败，0评分；不是V1。
- FLUX REWARD attempt2：配置 `771e0067950e25b3da0552e04cfefabb8ec93a118aa42052049597832988b821`，整体FAILED；已完成48prefix sides、12原选择、Native1，由恢复合同复用，不伪装整体完成。
- SD15训练：`scripts/latentatlas-sd15-v0-20261016/`，formal spec SHA `c46febc7e40ae853197945f62180b7aa5315f9118ff7ddf4659bc68631d271bc`。
- SD15 SOURCE配置 `453b7449d6d3330548bf5d05b218d1e728e2c81f8ef0fbc0e75348779e764003`；联合REWARD-r2配置 `ed0050522a3c740eb52546fdd3f6c7badb9a9ae1bd17dd9650a3db380e85f471` 实际COMPLETE，以独立账本完成其余240科学sides，包含两源终态。
- 普通基线：`scripts/latentatlas-noisy-spatial-baseline-20261016/`；独立分析：`scripts/latentatlas-noisy-v0-analysis-20261016/`，不import生产selector/analyze。72项合成测试与实际结果复算分别留证。

## 4. Dataset / Input

同4个固定DEV prompts，每源2个seed：FLUX.1-dev 8条、SD1.5 8条，共16轨迹、48prefix。参考为SD3.5。Cosmos当前已有的是encoder，不能算第二完整generator。两源均输出1024²以对齐参考128²网格；**SD15常用512训练配置与本轮1024部署有差异，不代表其标准/最佳配置性能**。两源质量分离较大，限制对细粒度跨来源共同标尺的检验。

新SD15训练沿用FIT64、VAL64、128同图RGB与参考T0缓存，不是新独立数据。4个DEV prompt是主要统计单位；phase、两噪声流、两个方法和重叠pool均重复同批候选，72决策不是72独立样本。保留确认prompt未运行，不能用换seed/fold制造fresh证据。

## 5. Parameters

FLUX每候选28个去噪根，SD15 PNDM名义28步实际29个UNet根（CFG batch2）；观察索引7/14/21不代表相同噪声或相同剩余成本。FLUX flow与SD15 epsilon分别按原参数化恢复当前clean估计；两源P入口BF16。SD15 baseline输入也先F32→BF16→精确FP32，与P实际输入law一致。冻结DiNa参考sigma=.4002932608127594、t=400.29327392578125，与源时间分开。

SD15 V0为4→64→64→16、38288参数、1000更新，effective batch32，原AdamW和schedule前1000步；固定final1000，VAL仅坐标诊断，不以Reward训练/选模。普通共享3×3 affine ridge同FIT64、每图等权、FIT-only标准化、lambda1e−3、intercept不惩罚，输出BF16。部署时预训练模型、P及ridge均固定。

## 6. Command

GPU执行只用封存controller/owner、全局互斥锁、前台连接、资源cap及原子调用账本。72项两方法/三pool选择先封存，随后读取当前终态。旧FLUX12份receipt保持原字节，scope只在分析内存补齐。独立CLI与SHA绑定入口：`scripts/latentatlas-noisy-v0-analysis-20261016/README.md`；本页不复制无SHA的裸GPU命令。

## 7. Results

### 训练与普通坐标基线

| 项目 | 实际执行 | 结果与范围 |
|---|---|---|
| SD15编码 | 128次VAE mode编码、1次加载 | BF16/raw；84.541s阶段墙时 |
| 技术训练 | 3更新、96训练前向及96反向图像单位、128VAL、2 parity前向 | 1次checkpoint load；72.356s |
| 正式训练 | fresh1000、32000训练前向及32000反向图像单位、192VAL、4 parity前向 | 2次checkpoint load；554.801s；VAL NMSE0/500/1000=2.853299/.275762/.253248，仅诊断 |
| FLUX ordinary ridge | FIT64一次、128次CPU线性评价 | VAL NMSE .1562862425，主控原数组复核通过 |
| SD15 ordinary ridge | FIT64一次、128次CPU线性评价 | VAL NMSE .3399357484，独立原数组验证通过 |

SD15固定checkpoint SHA `25188b4bd5055b96e63576566f689899fc193194b180688b4b334cdaa54a0792` 已回收。P_RELOAD账本角色实际是current/reloaded两实例parity forward：总6次前向与3次checkpoint加载分列，不混为加载次数。阶段墙时含CPU/加载/I/O，不是纯GPU kernel时间；未记录逐step training loss，不能补称存在。 三个外层监督窗口合计715.841s，取代而非叠加711.699s worker合计；差4.142s属于worker外监督开销。

### 真实终态选择

288科学side=192 prefix + 96三路terminal；48个旧FLUX prefix side合法复用而未重复评分。72选择=2方法×3phase×3pool×4prompt。主控与独立分析均从原scores/receipts重建。

| 方法 | phase索引 | FLUX gain | SD15 gain | mixed gain | mixed−固定FLUX |
|---|---:|---:|---:|---:|---:|
| V0 | 7 | .157227 | .597656 | 3.038574 | 0 |
| V0 | 14 | .096680 | .597656 | 2.978027 | 0 |
| V0 | 21 | .157227 | .597656 | 3.038574 | 0 |
| ordinary ridge | 7 | .086914 | .597656 | 2.968262 | 0 |
| ordinary ridge | 14 | .096680 | .597656 | 2.978027 | 0 |
| ordinary ridge | 21 | .157227 | .597656 | 3.038574 | 0 |

Gain是被选候选两流terminal Native DiNa均值减同有限池uniform精确期望。mixed四候选、单源两候选，成本和随机参照不同。V0/ridge相同34/36；两个差异是dev-04早期FLUX选择在单源与mixed中重复体现，V0该物理事件DiNa效用高.28125，四prompt均值高.0703125。全部24项mixed决策都选FLUX且等于相应固定FLUX策略，新增SD15前缀未带来观察效用。V0选择流分歧0；ridge早期FLUX/mixed各1，重复同一prompt；该物理事件ridge的两个流分歧、均值恰为精确tie，选择按事前固定candidate ID规则；不得包装为两个独立V0胜利。

### 外部质量代理与终态保真

固定选择后，PickScore对16终态图评分，未改变P、候选、phase或选择。V0 FLUX三时点gain为−.116228/−.001175/−.116228，均不正；SD15三时点均+.431391。ridge FLUX为+.004790/−.001175/−.116228，唯一早期DiNa优势在该代理下反向。DiNa/PickScore对FLUX4个物理候选对有3对反序，SD15 4对一致。PickScore是外部学习代理，不是human truth，也不是统计独立确认。

两条P终态路线对Native在四mixed pool的24个平均分pair signs均保留，但逐draw RMSE仍为FLUX1.882/1.909、SD15 .713/.695。标量误差大与本样本排序保留可并存；大来源差距、margin和抵消都是普通解释，未识别特殊几何。终态对照不能单独识别中间clean估计误差。

### 执行失败与完整成本（不删除、不算科学阴性）

- FLUX r1最初后台尝试CPU退出，无模型调用；前台因2700s预算低估停止，science9尝试（8完成+1pending）、tech1、text8、generation pending1，732.165s owner，无完整候选。退出根因未确认。
- FLUX r2 SOURCE完成224science+1tech FLUX、40science+1tech P、8decode/8encode，owner4524.275s；worker4051.856s嵌套，不相加。SD15 SOURCE完成232 UNet根/464 CFG单位、P40、decode8/encode8、text4根/8单位，owner241.542s。两源真实raw估计转换已独立逐位核验。
- selector清单包含空manifest自身的IO bug经CPU红绿修复，SOURCE不变。45fdf REWARD加载期因监督25s查询超时受控停止，science/tech/text/Native全0，但owner247.244918s保留，峰值unknown；不能用0前向写0成本。
- 771 REWARD完成48prefix/12choices/Native1，因TEXT15预计算预算停在terminal science0；整体FAILED，owner403.963101s。jointed005在独立新账本复用原完成分支，补240science/Native15（SD8+FLUX7），owner565.234030s；不把partial伪装完整成功。
- CPU prefix r1已算affine1后非连续张量保存失败，完成0/保存0、supervisor51.901327s；只修contiguous、不改数值的r2完成48次、24.896491s。累计真实affine49。普通affine属于模型操作，准确说0预训练模型调用，不说所有model0。
- PickScore原SQLite另25 roots：load1、science image16/text4、tech image2/text2，owner89.419443s；独立附表，不计DiNa前向。

四原账本939 roots与288科学sides逐项join；invocations、CFG image units、backward、optimizer、加载、CPU线性应用分别记单位，不合成时间。owner monotonic不强制等于epoch差，不叠加child/worker/transport；未归属余时不能全叫加载。所有轨迹已完整生成，未执行真实提前停止/恢复policy，因此没有实测加速。 费用导出中的legacy source_id是ledger owner身份，联合账本下FLUX操作须按role/metadata归属。首次detached CPU preflight无模型调用但可靠墙时未知，不补0；已记录owner窗口不是完整租赁时长。

## 8. Analysis

本轮支持受限功能可行性，不支持REC独有机制、通用Noisy迁移、来源互补或人类质量收益。强普通基线覆盖几乎全部选择，mixed增益由避免本池低分来源解释；FLUX两评价端点错配未解决。四DEV阳性不是独立确认，不能追分调参后再称验证。

理想独立terminal评价噪声下，合法选择减uniform在固定池条件下无max选大偏差；有限流oracle最大值有向上偏差，regret不是总体oracle无偏估计。实际分域PRNG哈希只是可复现合同，不是概率独立证明。当前clean估计与一次实际终态比较不能独立认证中间时点跨VAE保真。

## 9. Problems

SD15 1024部署差异、来源质量分离、固定4 DEV、单DiNa与外部代理端点冲突限制解释。完整16图contact sheet显示SD15有重复或碎片结构；固定pipeline/CFG/scheduler/scaling核查未定位直接实现错配，也未确定劣化根因。没有据此自动改dtype、源配置、P或预算。V0/ridge训练曝光和优化成本不同，须保留。

## 10. Next Steps

本轮V0闭环收口，不追分调参，不自动扩模型/样本或构造V1。优先澄清原创科学增量与DiNa/质量端点关系；若继续部署验证，先明确匹配源设置、目标端点与同信息/成本强对照，冻结方案后再用未消费prompt独立确认。当前没有已识别的修复型V1。

内部稿已完成审查修订与交付验收，状态为**DRAFT_COMPLETE / IDEA_VALIDATION_PARTIAL / SUBMISSION_NOT_READY**；投稿与根本应用目标改变由用户决定。后续本地分析/写作0模型、0网络、0GPU。

## 11. Sources

证据直达：独立科学原数组与72选择（原件定位：`docs/latentatlas-noisy-v0-2026-10-16/analysis/actual-science-r1/analysis.json`）；最终含QUALITY完整费用（原件定位：`docs/latentatlas-noisy-v0-2026-10-16/analysis/actual-cost-with-quality-r1/cost-accounting.json`）；主控原分数精确选择复算（原件定位：`docs/latentatlas-noisy-v0-2026-10-16/analysis/primary-check-selection.json`）；主控16原PickScore复算（原件定位：`docs/latentatlas-noisy-v0-2026-10-16/analysis/primary-check-quality.json`）；当前内部稿正文（原件定位：`deliverables/latentatlas-cvpr-internal-2026-10-16/main.tex`）。

- `docs/latentatlas-noisy-v0-2026-10-16/analysis-contract.md`：事前分析合同。
- `docs/latentatlas-noisy-v0-2026-10-16/analysis/actual-science-r1/{analysis.json,identity-audit.json,input-sha256.json,complete.json}`：原288sides、72choices、tensor/seed/owner绑定与18/36结果。
- `docs/latentatlas-noisy-v0-2026-10-16/analysis/actual-cost-with-quality-r1/{cost-accounting.json,input-sha256.json,complete.json}`：四ledger、失败、训练/CPU及QUALITY原账本费用。
- `docs/latentatlas-noisy-v0-2026-10-16/analysis/primary-check-selection.json`、`primary-check-quality.json`、`primary-check-flux-conversion.json`、`primary-check-sd15-conversion.json`：主控独立原分数/数组复核。
- `raw/projects/latentatlas/noisy-v0-flux-dev-20261016-r2/remote-run/`；`docs/latentatlas-noisy-v0-2026-10-16/sd15-noisy/approved-source-execution-r1/remote-run/`、`approved-joint-reward-r2/remote-run/`；`independent-quality/approved-quality-r3/remote-run/`：完整回收原件。
- `docs/latentatlas-noisy-v0-2026-10-16/sd15/execution-report.md`、`baseline/prefix-application-execution-report.md`：训练和普通基线执行身份；旧失败原件保留。
- `deliverables/latentatlas-cvpr-internal-2026-10-16/{main.tex,supplement.tex}`：完成的内部稿与完整证明，实质修订及8+8页验收通过，未达到投稿就绪。
- `latentatlas-current-evidence-map`、`latentatlas-theory-map`、`latentatlas-research-decisions`、`latentatlas-paper-framework`、`latentatlas`、[latentatlas-r17-real-decision-audit-20261016](latentatlas-r17-real-decision-audit-20261016.md)。
