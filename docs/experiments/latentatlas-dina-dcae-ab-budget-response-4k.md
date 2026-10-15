# DC-AE A–B 固定日程训练预算响应预实验

归档日期：2026-10-10；证据层级：主要最终报告＋历史页面。

## Experiment

在旧四格实验A=P0/T0、B=P0/T1各自1000步完整状态上继续同一原12000步学习率日程，先统一到2000步。用预先冻结的全VAL自身目标坐标loss门决定是否把两臂都继续到4000步。随后在固定1008对、28关联组、4流上评价选定终点。不能把阶段门控解释为数学收敛证明。

## Config

[历史配置摘要](../../configs/experiments/latentatlas-dina-dcae-ab-budget-response-4k.json)，不是可派发GPU任务。

**输入与范围：** 开发集1,008对 / 28组 / 4流；固定2K门控

旧64 FIT/64 VAL Anchor，T0/T1与共同W0；旧A、B、Native、G逐行分数现已通过远端CPU对旧F1最终封存链和1008行来源身份核验，可作为新评分入口的参照；新A/B评分入口尚未运行。旧A/B各自1000步checkpoint由原不可变`verify_fit`在远端CPU独立通过；三份1K loss CSV逐字段与原封存状态一致。128对stream0探针按身份哈希冻结，但门控seal之前不得评分。

## Result

**当前归档分类：** `STOP_AT_2K`

A2000 Accuracy65.179%，B2000 64.856%；原3%/1% VAL门控未通过。



## Conclusion

未训练2001–4000步；4K结果不存在。旧guard不确定性保留。

完整指标、区间、成本和原失败见下方最终报告。

## Next

本次只导入文档。原实验下一步为历史建议，需独立授权；不由本仓库自动执行。

- `raw/experiments/latentatlas/dina-dcae-ab-budget-response-2026-09-27/preimplementation-gate-frozen-20260927T102657/USER_AUTHORITY.md`
- `raw/experiments/latentatlas/dina-dcae-ab-budget-response-2026-09-27/preimplementation-gate-frozen-20260927T102657/USER_AUTHORITY_ADDENDUM_R1.md`
- `raw/experiments/latentatlas/dina-dcae-ab-budget-response-2026-09-27/preimplementation-gate-frozen-20260927T102657/STARTING_STATE_READONLY_AUDIT.json`
- `raw/experiments/latentatlas/dina-dcae-ab-budget-response-2026-09-27/preimplementation-gate-frozen-20260927T102657/SEALED_ORIGIN_INDEPENDENT_VERIFICATION.json`
- `raw/experiments/latentatlas/dina-dcae-ab-budget-response-2026-09-27/preimplementation-gate-frozen-20260927T102657/USER_SUPPLIED_1K_LOSS_CSV_AUDIT.json`
- `raw/experiments/latentatlas/dina-dcae-ab-budget-response-2026-09-27/preimplementation-gate-frozen-20260927T102657/PHASE1_COORDINATE_GATE_SPEC_RECEIPT.json`
- `raw/experiments/latentatlas/dina-dcae-ab-budget-response-2026-09-27/preimplementatio

（其余历史细节见来源快照。）

## Sources

- [来源快照](../source-snapshots/latentatlas-dina-dcae-ab-budget-response-4k.txt)，原页面定位 `wiki-store/wiki/experiments/latentatlas-dina-dcae-ab-budget-response-4k.md`。
- [最终原报告文本](../reports/latentatlas-dina-dcae-ab-budget-response-4k-final.txt)：路径仅为来源定位；其中历史状态以最终段落/追加回执为准。
- [来源清单](../../results/source_manifest.json)记录原始与导出文件指纹及证据层级。
