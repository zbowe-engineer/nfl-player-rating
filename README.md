# Author, Credits
Author:
Zachary Bowe
Machine Learning & Embedded Systems Engineer
GitHub: https://github.com/zbowe-engineer

# NFL Player Rating Model

This project builds a machine learning model to evaluate NFL player performance using multi‑year data from nfl_data_py (official NFL FastR data) and Spotrac salary cap information.
The goal is to create a reproducible, data‑driven rating system that compares players across seasons, positions, and statistical categories — and ultimately identifies under‑ and over‑valued players.

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
  src/            - Python scripts (data downloader lives here)
  data/           - Downloaded CSV files (ignored by Git)
  notebooks/      - Jupyter notebooks for analysis
  venv/           - Virtual environment (ignored by Git)
  .gitignore
  README.md
  
---

# Data Source

NFL Statistics (2019–2024)
Pulled from nfl_data_py, which provides:
• 	Weekly player stats
• 	Season‑level summaries
• 	Player metadata (name, position, team, ID)
This ensures stable, legal, reproducible data ingestion without scraping.
Salary Cap Data (2019–2024)
Downloaded from Spotrac using , including:
• 	Player cap hit
• 	Cap hit percentage
• 	Team
• 	Season
All salary data is cleaned and standardized during the merge process.

# Future Work
TBA

