# Telco Customer Churn — A Data Mining Case Study

An end-to-end data mining project on a real telecom dataset (~7,000 customers), built to apply and demonstrate the core techniques from a university Data Mining course: data quality assessment, preprocessing, decision trees, model evaluation (precision/recall/ROC), Naive Bayes, SVM, association rule mining, and customer segmentation via clustering.

## Why this project

Most portfolio churn projects stop at "train a model, report accuracy." This one is structured to show the *reasoning* behind each step — manual sanity-checks of the maths behind the models (Gini impurity, support/confidence/lift), explicit over/underfitting diagnosis, and a plain-English business write-up at the end. The goal is to demonstrate understanding, not just library calls.

## Dataset

[IBM Telco Customer Churn](https://github.com/IBM/telco-customer-churn-on-icp4d) — 7,043 customers, 21 attributes (demographics, account info, services subscribed, billing, and whether they churned). Loaded directly from the source CSV in the notebook, no manual download needed.

## What's inside

```
telco-churn-datamining/
├── notebooks/
│   └── 01_churn_analysis.ipynb   ← main analysis, open this first
├── src/
│   └── utils.py                  ← reusable helper functions (imported by the notebook + tested)
├── tests/
│   └── test_utils.py             ← unit tests for src/utils.py
├── requirements.txt
└── README.md
```

## Techniques covered

| Stage | Techniques |
|---|---|
| Data understanding | Attribute-type classification (nominal/ordinal/interval/ratio), data quality audit (missing values, silent type errors) |
| Preprocessing | Cleaning, feature engineering (tenure bucketing), categorical encoding |
| Classification | Decision trees (with manual Gini calculation), pruning via depth control, Naive Bayes, SVM |
| Evaluation | Train/test split, precision/recall/F1, confusion matrix, ROC curves, AUC — chosen deliberately over raw accuracy because the target class is imbalanced |
| Pattern mining | Association rule mining (Apriori) over service/contract combinations, ranked by support, confidence, and lift |
| Segmentation | K-means clustering on tenure/spend, elbow method for choosing k |

## How to run it

**Option A — Google Colab (recommended, zero setup):**

1. Go to [colab.research.google.com](https://colab.research.google.com)
2. File → Open notebook → GitHub tab → paste this repo's URL
3. Open `notebooks/01_churn_analysis.ipynb`
4. Runtime → Run all

The dataset loads directly from a URL in the first cells — nothing to upload.

**Option B — locally:**

```bash
git clone https://github.com/<your-username>/telco-churn-datamining.git
cd telco-churn-datamining
pip install -r requirements.txt
jupyter notebook notebooks/01_churn_analysis.ipynb
```

## Status

This notebook is a **working template with guided TODOs**, not a finished report — it's designed to be completed section by section as a learning exercise. Sections 1–6 are ready to work through now; Section 7 (clustering) is scaffolded ahead of where the course curriculum reaches it, to keep the project structure complete.

## License

Code in this repo: MIT. Dataset: IBM Telco Customer Churn (public sample dataset, see IBM's repo for terms).
