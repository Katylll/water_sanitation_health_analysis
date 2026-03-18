
import pandas as pd # type: ignore
from sqlalchemy import create_engine # type: ignore
import db_config as cfg

engine = create_engine(f'postgresql+psycopg2://{cfg.DB_USER}:{cfg.DB_PASSWORD}@{cfg.DB_HOST}:{cfg.DB_PORT}/{cfg.DB_NAME}')
conn = engine.connect()

def get_country_id_map():
    country_df = pd.read_sql("SELECT * FROM country", conn)
    return dict(zip(country_df['country_name'], country_df['country_id']))

def load_country_data():
    df = pd.read_csv('data/CountryReference.csv')
    df.rename(columns={'Name': 'country_name'}, inplace=True)  # Only if needed
    df = df[['country_name']]
    df.drop_duplicates(subset=['country_name'], inplace=True)

    existing_df = pd.read_sql("SELECT country_name FROM country", conn)
    existing_countries = set(existing_df['country_name'].tolist())
    df = df[~df['country_name'].isin(existing_countries)]

    if not df.empty:
        df.to_sql('country', engine, if_exists='append', index=False)
        print("✅ country table loaded.")
    else:
        print("✅ All countries already exist, no new insert needed.")



def load_table(csv_file, table_name):
    df = pd.read_csv(f'data/{csv_file}')
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

    if 'countryid' in df.columns:
        df.rename(columns={'countryid': 'country_id'}, inplace=True)

    if table_name == "climate_indicators":
        df.rename(columns={
            "temperature_(°c)": "temperature",
            "rainfall_(mm_per_year)": "rainfall"
        }, inplace=True)

    if table_name == "socio_economic_indicators":
        df.rename(columns={
            "gdp_per_capita_(usd)": "gdp_per_capita",
            "sanitation_coverage_(%_of_population)": "sanitation_coverage",
            "healthcare_access_index_(0-100)": "healthcare_access_index"
        }, inplace=True)

    if table_name == "water_sources":
        df.rename(columns={
        "access_to_clean_water": "access_to_clean_water_percent",
        "water_treatment_method": "water_treatment"
    }, inplace=True)

    if table_name == "measurements":
        df.rename(columns={
            "bacteria_count": "bacterial_count"
        }, inplace=True)

    df.to_sql(table_name, engine, if_exists='append', index=False)
    print(f"✅ {table_name} table loaded.")


load_country_data()
load_table('climate indicators.csv', 'climate_indicators')  
load_table('social economic indicators.csv', 'socio_economic_indicators')
load_table('population denstiy.csv', 'population_density')
load_table('Measurement.csv', 'measurements')
load_table('water indicators.csv', 'water_sources')
load_table('health indicators.csv', 'health_indicators')
