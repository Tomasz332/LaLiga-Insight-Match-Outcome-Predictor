# ⚽ LaLiga Insight: Football Match Outcome Predictor

*Predicting Victory, Empowering Winning Strategies Instantly*

![Last Commit](https://img.shields.io/github/last-commit/sanidavidanagama/LaLiga-Insight-Match-Outcome-Predictor?style=flat-square)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=flat-square&logo=jupyter)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)

Built with the tools and technologies:  
`Python` · `Jupyter Notebook` · `scikit-learn` · `BeautifulSoup` · `pandas`

---

## 📑 Table of Contents
- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Testing](#testing)
- [Data Sources](#-data-sources)
- [License](#-license)

---

## 📖 Overview
**LaLiga Insight: Match Outcome Predictor** is a developer-focused tool designed to forecast football match results using historical LaLiga data and machine learning.  
It integrates scraping, preprocessing, and predictive modeling into a streamlined workflow, enabling accurate and scalable sports analytics.

---

## ✨ Features
- 🔎 **Data Collection**: Automated scraping and consolidation of diverse sports data sources.  
- 📊 **Predictive Modeling**: Logistic regression models classify match outcomes with high accuracy.  
- 🧹 **Data Preprocessing**: Ensures quality and consistency via cleaning, transformation, and scaling.  
- 🧩 **Modular Architecture**: Designed for easy extension and integration into analytics pipelines.  
- 📈 **Analytical Insights**: Generates probabilistic forecasts to support informed decision-making.  

---

## 📂 Project Structure
```bash
LaLiga-Insight-Match-Outcome-Predictor/
├── src/ # Deployable prediction script
│ └── Match_Predictor.py
├── notebooks/ # Exploration, preprocessing, modeling, scraping
├── models/ # Trained models + scalers
├── data/ # Raw, interim, and processed data
├── requirements.txt # Dependencies
└── README.md # Documentation
```

## 🚀 Getting Started

### Prerequisites
- **Programming Language**: Python 3.10+  
- **Package Manager**: Pip  

### Installation
Clone the repository and install dependencies:



#### Clone repo
```bash
git clone https://github.com/sanidavidanagama/LaLiga-Insight-Match-Outcome-Predictor.git
```

#### Navigate to directory
```
cd LaLiga-Insight-Match-Outcome-Predictor
```

#### Install dependencies
```
pip install -r requirements.txt
```

#### Usage
Run predictions on a fixture CSV:

```bash
python src/Match_Predictor.py --input data/processed/2025-season-fix.csv
```

#### Testing
Run the test suite with:
```bash
pytest
```
  
---


## 📊 Data Sources
[FBRef](https://fbref.com/en/comps/12/history/La-Liga-Seasons) – Advanced football statistics  
[Transfermarkt](https://www.transfermarkt.com/laliga/gesamtspielplan/wettbewerb/ES1?saison_id=2024&spieltagVon=1&spieltagBis=38) – Historical fixtures and results

---
     
## 📜 License
Distributed under the MIT LICENSE  
See [LICENSE](https://github.com/sanidavidanagama/LaLiga-Insight-Match-Outcome-Predictor/blob/main/LICENSE) for more information.

---

## 👤 Author

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sanida%20Vidanagama-blue?style=flat-square&logo=linkedin)](https://www.linkedin.com/in/sanida-vidanagama-246a14297/)
[![Kaggle](https://img.shields.io/badge/Kaggle-Sanida%20Vidanagama-20BEFF?style=flat-square&logo=kaggle)](https://www.kaggle.com/sanidavidanagama)
[![GitHub](https://img.shields.io/badge/GitHub-sanidavidanagama-181717?style=flat-square&logo=github)](https://github.com/sanidavidanagama)
[![Email](https://img.shields.io/badge/Email-sanidavidanagama%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:sanidavidanagama@gmail.com)
