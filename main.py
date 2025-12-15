import streamlit as st

with st.form(key='my_form'):
    col1, col2 = st.columns(2)
    with col1:
        name_label = st.subheader('Name')
    with col2:
        name_input = st.text_input(label='Enter your name')

    submit = st.form_submit_button(label='Submit')