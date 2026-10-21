> 已完成记录的文档导出（采集：2026-10-21）。原件定位和原始/导出SHA见 [来源清单](../source_manifest.json)；未入仓的引用保留定位文字。

# LatentAtlas D56：隐藏特征与共同输出头诊断

## 1. Date

2026-10-18。完成真实执行、保存矩阵及原始分数的独立复算。

## 2. Purpose

D53发现原REC的指定仿射投影Q丢失四个主条件赢家。D56比较原REC（P）、学后隐藏特征重新求头（P1）、原初始化特征同规则求头（P0），区分表示和实际输出头的作用，并保留两个评分条件的选择边界。

## 3. Code Version / Commit

基线HEAD `a0d0712da40e58fd203572fd2b8d4f04ad4f7ce3`，分支`codex/latentatlas-d44-affine-gate`。新增代码` scripts/latentatlas-feature-readout-d56-20261018/`由逐文件SHA封存，未把未提交实现冒充该HEAD内容。最终合成测试24/24、0跳过；Sol6.1实施与定向独立审查，主控验收和运行。

## 4. Dataset / Input

原Cosmos→SD3.5 T0同图Clean FIT64，原D44四个已消费DEV组/四对/八图，与FIT无重叠。原四对按P主条件成功、两旧ridge失败选出；不能估计总体胜率。两评分条件、两噪声流不增加独立图像数。原初始化和checkpoint身份、source/teacher、文本、epsilon及时间合同已核。

## 5. Parameters

两个64通道隐藏端点，含截距65维，按图像等权OLS、ridge0、FP64统计、相对谱门1e−10、rank65。原FP32 master/CUDA BF16 autocast路径；头系数FP64→FP32一次。RM分数、梯度、隐藏及偏好标签均不进入拟合。u=.4/.1，沿原两流；Native合格门.125，方法近零门≤.0625。

## 6. Command

两GPU阶段由封存`supervise.py --config gpu-config-r1.json --sha256 ff56cb6bba307cee38610d2681d7df26c213c65d139282a4fe65808ee786810c --phase 1/2`分别启动，中间执行固定CPU拟合。实际完整调用见`d56-execution/phase1-launch-receipt.json`、`cpu-launch-receipt.json`、`phase2-launch-receipt.json`。各阶段已完成，旧claim禁止再次执行；复核已有结果使用本地分析入口，不重放模型。

## 7. Results

| 评分条件 | P原REC | P1学后特征OLS | P0初始化特征OLS |
|---|---|---|---|
| u=.4，四例合格 | 4正确 | 4正确 | 2正确、2反向 |
| u=.1，三例合格 | 2近零、1反向 | 2近零、1反向 | 1近零、2反向 |

弱条件另1例Native低信号。P0主条件成功为aa0c08c7/e58f945b，P1相对P0修复32d0ce83/90070ef0。P1−P0在弱条件三个合格案例均有正向分差作用，仍未恢复严格赢家。完整8行数值见结果报告（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/feature-readout-result-d56.md`）。

P1/P0理想FIT归一化损失为.09851217538/.32879250046；原头在同一最终隐藏统计上为.09925002903。均非BF16部署FIT实测。两设计均rank65，独立矩阵复核损失差≤3.33e−16；原始评分按精确有理数另行join复算一致。

真实调用：隐藏144、完整REC2、头18、DiNa68（4技术＋64科学）；含嵌套图身146/头层20/骨干68，不能相加当独立模型样本。CPU拟合2/访问128，24.372秒；GPU两段累计941.831秒，上限1800秒。VAE、文本、生成、A2、梯度训练0。228文件全部回收核SHA，472项模型及嵌套预约完成，冻结状态一致，最终锁空闲。

## 8. Analysis

本次头替换保留四个原主条件成功；其中两例用固定初始化非线性表示已能实现，另外两例呈现学后表示在同读出规则下的功能收益。弱条件结果说明，坐标最优头没有解决同一接口的条件边界。普通非线性配对回归仍是最强机制对照；核心创新需产生跨未筛选图像和条件的事前预测。

### D58离线增量（2026-10-18）

原输出空间分解（原件定位：`docs/latentatlas-anchor-theory-2026-10-17/spatial-correction-decision-d58.md`）使用同八图的P0/P1和SHA匹配Native：欧氏等图平均cosine=.85770，修正非共线能量26.38%，空间变化能量74.26%。均值/变化两部分八图均降低坐标误差，均值收益占比均值34.35%；原H下同类结构保持。主控独立标准库从24张量复算2,530项通过，没有新增模型或RM评价。数据仍为原选定DEV4。

下一固定互换方案用P0均值+P1变化及P1均值+P0变化，直接检验冻结赢家；≤68次DiNa、GPU20分钟，其他前向0。科学方案已固定，执行器和真实结果尚未完成，当前本地阶段无需服务器。

## 9. Problems

执行资格全部通过，没有技术失败被当成科学阴性。65维初始化类不包含D44完整153维仿射类，本结果只比较指定初始化/读出规则。数据是成功筛选过的Clean开发案例；本轮没有独立确认、真实生成Noisy迁移、人类质量或成本收益证据。独立复核针对保存产物，未二次重跑模型或原FIT。

## 10. Next Steps

停止追加头、随机种子或宽度搜索。下一主问题是：Anchor-only学得的修正能否产生超过普通拟合解释的、跨新图和预声明评分条件的功能预测。先形成可由合法信息估计的结构与反驳条件，再考虑强固定特征/未筛选组验证。下一阶段本地理论，无需GPU；同类固定小实验已由用户授权自主进行，无需再确认研究顺序。

相关：`latentatlas`、[latentatlas-affine-carrier-d53-20261018](latentatlas-affine-carrier-d53-20261018.md)、`latentatlas-theory-map`、`latentatlas-research-decisions`、`latentatlas-paper-framework`。

## 11. Sources

- `docs/latentatlas-anchor-theory-2026-10-17/feature-readout-result-d56.md`。
- `docs/latentatlas-anchor-theory-2026-10-17/d58-coordinate-audit/coordinates.json`、`d58-root-recompute.json`：本轮坐标计算与独立复算。
- `docs/latentatlas-anchor-theory-2026-10-17/d56-execution/`：封存方案/权限、代码审查、执行回执、矩阵与分数独立复核。
- `raw/projects/latentatlas/d56-feature-readout-20261018-r1/final-snapshot/`：输入身份、源码、调用账本、FIT统计/头、隐藏/预测及评分。
- `raw/projects/latentatlas/d44-affine-gate-20261018-r1/gpu-evaluation/scores.jsonl`：复用原Native/P分数。
- `docs/latentatlas-anchor-theory-2026-10-17/affine-gate-roster-d44.json`：固定四对身份和选择历史。
