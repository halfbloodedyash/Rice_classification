import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import tensorflow as tf
import tensorflow_hub as hub
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import cv2
from flask import Flask, request, render_template

# Ensure TensorFlow Hub is imported and KerasLayer is properly referenced
def KerasLayer(*args, **kwargs):
    return hub.KerasLayer(*args, **kwargs)

model = tf.keras.models.load_model(filepath='rice.h5', custom_objects={'KerasLayer': KerasLayer})
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/details')
def pred():
    return render_template('details.html')

@app.route('/result', methods=['GET', 'POST'])
def predict():
    if request.method == "POST":
        f = request.files['image']
        basepath = os.path.dirname(__file__)
        filepath = os.path.join(basepath, 'Data', 'val', f.filename)
        f.save(filepath)
        
        a2 = cv2.imread(filepath)
        a2 = cv2.resize(a2, (224, 224))
        a2 = np.array(a2)
        a2 = a2 / 255
        a2 = np.expand_dims(a2, 0)

        pred = model.predict(a2)
        pred = pred.argmax()

        df_labels = {
            'arborio': 0,
            'basmati': 1,
            'ipsala': 2,
            'jasmine': 3,
            'karacadag': 4
        }

        prediction = None
        for i, j in df_labels.items():
            if pred == j:
                prediction = i

        return render_template('results.html', prediction_text=prediction)

if __name__ == "__main__":
    app.run(debug=True)
