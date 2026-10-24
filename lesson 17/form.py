import streamlit as st


with st.form ("my_form", clear_on_submit=True):
    name = st.text_input("Name")

    age = st.slider("Age",min_value=0,max_value=100)

    email = st.text_input("email")

    biography = st.text_area("short bio")

    terms = st.checkbox("i agree to the terms and conditions")

    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    st.write("Name of the person is",Name)
    st.write("Age of the person is",Age)
    st.write("email of the person is",email)
    st.write("bio of the person is",biography)

    if terms:
        st.write("you agreed to the terms and conditions")
    else:
        sr.write("you did not agree with terms and conditions")




