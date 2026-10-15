# Related Work 来源与核查记录

核查日期：2026-10-15。规范综述入口只有 [docs/related_work.md](../related_work.md)，文献键见 [references.bib](../references.bib)。本文件记录出处与证据边界，不创建重复论文页。

## 1. 原文实际阅读范围

六篇重点论文均核读了原文的方法、实验及与判断直接相关的附录，而非仅使用 Abstract。下列“未研究某问题”限定为这些已读章节，不是穷尽检索或无前作证明。

| 文献 / 版本 | 实际核查位置 | 支撑的分析及官方来源 |
| --- | --- | --- |
| P1，arXiv v1及出版社全文 | §4模型与映射、§5 support set、§6结果、§7 StyleGAN | 150图 support set、同图编码/回归、重建范围限制；[arXiv全文](https://arxiv.org/html/2207.06812)、[期刊全文](https://link.springer.com/article/10.1007/s00521-022-07890-2) |
| P2，v1 | §3.1–3.2、§4、A.4–A.5 | 模型/DM表示、9000训练与100 holdout、ridge、重建及probe指标、失败；[全文](https://arxiv.org/html/2407.13449v1) |
| P3，v3 | §3、§4 self-stitch、§5.1–5.4、Appendix C | 冻结权限、层位置、FFM/TLT、linear/MLP/LoRA、分类/分割；[全文](https://arxiv.org/html/2603.12433v3)、[CVPR登记](https://openaccess.thecvf.com/content/CVPR2026/html/Mai_Revisiting_Model_Stitching_In_the_Foundation_Model_Era_CVPR_2026_paper.html) |
| P4，v1 | §3.2、§4.1、§5、A.4、C.1、D.1、E.1 | expected reward与soft value区别、层搜索、学生后缀微调、VAE noisy baseline、各任务指标；[全文](https://arxiv.org/html/2605.19804v1) |
| P5，指定v2 | §2–4、§5–6、S2、S6.1、S9 | 独立Gaussian/已知协方差假设、RKHS估计、分布界、Tweedie/conditional解释限制及未知方差；[全文](https://arxiv.org/html/2501.00212v2) |
| P6，v2及正式会议登记 | §4.1–4.3、§5、B.2、C.3 | noisy网络、clean评分噪声封装、训练/LoRA与跨共享空间边界；[全文](https://arxiv.org/html/2602.11146v2)、[PMLR](https://proceedings.mlr.press/v306/liu26fh.html) |

DC-AE保留既有组件分析，本轮复核其[arXiv作者、题名和ICLR 2025标注](https://arxiv.org/abs/2410.10733)，未将其列为六篇深读对象或新增实验。

## 2. 书目信息与版本差异

- **P1年份：**[出版社](https://link.springer.com/article/10.1007/s00521-022-07890-2)与[Crossref DOI元数据](https://api.crossref.org/works/10.1007/s00521-022-07890-2)均确认在线2022-10-07、正式卷35(4)为2023-02、页3155–3172。BibTeX按期刊卷期写2023，备注在线2022；不按DOI中的2022猜卷期年。
- **P2题名：**[arXiv登记](https://arxiv.org/abs/2407.13449)为 *Exploring Representational Similarities Between Latent Spaces of Generative Image Models*，v1全文标题为 *Investigating Representational Similarities in Generative Image Models*。同一ID仅一个条目；引用用登记标题，保留异名备注。全文中的ICML关键词不作为会议接收证据。
- **P3会议：**CVPR正式页面的题名、9位作者、会议及页41342–41351已直接读取HTML元标签核对。浏览器抓取曾403，随后只读HTTP取得200；Method分析采用标明的arXiv v3，未声称正式PDF与v3逐字相同。
- **P4出处：**核对11位作者、2026-05-19的v1及官方实现归属。未发现并确认正式会议登记，因此只写预印本，不由代码或知名作者推定会议。
- **P5年份：**ID虽为2501，首版登记日期是2024-12-31，指定v2是2026-07-10。BibTeX用被阅读版本2026并注明首版日期；不静默写成已核实的2025期刊文献。
- **P6姓名：**PMLR页面/自动BibTeX将第三位作者显示为“Zhi Yida / Yida, Zhi”，而[arXiv v2作者元数据与正文](https://arxiv.org/abs/2602.11146v2)、[作者官方README引用](https://github.com/HKUST-C4G/diffusion-rm/blob/5a5a025e3ed090c86e96af0d924153569e2cace8/README.md#-citation)为“Yida Zhi / Zhi, Yida”。本仓采用后者的姓名顺序；其余完整11人顺序逐项核对，会议/页码采用正式PMLR，保留此差异说明。
- **DC-AE：**9位作者逐项核对，2024预印本与ICLR 2025出处分开，不创建第二个DC-AE条目。

## 3. 官方实现的静态核查

只读取公开代码/文档，没有执行、安装其依赖或下载权重。提交号固定本次所读版本，不能把当前仓库代码默认配置直接当论文实验配置。

<a id="stitchvm"></a>
### StitchVM

官方仓库所读提交：`7d4b3103d08acd43102ef6a84e1ae2c70e0f700b`。

- [Stage 2文档](https://github.com/prs-eth/StitchVM/blob/7d4b3103d08acd43102ef6a84e1ae2c70e0f700b/docs/STAGE2_VALUE_MODEL_DISTILLATION.md)明确区分 trainable adapter / residual / reward suffix 与 frozen VAE / DiT prefix / full reward teacher / aesthetic MLP。
- 同页明确当前多分辨率训练配方与论文不同。因此综述中的论文训练权限与数据以§4.1、§5.1、附录D.1为准；当前代码只作可定位的实现旁证。
- 主文Eq.(8)的MSE回归最优解是 conditional expected terminal reward；与§3.2的log-expected-exp soft value并非严格相同，A.4作近似关系分析。不能把它写成已精确恢复任意生成器的无偏soft value。
- 附录D.1已包含 SD3/FLUX noisy VAE latent直接拼接的baseline。准确差别是接入位置、监督与冻结权限，不是“它没有研究异构VAE或noisy输入”。

### DiNa

官方仓库所读提交：`5a5a025e3ed090c86e96af0d924153569e2cace8`。

- [inference.py](https://github.com/HKUST-C4G/diffusion-rm/blob/5a5a025e3ed090c86e96af0d924153569e2cace8/diffusion_rm/infer/inference.py#L104)：`reward(text_conds, latents, u=0.1)`，按scheduler就近取得sigma/timestep，在`add_noise`启用时以`(1-sigma)*latents+sigma*noise`构造输入。这个默认0.1与论文§5.2推荐0.4不应混写；本项目原reference合同也必须另保留。
- [sd3_rm.py](https://github.com/HKUST-C4G/diffusion-rm/blob/5a5a025e3ed090c86e96af0d924153569e2cace8/diffusion_rm/models/sd3_rm.py#L309)：底层`forward`直接消费`latents`与`timesteps`和文本特征，不能把clean封装与底层输入语义等同。
- 附录C.3在不同骨干上实例化DiNa的实验不是同一个checkpoint跨所有VAE；共享latent的SD3.5-M→L证据也不是异构VAE通用保证。

<a id="internal-evidence"></a>
## 4. LatentAtlas 既有证据定位

本仓10月10日已归档的报告继续保留原位置。10月15日新增研究阶段的原件尚未完整导入本仓；这里仅为文献分析记录已读原件和指纹，**不写成仓内可下载的完整实验交付**。下列路径以维护者的`科研与学习/`知识库根目录为起点，是工件定位文字，不是假装能在GitHub打开的相对链接。导师需要原件时可向维护者YEGRX索取；不以本轮文档校验代替原科学验收。

| 原件 | SHA256（2026-10-15读回） | 支撑的综述内容 |
| --- | --- | --- |
| `wiki/experiments/latentatlas-cross-encoder-reward-consistency-dev28.md` | `432561c8357b505cc59a9b2d9e3519af133b70c98fa91f5999c2f0603e42e1c2` | DEV28范围、独立新组NOT_RUN及校准信息限制 |
| `raw/projects/latentatlas/r17-cross-encoder-consistency-20261014/dev28-analysis-r1/result.json` | `77993bd7ec12335d1056899db92b1aaf605424b637626c9101f7b0c203022e80` | FF/FC/CF/CC、3999分母、3.5696pp额外失配、offset/affine诊断 |
| `wiki/experiments/latentatlas-noisy-anchor-reuse-minimal-pilot.md` | `10bf04e5a7e0f647474a2d0e4ac989f8cc63c02faabfa57c1f24f21496ea4685` | A/B18图72对与C两prompt四图的当前完成状态 |
| `wiki/deliverables/latentatlas-noisy-anchor-reuse-minimal-pilot-20261015-continuation-r2/FINAL_PILOT_DECISION.md` | `2657d95259df75b19e3c34c13e9dce48091d68c6189a007de9926e04c9ee0373` | 两档67/72、tie变化、原Clean反序、真实trajectory范围与失败边界 |

DEV中`d`表示Native-tie排除后的失配率，`Delta=(dFC+dCF-dFF-dCC)/2`，单位pp。人工加噪与真实trajectory的source sigma不等于后续DiNa reference noise；18图Pilot只使用stream0。独立新组校准/确认未做，不能把两折开发诊断称为新组认证。C的两prompt、两seed不是随机代表性确认集，67/72也不是人类偏好准确率。

## 5. PDF、目录与检查范围

- 本仓没有论文PDF归档惯例，本轮不保存/镜像PDF，仅提供出版社、会议、arXiv官方可访问入口。公开可读或代码有许可证不自动赋予所有版本论文再分发权；没有逐份完成PDF许可审核，不擅自扩建镜像目录。
- 不重复创建顶层`related_work/`或`papers/`，沿用既有`docs/related_work.md`。`docs/related_work/`只放本来源审计。
- 变更允许集合：`README.md`、`docs/related_work.md`、`docs/references.bib`、本文件。未修改实验代码、配置、权重、结果或历史记录。
- 检查对象是引用元数据、BibTeX语法/唯一性、Markdown文件与锚点、官方URL访问及既有CPU文档完整性；不构成新的模型评分、论文实验复现或科研独立确认。
