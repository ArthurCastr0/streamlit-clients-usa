import streamlit as st


def display_kpis(df):
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_customers = df["Customer ID"].nunique()
    average_order = df.groupby("Order ID")["Sales"].sum().mean()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Chiffre d'affaires", f"${total_sales:,.0f}")

    with col2:
        st.metric("Profit", f"${total_profit:,.0f}")

    with col3:
        st.metric("Clients", total_customers)

    with col4:
        st.metric("Panier moyen", f"${average_order:,.2f}")