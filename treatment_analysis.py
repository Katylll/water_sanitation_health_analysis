import pandas as pd # type: ignore
import matplotlib.pyplot as plt # type: ignore
import seaborn as sns # type: ignore
from sqlalchemy import create_engine # type: ignore

engine = create_engine("postgresql+psycopg2://postgres:123456@localhost:5432/Mini project")

query = "SELECT * FROM treatment_effectiveness_summary"
df_treatment = pd.read_sql(query, engine)

print(df_treatment.head())
df_treatment['year'] = df_treatment['year'].astype(int)
df_treatment.sort_values(by=['country_name', 'year'], inplace=True)

plt.figure(figsize=(10, 6))
sns.boxplot(data=df_treatment, x='water_treatment', y='avg_bacterial_count', hue='water_source_type')
plt.title("Bacteria Levels by Treatment Type and Water Source")
plt.ylabel("Bacterial Count (CFU/ml)")
plt.xlabel("Treatment Method")
plt.legend(title="Source Type")
plt.tight_layout()
plt.savefig("bacteria_by_treatment.png")
plt.show()

sns.set(style="whitegrid")
g = sns.lmplot(
    data=df_treatment,
    x="avg_clean_water_access",
    y="effectiveness_score",
    col="country_name",
    col_wrap=3,
    height=4,
    aspect=1.2,
    scatter_kws={'alpha': 0.6, 's': 50},
    line_kws={'color': 'red'},
    truncate=False,
    markers='o'
)
g.set_axis_labels("Access to Clean Water (%)", "Effectiveness Score")
g.set_titles("{col_name}")
g.fig.subplots_adjust(top=0.92)
g.fig.suptitle("Access to Clean Water vs Effectiveness Score (by Country)", fontsize=16)
plt.savefig("facet_regression_access_vs_score_by_country.png", bbox_inches="tight")
plt.show()

plt.figure(figsize=(10, 6))
sns.lineplot(data=df_treatment, x='year', y='effectiveness_score', hue='country_name', marker='o')
plt.title("Treatment Effectiveness Score Over Time")
plt.ylabel("Score")
plt.xlabel("Year")
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig("score_over_time_by_country.png")
plt.show()