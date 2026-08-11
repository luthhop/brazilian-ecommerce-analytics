from __future__ import annotations

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = PROJECT_ROOT / "data" / "processed" / "orders_analytics.csv"


st.set_page_config(
    page_title="Brazilian E-commerce Analytics",
    page_icon=":bar_chart:",
    layout="wide",
)


@st.cache_data(show_spinner=False)
def load_data(path: Path) -> pd.DataFrame:
    if not path.exists():
        st.error(
            "Dataset processado nao encontrado. Execute primeiro o notebook "
            "03_feature_engineering_and_dataset.ipynb."
        )
        st.stop()

    df = pd.read_csv(path)
    date_columns = [
        "order_purchase_timestamp",
        "order_approved_at",
        "order_delivered_carrier_date",
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
    ]

    for column in date_columns:
        df[column] = pd.to_datetime(df[column], errors="coerce")

    df["order_date"] = df["order_purchase_timestamp"].dt.date
    df["is_late_label"] = df["is_late"].map({0.0: "No", 1.0: "Yes"})
    df["main_category"] = df["main_category"].fillna("unknown")
    df["main_payment_type"] = df["main_payment_type"].fillna("unknown")

    return df


def format_currency(value: float) -> str:
    return f"R$ {value:,.2f}"


def format_currency_compact(value: float) -> str:
    if abs(value) >= 1_000_000:
        return f"R$ {value / 1_000_000:.2f}M"
    if abs(value) >= 1_000:
        return f"R$ {value / 1_000:.2f}K"
    return format_currency(value)


def format_pct(value: float) -> str:
    return f"{value:.2f}%"


orders = load_data(DATA_PATH)

st.title("Brazilian E-commerce Analytics")
st.caption("Sales, delivery performance and customer satisfaction analysis")

with st.sidebar:
    st.header("Filters")

    min_date = orders["order_purchase_timestamp"].min().date()
    max_date = orders["order_purchase_timestamp"].max().date()
    selected_dates = st.date_input(
        "Purchase date range",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date,
    )

    if len(selected_dates) == 2:
        start_date, end_date = selected_dates
    else:
        start_date, end_date = min_date, max_date

    status_options = sorted(orders["order_status"].dropna().unique())
    selected_status = st.multiselect(
        "Order status",
        options=status_options,
        default=["delivered"],
    )

    state_options = sorted(orders["customer_state"].dropna().unique())
    selected_states = st.multiselect(
        "Customer state",
        options=state_options,
        default=[],
    )

    category_options = sorted(orders["main_category"].dropna().unique())
    selected_categories = st.multiselect(
        "Main category",
        options=category_options,
        default=[],
    )

filtered = orders[
    (orders["order_date"] >= start_date)
    & (orders["order_date"] <= end_date)
].copy()

if selected_status:
    filtered = filtered[filtered["order_status"].isin(selected_status)]

if selected_states:
    filtered = filtered[filtered["customer_state"].isin(selected_states)]

if selected_categories:
    filtered = filtered[filtered["main_category"].isin(selected_categories)]

if filtered.empty:
    st.warning("No records match the selected filters.")
    st.stop()

total_orders = filtered["order_id"].nunique()
total_revenue = filtered["product_revenue"].sum()
avg_ticket = filtered["product_revenue"].mean()
avg_review = filtered["review_score"].mean()
late_rate = filtered["is_late"].dropna().mean() * 100
avg_delivery = filtered["delivery_days"].mean()

kpi_cols = st.columns(6)
kpi_cols[0].metric("Orders", f"{total_orders:,.0f}")
kpi_cols[1].metric("Product revenue", format_currency_compact(total_revenue))
kpi_cols[2].metric("Avg. ticket", format_currency(avg_ticket))
kpi_cols[3].metric("Avg. review", f"{avg_review:.2f}")
kpi_cols[4].metric("Late rate", format_pct(late_rate))
kpi_cols[5].metric("Avg. delivery", f"{avg_delivery:.1f} days")

