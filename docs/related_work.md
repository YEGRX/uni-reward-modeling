# Related Work / 相关工作与组件

本页先登记与已完成实验直接相关的官方来源。它不是完整文献综述；资源关系不等同于预算匹配比较，模型的预训练数据重叠尚未排除。

## Beyond VLM-Based Rewards: Diffusion-Native Latent Reward Modeling

- Venue: arXiv:2602.11146；正式会议接收情况未在本次确认。
- Key idea: 在带噪扩散状态中进行潜空间偏好奖励建模（DiNa-LRM）。
- Limitation relevant here: 本项目核对其冻结读出对不同编码器接口的适用性；不能用本项目某个外部面板结果否定原工作的全部设定。
- Relation: LatentAtlas的主要冻结读出及Native参考。SRC0只有来源域操作性资格，不是精确论文复现。
- Sources: [论文](https://arxiv.org/abs/2602.11146)、[官方实现](https://github.com/HKUST-C4G/diffusion-rm)、[SRC0记录](experiments/latentatlas-dina-src0-source-domain-parity.md)。

## Deep Compression Autoencoder for Efficient High-Resolution Diffusion Models

- Venue: ICLR 2025（官方仓库标记）。
- Key idea: 高空间压缩的连续自编码器（DC-AE）。
- Limitation relevant here: 图像重建能力不自动证明其潜变量可直接接入另一个冻结奖励读出。
- Relation: 本项目的目标编码器之一；弱接口、强接口、Anchor数量及固定候选的实验分别记录。
- Sources: [论文](https://arxiv.org/abs/2410.10733)、[官方DC-AE说明](https://github.com/mit-han-lab/efficientvit/blob/master/applications/dc_ae/README.md)、[官方仓库](https://github.com/mit-han-lab/efficientvit)、[Anchor比较](experiments/latentatlas-dina-dcae-strong-anchor64-vs256-fixed2k-newgroups.md)。

## 独立RGB读出与其他目标编码器

FLUX、Cosmos、PickScore与HPSv3在本项目中的具体checkpoint、预处理与角色以实验报告为准。本次没有重新下载、运行或全面核对其最新公开版本，因而不追加未核实的论文元信息。

- [FLUX机制与PickScore读出](experiments/latentatlas-frozen-projector-mechanism-and-readout.md)。
- [Cosmos固定配方](experiments/latentatlas-dina-unseen-encoder-fixed-recipe-portability.md)。
- [HPSv3修复后六臂](experiments/latentatlas-hpsv3-frozen-interface-reuse.md)：decoder介导复用，两REC结论未确立。

## 尚需比较的工作

同信息量、同配对Anchor和同预算的简单坐标/仿射/岭回归或低秩baseline，以及独立确认，仍是论证缺口。已有ridge/SVD CPU坐标拟合不能当作完成Reward行为比较；见[投稿证据整理](experiments/latentatlas-submission-evidence-20261009.md)。
