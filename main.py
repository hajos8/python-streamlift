import streamlit as st
import time

with st.form(key='my_form'):
    col1, col2 = st.columns(2)
    with col1:
        header1 = st.subheader('Politician')
        name_input = st.text_input(label='Enter your name')
        age = st.number_input(label='Enter your age', min_value=18, max_value=120, step=1)

    with col2:
        header2 = st.subheader('Party')
        party_input = st.selectbox(label='Select your party', options=['Fidesz', 'Tisza', 'Jobbik', 'LMP', 'DK', 'MSZP', 'Momentum'])
        color_input = st.color_picker(label='Pick your party color', value='#FF6A00')

    col3, col4 = st.columns(2)
    with col3:
        header3 = st.subheader('Lie')
        lie_input = st.text_area(label='Tell his lie')

    with col4:
        header4 = st.subheader('Truth')
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTRtFzaqzY2Koagn6ujSsyZrSEp8PXS2vuc_Hxk__hvsBPtHgl9TdY-dXLHrzWgkR76FvmRk4kTJpzEKCipM-KMuXhmsyxmHb-LDRAGQx1-&s=10')
        consent = st.checkbox(label='I agree to tell the truth', value=False)

    with st.spinner("Wait for it...", show_time=True):
        if(consent and age >= 18 and name_input and party_input and lie_input):
            time.sleep(5)
            form_data = {
                'name': name_input,
                'age': age,
                'party': party_input,
                'party_color': color_input,
                'lie': lie_input
            }

            st.success('Form submitted successfully!')
            st.json(form_data)
        else:
            st.error('Please fill out all fields and agree to tell the truth.')

    

    submit = st.form_submit_button(label='Submit')