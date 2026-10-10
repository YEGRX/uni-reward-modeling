# DC-AE 训练目标 × 空间接口四格预实验

归档日期：2026-10-10；证据层级：主要最终报告＋历史页面。

## Experiment

在固定 64 FIT / 64 VAL、1008 对 / 28 组、四流和 1000 步预算下，分开比较教师目标 T0/T1 与空间接口 P0/P1。A=P0T0 精确复用旧封存终点；B=P0T1、C=P1T0、D=P1T1 新训练。零目标偏好标签。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-dina-dcae-target-spatial-factorial.json)，不是可派发GPU任务。

**输入与范围：** 开发集1,008对 / 28组 / 4流

旧 A、128 Anchor、1008 对评价行与 28 个关联组均有只读来源核验。B/C/D 各 1000 步终点经独立远端 CPU 验证。新评分 24,192 科学条件、115 技术条件；未读取 retired future、old TEST 或 External。

## Result

**当前归档分类：** `JOINT_GAIN_NOT_ESTABLISHED`

A/B/C/D Accuracy64.16/64.43/62.82/63.59%；B/C/D未确立Accuracy与排序的联合改善。



## Conclusion

固定四格控制，单seed；坐标与行为端点分开，不挑较好checkpoint。

完整指标、区间、成本和原失败见下方最终报告。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

- `raw/experiments/latentatlas/dina-dcae-target-spatial-factorial-2026-09-26/verified-complete-20260927-r1/FINAL_REPORT.md`
- 同目录 `FINAL_SEAL_R1.json`、`FINAL_SEAL_INDEPENDENT_READBACK_R1.json`、`PORTABLE_LOCAL_REPLAY_VERIFICATION_R1.json`、`PORTABLE_REMOTE_FETCH_R1.json`、`F0_FREEZE_RECEIPT.json`。
- 远端全量证据：`/opt/latentatlas/dina-dcae-target-spatial-factorial-20260926-r1/run/`，分析逐行证据、B/C/D checkpoints 与 final inventory 均有 SHA 绑定。

## Sources

- [来源快照](../source-snapshots/latentatlas-dina-dcae-target-spatial-factorial.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-dina-dcae-target-spatial-factorial.md`。
- [最终原报告文本](../reports/latentatlas-dina-dcae-target-spatial-factorial-final.txt)：路径仅为来源定位；其中历史状态以最终段落/追加回执为准。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
