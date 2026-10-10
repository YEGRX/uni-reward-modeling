# DINA-SRC0 HPDv3 源域能力验证

归档日期：2026-10-10；证据层级：主要最终报告＋历史页面。

## Experiment

Research gap：此前缺少 DiNa 官方 checkpoint 在 HPDv3 源任务上的 sanity/parity check。SRC0 使用当前已冻结、尽可能 paper-matched 的 inference protocol，检验是否恢复论文级别 Reward 能力；属于 source-domain parity / qualification，不是整篇论文 exact reproduction，也不重新训练或优化 DiNa。

LatentAtlas 核心：已 qualified 的 frozen Reward function，能否通过低成本 representation/interface registration 被异构/新 VAE 在 **0 target Reward labels** 下复用。跨所有 preference datasets 的 OOD 泛化不属于当前主线；不会因 External 差转向改进 DiNa、重训 Reward head 或 universal preference modeling。

用户明确无法联系作者，并授权自主解决。后续不以等待作者回复作为前置条件。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-dina-src0-source-domain-parity.json)，不是可派发GPU任务。

**输入与范围：** 14,400对 / 400组 / 10流

完整 `MizzenAI/HPDv3@5ac4b5b5f2ef42c4613dec612473170b131552db/test.json`。

- 原始文件 10,006,262 bytes，SHA256 `3e762a4025b1fc46d0a3c108f4c74da4d8257c2b8987bfce98aa9247c8956b69`，Git blob OID 同时验证。
- 冻结合同并完成数据入口复审后，实际核对 **14,400 对偏好、4,133 个不同图像路径**，保留完整源行，不抽取有利子集。
- 原始图像来自同一固定版本的 13 段归档，总计 139,119,843,682 bytes。逐段断点下载、长度与 SHA 校验，再提取所需原图。
- 不同路径不等于不同图像字节；最终统计以图像字节身份或相同 prompt 的连通组进行 bootstrap。

## Result

**当前归档分类：** `QUALIFIED`

DiNa源域Accuracy 74.4451%；中央90% [73.5972%,75.2715%]。



## Conclusion

来源域操作性资格，不是精确论文复现或外部分布泛化。

完整指标、区间、成本和原失败见下方最终报告。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

SRC0已通过，按原协议进入SHIFT0，使用同一冻结Reward/runtime区分dataset/task shift；随后按既定算力、数据与注册准入推进REG1。原协议§28规定SHIFT0外部结果本身不阻塞REG1。异构接口注册和target Reward reuse仍无本轮结论；不修改DiNa权重或转为通用偏好训练。

当前SRC0 GPU阶段已结束，统计与核验已完成；后续SHIFT0实现准备只需CPU/代码审查，真正进入新GPU评分前再验证准入。每两小时自动检查保持，旧DINA1不启动。

相关：`latentatlas`（原wiki关联）、[latentatlas-dina-dataset-runtime-diagnostic](latentatlas-dina-dataset-runtime-diagnostic.md)、[latentatlas-dina0-r1-native-qualification](latentatlas-dina0-r1-native-qualification.md)。

## Sources

- [来源快照](../source-snapshots/latentatlas-dina-src0-source-domain-parity.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-dina-src0-source-domain-parity.md`。
- [最终原报告文本](../reports/latentatlas-dina-src0-source-domain-parity-final.txt)：路径仅为来源定位；其中历史状态以最终段落/追加回执为准。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
