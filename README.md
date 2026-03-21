# NFL Player Rating Model

This project builds a machine learning model to evaluate NFL player performance using multi-year data from Pro Football Reference (PFR). The goal is to create a reproducible, data-driven rating system that compares players across seasons, positions, and statistical categories.

---

# Project Overview

This project includes:

- Automated data collection from Pro Football Reference  
- Clean, organized project structure for analysis and modeling  
- Reproducible environment using a Python virtual environment  
- Scripts for downloading passing, rushing, receiving, defensive, and salary data  
- Future notebooks for data cleaning, feature engineering, and model development  

---
# Project Structure

NFL_Player_Rating/
  src/            - Python scripts (PFR downloader lives here)
  data/           - Downloaded CSV files (ignored by Git)
  notebooks/      - Jupyter notebooks for analysis
  venv/           - Virtual environment (ignored by Git)
  .gitignore
  README.md
  
---

# Data Source

All data is downloaded directly from **Pro Football Reference** using `pandas.read_html`.  
No raw data is stored in this repository — it is generated locally via the script.

---

