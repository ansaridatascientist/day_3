import streamlit as st

st.title("st.button")

if st.button("Say Hello!"):
    st.write("Why Hello There..!")
else:
    st.write("Goodbye")

