import plotly.express as px


def top_sales_customers(df):
    data = (
        df.groupby("Customer Name", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
    )

    fig = px.bar(
        data,
        x="Sales",
        y="Customer Name",
        orientation="h",
        color="Sales",
        color_continuous_scale="Blues",
        title="Top 10 clients par chiffre d'affaires"
    )

    fig.update_layout(yaxis=dict(categoryorder="total ascending"))

    return fig


def top_profit_customers(df):
    data = (
        df.groupby("Customer Name", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
        .head(10)
    )

    fig = px.bar(
        data,
        x="Profit",
        y="Customer Name",
        orientation="h",
        color="Profit",
        color_continuous_scale="Greens",
        title="Top 10 clients les plus profitables"
    )

    fig.update_layout(yaxis=dict(categoryorder="total ascending"))

    return fig


def top_states_profit(df):
    data = (
        df.groupby("State", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
        .head(10)
    )

    fig = px.bar(
        data,
        x="Profit",
        y="State",
        orientation="h",
        color="Profit",
        color_continuous_scale="Viridis",
        title="Top 10 des États les plus profitables"
    )

    fig.update_layout(yaxis=dict(categoryorder="total ascending"))

    return fig


def monthly_sales(df):
    data = df.copy()

    data["Month"] = data["Order Date"].dt.to_period("M").astype(str)

    data = (
        data.groupby("Month", as_index=False)["Sales"]
        .sum()
    )

    fig = px.line(
        data,
        x="Month",
        y="Sales",
        markers=True,
        title="Évolution du chiffre d'affaires"
    )

    return fig