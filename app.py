import streamlit as st

from config import DATA_PATH
from data.loader import load_data
from components.filters import create_filters
from components.kpis import display_kpis
from components.charts import *

st.set_page_config(
    page_title="Analyse Clients Arthur CASTRO-CINTAS",
    layout="wide"
)

st.title("Analyse des clients")
st.markdown("---")

df = load_data(DATA_PATH)

df = create_filters(df)

display_kpis(df)

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        top_sales_customers(df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        top_profit_customers(df),
        use_container_width=True
    )

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        top_states_profit(df),
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        monthly_sales(df),
        use_container_width=True
    )

st.markdown("---")

st.subheader("Données détaillées")

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)