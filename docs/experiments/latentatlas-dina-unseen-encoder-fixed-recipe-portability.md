# 操作性未见编码器固定 REC 接入预实验 Cosmos CI8x8

归档日期：2026-10-10；证据层级：主要最终报告＋历史页面。

## Experiment

在不重新选择结构、损失、Anchor、训练步数或科学阈值的条件下，检验固定 REC 配方能否把一个未参与该配方经验开发的连续图像编码器接入同一冻结 SD3.5-DiNa Reward。区分“有注册收益”和“达到近原生操作容忍范围”。这是编码器轴的单种子预实验，不是 fresh 数据确认。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-dina-unseen-encoder-fixed-recipe-portability.json)，不是可派发GPU任务。

**输入与范围：** 开发集1,008对 / 28组 / 4流；64 FIT+64 VAL

候选 `nvidia/Cosmos-0.1-Tokenizer-CI8x8` 为普通连续图像 AE，不是 KL-VAE；权重 SHA `84e4c12c10568faff20da744b51c45a6b1e4385af86e80ae56bf3d1b13cda413`。64 FIT + 64 VAL 同图 Anchor；已消费开发评价 1008 对／28 完整关联组／四条流。目标偏好标签用于最终固定评价，**训练与选点使用 0 个**。指定可检查项目记录未发现候选 checkpoint 或 family/protocol 参与本配方经验开发；公开名称已知、其他私人历史和上游图像重叠无法排除。历史一次非结构化搜索触及排除源文件字节，未解析科学行，已在访问账本披露。

## Result

**当前归档分类：** `REGISTERED_NEAR_NATIVE_WITHIN_PROTOCOL`

正确REC72.619%，NoReg44.618%，Perm49.082%；Native72.817%；Native一致率93.411%。



## Conclusion

通过该轮操作性near-native门槛；连续AE、操作性未见，开发评价已消费，上游重叠未知。

完整指标、区间、成本和原失败见下方最终报告。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

本任务结束；不自动启动下一实验。若另行授权，可用另一未见编码器、不同训练 seed/置换和 fresh 图片检验复现性。相关：[latentatlas-dina-vae2-dcae-recipe-portability](latentatlas-dina-vae2-dcae-recipe-portability.md)、[latentatlas-dina-reg1-functional-registration](latentatlas-dina-reg1-functional-registration.md)、`latentatlas`（原wiki关联）。

## Sources

- [来源快照](../source-snapshots/latentatlas-dina-unseen-encoder-fixed-recipe-portability.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-dina-unseen-encoder-fixed-recipe-portability.md`。
- [最终原报告文本](../reports/latentatlas-dina-unseen-encoder-fixed-recipe-portability-final.txt)：路径仅为来源定位；其中历史状态以最终段落/追加回执为准。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
