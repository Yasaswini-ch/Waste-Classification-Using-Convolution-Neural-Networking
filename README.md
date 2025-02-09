
 CNN Model for Plastic Waste Classification
Hi there, I'm  Yasaswini Ch!

Overview
This project focuses on building a Convolutional Neural Network (CNN) model to classify images of plastic waste into various categories. The primary goal is to enhance waste management systems by improving the segregation and recycling process using deep learning technologies.

Table of Contents
Project Description

Dataset

Model Architecture

Model Deployment

Training

Weekly Progress

How to Run

Technologies Used

Future Scope

Contributing

License

Project Description
Plastic pollution is a growing concern globally, and effective waste segregation is critical to tackling this issue. This project employs a CNN model to classify plastic waste into distinct categories, facilitating automated waste management.

Dataset
The dataset used for this project is the Waste Classification Data.

Key Details:
Total Images: 25,077

Training Data: 22,564 images (85%)

Test Data: 2,513 images (15%)

Classes: Organic and Recyclable

Purpose: To aid in automating waste management and reducing the environmental impact of improper waste disposal.

Dataset Link:
[Download Dataset](https://www.kaggle.com/datasets/techsash/waste-classification-data/data)

Model Architecture
The CNN architecture includes:

Convolutional Layers: Feature extraction

Pooling Layers: Dimensionality reduction

Fully Connected Layers: Classification

Activation Functions: ReLU and Softmax

Model Deployment
The trained CNN model is available on Kaggle: Kaggle Model Link (Insert link here)

Training
Optimizer: Adam

Loss Function: Categorical Crossentropy

Epochs: 5

Batch Size: 32

Weekly Progress
Week 1: Libraries, Data Import, and Setup
Date: 21st January 2025 - 24th January 2025

Activities:

Imported required libraries and frameworks.

Set up the project environment.

Explored the dataset structure.

Notebooks:

Week1-Libraries-Importing-Data-Setup.

Week 2: Model Training, Evaluation, and Predictions
Date: 28th January 2025 - 31st January 2025

Activities:

Trained the CNN model on the dataset.

Evaluated model performance using accuracy and loss metrics.

Visualized classification results with a confusion matrix.


Week 3: Model Deployment
Date: 4th February 2025 - 7th February 2025

Activities:

Developed a Streamlit web application for real-time waste classification.

Uploaded the trained model to Kaggle and GitHub for public access.

Finalized the project documentation and README formatting.


How to Run
Clone the repository:

git clone https://github.com/Yasaswini-ch/CNN-Plastic-Waste-Classification
cd CNN-Plastic-Waste-Classification
Install the required dependencies:

pip install -r requirements.txt
Run the Streamlit app:

streamlit run app.py
Technologies Used
Python

TensorFlow/Keras

OpenCV

NumPy

Pandas

Matplotlib



Future Scope
Expanding the dataset to include more plastic waste categories.

Improving model accuracy using transfer learning.

Deploying the model as a mobile application.

Contributing
Contributions are welcome! Open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

About
A deep learning-based Plastic Waste Classification system using Convolutional Neural Networks (CNNs) to categorize waste into recyclable and non-recyclable materials. This project aims to support sustainable waste management by leveraging AI-powered image classification.

