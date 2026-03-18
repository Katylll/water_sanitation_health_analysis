import pandas as pd # type: ignore
import seaborn as sns # type: ignore
import matplotlib.pyplot as plt # type: ignore
from sqlalchemy import create_engine # type: ignore

engine = create_engine("postgresql+psycopg2://postgres:123456@localhost:5432/Mini project")

query = "SELECT * FROM water_quality_risk_scores_sanitation_healthcare"
df_risk = pd.read_sql(query, engine)


df_risk['year'] = df_risk['year'].astype(int)
df_risk.sort_values(by=['country_name', 'year'], inplace=True)

plt.figure(figsize=(12, 6))
sns.lineplot(data=df_risk, x='year', y='avg_turbidity', hue='country_name', marker='o')
plt.title("Turbidity Over Time by Country")
plt.ylabel("Turbidity (NTU)")
plt.grid(True, linestyle='--', alpha=0.4)
plt.tight_layout()
plt.savefig("turbidity_over_time.png")
plt.show()

plt.figure(figsize=(12, 6))
sns.lineplot(data=df_risk, x='year', y='avg_dissolved_oxygen', hue='country_name', marker='o')
plt.title("Dissolved Oxygen Over Time by Country")
plt.ylabel("Dissolved Oxygen (mg/L)")
plt.tight_layout()
plt.savefig("oxygen_over_time.png")
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=df_risk,
    x='avg_sanitation_coverage',
    y='risk_score',
    size='avg_healthcare_access',
    hue='country_name',
    sizes=(50, 500),
    alpha=0.7
)
plt.title("Sanitation Coverage vs Risk Score (Bubble = Healthcare Access)")
plt.xlabel("Sanitation Coverage (%)")
plt.ylabel("Risk Score")
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig("sanitation_vs_risk_bubble.png")
plt.show()

g = sns.lmplot(
    data=df_risk,
    x="avg_sanitation_coverage",
    y="risk_score",
    hue="country_name",
    col="country_name",
    col_wrap=3,
    height=4.2,
    aspect=1.1,
    scatter_kws={"alpha": 0.6},
    line_kws={"color": "red"}
)
g.set_axis_labels("Sanitation Coverage (%)", "Risk Score")
g.set_titles("{col_name}")
g.fig.subplots_adjust(top=0.92, bottom=0.1, hspace=0.3, wspace=0.2)
g.fig.suptitle("Sanitation Coverage vs Risk Score by Country", fontsize=16)
plt.savefig("sanitation_vs_risk_facet.png", bbox_inches="tight")
plt.show()
