import pandas as pd
import streamlit as st
import os

def load_history():
    history_file = "./Data/history.csv"  # Update the path as needed
    if os.path.exists(history_file):
        try:
            # Read the file and remove any extra header rows or irrelevant data
            df = pd.read_csv(history_file, header=None)
            
            # Detect and remove any rows that are likely headers or incorrectly formatted
            df.columns = ["customerID", "gender", "SeniorCitizen", "Partner", "Dependents", "PhoneService", 
                          "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection", 
                          "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling", 
                          "PaymentMethod", "tenure", "MonthlyCharges", "TotalCharges", "PredictionDate", "ModelUsed"]

            # Drop rows where 'customerID' column contains header values or duplicates
            df = df[df['customerID'] != "customerID"]
            
            # Convert numeric columns to appropriate types
            df['tenure'] = pd.to_numeric(df['tenure'], errors='coerce')
            df['MonthlyCharges'] = pd.to_numeric(df['MonthlyCharges'], errors='coerce')
            df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
            
            return df
        except pd.errors.ParserError as e:
            st.error(f"Error loading CSV file: {e}")
            return pd.DataFrame()  # Return an empty DataFrame on error
    else:
        st.warning("No history file found.")
        return pd.DataFrame()  # Return an empty DataFrame if the file does not exist

def display_history():
    df = load_history()
    if not df.empty:
        st.write("### Prediction History")
        st.dataframe(df)  # This will display the DataFrame in the Streamlit app
    else:
        st.write("No data to display.")

def main():
    st.title("Prediction History")
    display_history()

if __name__ == "__main__":
    main()
