import streamlit as st
from datetime import datetime

st.title("Deteksi Berita Hoax")

# Initialize session state for correction
if 'correction' not in st.session_state:
    st.session_state.correction = None
if 'detection_result' not in st.session_state:
    st.session_state.detection_result = None

# Dropdown for selecting a model
model = st.selectbox(
    "Pilih model",
    ["cahya/bert-base-indonesian-522M", "indobenchmark/indobert-base-p2"]
)

# Text input for the headline
headline = st.text_input("Masukkan judul berita")

# Text area for the article content
content = st.text_area("Masukkan konten berita")

# Detection button
if st.button("Deteksi"):
    if headline and content:
        # Dummy detection result
        st.session_state.detection_result = "Non-Hoax"  # Replace with actual detection logic if needed

# Display the detection result and correction options
if st.session_state.detection_result:
    st.success(f"Prediksi: {st.session_state.detection_result}")

    st.write("Correction")
    st.session_state.correction = st.radio("", ("Non-Hoax", "Hoax"), index=0 if st.session_state.correction == "Non-Hoax" else 1)

    # Save button
    if st.button("Save"):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open('corrections.csv', 'a', encoding='utf-8') as f:
            f.write(f"{headline},{content},{st.session_state.detection_result},{st.session_state.correction},{timestamp}\n")
        st.success("Koreksi telah disimpan.")
