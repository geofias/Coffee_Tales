import streamlit as st
from PIL import Image
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np

# Loading trained moel
model = tf.keras.models.load_model('model', 
                                   custom_objects={'KerasLayer':hub.KerasLayer})

st.title('Coffe Leaf Disease Detection')

class_names = ['[UNK]', 'healthy', 'rust', 'miner', 'cerscospora', 'phoma']

uploaded_file = st.file_uploader("Load a coffee leaf image...", type="jpg")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Loaded Image', use_column_width=True)
    
    # Preprocese the image
    img = image.resize((224, 224))
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    
    # Make the prediction
    prediction = model.predict(img)
    confidence = round(np.max(prediction[0]) * 100, 2)
    predicted_class = class_names[np.argmax(prediction[0])]
    st.write(f'Prediction: {predicted_class}')
    st.write(f'Confidence: {confidence}')
