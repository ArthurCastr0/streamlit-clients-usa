import pandas as pd
import streamlit as st


@st.cache_data
def load_data(path):
    df = pd.read_csv(path, encoding="latin-1")

    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])

    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

    return df