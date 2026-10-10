# 证据、文件与复现边界

## 仓内内容

| 位置 | 内容 | 证据边界 |
| --- | --- | --- |
| [实验索引](experiments/index.md) / [日志](experiment_log.md) | 85条带来源记录 | 72条视觉/接口历史，13条理论或规定模型 |
| `docs/reports/` | 15项主要实验最终报告的可移植文本导出 | 根据最终报告整理，不是本次重跑 |
| `docs/source-snapshots/` | 85份wiki来源快照 | 70项仅来源快照，未重审原始资产 |
| `configs/experiments/` | 数据、参数、版本、状态的历史配置摘要 | `historical_documentation_not_executable`；不能派发生产任务 |
| [Q32历史执行配置](../configs/q32-forward-original-execution-config.json) | 新协议固定范围的原配置 | 配套全部生产caller与模型未入仓，不能单文件重跑 |
| `results/evidence/` | Q32原FD失败、新协议VAL/MAIN8数值及既有独立回执 | 既有CPU接受不等于新独立科学确认 |
| `results/figures/` | 原实验输出图及图数据 | 本次没有生成新的科学效果图 |
| [来源清单](../results/source_manifest.json) | 原文件SHA、导出文件SHA、来源定位 | 本地用户名/地址规范化后，导出SHA可以不同 |
| [仓内资产清单](../results/repository_assets.json) | 报告/快照/配置/证据/图片逐文件SHA | 运行入口核对这些文件的完整性 |

`wiki-store/` 与 `LatentAtlas-runs/` 是维护者存储中的相对来源定位符，不是本仓目录或已发布下载地址。原完整来源文件未改写；入仓文本只规范化维护者绝对路径和私有网络地址，历史实验数值不变。来源SHA与导出SHA分开保存。

## 现在可运行的CPU核对

```bash
bash scripts/reproduce.sh
# 任意目录亦可调用绝对路径；无需安装第三方包。
python3 scripts/reproduce_records.py --check
```

Python 3.9+标准库。入口验证来源、记录和配置对应关系及仓内资产SHA，从归档的结果JSON重建：

- `results/tables/experiment_summary.csv`：15项主要实验摘要。
- `results/tables/q32_main8.csv`：六臂全部标量指标和已报告区间。
- `results/tables/q32_main8_effects.csv`：四项主效应及调整区间/原分类。
- `results/tables/q32_val.csv`：VAL六臂风险、坐标保护和区间。

普通入口写入上述确定性表格并验证；`--check`只比较现有文件。既有数字/区间直接取自归档JSON，**不在这里重新拟合、bootstrap或计算新的科学结论**。这是结果表与文件完整性复现，不是从原始评分矩阵重新独立计算整个研究，也不是GPU复现。

## 完整原始CPU回放

[外部工件登记表](../results/artifact_registry.json)列出原数值停止包和后续前向审计包。后者90851723字节、7949个原始工件，SHA `bc8fabf4214cd7d1145df380cd43413ce9feb760248c8241c28b26d093f91b96`。完整包留在Git外；实验室共享下载地址尚未设置，向维护者YEGRX获取。

已有[本地portable回执](../results/evidence/q32-forward/LOCAL_PORTABLE_CPU_REPLAY.json)记录7856次算术对照与7949文件接受；[MAIN8远端CPU回执](../results/evidence/q32-forward/MAIN8_INDEPENDENT_CPU_ACCEPTANCE.json)和[封存回执](../results/evidence/q32-forward/REMOTE_SEAL.json)一并保留。回执是历史证据，此PR并未重新执行这些科学回放。详细失败、恢复与范围见[最终报告](reports/latentatlas-frozen-candidate-forward-audit-final.txt)。

## 从GPU原始输入重现

需要固定身份的数据/缓存、权重及其许可、完整历史生产caller、原输入准入/spec/pins、环境和append-only账本。它们没有全部随本PR交付；因此不提供会下载不明数据或启动新实验的训练/评分脚本。`scripts/train.sh`明确拒绝训练，`scripts/eval.sh`仅作上述CPU记录核对。

完整GPU重现不能仅靠已有portable数值包；缺失工件与权限应逐项补齐后，依具体协议运行。不要将按图去重的864次误当成pair-specific MAIN8的6912次，也不要重新选组/调半径/挑checkpoint使结果通过。

## 结论限制

- 原Q32 FD失败保持失败；新协议VAL/MAIN8不恢复导数模型资格。
- VAL固定行动门槛通过只授权当时的MAIN8阶段；普通双侧区间跨0仍保留。
- MAIN8的Q32教师误差退化得到支持；人类Accuracy变化和Q32对A32优势未确立。C32更低教师误差来自二级未调整比较。
- MAIN8是已使用开发池中固定8组；不声称论文级独立确认。P32仅VAL，未评价MAIN8。
- HPSv3为六臂，F_NOREG协议缺席；decoder介导读出不能证明直接潜空间复用。
- 理论/规定模型页的数学验证不构成真实视觉增益或机制因果证明。
