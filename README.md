# Pandas Fundamentals

A complete, structured practice repository covering Pandas from basics to advanced data manipulation — built as part of a hands-on journey in Machine Learning and Data Science.

---

## 📌 About This Repository

This repository covers all core Pandas concepts with real CSV datasets. Each script is focused on one topic, numbered in learning order, and written with clear comments. Pandas is the most important library for data analysis and is used in every Machine Learning pipeline.

---

## 📁 Repository Structure

```
pandas-fundamentals/
│
├── scripts/
│   ├── basics/
│   │   ├── 01_series.py                   # Series creation, indexing, operations
│   │   ├── 02_dataframe.py                # DataFrame creation from list and dict
│   │   └── 03_arithmetic_operations.py    # Column operations and computed fields
│   │
│   ├── data_cleaning/
│   │   ├── 04_missing_values.py           # dropna, fillna, ffill, bfill
│   │   └── 05_missing_values_advanced.py  # replace, interpolate
│   │
│   ├── data_manipulation/
│   │   ├── 06_groupby.py                  # GroupBy, aggregation functions
│   │   ├── 07_merge_concat.py             # merge, concat with join types
│   │   ├── 08_join_append.py              # join, append DataFrames
│   │   └── 09_insert_delete.py            # insert, pop, drop columns
│   │
│   ├── file_handling/
│   │   ├── 10_read_csv.py                 # read_csv with all parameters
│   │   ├── 11_csv_basic.py                # to_csv, write options
│   │   └── 12_csv_functions.py            # describe, head, tail, loc, sort
│   │
│   └── analysis/
│       └── 13_pivot_table.py              # pivot, melt, reshape data
│
├── data/
│   └── raw/
│       ├── panda_practise.csv             # Main dataset for file handling
│       └── panda_practise2.csv            # Dataset with missing values
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧠 Topics Covered

| # | Topic | Key Concepts |
|---|-------|-------------|
| 01 | Series | Creation, custom index, dtype, operations |
| 02 | DataFrame | From list, dict, column selection, cell access |
| 03 | Arithmetic Operations | Computed columns, conditions, percentage |
| 04 | Missing Values | dropna, fillna, ffill, limit |
| 05 | Advanced Missing Values | replace, interpolate, limit_direction |
| 06 | GroupBy | groupby, get_group, min, max, sum, mean |
| 07 | Merge & Concat | inner/outer merge, indicator, concat axis |
| 08 | Join & Append | left/outer join, append rows |
| 09 | Insert & Delete | insert, pop, drop columns |
| 10 | Read CSV | nrows, usecols, skiprows, index_col, header |
| 11 | Write CSV | to_csv, index, custom headers |
| 12 | CSV Functions | describe, head, tail, loc, sort_index |
| 13 | Pivot & Melt | pivot table, melt wide to long |

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)

---

## 🚀 How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/Arifkhan171/pandas-fundamentals.git
cd pandas-fundamentals
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Run any script:**
```bash
python scripts/basics/01_series.py
python scripts/data_cleaning/04_missing_values.py
```

---

## 👤 Author

**Arif Khan**
Final Year CS Student | University of Loralai | ML • Deep Learning • Agentic AI

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin)](https://www.linkedin.com/in/arif-khan-71a711376)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github)](https://github.com/Arifkhan171)

---

> ⭐ Part of a complete Data Science & AI portfolio — from Pandas basics to Agentic AI systems.
