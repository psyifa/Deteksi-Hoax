import streamlit as st
import pandas as pd

# Data
data = {
    "Pretrained Model": [
        "indobenchmark/indobert-base-p2", 
        "indobenchmark/indobert-base-p2",
        "cahya/bert-base-indonesian-522M",
        "cahya/bert-base-indonesian-522M",
        "indobenchmark/indobert-base-p2",
        "indobenchmark/indobert-base-p2"
    ],
    "Label": [1, 0, 1, 0, 1, 1],
    "Precision": [0.568, 0.568, 0.568, 0.568, 0.568, 0.568],
    "Recall": [0.903, 0.903, 0.903, 0.903, 0.903, 0.903],
    "F1-Score": [0.697, 0.697, 0.697, 0.697, 0.697, 0.697],
    "Accuracy": [0.671, 0.671, 0.671, 0.671, 0.671, 0.671]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set up the Streamlit app
st.title("Model")
st.subheader("Matriks Evaluasi")

# Display the DataFrame as a table
st.table(df)
