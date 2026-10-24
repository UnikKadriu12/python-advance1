import streamlit as st

st.sidebar.header("Sidebar")

st.sidebar.write("this is a sidebar")

st.sidebar.selectbox("chose an option",["Option 1","option 2","option 3"])
st.sidebar.radio("Go to",["Home","settings"])