# R18 × DiNa 真实缓存选图 Pilot

归档日期：2026-10-10；证据层级：主要最终报告＋历史页面。

## Experiment

Research gap：有限带噪评分的条件指数恢复，是否能改善冻结奖励模型在真实候选上的最终选图？主端点是人类直接比较，不用模拟KL代替应用收益。

## Config

[历史配置摘要](../../configs/experiments/r18-dina-real-visual-pilot-20261010.json)，不是生产运行入口。

旧28组 / 252图 / 1,008 human pairs；4折回顾性交叉拟合

旧28 prompt groups、252图、1008完整人类pair。原生native每图固定最小pair ID的一次四流，前两流Y，后两流H，K2。HPS新版O原图mu与pixel/PNG/prompt身份匹配，训练折中位数二元U；human不入拟合。新56图组零重叠但缺clean teacher，单独审计，不拼接。

初始本地缺原图片字节；用户提供既有服务器<private-tailnet-host>后，已只读取回固定案例8张O原图，PNG与RGB像素hash8/8通过。两胜两负照片已渲染并实际查看；其余244图未下载。预训练数据重叠未知，历史源已消费，重切分不fresh。

## Result

**归档分类：** `NO_GAIN`

固定V2对原生四流选图胜率37.86%，对Logistic38.13%；两主比较97.5%区间上界均45.98%。

| 主Best4、人类评价 | 结果 | 95%组区间 | 97.5%组区间 |
|---|---:|---:|---:|
| V2对原生四流直接胜率 | 37.86% | 30.71–44.91% | 29.91–45.98% |
| V2对同标签Logistic胜率 | 38.13% | 31.16–45.09% | 30.18–45.98% |

选图对八对手胜率：V2 .56875、原生 .70067、Logistic .68683。Best9 V2对原生直接胜率37.5%，区间宽，未建立收益。全部reference/mean-exp/unpooled/V1/V2/no-higher在1176个组-条件-子集上选图100%相同；概率变化未转为决策变化。

本轮新增图/评分/teacher/human/GPU/API/基础模型更新均0。历史资源252图、252HPS标签、1008human pairs；取用1008 native位置，原bank8064 native调用。每折校准189teacher+756native。受控Best4完整proposal仍需九图四流36calls/group，不能只计最终4图。完整历史生成/人工费用UNKNOWN。最终R2科学运行wall .561秒，资产审计/测试/报告成本另计，不代表整轮总耗时；289全仓库测试15.72秒。

只读恢复8张原图文件6,225,335字节，传输压缩包6,225,572字节、15.3093秒；远端写入0，无新模型前向。CPU照片渲染与报告总耗时未完整计时。

## Conclusion

新增图片/评分/GPU0；固定案例8图已恢复，其余244图未下载。旧源已消费，B NOT_RUN，不声称fresh或论文级独立确认。

高阶乘积矩、结构处理、正归一化实际执行且保留。V1阈值.900–1.148全部归零对比；V2阈值.010–.020全部保留，与unpooled一致。主最高分并列64.46%，Best9 75%；粗分组是有证据的信息瓶颈。tanh与原raw平均选择一致，不支持把失败归于变换排序。V2 Brier .19985小于reference .20350，但弱于Logistic .17652；不能据此称应用成功。

当前适配器缺乏可信选图收益，论文方法贡献/novelty未获经验支持。真实指数积分精确风险无法从此bank识别，INCONCLUSIVE；不能把这个负结果扩大为所有R18理论无价值。

## Next

Stop扩大训练、GRPO、V3/V4与新确认。固定案例补图已完成：同格并列各有一次胜负，跨格反转也各有一次胜负；一胜例中人类与HPS方向相反。4例不能归因总体劣化，但显示信息损失及评价目标差异。先解释接口问题再决定是否值得另立事前冻结研究；本轮不继续V3/V4。补图不使旧数据fresh。

`r18-conditional-exponential-recovery`（原wiki关联）；[r18-method-mvp-20261010](r18-method-mvp-20261010.md)；`latent-reward-channels`（原wiki关联）。

本次只导入已有实验，不启动新阶段。

## Sources

- [来源快照](../source-snapshots/r18-dina-real-visual-pilot-20261010.txt)
- [最终报告文本](../reports/r18-dina-real-visual-pilot-20261010-final.txt)
- [来源清单](../../results/source_manifest.json)
