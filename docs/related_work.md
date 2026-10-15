# Related Work / 相关文献与科研分析

核查日期：2026-10-15。沿用本仓既有入口；本轮重点整理六篇文献，保留原有 DC-AE 组件条目，共七篇、每篇一个规范入口。[BibTeX](references.bib) · [原文核查、版本差异与内部证据定位](related_work/source_audit.md)。本页是文献分析，不执行或改写实验，也不证明研究问题已无相关前作。

## 阅读导航

| 分类 | 文献 | 年份 / 版本与出处 | 对 LatentAtlas 最直接的影响 |
| --- | --- | --- | --- |
| A 跨潜空间映射 | [P1 Comparing the latent space of generative models](#p1) | 2022预印本 / 2023期刊卷期 | 小型 support set + 线性映射已有先例 |
| A 生成模型 Stitching | [P2 All Roads Lead to Rome?](#p2) | 2024，arXiv v1 | 冻结生成模型间线性拼接；也研究加噪图像表示 |
| A 基础模型 Stitching | [P3 Revisiting Model Stitching](#p3) | CVPR 2026；核读 arXiv v3 | 冻结两端、功能评价及输出特征匹配已有系统研究 |
| B Noisy latent Reward | [P4 StitchVM](#p4) | 2026，arXiv v1 | noisy-latent stitching 已有直接前作；含不同 VAE 接入对照 |
| C Noisy-to-clean 理论 | [P5 RKHS measurement-error diffusion](#p5) | v1 2024-12-31；核读 v2 2026-07-10 | 分布恢复与条件均值不等于逐样本或 Reward 恢复 |
| D 下游技术基础 | [P6 DiNa-LRM](#p6) | ICML 2026，PMLR 306 | 原生 noisy Reward 与 clean 评分封装须区分 |
| 已有组件（保留） | [DC-AE](#dc-ae) | ICLR 2025 | 高压缩重建不保证冻结 Reward 兼容 |

## A. 跨潜空间映射与 Model Stitching

<a id="p1"></a>
### P1. Comparing the latent space of generative models

**Andrea Asperti, Valerio Tonelli.** *Neural Computing and Applications* 35(4):3155–3172，2023；在线发表2022-10-07。arXiv:2207.06812，2022。引用键：`asperti2023comparing`。

[arXiv](https://arxiv.org/abs/2207.06812) · [期刊 DOI](https://doi.org/10.1007/s00521-022-07890-2) · [出版社全文](https://link.springer.com/article/10.1007/s00521-022-07890-2)

- **问题与方法：**比较同类及异类生成模型的潜空间。固定已训练 VAE、SVAE、GAN、StyleGAN，用同图编码（GAN 需 inversion）构造对应点，以线性回归和 MSE 学习 relocation；CelebA 示例使用150张代表性 support images。
- **实验证据：**§4–7比较映射后重建、误差及语义外观；信息保留受原编码器损失和 StyleGAN 可生成范围限制，并非任意模型皆无损可逆。
- **与我们关系：**“少量同图 Clean Anchor 学习简单跨潜空间映射”与它高度重合，不能单独作为原创贡献。可借鉴 support coverage 与线性基线，但其重建证据不直接保证固定 DiNa 的分数或偏好排序。

<a id="p2"></a>
### P2. All Roads Lead to Rome? Exploring Representational Similarities Between Latent Spaces of Generative Image Models

**Charumathi Badrinath, Usha Bhalla, Alex Oesterling, Suraj Srinivas, Himabindu Lakkaraju.** arXiv:2407.13449v1，2024；未确认正式会议出处。引用键：`badrinath2024roads`。

[arXiv 登记](https://arxiv.org/abs/2407.13449) · [全文](https://arxiv.org/html/2407.13449v1)。全文页题名用 *Investigating Representational Similarities in Generative Image Models*，是同一 ID 的题名差异，不另建条目。

- **问题与方法：**在 CelebA 的 VAE、VQ-VAE、GAN、Glow NF、DM 间固定模型、拟合线性或 ridge 映射。通常用9000张同图配对编码；GAN 用生成图及已知 style latent。DM 表示是50步 DDIM 前向加噪图像，并非现代异构 VAE 的真实采样轨迹。
- **实验证据：**§3–4、附录A.4–A.5报告 latent MSE、像素 RMSE、LPIPS、FID及属性 probe accuracy/agreement；较好表示可拼接，VAE/DM 源也存在明显失败。
- **与我们关系：**提供生成模型线性 stitching 和语义保持基线，不能把这一框架称为首次提出；其配对预算并非我们的少量 Anchor，且未直接检验完整冻结 DiNa 的 Reward 功能复用。

<a id="p3"></a>
### P3. Revisiting Model Stitching In the Foundation Model Era

**Zheda Mai, Ke Zhang, Fu-En Wang, Zixiao Ken Wang, Albert Y. C. Chen, Lu Xia, Min Sun, Wei-Lun Chao, Cheng-Hao Kuo.** CVPR 2026，pp.41342–41351；arXiv:2603.12433v3。引用键：`mai2026revisiting`。

[CVPR 正式页](https://openaccess.thecvf.com/content/CVPR2026/html/Mai_Revisiting_Model_Stitching_In_the_Foundation_Model_Era_CVPR_2026_paper.html) · [arXiv](https://arxiv.org/abs/2603.12433) · [核读全文 v3](https://arxiv.org/html/2603.12433v3)

- **问题与方法：**异构 CLIP、DINOv2/v3、SigLIP2 的功能兼容性。冻结 source 前缀与 target 后缀，比较2/6/10/14/18/22层及 linear、MLP、LoRA stitch；比较局部特征匹配、Final Feature Matching（FFM）和 FFM→Task Loss Training。
- **实验证据：**§3–5以分类 accuracy、ADE20K mIoU及 self-stitch 控制评价，显示局部特征误差小不保证最终功能；MLP、FFM及两阶段训练在所测任务更有效，也存在弱源限制。
- **与我们关系：**“冻结两端，只训练 Projector，并检验功能兼容”已有强先例；须比较匹配监督预算的 stitching/FFM及 self-stitch，不能只比较无注册或置换。FFM读取冻结目标网络，不等于只用 clean 坐标 Anchor 的信息合同。

## B. Noisy Latent 与 Reward 接入

<a id="p4"></a>
### P4. Stitched Value Model for Diffusion Alignment（StitchVM）

**Hyojun Go, Hyungjin Chung, Prune Truong, Goutam Bhat, Li Mi, Zhaochong An, Zixiang Zhao, Dominik Narnhofer, Serge Belongie, Federico Tombari, Konrad Schindler.** arXiv:2605.19804v1，2026；未确认正式会议出处。引用键：`go2026stitched`。

[arXiv](https://arxiv.org/abs/2605.19804) · [全文](https://arxiv.org/html/2605.19804v1) · [官方代码](https://github.com/prs-eth/StitchVM)

**核心机制。**§4.1用截断扩散骨干处理 noisy latent，经 stitch adapter 接入截断图像 Reward 后缀。先用200图 probe、闭式最小二乘搜索层对，再训练1×1 affine + resize + residual MLP及 Reward 后缀。原完整 Reward 是冻结的教师，**被拼接的学生后缀会更新**。主文将目标写成对 clean Reward 的回归；附录D.1实际对 CLIP/DFN-CLIP/HPSv2 蒸馏图像 token 与 embedding，美学模型另有 score loss。无新增人类标签不等于没有 Reward 教师信息。

| 部件 / 数据 | 论文中的权限与作用 |
| --- | --- |
| SD3.5-M / SD3.5-L / FLUX.1-dev 扩散前缀、VAE | 冻结；扩散特征提供噪声感知能力 |
| Stitch adapter、学生 Reward 后缀 | 训练；不是完整原 Reward 权重不变 |
| 原完整 Reward 教师 / 文本编码器 / 美学评分 MLP | 教师冻结；该蒸馏阶段文本编码器不运行或更新；美学 MLP冻结 |
| AVA、HPDv2 无标签图像 | 论文训练5 epochs；200图仅用于层搜索，不是全部训练集 |

**实验与已有覆盖。**§5、附录D/E在不同噪声上报告 CLIP retrieval、HPSv2 preference accuracy、美学 SRCC，并检验 DPS、FK steering、DiffusionNFT 等生成对齐。它不仅涉及 SD3/FLUX 各自 VAE，还比较直接把其 **noisy VAE latent** 接到 Reward 后缀的 baseline；因此 noisy-latent stitching 本身已经是前作。跨骨干分别构造学生，不等于已证明用同一个完整冻结 DiNa、同一套 clean-only Anchors 即可跨异构 VAE。

**可研究区别，而非已证创新：**我们希望复用既有 clean Projector，不新增 noisy-state 接口训练，不在接口训练中读取 Reward 特征/分数，并保持完整 DiNa 权重不变。这是更严格的预算与冻结合同，尚未证明有效或新颖；源扩散 denoiser 的计算成本也必须计入。官方当前代码的多分辨率训练明确声明与论文配方不同，不能混写为论文复现。核查位置见[来源审计](related_work/source_audit.md#stitchvm)。

## C. Noisy-to-Clean 恢复理论

<a id="p5"></a>
### P5. Denoising Data with Measurement Error Using a Reproducing Kernel-based Diffusion Model

**Mingyang Yi, Marcos Matabuena, Zhiming Ma, Ruoyu Wang.** arXiv:2501.00212；v1为2024-12-31，本文核读 v2（2026-07-10），未确认正式发表出处。引用键：`yi2026denoising`。

[指定 v2](https://arxiv.org/abs/2501.00212v2) · [全文](https://arxiv.org/html/2501.00212v2)

- **问题与方法：**从受测量误差污染的数据恢复未知 clean 分布。主设定是独立、零均值、已知协方差 Gaussian error；§3构建 RKHS score estimator、正则化闭式解和反向 SDE。未知方差在补充S9另议。
- **实验证据：**§4在正则性、score 表示及采样条件下给分布 KL/TV 界；§5–6用模拟与血糖测量数据验证，不是高维 VAE 真实轨迹验证。界中的常数可能随维数恶化。
- **与我们关系：**可借鉴 score 去噪与误差分层，不能直接充当真实 diffusion 中间状态的 clean 恢复或 Reward 保真定理。补充S6.1也明确未完成完整 conditional posterior approximation 理论。

在上述加性 Gaussian 假设下，Tweedie 公式为

$$\mathbb E[X\mid Y=y]=y+\Sigma\nabla_y\log p_Y(y),\qquad Y=X+\epsilon.$$

它给出**条件均值**，不是该次生成对应的具体 clean 样本。反向采样的**边缘分布恢复**也不保证原样本身份；非线性 Reward 一般满足不了 $R(\mathbb E[X\mid Y])=\mathbb E[R(X)\mid Y]$。真实 prompt/CFG/数值积分轨迹及近似 velocity prediction，尚需另核条件和误差，不能直接套用测量模型。

## D. 冻结下游技术基础

<a id="p6"></a>
### P6. Beyond VLM-Based Rewards: Diffusion-Native Latent Reward Modeling（DiNa-LRM）

**Gongye Liu, Bo Yang, Yida Zhi, Zhizhou Zhong, Lei Ke, Didan Deng, Han Gao, Yongxiang Huang, Kaihao Zhang, Hongbo Fu, Wenhan Luo.** ICML 2026，PMLR 306:79354–79376；arXiv:2602.11146。引用键：`liu2026beyond`。这是已有条目的补充，不另建重复论文页。

[正式论文与会议信息](https://proceedings.mlr.press/v306/liu26fh.html) · [arXiv](https://arxiv.org/abs/2602.11146) · [核读全文 v2](https://arxiv.org/html/2602.11146v2) · [官方代码](https://github.com/HKUST-C4G/diffusion-rm)

**方法与训练。**§4的底层网络接收原生 noisy latent $z_t$、timestep $t$及文本条件 $c$；使用扩散多层视觉/文本特征、timestep FiLM、gated Q-Former 和 MLP。训练以 noisy preference pairs、noise-calibrated Thurstone likelihood/fidelity loss 监督；主实验采用 SD3.5-M、HPDv3偏好数据，比较 backbone LoRA 与冻结 backbone 的 Reward-head 训练。因此“我们冻结已训练 DiNa”是迁移实验合同，不能说原 DiNa 从未训练/微调。

**clean 接口不等于 clean 底层网络。**§4.3、§5.2由 clean 样本构造参考噪声输入，单噪声主文默认 $t=0.4$，也支持多时间特征 ensembling。官方 clean-latent `reward()` 封装可加噪后再调用显式 `latents, timesteps` 的底层网络；代码默认参数与论文推荐值还需区分。已经是 noisy 的 source state 不能不审查就再当 clean 传入，否则噪声及时间合同可能错位。

**结论与限制。**论文以多偏好 benchmark 和生成对齐验证 Reward；附录C.3明确，“多骨干可实例化该方法”不表示单个已训练 Reward 可任意跨不兼容 VAE，SD3.5-M→L迁移也是共享 latent 空间。我们因此研究在保持**同一个完整 DiNa**不变时的异构接口，但需要匹配 scaling/shift、packing、文本与 reference noise，并单独核验坐标、功能和混池评分。[既有来源资格记录](experiments/latentatlas-dina-src0-source-domain-parity.md)不是精确论文复现。

## 已有组件与交叉引用（保留）

<a id="dc-ae"></a>
### Deep Compression Autoencoder for Efficient High-Resolution Diffusion Models

Junyu Chen, Han Cai, Junsong Chen, Enze Xie, Shang Yang, Haotian Tang, Muyang Li, Yao Lu, Song Han；ICLR 2025，arXiv:2410.10733（2024首发）。引用键：`chen2025deep`。

DC-AE通过 residual autoencoding、解耦高分辨率适配提高空间压缩效率；高质量重建不自动证明其 latent 可由另一个冻结 Reward 正确读取。保留其原有目标编码器角色，不将本轮文献核对写成新模型运行。[论文](https://arxiv.org/abs/2410.10733) · [官方 DC-AE 文档](https://github.com/mit-han-lab/efficientvit/blob/master/applications/dc_ae/README.md) · [既有 Anchor 比较](experiments/latentatlas-dina-dcae-strong-anchor64-vs256-fixed2k-newgroups.md)。

FLUX、Cosmos、PickScore、HPSv3 的 checkpoint 与预处理仍以原报告为准：[FLUX机制与独立RGB读出](experiments/latentatlas-frozen-projector-mechanism-and-readout.md)、[Cosmos固定配方](experiments/latentatlas-dina-unseen-encoder-fixed-recipe-portability.md)、[HPSv3六臂](experiments/latentatlas-hpsv3-frozen-interface-reuse.md)。不额外扩展未核查的文献清单。

## Implications for LatentAtlas

### 1. Clean Anchor 为什么不足以单独支撑创新

P1已包含小 support set 的同图线性映射，P2扩展到多类生成模型，P3系统研究冻结网络的 stitching 与功能评价。因此 Clean Anchor → Projector → Frozen DiNa 具有工程与功能迁移价值，却不能只靠“跨 VAE 映射成功”“冻结模型只训练小接口”支撑顶会原创性。[原投稿证据记录](experiments/latentatlas-submission-evidence-20261009.md)中的缺口不能因补齐引用就视为解决。

比较时须区分 clean-coordinate-only、读取 Reward feature/score 的蒸馏、带任务标签训练及额外 source-denoiser 计算；不同信息量和成本不构成同预算优势。这里指出应比较的基线，不声称本轮已完成这些实验。

### 2. 已有结果到底支持到哪里

下表是**既有结果的文献讨论摘要**；10月15日两项来自已完成的本地报告，本轮只读核对，不重推模型、不重算统计。[完整来源、SHA和未入仓原件说明](related_work/source_audit.md#internal-evidence)。

| 层次 / 样本 | 已有观察 | 证据限制 |
| --- | --- | --- |
| Clean 接入，DEV28：28组、252图、1008对、4 reference streams | FLUX/FLUX Native agreement 91.6854%，Cosmos/Cosmos 93.4109% | 是已消费 DEV 的单路径功能保持，不是人类效用或跨源混池保证 |
| DEV28混合路径：3999个非Native-tie相关判断 | FC/CF agreement 88.9597%/88.9972%；额外失配 Delta=3.5696pp，95%CI [2.5487,4.6738]pp | 4032判断中排除33个Native tie；四流和同组相关，不能按3999独立样本解释 |
| 同一DEV两折14/14组 offset 校准 | Delta降至0.8252pp，削减76.88%；positive affine为0.8627pp | 消除大部分但不是全部失配；使用额外Reward信息，无正式校准CI；独立新组确认 NOT_RUN |
| 受控加噪 A/B Pilot：2个已消费组、18图、72对、stream0 | 原Clean及两个 source sigma 档均67/72 agreement；低档无排序变化，中档2个平局变化、无严格翻转 | 初步功能保持；不是等效证明、人类Accuracy或跨编码器混池评价；source sigma与DiNa reference noise分开 |
| 真实 FLUX.1-dev 轨迹 C Pilot：2个预定prompt×2seed，4图、8个轨迹点 | 茶壶同向；石桥Clean及两个noisy路径均与Native反向 | 一个prompt的Clean基线已反序；低档是最后Euler步，中档仅提前3步，不支持“真实Noisy-State迁移已成功” |

保留原 Q32 `LOCAL_METHOD_NUMERICALLY_UNQUALIFIED`、后续 `MAIN8_TRADEOFF_OR_DETERIORATION` 及 R18真实 `NO_GAIN`；新方向不改写它们，也不能把旧误差分析当作新方法成功。

### 3. 当前探索的问题与候选路线

> **Can a small set of Clean Anchors be reused for heterogeneous VAE noisy-state reward transfer?**
>
> 少量 Clean Anchor 能否复用于异构 VAE 真实 Noisy State 的冻结 Reward 接入？

```text
Source Noisy State
  → Source Clean Prediction
  → Existing Clean Anchor Projector
  → Canonical Latent
  → Frozen DiNa（单独固定 reference noise / timestep / text 合同）
```

这是**尚在探索的假设**。“先去噪再映射”是自然的已有技术组合，不直接构成新算法。P4已覆盖 noisy latent stitching，P5提供有条件的去噪工具，P6本身就是 noisy Reward；目前没有证明更窄的 clean-only Anchor 复用问题不存在前作。可能值得检验的是其明确预算下的适用与失败边界，而不是提前宣布研究空白。

后续问题应逐层区分：源 clean prediction 误差、Projector 响应、冻结 Reward 分数/排序保持、真实生成域与终态重编码差异，以及不同噪声阶段和异构路径间的共同标尺。**人工前向加噪不是原生生成轨迹；坐标对齐不意味着 Reward 保真；单路径准确不意味着混合路径排序可靠。**在真正未消费内容、非最后步轨迹与匹配简单基线上确认这些差别之前，不宣称统一无偏 value、新算法、生成加速或论文级独立确认。
