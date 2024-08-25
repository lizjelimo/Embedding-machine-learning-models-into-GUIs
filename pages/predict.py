import streamlit as st
import joblib
import pandas as pd
import os
import datetime
import sklearn

st.set_page_config(
    page_title="Predict",
    page_icon="🔮",
    layout="wide"
)

# Loading models
@st.cache_resource(show_spinner="Loading Random Forest Model...")
def load_forest_pipeline():
    pipeline = joblib.load("./models/second_best_model.pkl")
    return pipeline

@st.cache_resource(show_spinner="Loading Logistic Regression Model...")
def load_logistic_pipeline():
    pipeline = joblib.load("./models/best_model.pkl")
    return pipeline

def select_model():
    col1, col2 = st.columns(2)
    with col1:
        selected_model = st.selectbox("Select a model", options=["Random Forest", "Logistic Regression"], key="selected_model")
    
    if selected_model == "Random Forest":
        pipeline = load_forest_pipeline()
    else:
        pipeline = load_logistic_pipeline()

    return pipeline

def display_form():
    pipeline = select_model()
    with st.form("input_feature"):
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.write("### Demographic Information")
            gender = st.selectbox("Gender", ["Male", "Female"], key="gender")
            seniorcitizen = st.selectbox("Senior Citizen", ["Yes", "No"], key="seniorcitizen")
            partner = st.selectbox("Partner", ["Yes", "No"], key="partner")
            dependents = st.selectbox("Dependents", ["Yes", "No"], key="dependents")
        
        with col2:
            st.write("### Service and Product Usage")
            phoneservice = st.selectbox("Phone Service", ["Yes", "No"], key="phoneservice")
            multiplelines = st.selectbox("Multiple Lines", ["Yes", "No"], key="multiplelines")
            internetservice = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"], key="internetservice")
            onlinesecurity = st.selectbox("Online Security", ["Yes", "No"], key="onlinesecurity")
            onlinebackup = st.selectbox("Online Backup", ["Yes", "No"], key="onlinebackup")
            deviceprotection = st.selectbox("Device Protection", ["Yes", "No"], key="deviceprotection")
            techsupport = st.selectbox("Tech Support", ["Yes", "No"], key="techsupport")
            streamingtv = st.selectbox("Streaming TV", ["Yes", "No"], key="streamingtv")
            streamingmovies = st.selectbox("Streaming Movies", ["Yes", "No"], key="streamingmovies")
        
        with col3:
            st.write("### Contract and Billing Information")
            contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"], key="contract")
            paperlessbilling = st.selectbox("Paperless Billing", ["Yes", "No"], key="paperlessbilling")
            paymentmethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"], key="paymentmethod")
        
        with col4:
            st.write("### Financial Information")
            monthlycharges = st.number_input("Enter Monthly Charges", min_value=1.0, step=0.01, format="%.2f", key="monthly_charges")
            totalcharges = st.number_input("Enter Total Charges", min_value=1.0, step=0.01, format="%.2f", key="total_charges")
            tenure = st.number_input("Enter the tenure", min_value=1, step=1, format="%d", key="tenure")
        
        submitted = st.form_submit_button("Make Prediction")
        if submitted:
            make_prediction(pipeline)

def make_prediction(pipeline):
    # Collecting data from session state
    data = {
        "customerID": ["dummy_id"],
        "gender": [st.session_state["gender"]],
        "SeniorCitizen": [st.session_state["seniorcitizen"]],
        "Partner": [st.session_state["partner"]],
        "Dependents": [st.session_state["dependents"]],
        "PhoneService": [st.session_state["phoneservice"]],
        "MultipleLines": [st.session_state["multiplelines"]],
        "InternetService": [st.session_state["internetservice"]],
        "OnlineSecurity": [st.session_state["onlinesecurity"]],
        "OnlineBackup": [st.session_state["onlinebackup"]],
        "DeviceProtection": [st.session_state["deviceprotection"]],
        "TechSupport": [st.session_state["techsupport"]],
        "StreamingTV": [st.session_state["streamingtv"]],
        "StreamingMovies": [st.session_state["streamingmovies"]],
        "Contract": [st.session_state["contract"]],
        "PaperlessBilling": [st.session_state["paperlessbilling"]],
        "PaymentMethod": [st.session_state["paymentmethod"]],
        "tenure": [st.session_state["tenure"]],
        "MonthlyCharges": [st.session_state["monthly_charges"]],
        "TotalCharges": [st.session_state["total_charges"]],
    }

    columns = ["customerID","gender","SeniorCitizen", "Partner", "Dependents", "PhoneService",  "MultipleLines", "InternetService", "OnlineSecurity", 
               "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod", "tenure", "MonthlyCharges", "TotalCharges"]

    df = pd.DataFrame(data, columns=columns)

    # Convert to numeric (necessary to avoid issues with the median strategy)
    df['tenure'] = pd.to_numeric(df['tenure'], errors='coerce')
    df['MonthlyCharges'] = pd.to_numeric(df['MonthlyCharges'], errors='coerce')
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Adding additional metadata
    df['Prediction Time'] = datetime.date.today()
    df['Model Used'] = st.session_state['selected_model']
    
    # Save the data to a history file
    df.to_csv("./Data/history.csv", mode="a", header=not os.path.exists("./Data/history.csv"), index=False)
    
    # Make prediction and get probabilities
    pred = pipeline.predict(df)
    prediction = pred[0]
    
    prob = pipeline.predict_proba(df)
    probability = prob[0]
    
    # Updating session state
    st.session_state["prediction"] = prediction
    st.session_state["probability"] = probability

    # Display results
    st.markdown(f"### Prediction: {prediction}")
    st.markdown(f"### Probability: {probability}")

# Main execution
if __name__ == "__main__":
    st.title("Make a prediction")
    display_form()
    
    # Display prediction result
    prediction = st.session_state.get("prediction")
    probability = st.session_state.get("probability")

    # Display results
    if prediction is None:
        st.markdown("### Predictions will show here after you submit the form")
    elif prediction == 1:  # Assuming 1 corresponds to "Yes"
        probability_of_yes = probability[1] * 100
        st.markdown(f"### The client will leave the company with a probability of {round(probability_of_yes, 2)}%")
    else:
        probability_of_no = probability[0] * 100
        st.markdown(f"### The client will not leave the company with a probability of {round(probability_of_no, 2)}%")
