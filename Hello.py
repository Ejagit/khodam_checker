import streamlit as st
import pandas as pd
import random
import os
from PIL import Image

# Function to load data
@st.cache_data
def load_data():
    df = pd.read_csv('dataset/khodam_dataset_larger.csv')
    return df

# Load data
df = load_data()

# Labels (Jenis Khodam)
labels = df['Jenis Khodam'].unique()

# Path to the directory containing images
IMAGE_DIR = 'ghost_photo/'

# List all image files in the directory
image_files = [os.path.join(IMAGE_DIR, file) for file in os.listdir(IMAGE_DIR) if file.endswith(('jpg', 'jpeg', 'png'))]

# Streamlit app
st.title("Prediksi Khodam")

# Input form
name_input = st.text_input("Masukkan Nama:", "")

if name_input:
    # Option to predict a random khodam type from the dataset
    if st.button("Cek Khodam"):
        random_prediction = random.choice(labels)
        
        # Display jenis khodam di atas gambar dengan font besar dan ditengah
        st.markdown(f"## **{name_input} - {random_prediction}**")
        
        # Randomly select an image from the directory
        if image_files:
            random_image_path = random.choice(image_files)
            image = Image.open(random_image_path)
            st.image(image, use_column_width=True)
        else:
            st.write("Gambar tidak tersedia.")
