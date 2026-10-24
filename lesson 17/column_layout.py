import streamlit as st

col1,col2,col3,col3,col4,col5 = st.columns(5,gap="small", vertical_alignment="center")

with col1:
    st.header("Kolona e pare")

    st.write ("kjo eshte kolona e pare")
    with col2:
        st.header("Kolona e dyte")

        st.write("kjo eshte kolona e pare")
    with col3:
        st.header("Kolona e tret")

        st.write("kjo eshte kolona e pare")
    with col4:
        st.header("Kolona e kater")

        st.write("kjo eshte kolona e pare")
        with col5:
            st.header("Kolona e peste")

            st.write("kjo eshte kolona e pare")