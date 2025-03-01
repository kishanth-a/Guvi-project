# 📰 News Classification with Fine-Tuned Hugging Face Model

## 📌 Project Overview
This project focuses on classifying news articles into predefined categories using a fine-tuned Hugging Face transformer model. Leveraging state-of-the-art NLP techniques, we train and deploy a robust text classification system to categorize news articles efficiently.

## ✨ Key Features
- Fine-tuned transformer-based model (e.g., BERT, RoBERTa) for accurate text classification.
- Preprocessing pipeline with tokenization and vectorization.
- Model training with multiple architectures to compare performance.
- Deployed as a web application using **Streamlit/Gradio**.
- Hosted on **AWS (S3, EC2, RDS)** for scalability and efficiency.
- Interactive UI for users to classify news articles in real time.

## 📊 Dataset Information
- **Size**: ~120,000 training samples, 7,600 test samples.
- **Classes**: 4 equally distributed categories.
- **Preprocessing**:
  - Tokenization using Hugging Face's pre-trained tokenizer.
  - Stop words **not removed** (since transformers handle them effectively).
  - Splitting dataset into batches for training due to computational constraints.

## 🏗 Approach
1. **Data Preprocessing**
   - Loaded dataset and balanced class distribution.
   - Tokenized text using Hugging Face’s tokenizer.
   - Managed batch training due to limited computing power.

2. **Model Selection & Training**
   - Fine-tuned **BERT, RoBERTa, and RNN**.
   - Used **cross-entropy loss** and Adam optimizer.
   - Evaluated models using accuracy and loss.

3. **Deployment**
   - Built web UI using **Streamlit**.
   - Hosted model on AWS (EC2 for inference, S3 for storage, RDS for logs).
   - Implemented real-time predictions with a user-friendly interface.

## 📈 Model Training & Evaluation
- **Training Strategy**: Trained on **15,000 samples per batch** to optimize memory usage.
- **Best Model**: RoBERTa achieved the highest accuracy.
- **Metrics**:
  - Accuracy: **95%**

## 🎥 Project Demo
🔗 [Live Demo](https://github.com/kishanth-a/Guvi-project/blob/main/AG_News_Classification/demo_video.mp4) 

## 💼 Business Use Case
- **News Aggregators**: Automatically categorize news articles for users.
- **Fake News Detection**: Identify and filter misleading news content.
- **Content Recommendation**: Suggest relevant articles based on user preferences.
- **Media Monitoring**: Track and analyze trends across various news categories.

## 🏁 Conclusion
This project demonstrates the power of fine-tuned transformer models in **automating text classification**. The solution is scalable, accurate, and applicable to various real-world NLP tasks. Future improvements could include multi-label classification, topic modeling, and real-time news streaming analysis.

🚀 **Next Steps:** Optimize inference speed, integrate with larger datasets, and explore multilingual news classification.

---

## 📢 Connect With Me
📧 Email: kishanth.kichoo@gmail.com  
🔗 LinkedIn: [Kishanth](https://www.linkedin.com/in/kishanth-arunachalam)  
📂 GitHub: [Kishanth](https://github.com/kishanth-a)  

Feel free to contribute, fork the repo, or submit issues! 🎯
