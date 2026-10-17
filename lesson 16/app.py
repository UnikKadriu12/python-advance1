import streamlit as st

if st.button("click me"):
    st.write("buttoni eshte klikuar")


if st.checkbox("check me to show some text"):
    st.write("you're seeing this text because you checkd the checkbox")



user_input = st.text_input("Enter some text")

st.write("you enterd:", user_input)



age = st.number_input("enter age",min_value=0,max_value=100)

st.write(f"your age is {age}")

message3= st.text_area("Enter a Message")

st.write("you have enterd ", message3)

choice = st.radio("Pick one",["ai","Python adv","code 1"])

if st.button("Succes"):
    st.success("Operation was succesful")



try:
    1/0

except Exception as e:

    st.exception(e)
