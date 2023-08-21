import streamlit as st

st.session_state.disabled = True

# input nama visitor
name = st.text_input("Siapa nama kamu? ")

# output akhir di streamlit
if name:
  st.write("Hello, ", name,". Thank you for visiting.")
