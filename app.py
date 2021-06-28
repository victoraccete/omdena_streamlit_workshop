import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

TITLE = "Streamlit demonstration"
st.title(TITLE)
DESCRIPTION = "Using titanic dataset"
st.markdown(DESCRIPTION)
st.sidebar.title(TITLE)

@st.cache(persist=True)
def load_data():
    data = pd.read_csv("titanic.csv")
    return data
data = load_data()
st.write(data)
