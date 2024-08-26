import streamlit as st
import pandas as pd

def show_dashboard():
    st.title("Dashboard")

    # Example of adding a chart
    st.subheader("Example Chart")
    st.line_chart([1, 2, 3, 4, 5, 6])

    # Example of adding a data table
    st.subheader("Example Data Table")
    data = {
        "Column 1": [1, 2, 3],
        "Column 2": [4, 5, 6],
    }
    df = pd.DataFrame(data)
    st.dataframe(df)

    # Example of adding interactive elements
    st.subheader("Interactive Element")
    option = st.selectbox("Choose an option", ["Option 1", "Option 2"])
    st.write(f"You selected {option}")

if __name__ == "__main__":
    show_dashboard()

