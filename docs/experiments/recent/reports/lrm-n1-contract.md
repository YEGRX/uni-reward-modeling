> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# LRM-N1：真实Noisy State与冻结DiNa合同

状态：实际执行与核查完成。8个真实状态、64逻辑科学分数和8项技术检查均已保存并独立核验；详见结果与REPRODUCIBILITY。

## 真实源轨迹

FLUX.1-dev使用R1原revision、1024²、28步、guidance embedding3.5、true_cfg_scale1、BF16和原CPU seed Generator。实际安装diffusers0.36.0的pipeline/scheduler源码及SHA见 `REPRODUCIBILITY/source-identity.json`，完整文本见该目录。并行的人工终态加噪不进入本轮。

源状态u_t是Transformer实际输入，shape `[1,4096,64]`。pipeline先把调度timestep转换到latent的BF16，再除1000给Transformer。保存原scheduler FP32 t、σ与实际BF16模型t，三者分开。

原模型输出为Flow velocity；本配置不执行负条件第二次CFG。保存原model output及传给scheduler的effective velocity，要求逐位相等。调度器先将当前sample提升FP32，再按源码原运算

`u_next = (u_t.float() + (sigma_next - sigma_t) * effective_velocity).to(effective_velocity.dtype)`。

注意这里保留原0维sigma与BF16 velocity的PyTorch乘法提升规则，不改写为所有乘数FP32。本轮从真实k21缓存接续至k27，将这7步的原scheduler返回与上述重建逐位比较；0–20步由原历史轨迹提供。目标点是**更新前**k23/k26：实际σ=.40707841515541077/.19545459747314453；t=407.07843017578125/195.45458984375。需对应8条真实状态，不从终态倒推。

## 源VAE坐标与即时估计

unpack为原pipeline `_unpack_latents(u,1024,1024,8)`，得到 `[1,16,128,128]`。源VAE scaling=.3611、shift=.1159。

- Direct输入：`q_t = unpack(u_t)/.3611+.1159`，按R1原decoder BF16两次操作，不附加标准化。
- 当前估计：`u_hat = (u_t.float()-sigma_t*v_t.float()).to(BF16)`，随后unpack与同一BF16反尺度，得到qhat。运算输入仅当前u_t和v_t。
- 当前图像：源冻结VAE.decode(qhat)→VaeImageProcessor→RGB8 PNG。完整桥A使用此PNG的像素，而非未来终态。
- 终态身份：4条接续terminal逐位等于R1原final_native_u后，复用R1已经逐像素核验的生成PNG及原T1编码。PNG SHA、终态SHA和来源不能互换。

源VAE权重SHA `f5b59a26851551b67ae1fe58d32e76486e1e812def4696a4bea97f16604d40a3`。把带噪u转换为decoder原坐标只明确接口输入语义，分布是否适配是本轮科学问题。

## 接口和目标参考

正式REC来自D73 FLUX trial00 step5000，SHA `801c8d5868b63ea486c057a47dfdff17ebf230ec481f974a066e6f2f1a61ef47`，按原strict loader、CUDA BF16 autocast和prediction backend运行。强Affine为reflect k5、lambda.001，SHA `e49ff18ba382941f783dbe5febfebf3f9e77503f25ee20cca94a66ea34403734`；系数已有FIT标准化折叠，按原CPU FP32部署后一次BF16 cast。本轮训练与checkpoint选择0。

A的参考VAE为原SD3.5：RGB8→原共同FP32像素归一化→NCHW BF16→固定CUDA posterior sample→`(z-.0609)*1.5305`。当前每图posterior seed与候选/k确定性绑定，终态保留R1原posterior。RGB8量化是本合同的一部分。

## 冻结DiNa与直接入口

DiNa revision `31d99dc51bf4c6fd46eb6a5ba0d352e36320cad9`，沿R1原admission逐文件核查全部SD3.5、DiNa和官方源码。原模型及三个文本编码器、参考VAE均冻结；唯一active adapter为rm_lora，六项state前后须一致。

官方模型源码 `SD3RewardModel.forward(latents,...,timesteps)` 直接提取带时刻特征并输出raw reward；加噪发生在其外层inferencer.reward。N1禁用该外层入口，显式调用前者：

`model(latents=sealed_noisy_BF16, timesteps=sealed_FP32_t, **pinned_conditions)`。

A/B/FINAL预先按原helper算 `((1-sigma_r)*clean + sigma_r*epsilon).to(BF16)`；C/D直接使用对应接口输出，无第二次人工加噪。实际model pre-hook同时校验latents和timesteps fingerprint；实际RM/backbone root一一计数，禁止其它未登记模型调用。

参考噪声目标固定.4/.2，实际离散σ/t来自同一原noise scheduler最近点。完整科学输入、实际时间、epsilon、条件指纹及模型state在首个RM前封存到 `score/score-precommit.json`。默认.4须精确等于R1；.2作为非默认时间单列比较。数值相近的源/参考σ不构成噪声分布对齐证明。

当前runtime技术门：4个历史终态raw scalar精确重现；默认和后期时间的原显式加噪helper与已构造noisy直接前向一致；后期一次精确重复。计划8次，失败即停止。以这些当前技术门替代再次运行原16-call资格门，从而保持本轮技术≤12。

## 评价对象

A评价当前估计所代表图像，FINAL评价实际完整生成图像；各时点独立比较。C/D与A的score difference为行为差异，不是已配对参考噪声的映射误差。B成功归为clean-estimate bridge，C/D成功才归为direct noisy现象。2个Prompt是统计单位，所有状态/seed/噪声流相关性保留。

来源：用户协议（原件定位：`raw/projects/latentatlas/lrm-n1-20261021/user-request.txt`）、评分预提交（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/LATENTATLAS_LRM_N1_REAL_NOISY_TRANSFER/SCORE_PROTOCOL_PRECOMMIT.md`）、原R1 `LATENT_CONTRACT_VERIFICATION.md`、原D73部署代码；[DiNa官方实现](https://github.com/HKUST-C4G/diffusion-rm)、[原论文§4与§5](https://arxiv.org/html/2602.11146v1)。

## 本轮实际验收

源k23/k26实际模型时间为.408203125/.1953125；DiNa实际σ/t为.4002932608127594/400.29327392578125与.2001733034849167/200.17330932617188。四条历史真实k21接续全部精确复现终态，source state前后相同。CPU独立复算24个velocity/Euler/qhat检查逐位通过；反尺度16项使用CUDA opmath展开后全部逐位通过，原CPU BF16 scalar addition差异保留。实际输入未改变。原64分数、64实际input SHA及64 BF16 scalar SHA已验收。
