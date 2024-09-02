import streamlit as st
import plotly.express as px
import pandas as pd
import os
import streamlit_shadcn_ui as ui
import warnings

warnings.filterwarnings("ignore")

def show_dashboard():
    st.title(":bar_chart: Welcome to the Dashboard!")

    # ------ Set visualization view page
    col1, col2, col3 = st.columns(3)
    with col2:
        options = st.selectbox('Choose viz to display', options=['', 'EDA Dashboard', 'KPIs Dashboard'])
    
    # File uploader for various formats
    fl = st.file_uploader(":file_folder: Upload a file", type=["csv", "txt", "xlsx", "xls"])
    if fl is not None:
        filename = fl.name
        st.write(f"Uploaded file: {filename}")
        if filename.endswith('.csv'):
            df = pd.read_csv(fl, encoding="ISO-8859-1")
        elif filename.endswith(('.xlsx', '.xls')):
            df = pd.read_excel(fl)
        else:
            st.error("Unsupported file format!")
            df = None
    else:
        default_file_path = "Data/data_1.csv"
    if os.path.isfile(default_file_path):
        df = pd.read_csv(default_file_path, encoding="ISO-8859-1")
        st.write("Using default file.")
    else:
        st.error("Default file not found!")
        df = None 
        
        
    


    def eda_viz():
        st.subheader('EDA Dashboard')
        column1, column2 = st.columns(2)
        with column1:
            fig = px.histogram(df, x='tenure', title='Distribution of Tenure')
            st.plotly_chart(fig)
        with column1:
            fig = px.histogram(df, x='MonthlyCharges', title='Distribution of MonthlyCharges')
            st.plotly_chart(fig)
        with column1:
            fig = px.histogram(df, x='TotalCharges', title='Distribution of TotalCharges')
            st.plotly_chart(fig)

        with column2:
            fig = px.bar(df, x='Churn', title='Churn Distribution')
            st.plotly_chart(fig)
        with column2:
            fig = px.box(df, x='gender', y='TotalCharges', title='Total Charges Distribution across Gender')
            st.plotly_chart(fig)

    def kpi_viz():
        st.subheader('KPIs Dashboard')
        st.markdown('---')
        cols = st.columns(5)
        st.markdown('---')
        # ------- Grand Total Charges
        with cols[0]:
            grand_tc = df['TotalCharges'].sum()
            ui.metric_card(title="Grand TotalCharges", content=f"{'{:,.2f}'.format(grand_tc)}", key="card1")

        # ------- Grand Monthly Charges
        with cols[1]:
            grand_mc = df['MonthlyCharges'].sum()
            ui.metric_card(title="Grand MonthlyCharges", content=f"{'{:,.2f}'.format(grand_mc)}", key="card2")

        # ------- Average Customer Tenure
        with cols[2]:
            average_tenure = df['tenure'].mean()
            ui.metric_card(title="Average Tenure", content=f"{'{:,.2f}'.format(average_tenure)}", key="card3")

        # ------- Churned Customers
        with cols[3]:
            churned = len(df.loc[df['Churn'] == 1])
            ui.metric_card(title="Churn", content=f"{churned}", key="card4")

        # ------ Total Customers
        with cols[4]:
            total_customers = df['customerID'].count()
            ui.metric_card(title="Total Customers", content=f"{total_customers}", key="card5")

    def analytical_ques_viz():
        # ------ Answer Analytical Question 1
        mal_churned_customers = df[(df['gender']=='Male') & (df['Dependents']== 1) & (df['Churn']== 1)]['PaymentMethod'].value_counts()

        values = mal_churned_customers.values
        labels = mal_churned_customers.index

        treemap_df = pd.DataFrame({'labels': labels, 'values': values})

        fig = px.treemap(treemap_df, path=['labels'], values='values', color='values',
                         color_continuous_scale='Blues', title='Q1. How many male customers with dependents churned given their payment method?')
        st.plotly_chart(fig)

        # ------ Answer Analytical Question 2
        fem_churned_customers = df[(df['gender']=='Female') & (df['Dependents']== 1) & (df['Churn']== 1)]['PaymentMethod'].value_counts()

        values = fem_churned_customers.values
        labels = fem_churned_customers.index

        treemap_df = pd.DataFrame({'labels': labels, 'values': values})

        fig = px.treemap(treemap_df, path=['labels'], values='values', color='values',
                         color_continuous_scale='Blues', title='Q2. How many female customers with dependents churned given their payment method?')
        st.plotly_chart(fig)

        # ------ Answer Analytical Question 3
        churned = df[df['Churn'] == 1]

        fig = px.bar(churned, x='MultipleLines', color='gender', barmode='group',
                     title='Q3. What is the distribution for the customers who churned given their multiple lines status?',
                     labels={'MultipleLines': 'Multiple Lines', 'gender': 'Gender'})

        st.plotly_chart(fig)

        # ------ Answer Analytical Question 4
        monthly_charges = df.groupby('gender')['MonthlyCharges'].sum().reset_index()

        fig = px.pie(monthly_charges, names='gender', values='MonthlyCharges',
                     title='Q4. What percentage of MonthlyCharges was accumulated given the customer gender?',
                     color='gender',
                     labels={'gender': 'Gender', 'MonthlyCharges': 'Monthly Charges'})

        # Show the figure in Streamlit
        st.plotly_chart(fig)

        # ------ Answer Analytical Question 5
        monthly_charges = df.groupby('Churn')['TotalCharges'].sum().reset_index()

        fig = px.pie(monthly_charges, names='Churn', values='TotalCharges',
                     title='Q5. What percentage of TotalCharges was accumulated given customer churn status?',
                     color='Churn',
                     labels={'Churn': 'Churn', 'TotalCharges': 'Monthly Charges'})

        st.plotly_chart(fig)

    if options == 'EDA Dashboard':
        eda_viz()
    elif options == 'KPIs Dashboard':
        kpi_viz()
        analytical_ques_viz()
    else:
        st.markdown('#### No visual display selected yet')

if __name__ == '__main__':
    show_dashboard()
    

    