st.divider()

monthly = (
    filtered.groupby("order_year_month", as_index=False)
    .agg(
        orders=("order_id", "nunique"),
        product_revenue=("product_revenue", "sum"),
        avg_review=("review_score", "mean"),
    )
    .sort_values("order_year_month")
)

category_revenue = (
    filtered.groupby("main_category", as_index=False)
    .agg(
        orders=("order_id", "nunique"),
        product_revenue=("product_revenue", "sum"),
        late_rate=("is_late", "mean"),
        avg_review=("review_score", "mean"),
    )
    .sort_values("product_revenue", ascending=False)
    .head(10)
)
category_revenue["late_rate"] = category_revenue["late_rate"] * 100

state_revenue = (
    filtered.groupby("customer_state", as_index=False)
    .agg(
        orders=("order_id", "nunique"),
        product_revenue=("product_revenue", "sum"),
        avg_delivery=("delivery_days", "mean"),
        avg_review=("review_score", "mean"),
    )
    .sort_values("product_revenue", ascending=False)
    .head(10)
)

late_review = (
    filtered.dropna(subset=["is_late", "review_score"])
    .groupby("is_late_label", as_index=False)
    .agg(
        orders=("order_id", "nunique"),
        avg_review=("review_score", "mean"),
        avg_delay=("delay_days", "mean"),
    )
)

left_col, right_col = st.columns((1.25, 1))

with left_col:
    fig_monthly = px.line(
        monthly,
        x="order_year_month",
        y="orders",
        markers=True,
        title="Monthly order evolution",
        labels={"order_year_month": "Month", "orders": "Orders"},
    )
    fig_monthly.update_layout(height=420)
    st.plotly_chart(fig_monthly, use_container_width=True)

with right_col:
    fig_late = px.bar(
        late_review,
        x="is_late_label",
        y="avg_review",
        color="is_late_label",
        title="Average review score by delivery delay",
        labels={"is_late_label": "Late delivery?", "avg_review": "Average review"},
        text=late_review["avg_review"].round(2),
    )
    fig_late.update_layout(height=420, showlegend=False, yaxis_range=[0, 5])
    st.plotly_chart(fig_late, use_container_width=True)

left_col, right_col = st.columns(2)

with left_col:
    fig_categories = px.bar(
        category_revenue.sort_values("product_revenue"),
        x="product_revenue",
        y="main_category",
        orientation="h",
        title="Top categories by product revenue",
        labels={"product_revenue": "Revenue", "main_category": "Category"},
    )
    fig_categories.update_layout(height=500)
    st.plotly_chart(fig_categories, use_container_width=True)

with right_col:
    fig_states = px.bar(
        state_revenue.sort_values("product_revenue"),
        x="product_revenue",
        y="customer_state",
        orientation="h",
        title="Top states by product revenue",
        labels={"product_revenue": "Revenue", "customer_state": "State"},
    )
    fig_states.update_layout(height=500)
    st.plotly_chart(fig_states, use_container_width=True)

st.subheader("Operational drill-down")

table_cols = [
    "order_id",
    "order_status",
    "order_year_month",
    "customer_state",
    "main_category",
    "product_revenue",
    "freight_value",
    "main_payment_type",
    "delivery_days",
    "delay_days",
    "is_late_label",
    "review_score",
]

st.dataframe(
    filtered.sort_values("order_purchase_timestamp", ascending=False)[table_cols],
    use_container_width=True,
    hide_index=True,
)

st.subheader("Business takeaways")

takeaway_cols = st.columns(3)

takeaway_cols[0].info(
    "Delivery delay is a strong satisfaction signal: delayed orders have much lower "
    "average review scores in the project analysis."
)
takeaway_cols[1].info(
    "Revenue is concentrated in a small group of categories and states, especially "
    "health, beauty, watches, gifts and customers from SP."
)
takeaway_cols[2].info(
    "The dashboard can be used to monitor revenue, delivery time, late rate and "
    "review score by category, state and period."
)
