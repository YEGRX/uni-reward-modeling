# 0. Repository Structure （此部分仅为了解如何使用这个模版，不用包含在自己的项目中）

```
lab-project-template/
├── README.md                   ← 项目主文档（你现在读的这个）
├── project.yaml                ← 项目状态卡，最常查看的文件
├── TODO.md                     ← 当前任务列表，按优先级排列
├── LICENSE
├── .gitignore
├── .env.example                ← 环境变量模板，复制为 .env 后填入真实值
│
├── docs/
│   ├── idea.md                 ← 研究想法、问题定义、与 prior work 的对比
│   ├── related_work.md         ← 相关文献笔记
│   └── experiment_log.md       ← 实验记录，每次实验必须写一条
│
├── src/                        ← 源代码
├── configs/                    ← 实验配置文件（yaml/json）
├── checkpoints/                ← 模型权重（不进 git）
├── data/                       ← 数据集（不进 git，见 data/README.md）
│
├── results/
│   ├── figures/                ← 生成的图表
│   ├── tables/                 ← 生成的表格
│   └── demos/                  ← Demo 输出
│
├── scripts/
│   ├── train.sh                ← 训练入口
│   ├── eval.sh                 ← 评估入口
│   └── reproduce.sh            ← 一键复现主要结果（必须保持可运行）
│
└── .github/
    ├── PULL_REQUEST_TEMPLATE.md
    └── ISSUE_TEMPLATE/
        ├── weekly_report.md    ← 每周进展汇报（New Issue → Weekly Report）
        ├── bug_report.md       ← Bug 报告
        └── experiment_request.md ← 新实验提案
```

## Key Rules

| 文件                       | 更新时机                                                       |
| -------------------------- | -------------------------------------------------------------- |
| `project.yaml`           | 每次 PR 合并时更新 `stage`、`best_result`、`last_update` |
| `docs/experiment_log.md` | 每次实验后必须追加一条记录                                     |
| `TODO.md`                | 每周同步当前优先级                                             |
| `scripts/reproduce.sh`   | 始终保持 `bash scripts/reproduce.sh` 可以无报错运行          |

每周通过 **New Issue → Weekly Report** 提交进展，无需开会即可同步状态（我会在每周组会前同步信息）。

---

# Project Title（从这里是你项目要包含的内容）

Short description of the project.

---

# 1. Problem

What problem are we solving?

Example:

Generate consistent motion from sparse sketch input.

---

# 2. Core Idea

One-sentence core idea.

Example:

Use diffusion inversion to extract motion prior from video models.

---

# 3. Why It Matters

Why is this problem important?

* gap in prior work
* potential impact
* application value

---

# 4. Method Overview

Pipeline:

Sketch → Motion Prior → Diffusion → Video

---

# 5. Current Status

Stage:

* [ ] Idea
* [ ] Running baseline
* [ ] Improving method
* [ ] Writing paper
* [ ] Finished

Current:

baseline reproduced

---

# 6. Key Results

Dataset:

Something-Something

Metric:

FVD

Result:

| method   | FVD |
| -------- | --- |
| baseline | 210 |
| ours     | 185 |

---

# 7. Next Step

* try temporal attention
* test longer sequence
* run ablation

---

# 8. How to Reproduce

```bash
bash scripts/reproduce.sh
```

---

# 9. Maintainer

Name:

Last update:

YYYY-MM-DD
