# 🐟 Multiclass Fish Image Classification

## 📌 Project Overview
This project focuses on **classifying fish images** into multiple categories using **Deep Learning**. We trained both a **CNN from scratch** and **pre-trained models (Transfer Learning)** to determine the best-performing approach. 
A **Streamlit application** was also developed to allow users to upload an image and get real-time predictions.

### **Key Features:**
- **Accurate Fish Classification**: Identifies fish species from images.
- **Deployment Ready Model**: A Streamlit web application for real-time predictions.
- **Model Benchmarking**: Comparing CNN vs. Transfer Learning models to determine the best architecture.

---

## 📊 Dataset Information
- **Format**: Images categorized into subfolders (11 fish species).
- **Structure**:
  ```
  Dataset/
  │── train/
  │   ├── fish_class_1/ 
  │   ├── fish_class_2/
  │── val/
  │── test/
  ```
- Totally 11 classes are available
- **Data Preprocessing & Augmentation**:
  - Rescaling pixel values to `[0,1]`.
  - Augmentation: **Rotation, width/height shift, shear, zoom, flipping**.
  - Used `ImageDataGenerator` for efficient processing.

---

## 🔬 Approach
### **Step-by-Step Process**
1. **Data Collection & Preprocessing**
   - Loaded images using `ImageDataGenerator`.
   - Applied data augmentation to improve generalization.
   - Ensured the dataset was already split into `train`, `val`, and `test` sets.

2. **Building & Training Models**
   - Implemented **CNN from scratch**.
   - Fine-tuned **5 Pre-trained Models**:
     - VGG16
     - ResNet50
     - MobileNet
     - InceptionV3
     - EfficientNetB0
   - Used **Adam** for Transfer Learning models.

3. **Model Evaluation & Selection**
   - Compared **Accuracy, Precision, Recall, F1-score, and Confusion Matrix**.
   - **Stored model performance in `all_model_performance.csv`**.
   - **Saved only the best-performing model** based on highest accuracy & lowest loss.

4. **Deployment with Streamlit**
   - Developed a **Streamlit web app** for real-time image classification.
   - Uploaded image -> Preprocessed -> Model Prediction -> Displayed Result.

---

## 🎯 Model Training & Evaluation
### **1️⃣ CNN from Scratch**
✅ Designed a **3-layer Convolutional Neural Network**.
✅ Used **ReLU activation**, **MaxPooling**, and **Dropout** to reduce overfitting.
✅ Achieved moderate accuracy but struggled with generalization.

### **2️⃣ Transfer Learning Models**
✅ **Fine-tuned 5 pre-trained models**.
✅ **VGG16 & ResNet50 performed the best**.
✅ **EfficientNetB0 was the most lightweight** with good accuracy.

### **3️⃣ Best Model Selection**
✅ **Sorted models based on highest accuracy & lowest loss**.
✅ **Stored final test results in `model_performance.csv`**.
✅ **Saved only the best model as `.pkl` for deployment**.

---

## 🎥 Project Demo
A **fully functional web application** was created using **Streamlit** to allow users to:
✅ Upload an image 📤
✅ Get a **real-time classification** 🏷️
✅ View **confidence scores** 📊

Sample Output:
```python
Predicted Class: Salmon 🐟
Confidence: 95.3%
```

---

## 📌 Project Deliverables
📂 **Trained Models**: Best-performing `.pkl` file.  
📂 **Streamlit Application**: Web app for fish classification.  
📂 **Python Scripts**: Training, evaluation, deployment scripts.  
📂 **Comparison Report**: `model_performance.csv` & `model_evaluation_results.csv`.  
📂 **GitHub Repository**: Well-documented codebase.  

---

## 🏁 Conclusion
✅ **Achieved high accuracy on fish classification** using deep learning.
✅ **Transfer Learning outperformed CNN from scratch**, especially **VGG16 & ResNet50**.
✅ **Built a user-friendly web app** for easy classification.
✅ **Project is scalable** and can be extended for **real-world applications** like marine research and fisheries management.

---

## 📢 Connect With Me
📧 Email: your.email@example.com  
🔗 LinkedIn: [Your LinkedIn Profile](https://www.linkedin.com/in/kishanth-arunachalam)  
📂 GitHub: [Your GitHub Profile](https://github.com/kishanth-a)  

Feel free to contribute, fork the repo, or submit issues! 🎯

