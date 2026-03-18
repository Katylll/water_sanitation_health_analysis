import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import plotly.express as px  # type: ignore
from sqlalchemy import create_engine  # type: ignore

# DB Connection
engine = create_engine("postgresql+psycopg2://postgres:123456@localhost:5432/Mini project")

st.set_page_config(page_title="Water Quality & Health Dashboard", layout="wide")
st.title("🌍 Water Quality, Treatment & Health Analytics Dashboard")
st.markdown("---")

# Sidebar menu
view_option = st.sidebar.selectbox(
    "Select Visualization Section:",
    (
        "Overview",
        "Contaminants",
        "Water Access Gaps",
        "Water Quality Risk Scores",
        "Treatment Effectiveness",
        "Year-over-Year Water Access"
    )
)


# Overview Page
if view_option == "Overview":
    st.markdown("This dashboard explores water pollution, treatment, and public health across multiple countries using data from the 'Mini Project' PostgreSQL database.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total Countries Tracked", value=10)
        st.metric(label="Views Created", value=5)
    with col2:
        st.metric(label="Dataset Records", value="~5,000")
        st.metric(label="Last Update", value="2025-06-11")
    with col3:
        st.metric(label="Visualization Files", value=25)

# Section 1: Contaminants
elif view_option == "Contaminants":
    st.subheader("🧪 Contaminants and Waterborne Diseases")
    query_contaminants = "SELECT * FROM pollution_health_summary"
    df_contaminants = pd.read_sql(query_contaminants, engine)

    st.markdown("### 🔬 Correlation Between Water Contaminants and Disease Cases")
    corr = df_contaminants[["avg_nitrate", "avg_lead", "avg_diarrheal_cases", "avg_cholera_cases"]].corr()
    fig_corr = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale='RdBu_r',
        title="Contaminants vs Disease Correlation"
    )
    st.plotly_chart(fig_corr, use_container_width=True)

    st.markdown("### 💡 Avg Diarrheal Cases per 100,000 People by Country")
    df_sorted = df_contaminants.sort_values(by='avg_diarrheal_cases', ascending=False)
    fig_bar = px.bar(
        df_sorted,
        x='country_name',
        y='avg_diarrheal_cases',
        color='avg_diarrheal_cases',
        color_continuous_scale='Blues',
        title="Average Diarrheal Cases per 100,000 People by Country"
    )
    fig_bar.update_layout(
        xaxis_title="Country",
        yaxis_title="Avg Diarrheal Cases",
        xaxis_tickangle=-45
    )
    st.plotly_chart(fig_bar, use_container_width=True)


