# 💧 Water Quality & Health Analytics Dashboard

A data-driven system that explores the link between water pollution, socio-economic indicators, and public health outcomes across 10 countries. Built with PostgreSQL, Python ETL, and an interactive Streamlit dashboard.

---

## 📌 Project Overview

Water pollution is one of the top global health crises, particularly in regions with limited infrastructure. This project builds a relational database and analytics pipeline to uncover patterns between water contamination, treatment effectiveness, economic factors, and waterborne disease rates.

**Target users:**
- 🌍 Environmental economists — studying pollution trends and advising on policy
- 🏗️ Infrastructure planners — deciding where to improve water systems
- 🛠️ Technical developers — maintaining and extending the system

---

## 🗂️ Repository Structure

```
water-quality-analysis/
│
├── data/                          # Raw CSV source files
│   ├── Climate indicators.csv
│   ├── CountryReference.csv
│   ├── Health indicators.csv
│   ├── Measurement.csv
│   ├── Population density.csv
│   ├── Social economic indicators.csv
│   └── Water indicators.csv
│
├── sql/                           # SQL queries and exported results
│   ├── query_1_pollution_health.sql
│   ├── query_1_pollution_health.csv
│   ├── query_2_gdp_water_access.sql
│   ├── query_2_gdp_water_access.csv
│   ├── query_3_risk_scores.sql
│   ├── query_3_risk_scores.csv
│   ├── query_4_treatment_effectiveness.sql
│   ├── query_4_treatment_effectiveness.csv
│   ├── query_5_yoy_water_access.sql
│   └── query_5_yoy_water_access.csv
│
├── plots/                         # Generated visualisations
│   ├── contaminants/
│   │   ├── correlation_heatmap.png
│   │   └── diarrheal_cases_by_country.png
│   ├── gdp_water_access/
│   │   ├── access_to_clean_water_all_countries.png
│   │   └── gdp_per_capita_all_countries.png
│   ├── risk_scores/
│   │   ├── oxygen_over_time.png
│   │   ├── sanitation_vs_risk_bubble.png
│   │   ├── sanitation_vs_risk_facet.png
│   │   └── turbidity_over_time.png
│   ├── treatments/
│   │   ├── bacteria_by_treatment.png
│   │   ├── facet_regression_access_vs_score_by_country.png
│   │   └── score_over_time_by_country.png
│   └── yoy_water_access/
│       ├── heatmap_yoy_change.png
│       └── facet_access_by_country_source.png
│
├── db_config.py                   # Database connection settings
├── database_config.py             # SQLAlchemy engine helper
├── etl.py                         # ETL pipeline (load CSVs → PostgreSQL)
├── etl_analysis.py                # Exploratory analysis scripts
├── risk_score_analysis.py         # Risk score visualisations
├── treatment_analysis.py          # Treatment effectiveness visualisations
├── water_access_yoy.py            # Year-over-year water access visualisations
├── app.py                         # Streamlit dashboard
├── requirements.txt               # Python dependencies
└── README.md
```

---

## 🗃️ Database Design

The database uses a **normalised relational schema** (up to 3NF) implemented in PostgreSQL, optimised for OLAP-style analytical queries.

**Core tables:**

| Table | Description |
|---|---|
| `country` | Country reference data |
| `water_sources` | Water source types and access percentages |
| `measurements` | pH, turbidity, bacterial count, dissolved oxygen, nitrates, lead |
| `health_indicators` | Diarrheal and cholera cases per 100,000 people |
| `climate_indicators` | Temperature and annual rainfall |
| `socio_economic_indicators` | GDP per capita, sanitation coverage, healthcare access |
| `population_density` | Population density by country and year |

**Analytical views:**

| View | Purpose |
|---|---|
| `pollution_health_summary` | Links contaminants with health outcomes |
| `gdp_vs_water_access` | Compares GDP per capita with clean water access |
| `water_quality_risk_scores_sanitation_healthcare` | Composite environmental risk score |
| `treatment_effectiveness_summary` | Treatment method vs bacterial count reduction |
| `water_access_yoy_by_source` | Year-over-year change in water access by source type |

---

## ⚙️ Setup Instructions

### Prerequisites

- Python 3.11+
- PostgreSQL (with a database named `Mini project`)
- `pgAdmin 4` (optional, for running SQL queries manually)

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/water-quality-analysis.git
cd water-quality-analysis
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the database

Edit `db_config.py` with your PostgreSQL credentials:

```python
DB_USER = "postgres"
DB_PASSWORD = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "Mini project"
```

### 5. Create the database schema

Run the SQL schema script in pgAdmin 4 or via psql to create all tables and views before loading data.

### 6. Run the ETL pipeline

```bash
python etl.py
```

This loads all CSV files from the `data/` folder into PostgreSQL.

### 7. Launch the dashboard

```bash
streamlit run app.py
```

---

## 📊 Dashboard Sections

| Section | What it shows |
|---|---|
| **Overview** | Project summary and dataset stats |
| **Contaminants** | Correlation between nitrate/lead levels and disease cases; diarrheal cases by country |
| **Water Access Gaps** | GDP vs clean water access scatter; access and GDP trends over time |
| **Water Quality Risk Scores** | Turbidity and dissolved oxygen over time; sanitation coverage vs risk score bubble chart |
| **Treatment Effectiveness** | Bacterial count by treatment type; access vs effectiveness score; trends over time |
| **Year-over-Year Water Access** | YoY change heatmap by country; water access by source type over time |

---

## 🧪 Running Analysis Scripts Standalone

To regenerate the saved plots without the dashboard:

```bash
python risk_score_analysis.py      # Risk score visualisations
python treatment_analysis.py       # Treatment effectiveness charts
python water_access_yoy.py         # YoY water access charts
python etl_analysis.py             # GDP and contaminant exploratory analysis
```

---

## 📦 Requirements

```
streamlit
pandas
sqlalchemy
psycopg2-binary
plotly
seaborn
matplotlib
```

Generate with:
```bash
pip freeze > requirements.txt
```

---

## 🔒 Security Note

The `db_config.py` file contains database credentials. Before pushing to GitHub, either:
- Add `db_config.py` to `.gitignore` and provide a `db_config.example.py` template, or
- Replace credentials with environment variables using `os.environ`

---

## 👩‍💻 Author

Built by Katy as a mini-project exploring water pollution, public health, and socio-economic data across 10 countries.
