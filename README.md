\# 🧠 Brain Tumor Detection Using Deep Learning (CNN)



\## 📌 Project Overview



This project develops a deep learning model for classifying brain MRI images using Convolutional Neural Networks (CNNs) and Transfer Learning.



The project uses the \*\*MobileNetV2\*\* pretrained architecture to learn visual patterns from MRI images and classify them into four categories: Glioma, Meningioma, Pituitary Tumor, and Healthy Brain.



The complete workflow includes image preprocessing, data augmentation, model training, evaluation, and prediction.



> \*\*Disclaimer:\*\* This project is developed for educational and research purposes only. It is not intended to be used as a medical diagnostic tool.



\---



\## 🎯 Objectives



\- Develop a CNN-based model for brain MRI image classification.

\- Apply image preprocessing and data augmentation techniques.

\- Use Transfer Learning with the MobileNetV2 pretrained model.

\- Train and evaluate the model on brain MRI images.

\- Analyze model performance using appropriate evaluation metrics.

\- Build a foundation for deploying the trained model as a web application.



\---



\## 🧠 Approach



The project follows the following deep learning workflow:



```text

MRI Images

&#x20;    ↓

Image Preprocessing

&#x20;    ↓

Data Augmentation

&#x20;    ↓

MobileNetV2 Transfer Learning

&#x20;    ↓

Model Training

&#x20;    ↓

Model Evaluation

&#x20;    ↓

Brain Tumor Classification

```



\---



\## ✨ Application Features



\- Upload brain MRI images for prediction.

\- Classify MRI images into four categories.

\- Display the predicted class and confidence score.

\- Show prediction probabilities for all classes.

\- Provide educational information about brain tumor categories.

\- Interactive web interface developed using Streamlit.



\---



\## 🛠️ Technologies Used



\- \*\*Programming Language:\*\* Python 3.11

\- \*\*Deep Learning:\*\* TensorFlow and Keras

\- \*\*Model Architecture:\*\* MobileNetV2

\- \*\*Web Framework:\*\* Streamlit

\- \*\*Data Processing:\*\* NumPy and Pandas

\- \*\*Image Processing:\*\* Pillow and OpenCV

\- \*\*Development Environment:\*\* Jupyter Notebook



\---



\## 📂 Project Structure



```text

brain-tumor-detection-cnn/

│

├── app.py

├── Brain Tumor Detection Using Deep Learning (CNN).ipynb

├── brain\_tumor\_mobilenetv2\_model.h5

├── class\_names.pkl

├── requirements.txt

├── requirements-lock.txt

├── .gitignore

└── README.md

```



\---



\## 💻 Installation and Usage



\### 1. Clone the Repository



```bash

git clone YOUR\_GITHUB\_REPOSITORY\_URL

cd brain-tumor-detection-cnn

```



Replace `YOUR\_GITHUB\_REPOSITORY\_URL` with the actual URL of this repository.



\### 2. Create a Virtual Environment



Using Python 3.11, run:



```bash

py -3.11 -m venv .venv

```



Activate the environment in Git Bash:



```bash

source .venv/Scripts/activate

```



\### 3. Install Dependencies



Upgrade pip:



```bash

python -m pip install --upgrade pip

```



Install the pinned dependencies:



```bash

pip install -r requirements-lock.txt

```



\### 4. Run the Application



```bash

streamlit run app.py

```



Open the local URL displayed in your terminal, usually:



`http://localhost:8501`



\### 5. Make a Prediction



1\. Open the \*\*Prediction\*\* page.

2\. Upload an MRI image in JPG, JPEG, or PNG format.

3\. View the predicted category and confidence score.

4\. Review the probability scores for the four classes.



\---



\## 📊 Model Information



| Parameter | Description |

|---|---|

| Model Architecture | MobileNetV2 Transfer Learning |

| Input Image Size | 224 × 224 pixels |

| Input Channels | 3 (RGB) |

| Number of Output Classes | 4 |

| Classification Categories | Glioma, Healthy, Meningioma, Pituitary |



The application currently displays the following metrics:



| Metric | Reported Value |

|---|---:|

| Training Accuracy | 92.86% |

| Validation Accuracy | 89.24% |

| Test Accuracy | Approximately 94% — reported in the project conclusion; requires verification |



\*\*Note:\*\* These figures should be verified against the notebook's actual training history and evaluation results. Training, validation, and test accuracy are different metrics and should not be treated as interchangeable.



\---



\## 📁 Dataset



The original dataset ZIP file is excluded from this repository because of its size.



The trained model and class labels are provided separately for inference. To retrain the model, obtain the dataset from its original source and follow the notebook's preprocessing and training workflow.



The dataset source, licensing information, and exact train-validation-test split should be documented here once verified.



\---



\## ✅ Conclusion



A brain tumor classification system was developed using Transfer Learning with MobileNetV2.



The project aims to classify brain MRI scans into four categories:



\- Glioma

\- Meningioma

\- Pituitary Tumor

\- Healthy Brain



The workflow incorporates image preprocessing, data augmentation, model training, evaluation, and single-image prediction. The trained model has also been integrated into a Streamlit application, allowing users to upload MRI images and view classification results.



The model's reported performance should be validated against reproducible evaluation results before making claims about its reliability or generalization to unseen MRI scans.



\---



\## 🔮 Future Developments



\### 1. Improve Dataset Quality and Diversity



\- Use larger and more diverse MRI datasets from multiple sources.

\- Evaluate performance across different imaging devices and patient populations.

\- Address class imbalance using appropriate augmentation and sampling techniques.



\### 2. Explore Advanced Deep Learning Architectures



Compare MobileNetV2 with other architectures, such as:



\- EfficientNet

\- DenseNet

\- ResNet152

\- Vision Transformers (ViT)



Benchmark the models using consistent datasets and evaluation metrics.



\### 3. Extend Classification to Tumor Segmentation



Explore segmentation architectures such as:



\- U-Net

\- Mask R-CNN



This could enable tumor boundary visualization and, where appropriate data and validation are available, tumor size estimation.



\### 4. Investigate Multimodal Deep Learning



Explore combining MRI images with additional clinical information, where ethically and legally permitted, to investigate whether multimodal approaches improve model performance.



\### 5. Deploy the Web Application



Potential deployment technologies include:



\- Streamlit

\- Flask

\- FastAPI

\- Docker

\- Cloud platforms



A deployed application could provide an accessible interface for research demonstrations and model testing.



\### 6. Explore Ensemble Learning



Combine predictions from multiple models and evaluate whether ensemble learning improves robustness and generalization.



\### 7. Clinical Validation and Safety Evaluation



Before any clinical use, future work would require appropriate collaboration with medical professionals and rigorous validation, including:



\- Independent testing on representative datasets

\- Sensitivity and specificity analysis

\- Assessment of false-positive and false-negative predictions

\- Evaluation of potential bias and limitations

\- Relevant regulatory and clinical review



\---



\## ⚠️ Medical Disclaimer



This project is intended for educational and research purposes only. It is not a clinically validated diagnostic system and must not be used to diagnose medical conditions, recommend treatment, or make healthcare decisions.



Model predictions can be incorrect or misleading. Always consult a qualified healthcare professional for medical evaluation.



\---



\## 📄 License



No license has been added yet. A suitable open-source license should be selected before permitting others to reuse, modify, or redistribute this project.



