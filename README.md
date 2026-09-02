# AI Market Intelligence & Automated Anomaly Pipeline

An end-to-end data engineering and business intelligence project that automates data cleaning, performs statistical anomaly detection on global AI company metrics, and feeds live data into a Power BI dashboard.

## 🚀 Project Architecture & Workflow
1. **Data Ingestion & Preprocessing:** Python and Pandas ingest raw market data, handle missing values via median imputation, and clean data types.
2. **Statistical Anomaly Detection:** Applies Z-score calculations on financial metrics (such as Annual R&D Spend) to automatically flag extreme outliers and high-spender companies.
3. **Daily Cloud Automation:** Powered by **GitHub Actions**, a scheduled cron job runs the cleaning script daily at 09:00 UTC, automatically updating and committing the processed dataset back to the repository.
4. **Business Intelligence:** Seamlessly integrated with **Power BI** via direct raw links to track real-time trends, active users, model parameters, and anomaly flags.

## 🛠️ Tech Stack
* **Language:** Python (Pandas, Datetime)
* **Automation & CI/CD:** GitHub Actions (Cron Scheduling)
* **Version Control:** Git & GitHub Codespaces
* **Visualization:** Power BI Desktop

## 📂 Repository Structure
```text
ai-market-intelligence-pipeline/
│
├── .github/
│   └── workflows/
│       └── automation.yml      # Daily GitHub Actions workflow
├── data/
│   ├── ai_companies_raw.csv    # Raw Kaggle dataset
│   └── processed_ai_data.csv   # Cleaned dataset with anomaly flags
├── scripts/
│   └── pipeline.py             # Data cleaning & Z-score anomaly script
└── README.md
