import streamlit as st

st.session_state.disabled = True

# input nama visitor
name = st.text_input("Siapa nama kamu? ")

# Say hello to visitor
output = print("Hello, ", name +" thank you for visiting.", :smile:)

# output akhir di streamlit
st.write(output)
