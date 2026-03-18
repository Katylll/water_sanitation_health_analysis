from sqlalchemy import create_engine # type: ignore
import pandas as pd # type: ignore

# Database credentials (replace these)
db_user = 'postgres'
db_password = '123456'
db_host = 'localhost'
db_port = '5432'
db_name = 'Mini project'


engine = create_engine(f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

# query = "SELECT * FROM pollution_health_summary"

# df = pd.read_sql(query, engine)

# print(df.head())  # Check data
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
# print(df.info())
# print(df.describe())
# print(df.head())
# df_sorted = df.sort_values(by='avg_diarrheal_cases', ascending=False)

# # plt.figure(figsize=(12, 6))
# # sns.barplot(data=df_sorted, x='country_name', y='avg_diarrheal_cases', palette='Blues_d')
# # plt.title("Average Diarrheal Cases per 100,000 People by Country")
# # plt.xticks(rotation=45)
# # plt.ylabel("Avg Diarrheal Cases")
# # plt.tight_layout()
# # plt.savefig("diarrheal_cases_by_country.png")
# # plt.show()

# plt.figure(figsize=(8, 6))
# corr = df[['avg_nitrate', 'avg_lead', 'avg_diarrheal_cases', 'avg_cholera_cases']].corr()
# sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
# plt.title("Correlation Between Water Pollutants and Disease Cases")
# plt.tight_layout()
# plt.savefig("correlation_heatmap.png")
# plt.show()


query2 = "SELECT * FROM gdp_vs_water_access"  
df_gdp_water = pd.read_sql(query2, engine)
print(df_gdp_water.head())
df_gdp_water['year'] = df_gdp_water['year'].astype(int)
df_gdp_water.sort_values(by=['country_name', 'year'], inplace=True)

# plt.figure(figsize=(8, 6))
# sns.scatterplot(data=df_gdp_water, x='avg_gdp_per_capita', y='access_to_clean_water_percent', hue='year', palette='viridis', s=100)
# plt.title("GDP Per Capita vs Access to Clean Water (Bangladesh)")
# plt.xlabel("GDP Per Capita")
# plt.ylabel("Access to Clean Water (%)")
# plt.tight_layout()
# plt.savefig("gdp_vs_clean_water.png")
# plt.show()
import matplotlib.ticker as mtick # type: ignore

# plt.figure(figsize=(12, 6))
# sns.lineplot(data=df_gdp_water, x='year', y='access_to_clean_water_percent', hue='country_name', marker='o', palette='tab10')
# plt.title("Access to Clean Water Over Time (2000–2025)")
# plt.xlabel("Year")
# plt.ylabel("Access to Clean Water (%)")
# plt.ylim(0, 100)
# plt.grid(True, linestyle='--', alpha=0.4)
# plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.tight_layout()
# plt.savefig("access_to_clean_water_all_countries.png")
# plt.show()

# plt.figure(figsize=(12, 6))
# sns.lineplot(data=df_gdp_water, x='year', y='avg_gdp_per_capita', hue='country_name', marker='s', palette='tab10')
# plt.title("GDP Per Capita Over Time (2000–2025)")
# plt.xlabel("Year")
# plt.ylabel("GDP Per Capita (USD)")
# plt.grid(True, linestyle='--', alpha=0.4)
# plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.tight_layout()
# plt.savefig("gdp_per_capita_all_countries.png")
# plt.show()