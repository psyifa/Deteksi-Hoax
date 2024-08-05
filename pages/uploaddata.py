import streamlit as st
import pandas as pd

st.title("Upload Data")

uploaded_file = st.file_uploader("Pilih file CSV untuk diupload", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Data yang Diupload:")
    st.write(data)
    
    # Simulasi penambahan kolom deteksi
    if 'Content' in data.columns:
        data['Deteksi'] = "HOAX"  # Ganti dengan logika deteksi yang sesuai jika diperlukan
        st.write("Data dengan Hasil Deteksi:")
        st.write(data)
        # Optional: Save the modified data
        # data.to_csv('detected_data.csv', index=False)
    else:
        st.write("Kolom 'Content' tidak ditemukan di data.")
