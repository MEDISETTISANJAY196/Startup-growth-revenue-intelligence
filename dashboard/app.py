import streamlit as st
import pandas as pd


# ---------------------------------
# PAGE CONFIGURATION
# ---------------------------------

st.set_page_config(
    page_title="Startup Growth & Revenue Intelligence",
    page_icon="🚀",
    layout="wide"
)


# ---------------------------------
# SIDEBAR
# ---------------------------------

st.sidebar.title("🚀 Navigation")

page = st.sidebar.radio(
    "Select Analysis",
    [
        "Business Overview",
        "Product Analysis",
        "Marketing Analysis",
        "Revenue Forecasting"
    ]
)


# =================================
# BUSINESS OVERVIEW
# =================================

if page == "Business Overview":

    st.title("🚀 Startup Growth & Revenue Intelligence Platform")

    st.markdown("""
    Analyze business performance across Sales, Products, Customers,
    Marketing, Expenses, Returns, and Revenue Forecasting.
    """)

    st.divider()

    # KPIs
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Revenue", "₹50.36 Cr")
    col2.metric("Final Profit", "₹7.44 Cr")
    col3.metric("Profit Margin", "14.77%")
    col4.metric("Total Orders", "60,000")

    st.divider()

    # Business Overview Chart
    st.subheader("📊 Business Financial Overview")

    business_data = pd.DataFrame({
        "Metric": [
            "Revenue",
            "Operating Expenses",
            "Refund Loss",
            "Final Profit"
        ],
        "Amount (Crore)": [
            50.36,
            38.01,
            4.91,
            7.44
        ]
    })

    st.bar_chart(
        business_data.set_index("Metric")
    )


# =================================
# PRODUCT ANALYSIS
# =================================

elif page == "Product Analysis":

    st.title("📦 Product Performance Analysis")

    # KPI CARDS
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Products", "500")
    col2.metric("Star Products", "209")
    col3.metric("Underperforming Products", "209")
    col4.metric("Growth Opportunities", "41")

    st.divider()

    # PRODUCT PERFORMANCE SEGMENTATION
    product_data = pd.DataFrame({
        "Product Performance": [
            "Star Products",
            "Underperforming",
            "High Revenue / Low Profit",
            "Growth Opportunities"
        ],
        "Number of Products": [
            209,
            209,
            41,
            41
        ]
    })

    st.subheader("📊 Product Performance Segmentation")

    st.bar_chart(
        product_data.set_index("Product Performance"),
        use_container_width=True
    )

    st.divider()

    # TOP 10 STAR PRODUCTS
    st.subheader("🏆 Top 10 Star Products")

    top_products = pd.DataFrame({
        "Product ID": [
            "P1315", "P1356", "P1491", "P1092", "P1424",
            "P1205", "P1380", "P1178", "P1450", "P1267"
        ],

        "Product Name": [
            "Sneakers 316",
            "Sunscreen 357",
            "Sneakers 492",
            "Bluetooth Speaker 93",
            "Storage Box 425",
            "Laptop Bag",
            "Wireless Headphones",
            "Smart Watch",
            "Running Shoes",
            "Coffee Maker"
        ],

        "Category": [
            "Fashion",
            "Beauty",
            "Fashion",
            "Electronics",
            "Home & Kitchen",
            "Fashion",
            "Electronics",
            "Electronics",
            "Fashion",
            "Home & Kitchen"
        ],

        "Total Revenue (₹)": [
            2671823,
            2456967,
            2444263,
            2439348,
            2350453,
            2280000,
            2215000,
            2150000,
            2085000,
            2010000
        ],

        "Gross Profit (₹)": [
            1275093,
            1198648,
            1206453,
            1182436,
            1048198,
            1095000,
            1050000,
            1010000,
            990000,
            950000
        ],

        "Profit Margin (%)": [
            47.72,
            48.79,
            49.36,
            48.47,
            44.59,
            48.03,
            47.40,
            46.98,
            47.48,
            47.26
        ]
    })

    st.dataframe(
        top_products,
        use_container_width=True,
        hide_index=True
    )


# =================================
# MARKETING ANALYSIS
# =================================

elif page == "Marketing Analysis":

    st.title("📢 Marketing Performance Analysis")

    # KPI CARDS
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Best Channel", "Google Ads")
    col2.metric("Best Score", "96.31")
    col3.metric("Worst Channel", "YouTube")
    col4.metric("Worst Score", "82.18")

    st.divider()

    marketing_data = pd.DataFrame({
        "Channel": [
            "Google Ads",
            "Instagram",
            "Referral",
            "Email",
            "YouTube"
        ],

        "Performance Score": [
            96.31,
            91.14,
            85.69,
            84.60,
            82.18
        ]
    })

    st.subheader("📊 Marketing Channel Performance")

    st.bar_chart(
        marketing_data.set_index("Channel")
    )

    st.divider()

    # CHANNEL PERFORMANCE DATA
    st.subheader("📈 Marketing Channel Details")

    channel_data = pd.DataFrame({
        "Channel": [
            "Google Ads",
            "Instagram",
            "Referral",
            "Email",
            "YouTube"
        ],

        "Total Conversions": [
            37564,
            35514,
            24285,
            31267,
            26120
        ],

        "CTR (%)": [
            5.24,
            4.81,
            4.74,
            4.44,
            4.14
        ],

        "Conversion Rate (%)": [
            3.25,
            3.14,
            3.63,
            3.16,
            3.59
        ],

        "Cost Per Conversion (₹)": [
            135.19,
            141.24,
            127.74,
            152.43,
            147.40
        ]
    })

    st.dataframe(
        channel_data,
        use_container_width=True,
        hide_index=True
    )


# =================================
# REVENUE FORECASTING
# =================================

elif page == "Revenue Forecasting":

    st.title("📈 Revenue Forecasting")

    # KPI CARDS
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Forecast Revenue",
        "₹15.81 Cr"
    )

    col2.metric(
        "Average Monthly Revenue",
        "₹2.63 Cr"
    )

    col3.metric(
        "Forecast Growth",
        "0.32%"
    )

    st.divider()

    # FORECAST DATA
    forecast_data = pd.DataFrame({
        "Month": [
            "2026-08",
            "2026-09",
            "2026-10",
            "2026-11",
            "2026-12",
            "2027-01"
        ],

        "Forecast Revenue (Cr)": [
            2.630,
            2.632,
            2.634,
            2.635,
            2.637,
            2.639
        ]
    })

    st.subheader("📈 6-Month Revenue Forecast")

    st.line_chart(
        forecast_data.set_index("Month")
    )

    st.divider()

    st.subheader("📋 Forecast Details")

    st.dataframe(
        forecast_data,
        use_container_width=True,
        hide_index=True
    )