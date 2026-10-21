# LatentAtlas：让不同 VAE 复用同一个潜空间奖励模型

我们想让使用不同VAE的生成模型，共用一个已经训练好的Reward Model。Reward Model的参数不动，只用少量图片训练一个小的转换网络，把其他VAE的latent转换成它能读取的表示。我们关心的是：转换以后，原来的评分判断还能保留多少，以及训练和使用这个转换网络要付出多少成本。

[研究背景](#motivation) · [我们的想法](#idea) · [实验](#experiments) · [主要参考文献](#references) · [完整实验档案](docs/experiments/index.md)

<a id="motivation"></a>
## 一、为什么做这件事

很多图像生成模型先在VAE的latent里生成内容，最后再解码成图片。latent可以简单理解为图片的压缩表示。像素空间的Reward Model需要看到图片才能打分，潜空间Reward Model则直接读取这些表示。其中，能够处理带噪状态的模型，还可以在生成中途评价候选，让我们有机会提前决定哪些值得继续生成。

问题是，不同VAE对同一张图片的表示并不一样。Reward Model学会读取一种VAE的latent后，不一定能直接读懂另一种。即使输入大小相同，里面的数值和表示方式也可能不同，评分和好坏排序就可能跟着改变。

我们主要研究的是LRM，也就是在latent里评价生成中途带噪状态的Reward Model。我们希望在图片还没生成完时，就用它判断候选的好坏，帮助选择哪些值得继续生成。这里要解决的问题是：当生成模型换用了另一种VAE，能不能继续使用同一个已经训练好的LRM，让它仍能评价这些带噪状态，同时尽量保留直接在latent里评分的效率优势？

对于生成中途的带噪latent，可以先根据生成器当前的预测，估计一份清晰的latent，再解码成图片，用LRM对应的VAE重新编码后评分。这给了我们一条完整的参考路径。我们想检查，能不能用一个小接口减少中间的转换步骤，同时保留有用的评分判断。

我们首先要看，在不同噪声阶段，转换以后还能保留多少原LRM的评分和排序。然后再算成本：学习这个接口用了多少图片和算力，实际评分时增加了什么计算，又省下了什么步骤。如果要用这些评分指导生成，还需要检查它是否真的能帮助选出更好的结果。

已有LRM工作也遇到过跨VAE使用的问题。LRM/LPO把SD1.5版本的奖励模型用于不同VAE的SDXL时，部分生成指标反而下降。DiNa也明确区分了两件事：为不同生成模型分别训练一个奖励模型，以及让它们共用同一个已经训练好的奖励模型。PRISM则指出，跨VAE使用需要解码再重编码，并把跨模型转换接口列为后续方向。

相关原文：[LRM/LPO](https://arxiv.org/html/2502.01051v5) · [DiNa附录C.3](https://arxiv.org/html/2602.11146v2) · [PRISM §4.5](https://arxiv.org/html/2606.20310v1#S4.SS5)。

<a id="idea"></a>
## 二、我们的想法：同图Anchor和转换接口

不同VAE虽然用不同的方式表示图片，但我们可以把同一批图片交给它们编码。我们最初的直觉是，一批内容相似的图片，在不同空间里的坐标虽然不同，它们之间仍可能保留某些相似的位置关系。因此，我们想到用同一批图片在两个空间中作参照，看看能不能学出它们之间的转换。

具体做法是，把同一张图片分别输入源VAE和参考VAE，得到一对latent。这些来自同一张图的对应表示，就是我们说的Anchor。它们给转换网络提供了最直接的对照：源空间里的这份表示，对应参考空间里的哪份表示。这里参考VAE使用的是DiNa原本接受的SD3.5 VAE。

有了这些对应样本，我们再训练一个小网络，把源VAE的latent转换成接近参考VAE的表示。这个转换网络叫Projector，当前使用的小卷积版本叫REC。训练时只调整REC，让它的输出尽量接近同一张图的参考latent。两个编码器和DiNa都保持不变，也不向接口提供图片的好坏标签。

我们设想的使用方式是，让源模型的latent先经过REC转换，再交给原来的DiNa评分。REC负责转换表示，图片好不好仍由DiNa判断。我们希望保留它已经学到的判断标准，所以固定DiNa的参数，只训练输入前的这段转换。评分究竟能保留多少，要通过对照实验检查。

最开始，我们想构建一个共同空间，也就是“latent的latent”，让不同VAE都能通过它进行转换。后来发现，用少量同图配对训练一个小接口，已经能在已有实验中保留不少DiNa的排序判断，我们便先沿着这条更具体的路线继续验证，没有再继续构建那个共同空间。

训练接口时，我们最初用的是完整图片编码得到的latent，称为Clean latent。它和生成中途的带噪latent不是同一种输入。因此，Clean上的结果先回答“这个转换办法有没有用”，之后还要拿真实生成过程中的带噪状态来试，检查它在生成中途能不能继续保留DiNa的判断。

<a id="experiments"></a>
## 三、实验

### 3.1 Anchor有没有用

在Cosmos实验中，我们比较了正确配对、打乱配对和不训练接口三种情况，看转换后DiNa对图片的排序是否保持一致。正确配对时，一致率达到93.4%；打乱配对或不训练时，都只有约60%。这说明同一张图片在两个空间中的正确对应，确实有助于保留DiNa的判断。

我们也在DC-AE上比较过Anchor数量。这一轮用的是DC-AE的较大接口，固定网络结构和训练次数，只把训练图片从64张增加到256张。它与完整解码—重编码参考路径的排序一致率，从85.9%提高到88.7%。在这次实验中，更多正确配对带来了改善。

[正确配对与打乱对照的原报告](docs/reports/latentatlas-dina-unseen-encoder-fixed-recipe-portability-final.txt) · [DC-AE图片数量实验](docs/experiments/latentatlas-dina-dcae-strong-anchor64-vs256-fixed2k-newgroups.md)

### 3.2 REC能保留多少DiNa的评分能力

接下来，我们检查REC能保留多少DiNa的评分能力。先用64张图片训练接口，再用另外64张图片选模型。评价时，让同一张图走两条路：一条经过SD3.5 VAE编码后直接交给DiNa；另一条经过源编码器和REC转换后，再交给同一个DiNa。最后比较两条路径对图片的排序是否一致。

在28组、252张图构成的1008对评价中，FLUX和Cosmos来源的排序一致率分别达到94.7%和94.6%。也就是说，换了编码路径后，约95%的比较仍保留了DiNa原来的判断。这里的95%是与原DiNa的排序一致，不是人类偏好准确率；这批图片也已用于方法开发，还需要在独立的新图片上确认。

[FLUX原结果](docs/experiments/recent/reports/d73-flux.md) · [Cosmos原结果](docs/experiments/recent/reports/d73-cosmos.md)

### 3.3 和其他方法相比怎么样

正确配对有效，还需要检查简单方法是否已经够用。因此，我们把REC与普通仿射映射、已有的SD-Latent-Interposer，以及另一种小卷积接口A2进行比较。仿射映射用加权组合和偏置换算表示；Interposer也是跨VAE转换网络，分别测试只对齐表示和加入双向转换要求的版本。各方法使用相同的64张训练图和64张验证图，根据表示误差选模型，再用同一个DiNa评价。

下面比较转换后与原DiNa的排序一致率，数值越高，说明保留的原判断越多。

| 转换方法 | FLUX | Cosmos |
| --- | ---: | ---: |
| 普通仿射映射 | 91.6% | 90.1% |
| Interposer：对齐表示 | 90.5% | 92.3% |
| Interposer：加入双向转换要求 | 86.6% | 92.7% |
| 我们的小卷积接口REC | **94.7%** | 94.6% |
| 另一种小卷积接口A2 | 92.9% | **94.9%** |

Interposer使用的是在本批图片上重新适配的版本。这些方法的配对图片相同，实际训练计算量并不完全相同。

在这批开发图片上，REC比所选仿射映射更能保留DiNa的排序，两个来源的统计比较都支持这个改善。与Interposer相比，FLUX上的排序改善也得到支持；Cosmos虽然平均一致率更高，但考虑组间波动后，还不能确认排序有优势。REC和A2也没有分出可靠高下，所以目前不能说REC优于所有对照方法。

[完整比较与统计区间](docs/experiments/recent/README.md#d73)

### 3.4 方向偏在哪里，以及真实Noisy实验

我们原本想解决的是，在生成还没完成时，让不同VAE共用同一个LRM。后来不少实验都在拿完整图片编码出的Clean latent做转换，并调整接口来提高与原DiNa的排序一致率。这些实验验证了接口的可行性，但研究重心逐渐变成了Clean表示转换和原排序恢复，还没有直接回答：生成中途的带噪状态能不能接入，得到的评分又能不能帮助实际生成。

#### 补做真实生成实验后，发现了什么

我们随后开始用生成器实际产生的latent检查接口。在终态实验中，4条提示词的候选选择，REC和简单仿射都与完整参考路径保持一致，这一轮没有显示出REC额外的选图收益。

真实Noisy实验用了2条提示词、4条生成轨迹，在28步采样中取两个靠后的时点，比较直接转换和先预测清晰状态再转换。

| 方法 | 较早时点 | 较晚时点 |
| --- | --- | --- |
| 先预测清晰状态，再用REC转换 | 2条都同选 | 2条都同选 |
| 带噪状态直接用REC转换 | 2条都同选 | 1条同选、1条反向 |
| 带噪状态直接用仿射转换 | 1条同选、1条平局 | 1条同选、1条反向 |

这里的“同选”指与完整参考评分路径选中同一候选。这次结果说明，原Clean接口直接处理带噪状态还不稳定；先预测清晰状态再转换，在这几个例子里保留了选择。但样本很少、时点也接近生成结束，还不能说明早期生成中同样有效。

[真实终态实验](docs/experiments/recent/reports/lrm-r1-results.md) · [真实Noisy实验](docs/experiments/recent/reports/lrm-n1-results.md) · [原始评分表](docs/experiments/recent/tables/lrm-n1-four-path-scores.csv)

#### 下一步怎么改进

下一步应把重点放回真实的LRM使用场景。先确认原DiNa在目标生成内容上的判断是否有用，再在独立的新轨迹上，检查不同噪声阶段的评分和选择。比较时保留完整参考路径、简单仿射和现有REC，并区分直接转换与先预测清晰状态再转换。

同时，把接口训练、去噪预测、编解码和LRM评分的实际成本算清楚。我们需要知道，这个接口是否以可以接受的代价保留了有用判断，而不只是继续提高Clean实验里的一致率。

[已有Reward有效性分析](docs/experiments/recent/reports/lrm-r2-validity.md)

<a id="references"></a>
## 四、主要参考文献

### LRM/LPO

*Diffusion Model as a Noise-Aware Latent Reward Model for Step-Level Preference Optimization*

这篇工作先用偏好数据训练一个能评价带噪latent的LRM，再用它比较生成中途的候选，并优化生成模型。它还尝试把SD1.5版本的LRM用于其他生成模型，在不同VAE的SDXL上观察到部分指标下降。

它和我们都关心生成中途的奖励反馈，也为跨VAE复用的需求提供了实际例子。区别在于，它主要研究怎样训练LRM、怎样用它优化生成；我们希望保留已经训练好的LRM，只用少量同图配对学习输入转换。

[论文](https://arxiv.org/html/2502.01051v5) · [官方代码](https://github.com/Kwai-Kolors/LPO)

### DiNa-LRM

*Beyond VLM-Based Rewards: Diffusion-Native Latent Reward Modeling*

DiNa利用扩散模型处理不同噪声的能力，训练奖励模型，让它根据latent、时间步和文本判断候选的好坏。它也提供完整图片或Clean latent的评分入口，评分时会按设置构造带噪输入。

DiNa是我们实际复用的下游模型。原论文研究怎样学到奖励能力，我们研究换了VAE以后怎样继续使用这份能力。我们的实验固定已经训练好的完整DiNa，只调整输入接口。原论文在多个生成模型上分别训练DiNa，并不等于同一份DiNa权重可以直接接收任意VAE的表示。

[论文](https://proceedings.mlr.press/v306/liu26fh.html) · [官方代码](https://github.com/HKUST-C4G/diffusion-rm)

### PRISM

*Through the PRISM: Preference Representation in Intermediate States of Video Diffusion Models*

PRISM研究视频生成。它固定视频扩散模型的主体，训练一个评分模块，直接从带噪latent中读取偏好信息，并用来提前筛选候选。

它与我们都关注生成中途的评价。作者明确指出，换用不同VAE后，需要先解码再重编码，并把跨模型转换接口列为后续方向。这与我们的使用需求很接近。区别在于，它研究视频奖励建模，我们目前研究图像模型中已有LRM的复用；它报告的效率收益也不能直接当作我们的结果。

[论文，重点§4.5](https://arxiv.org/html/2606.20310v1)

### SD-Latent-Interposer（开源项目）

这个项目用配对latent训练卷积网络，把一种VAE的表示转换成另一种，供后续生成流程使用。它是开源实现，不是一篇论文。

它与我们的训练方式很接近：都用对应图片产生的latent监督转换网络。区别主要在评价目标——我们还要检查转换后，同一个冻结Reward Model的评分和排序是否保持。用途不同不代表转换方法本身就是新的，所以我们把它作为直接对照。

[官方仓库](https://github.com/city96/SD-Latent-Interposer)

### Latent Space Translation via Semantic Alignment（NeurIPS 2023）

这篇工作把对应内容输入不同编码器，得到配对表示，再计算空间之间的转换关系。它比较线性、正交和仿射等变换，转换后接入原来的分类器或解码器，检查功能还能不能保持。

这与我们的Anchor思路非常接近：都用对应样本学习空间转换，再复用已有的下游模型。它主要验证分类、跨模态和重建等任务，我们具体检查潜空间奖励模型的评分、排序和使用成本。因此，“用同图配对翻译表示”已有明确先例，我们需要说明的是，这样做在LRM场景中到底有什么实际效果。

[论文](https://papers.neurips.cc/paper_files/paper/2023/hash/ad5fa03c906ca15905144ca3fbf2a768-Abstract-Conference.html)

### Revisiting Model Stitching in the Foundation Model Era（CVPR 2026）

这篇工作尝试把不同视觉模型的前后部分连接起来。原有网络保持固定，只训练中间的连接层，再检查组合后能否完成分类、分割等任务。它发现，只让连接处的表示接近，未必能保留最后的功能，因此还研究了匹配最终特征和使用任务目标训练连接层。

它和我们都用小接口连接已有模型。我们目前用配对latent训练REC，与它在连接处匹配表示的做法接近。它提醒我们，坐标接近以后还必须检查评分。若借鉴它的最终特征匹配，就需要读取下游模型的特征，训练时使用的信息也会比目前更多。

[论文](https://openaccess.thecvf.com/content/CVPR2026/html/Mai_Revisiting_Model_Stitching_In_the_Foundation_Model_Era_CVPR_2026_paper.html)

### Stitched Value Model for Diffusion Alignment（StitchVM，2026预印本）

StitchVM把扩散模型处理带噪latent的能力，接到已有图像Reward Model的后半部分。它先选择连接位置，再用原奖励模型提供的信息，训练中间接口和被接入的奖励后缀，最后用于生成引导和训练对齐。

它和我们都想复用已有奖励能力，并在生成中途评分，所以Noisy latent上的模型拼接已经有直接前作。区别在于，它会更新奖励后缀，并用奖励模型的信息训练；我们希望完整DiNa保持不变，接口只用同图坐标配对学习。这样的限制是否值得，要通过实际评分效果和完整成本来比较。

[论文](https://arxiv.org/html/2605.19804v1) · [官方代码](https://github.com/prs-eth/StitchVM)

### Latent Space Translation via Inverse Relative Projection（2024）

这篇工作先用一个样本与各个Anchor的关系来描述它，再借助目标空间的Anchor，把这种相对描述还原成目标坐标。这样，相对表示就成了不同空间之间的中转站；转换效果依赖两个空间的相对关系以及数值尺度等条件。

它与我们最早“latent的latent”设想比较接近，都希望借助对应样本找到空间之间的共同点。当前REC则直接学习源空间到参考空间的转换，没有经过共享中间空间。这篇可以作为以后重新考虑共同空间时的参照，目前我们还没有验证这条路线能保留多少LRM评分能力。

[论文](https://arxiv.org/html/2406.15057v1)

完整作者、版本与其他相关论文见 [Related Work](docs/related_work/README.md)、[BibTeX](docs/related_work/references.bib)和[原文核查记录](docs/related_work/source_audit.md)。

## 实验与原始记录入口

- [近期详细记录](docs/experiments/recent/README.md)：原编号、设置、报告和结果表。
- [全部实验索引](docs/experiments/index.md) · [逐次日志](docs/experiment_log.md)：包括历史失败与停止记录。
- [文档与结果核对说明](docs/evidence-and-reproduction.md)：`bash scripts/reproduce.sh --check`，检查保存的文件与表格，不运行模型。

更新：2026-10-21 · Maintainer: YEGRX
