import streamlit as st
import pandas as pd

# Set up the Streamlit app layout
st.title("Deteksi Berita Hoax")
st.write("Unggah File CSV untuk mendeteksi")

# Dropdown for model selection
model_option = st.selectbox(
    'Pilih Model',
    ('cahya/bert-base-indonesian-522M', 'indobenchmark/indobert-base-p2')
)

# File uploader
uploaded_file = st.file_uploader("Unggah file disini", type="csv")

# Initialize session state to store the corrections
if 'corrections' not in st.session_state:
    st.session_state.corrections = []

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("### Uploaded Data")
    st.dataframe(df)
    
    if st.button("Deteksi"):
        # Simulate detection results
        df['Result'] = 'Non-Hoax'
        df['Correction'] = ''

        # Save detection results in session state
        st.session_state.df = df
        st.session_state.corrections = [''] * len(df)

    if 'df' in st.session_state:
        df = st.session_state.df
        
        # Display detection results
        st.write("### Detection Results")
        st.dataframe(df)
        
        # Display correction buttons
        for i in range(len(df)):
            st.write(f"Row {i+1}: {df.iloc[i]['Title']}")
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Hoax {i+1}"):
                    st.session_state.corrections[i] = 'Hoax'
            with col2:
                if st.button(f"Non-Hoax {i+1}"):
                    st.session_state.corrections[i] = 'Non-Hoax'
        
        # Update DataFrame with corrections
        for i in range(len(st.session_state.corrections)):
            df.at[i, 'Correction'] = st.session_state.corrections[i]
        
        st.write("### Corrected Data")
        st.dataframe(df)
        
        # Save corrected data
        if st.button("Simpan"):
            df.to_csv("corrected_data.csv", index=False)
            st.success("Data saved successfully")
