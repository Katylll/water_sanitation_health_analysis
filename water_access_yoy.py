import pandas as pd # type: ignore
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore

from sqlalchemy import create_engine # type: ignore
engine = create_engine("postgresql+psycopg2://postgres:123456@localhost:5432/Mini project")

query = "SELECT * FROM water_access_yoy_by_source"
df_access = pd.read_sql(query, engine)

df_access['year'] = df_access['year'].astype(int)
df_access['avg_clean_water_access_percent'] = df_access['avg_clean_water_access_percent'].astype(float)
df_access.sort_values(by=['country_name', 'water_source_type', 'year'], inplace=True)

df_heat = df_access.pivot_table(index='country_name', columns='year', values='yoy_change')
plt.figure(figsize=(14, 6))
sns.heatmap(df_heat, annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)
plt.title("Year-over-Year Change in Water Access (%) by Country")
plt.xlabel("Year")
plt.ylabel("Country")
plt.tight_layout()
plt.savefig("heatmap_yoy_change.png")
plt.show()

g = sns.relplot(
    data=df_access,
    x="year", y="avg_clean_water_access_percent",
    col="country_name", hue="water_source_type",
    kind="line", marker="o", col_wrap=3,
    facet_kws={'sharey': False}
)
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle("Access to Clean Water by Source Over Time (Each Country)")
plt.savefig("facet_access_by_country_source.png", bbox_inches='tight')
plt.show()