# Section 2: Water Access Gaps
elif view_option == "Water Access Gaps":
    st.subheader("💰 GDP vs Water Access")
    query_gdp = "SELECT * FROM gdp_vs_water_access"
    df_gdp = pd.read_sql(query_gdp, engine)
    df_gdp['year'] = df_gdp['year'].astype(int)

    selected_country = st.selectbox("Select a country:", df_gdp["country_name"].unique())
    df_country = df_gdp[df_gdp["country_name"] == selected_country]

    st.markdown("### GDP vs Access to Clean Water")
    fig_scatter = px.scatter(
        df_country,
        x="avg_gdp_per_capita",
        y="access_to_clean_water_percent",
        color="year",
        size="avg_gdp_per_capita",
        title=f"{selected_country} – GDP vs Water Access"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    st.markdown("### 📈 Access to Clean Water Over Time")
    fig_access = px.line(
        df_gdp,
        x="year",
        y="access_to_clean_water_percent",
        color="country_name",
        markers=True,
        title="Access to Clean Water Over Time"
    )
    st.plotly_chart(fig_access, use_container_width=True)

    st.markdown("### 💹 GDP Per Capita Over Time")
    fig_gdp = px.line(
        df_gdp,
        x="year",
        y="avg_gdp_per_capita",
        color="country_name",
        markers=True,
        title="GDP Per Capita Over Time"
    )
    st.plotly_chart(fig_gdp, use_container_width=True)

# Section 3: Risk Scores
elif view_option == "Water Quality Risk Scores":
    st.subheader("⚠️ Water Quality Risk Scores")
    query = "SELECT * FROM water_quality_risk_scores_sanitation_healthcare"
    df_risk = pd.read_sql(query, engine)
    df_risk['year'] = df_risk['year'].astype(int)

    st.markdown("### Turbidity Over Time")
    fig_turbidity = px.line(df_risk, x="year", y="avg_turbidity", color="country_name", markers=True)
    st.plotly_chart(fig_turbidity, use_container_width=True)

    st.markdown("### Dissolved Oxygen Over Time")
    fig_oxygen = px.line(df_risk, x="year", y="avg_dissolved_oxygen", color="country_name", markers=True)
    st.plotly_chart(fig_oxygen, use_container_width=True)

    st.markdown("### Sanitation Coverage vs Risk Score (Bubble = Healthcare Access)")
    fig_bubble = px.scatter(
        df_risk, x="avg_sanitation_coverage", y="risk_score",
        size="avg_healthcare_access", color="country_name", size_max=60
    )
    st.plotly_chart(fig_bubble, use_container_width=True)

    st.markdown("### Sanitation Coverage vs Risk Score by Country")
    fig_facet = px.scatter(
        df_risk,
        x="avg_sanitation_coverage",
        y="risk_score",
        color="country_name",
        facet_col="country_name",
        facet_col_wrap=3,
        trendline="ols"
    )
    st.plotly_chart(fig_facet, use_container_width=True)

# Section 4: Treatment
elif view_option == "Treatment Effectiveness":
    st.subheader("🧪 Treatment Effectiveness")
    query = "SELECT * FROM treatment_effectiveness_summary"
    df_treatment = pd.read_sql(query, engine)
    df_treatment['year'] = df_treatment['year'].astype(int)

    st.markdown("### Bacteria Levels by Treatment Type and Water Source")
    fig_box = px.box(
        df_treatment,
        x='water_treatment',
        y='avg_bacterial_count',
        color='water_source_type',
        points="all"
    )
    st.plotly_chart(fig_box, use_container_width=True)

    st.markdown("### Access to Clean Water vs Effectiveness Score (by Country)")
    fig_reg = px.scatter(
        df_treatment,
        x="avg_clean_water_access",
        y="effectiveness_score",
        color="country_name",
        trendline="ols",
        facet_col="country_name",
        facet_col_wrap=3
    )
    st.plotly_chart(fig_reg, use_container_width=True)

    st.markdown("### Treatment Effectiveness Score Over Time")
    fig_line = px.line(
        df_treatment,
        x="year",
        y="effectiveness_score",
        color="country_name",
        markers=True
    )
    st.plotly_chart(fig_line, use_container_width=True)

# Section 5: Year-over-Year Water Access
elif view_option == "Year-over-Year Water Access":
    st.subheader("📊 Year-over-Year Change in Clean Water Access")

    query_yoy = "SELECT * FROM water_access_yoy_by_source"
    df_yoy = pd.read_sql(query_yoy, engine)
    df_yoy['year'] = df_yoy['year'].astype(int)
    df_yoy['avg_clean_water_access_percent'] = df_yoy['avg_clean_water_access_percent'].astype(float)
    df_yoy.sort_values(by=['country_name', 'water_source_type', 'year'], inplace=True)

    st.markdown("### 🔥 Year-over-Year Change in Water Access (%) by Country")
    df_heat = df_yoy.pivot_table(index='country_name', columns='year', values='yoy_change')

    fig_heat = px.imshow(
        df_heat,
        color_continuous_scale='RdBu_r',
        labels={'color': "YoY Change (%)"},
        aspect='auto',
        title="YoY Water Access Change by Country"
    )
    st.plotly_chart(fig_heat, use_container_width=True)

    st.markdown("### 📈 Access to Clean Water by Source Over Time")
    fig_facet = px.line(
        df_yoy,
        x="year",
        y="avg_clean_water_access_percent",
        color="water_source_type",
        facet_col="country_name",
        facet_col_wrap=3,
        markers=True,
        title="Water Access by Source Over Time (Each Country)"
    )
    fig_facet.update_yaxes(matches=None)  
    st.plotly_chart(fig_facet, use_container_width=True)


st.markdown("---")
st.caption("Data Source: Mini Project Database | Dashboard by Katy")