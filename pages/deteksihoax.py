import streamlit as st
import pandas as pd
from datetime import datetime

st.title("Deteksi Hoax Berita")

# Dropdown for selecting a model
model = st.selectbox(
    "Pilih Model",
    ["cahya/bert-base-indonesian-522M"]
    
)

# Text input for the headline
headline = st.text_input("Masukkan Judul Berita")

# Text area for the article content
content = st.text_area("Masukkan Konten Berita")

# Detection result
detection_result = None
correction = None

# Detection button
if st.button("Deteksi"):
    if headline and content:
        # Dummy detection result
        detection_result = "Non-Hoax"  # Replace with actual detection logic if needed

# Display the detection result and correction options in a single row
if detection_result:
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"Prediksi: {detection_result}")
    with col2:
        st.write("Correction")
        correction = st.radio("", ("Non-Hoax", "Hoax"))

    # Save button
    if st.button("Save"):
        st.write(f"Saved as {correction}")
        # Save correction to CSV
        with open('corrections.csv', 'a') as f:
            f.write(f"{headline},{content},{detection_result},{correction},{datetime.now()},Koreksi\n")
        st.write("Koreksi telah disimpan.")

# Display saved corrections
try:
    corrections = pd.read_csv('corrections.csv', names=['Title', 'Content', 'Prediction', 'Correct Label', 'Timestamp', 'Koreksi'])
    st.dataframe(corrections)
except FileNotFoundError:
    st.write("Belum ada data koreksi.")
