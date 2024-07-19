

# Rice Type Classification

This project involves building a web application to classify rice types using a pre-trained Convolutional Neural Network (CNN) model. The model is deployed using Flask, TensorFlow, and TensorFlow Hub.

## Project Overview

The Rice Type Classification project provides a web interface where users can upload images of rice, and the application will classify the type of rice using a pre-trained model. The application uses Flask for the web framework and TensorFlow for model inference.

## Features

- Upload rice images via a web interface.
- Predict rice types from the uploaded images using a pre-trained CNN model.
- Display prediction results on a results page.

## Prerequisites

- Python 3.7 or later
- TensorFlow
- TensorFlow Hub
- Flask
- OpenCV

## Installation

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd Rice-type-classification-CNN
   ```

2. **Create a Virtual Environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Required Packages**

   ```bash
   pip install -r requirements.txt
   ```

   Create a `requirements.txt` file with the following content:

   ```
   tensorflow
   tensorflow-hub
   flask
   opencv-python
   ```

4. **Place the Model File**

   Ensure the pre-trained model file `rice.h5` is placed in the project directory.

5. **Directory Structure**

   Make sure your project directory looks like this:

   ```
   /path/to/your/project
   ├── app.py
   ├── rice.h5
   ├── templates
   │   ├── index.html
   │   ├── details.html
   │   └── results.html
   └── Data
       └── val
   ```

## Usage

1. **Run the Flask Application**

   ```bash
   python app.py
   ```

2. **Open Your Web Browser**

   Navigate to `http://127.0.0.1:5000/` to access the application.

3. **Upload an Image**

   Use the form on the homepage to upload an image of rice and get the prediction.

## Troubleshooting

- **Model Not Loading**: Ensure that `rice.h5` is in the correct location and is compatible with the TensorFlow version.
- **Dependencies Issues**: Ensure that all required packages are installed and up-to-date.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have suggestions or improvements.

## License

This project is licensed under the MIT License. 

---
