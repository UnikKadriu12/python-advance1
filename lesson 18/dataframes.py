import pandas as pd
import streamlit as st


st.header("Displaying dataframes")

data = pd.DataFrame({
    'name':['Dua',"Erona","Lora"],
    'Age':[22,22,22],
    'City':["Prishtine","Prishtine","Prishtine"]

})

st.dataframe(data)