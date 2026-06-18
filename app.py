import streamlit as st
import pandas as pd

# ======================================
# PAGE CONFIG
# ======================================

st.set_page_config(
    page_title="FMCG AI Assistant",
    page_icon="🥤",
    layout="wide"
)

# ======================================
# LOAD DATA
# ======================================

sales_df = pd.read_csv("data/sales.csv")
inventory_df = pd.read_csv("data/inventory.csv")
products_df = pd.read_csv("data/products.csv")
stores_df = pd.read_csv("data/stores.csv")

# ======================================
# SIDEBAR
# ======================================

st.sidebar.title("📌 Navigation")

st.sidebar.info("""
Supported Queries

• Which products generated highest revenue?

• Show lowest revenue products

• Compare regional sales

• Which promotion performed best?

• Show stockout analysis
""")

# ======================================
# HEADER
# ======================================

st.title("🥤 FMCG AI Business Intelligence Assistant")

st.markdown("""
Conversational Analytics for Sales, Promotions,
Inventory and Regional Performance
""")

# ======================================
# KPI CARDS
# ======================================

total_revenue = sales_df["revenue"].sum()
total_units = sales_df["units_sold"].sum()
total_products = products_df["product_id"].nunique()
total_stores = stores_df["store_id"].nunique()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Revenue",
        f"₹{total_revenue:,.0f}"
    )

with col2:
    st.metric(
        "📦 Units Sold",
        f"{total_units:,}"
    )

with col3:
    st.metric(
        "🥤 Products",
        total_products
    )

with col4:
    st.metric(
        "🏪 Stores",
        total_stores
    )

# ======================================
# OVERVIEW CHART
# ======================================

st.subheader("📈 Revenue by Region")

overview = (
    sales_df.groupby("region")["revenue"]
    .sum()
)

st.bar_chart(overview)

# ======================================
# ANALYTICS FUNCTIONS
# ======================================

def top_products():

    merged = sales_df.merge(
        products_df,
        on="product_id"
    )

    return (
        merged.groupby("product_name")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )


def least_products():

    merged = sales_df.merge(
        products_df,
        on="product_id"
    )

    return (
        merged.groupby("product_name")["revenue"]
        .sum()
        .sort_values()
        .head(10)
        .reset_index()
    )


def regional_sales():

    return (
        sales_df.groupby("region")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )


def promotion_analysis():

    promo = sales_df[
        sales_df["promotion_flag"] == True
    ]

    return (
        promo.groupby("promotion_type")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
    )


def stockout_analysis():

    return inventory_df[
        inventory_df["stockout_flag"] == True
    ][[
        "product_id",
        "store_id",
        "closing_stock"
    ]].head(20)

# ======================================
# INTENT CLASSIFIER
# ======================================

def classify_intent(question):

    q = question.lower()

    if any(word in q for word in
           ["least", "lowest", "bottom", "worst"]):
        return "least_products"

    elif any(word in q for word in
             ["top", "highest", "best", "most"]):

        if any(word in q for word in
               ["promotion", "campaign"]):
            return "promotion_analysis"

        return "top_products"

    elif any(word in q for word in
             ["region", "regional",
              "north", "south",
              "east", "west",
              "compare"]):
        return "regional_sales"

    elif any(word in q for word in
             ["promotion",
              "campaign",
              "discount",
              "offer"]):
        return "promotion_analysis"

    elif any(word in q for word in
             ["stock",
              "inventory",
              "stockout"]):
        return "stockout_analysis"

    return "unknown"

# ======================================
# QUESTION BOX
# ======================================

st.subheader("💬 Ask a Business Question")

question = st.text_area(
    "",
    placeholder="Example: Which promotion performed best?"
)

# ======================================
# ANALYSIS
# ======================================

if st.button("🚀 Analyze"):

    if question.strip() == "":
        st.warning(
            "Please enter a question."
        )

    else:

        intent = classify_intent(question)

        st.success(
            f"Detected Intent: {intent}"
        )

        # ==================================
        # TOP PRODUCTS
        # ==================================

        if intent == "top_products":

            result = top_products()

            st.subheader(
                "🏆 Top Revenue Products"
            )

            st.dataframe(result)

            st.bar_chart(
                result.set_index(
                    "product_name"
                )["revenue"]
            )

            st.success("""
            These products generated the
            highest revenue and are the
            strongest performers in the
            beverage portfolio.
            """)

        # ==================================
        # LOWEST PRODUCTS
        # ==================================

        elif intent == "least_products":

            result = least_products()

            st.subheader(
                "📉 Lowest Revenue Products"
            )

            st.dataframe(result)

            st.bar_chart(
                result.set_index(
                    "product_name"
                )["revenue"]
            )

            st.success("""
            These products generated the
            lowest revenue and may require
            pricing, promotion or portfolio
            optimization.
            """)

        # ==================================
        # REGIONAL SALES
        # ==================================

        elif intent == "regional_sales":

            result = regional_sales()

            st.subheader(
                "🌍 Regional Sales Comparison"
            )

            st.dataframe(result)

            st.bar_chart(
                result.set_index(
                    "region"
                )["revenue"]
            )

            st.success("""
            Regional comparison helps identify
            high-performing markets and areas
            requiring additional focus.
            """)

        # ==================================
        # PROMOTIONS
        # ==================================

        elif intent == "promotion_analysis":

            result = promotion_analysis()

            st.subheader(
                "🎯 Promotion Performance"
            )

            st.dataframe(result)

            st.bar_chart(
                result.set_index(
                    "promotion_type"
                )["revenue"]
            )

            st.success("""
            This analysis highlights which
            promotional activities generated
            the highest revenue impact.
            """)

        # ==================================
        # STOCKOUTS
        # ==================================

        elif intent == "stockout_analysis":

            result = stockout_analysis()

            st.subheader(
                "📦 Stockout Analysis"
            )

            st.dataframe(result)

            st.success("""
            Stockout events indicate inventory
            replenishment gaps that could lead
            to missed sales opportunities.
            """)

        # ==================================
        # UNKNOWN
        # ==================================

        else:

            st.error("""
Question not supported.

Try:
• Which products generated highest revenue?
• Show lowest revenue products
• Compare regional sales
• Which promotion performed best?
• Show stockout analysis
""")

            result = None

        # ==================================
        # DOWNLOAD BUTTON
        # ==================================

        if "result" in locals() and result is not None:

            csv = result.to_csv(
                index=False
            )

            st.download_button(
                label="⬇ Download Results",
                data=csv,
                file_name="analysis_results.csv",
                mime="text/csv"
            )

# ======================================
# FOOTER
# ======================================

st.markdown("---")

st.caption(
    "AI Engineering Assessment | FMCG Beverage Analytics Assistant"
)