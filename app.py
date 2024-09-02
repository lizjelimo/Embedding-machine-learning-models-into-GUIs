import streamlit as st
import login
import dashboard
import data
import history 
import predict
import webbrowser

# Initialize session state for authentication
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Define a function to handle the login state
def check_authentication():
    return st.session_state.get('authenticated', False)

#Define a function to handle logout
def logout():
    st.session_state['authenticated'] = False
    st.session_state.pop('username', None)
    st.session_state['page'] = 'Login'

def show_home_page():
    st.markdown(""" 
        ### Welcome to the Churn Analysis App

        This app is designed to empower businesses with advanced churn analysis capabilities, helping you identify customers at risk of leaving and take action to retain them. Using predictive modeling, it analyzes key metrics to forecast churn probability. The app also segments customers based on their churn risk, providing tailored insights and actionable recommendations to improve retention. With interactive data visualizations, you can easily track churn trends, uncover root causes, and implement effective strategies to keep your customers engaged and loyal.
    """)

    # Key features
    st.subheader("How to use the app")
    st.markdown("""
        1. Upload your customer data in CSV format.
        2. Choose the relevant features for churn prediction.
        3. Choose the churn threshold and model type.
        4. Click on the 'Run analysis' button.
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
          Access an interactive overview of your churn analysis results. Visualize churn risks, explore customer segments, and dive deep into the insights that matter.
    """)
    # Display the subheader
    st.subheader("Need Help?")
    
    # Display the GitHub button
    if st.button('Visit Our GitHub'):
        # Open the GitHub repository in a new tab
        webbrowser.open_new_tab('https://github.com/lizjelimo/Embedding-machine-learning-models-into-GUIs.git')
    
    # Display the Contact Me button
    if st.button('Contact Me'):
        # When the button is clicked, display a link to open the email client
        st.markdown(
            '<a href="mailto:your.email@example.com?subject=Contact%20from%20Streamlit%20App" target="_blank">Click here to contact me</a>',
            unsafe_allow_html=True
        )

def main():
    if check_authentication():
        if 'page' not in st.session_state:
            st.session_state['page'] = 'Home'
        
        # Sidebar with logout option
        st.sidebar.title(f"Welcome, {st.session_state.get('username', '')}")
        if st.sidebar.button("Logout"):
            logout()
        
        # Navigation menu
        st.sidebar.title("Navigation:compass:")
        st.session_state['page'] = st.sidebar.selectbox(
            "Select Page", ["Home", "Dashboard", "Data", "History", "Predict"]
        )
        
        # Render the selected page
        if st.session_state['page'] == "Home":
            show_home_page()
        elif st.session_state['page'] == "Dashboard":
            dashboard.show_dashboard()
        elif st.session_state['page'] == "Data":
            data.main()
        elif st.session_state['page'] == "History":
            history.main()
        elif st.session_state['page'] == "Predict":
            predict.main()
        else:
            st.error("Page not found. Please select a valid page.")
    else:
            login.show_login()
    
            
            

if __name__ == "__main__":
    main()