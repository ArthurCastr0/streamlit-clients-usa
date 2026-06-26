import streamlit as st


def create_filters(df):
    with st.sidebar:
        st.header("Filtres")

        regions = st.multiselect(
            "Région",
            sorted(df["Region"].unique()),
            default=sorted(df["Region"].unique())
        )

        segments = st.multiselect(
            "Segment",
            sorted(df["Segment"].unique()),
            default=sorted(df["Segment"].unique())
        )

        categories = st.multiselect(
            "Catégorie",
            sorted(df["Category"].unique()),
            default=sorted(df["Category"].unique())
        )

        date_range = st.slider(
            "Date de commande",
            min_value=df["Order Date"].min().to_pydatetime(),
            max_value=df["Order Date"].max().to_pydatetime(),
            value=(
                df["Order Date"].min().to_pydatetime(),
                df["Order Date"].max().to_pydatetime()
            )
        )

    filtered_df = df[
        (df["Region"].isin(regions)) &
        (df["Segment"].isin(segments)) &
        (df["Category"].isin(categories)) &
        (df["Order Date"] >= date_range[0]) &
        (df["Order Date"] <= date_range[1])
    ]

    return filtered_df