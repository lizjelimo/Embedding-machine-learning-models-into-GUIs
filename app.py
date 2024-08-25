import streamlit as st


st.set_page_config(
    page_title = "Predict Churn",
    page_icon = ":hand:",
    layout = "wide"
)
st.title("Predict Churn")

st.markdown(""" 
            This app is designed to empower businesses with advanced churn analysis capabilities, helping you identify customers at risk of leaving and take action to retain them. Using predictive modeling, it analyzes key metrics to forecast churn probability. The app also segments customers based on their churn risk, providing tailored insights and actionable recommendations to improve retention. With interactive data visualizations, you can easily track churn trends, uncover root causes, and implement effective strategies to keep your customers engaged and loyal.
""")

#key features
st.subheader("How to use the app")
st.markdown("""
            1. Upload your customer data in CSV format.
            2. Choose the relevant features for churn prediction.
            3. Choose the churn threshold and model type.
            4. Click on the 'Run analysis' button
            5. Explore the churn segments and their characteristics.
            6. Monitor churn trends and make data-driven decisions.
            7. Explore the dashboard for visualized churn risks, customer segments, and key drivers.
            """)

st.subheader("App features")
st.markdown("""
- **Home**:
Welcome to the app! This is your starting point, where you can quickly access all features and get an overview of your churn analysis process.

- **Prediction**:
Use this feature to analyze your data and generate churn predictions. Understand which customers are at risk and take proactive steps to retain them.

- **History**:
View and manage past analyses. This section keeps a record of your previous predictions and insights, allowing you to track changes and trends over time.

- **Data**:
Upload, organize, and manage your customer data here. Ensure your data is ready for analysis by following simple upload and formatting steps.

- **Dashboard**:
Access an interactive overview of your churn analysis results. Visualize churn risks, explore customer segments, and dive deep into the insights that matter
            """)

