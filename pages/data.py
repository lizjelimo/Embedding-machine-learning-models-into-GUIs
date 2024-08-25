import streamlit as st
import pandas as pd

st.title("This is the data page")

@st.cache_data(persist = True)
def load_data():
    data = pd.read_csv(r"C:\Users\hp\Desktop\p4\Embedding-machine-learning-models-into-GUIs\Data\data_1.csv")
    return data

st.dataframe(load_data())