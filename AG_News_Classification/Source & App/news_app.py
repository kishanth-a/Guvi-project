import streamlit as st
import joblib
import boto3
import io
import mysql.connector
import torch
import datetime
from transformers import AutoTokenizer

# Connect to MySQL
def connect_db():
    conn = mysql.connector.connect(
        host="classification-project.c9w0sasgsepv.eu-north-1.rds.amazonaws.com",
        port=3306,
        user="admin", 
        password="kichoo1998",
        database="classification_project"
    )
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS user_login (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), interaction_time DATETIME);""")
    conn.commit()
    return conn, cursor

def store_data(name, time):
    conn, cursor = connect_db()
    cursor.execute("""INSERT INTO user_login (name, interaction_time) VALUES (%s, %s)""", (name, time))
    conn.commit()
    conn.close()

# Predict function
def classify_news(text):
    # Load the saved model
    # AWS S3 Configuration
    s3_bucket_name = "kishanth1998"  # Replace with your actual S3 bucket name
    s3_model_path = "best_model_RoBERTa_cpu.pkl"  # Path inside the bucket
    s3 = boto3.client("s3",
                      aws_access_key_id="AKIA4MI2J3MFV6WBT7HD",
                      aws_secret_access_key="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",
                      region_name="eu-north-1"
                    )
    model_obj = s3.get_object(Bucket=s3_bucket_name, Key=s3_model_path)
    model_data = io.BytesIO(model_obj['Body'].read())  # Read as byte stream

    # Load model into memory
    model = joblib.load(model_data)

    model.eval()
    tokenizer = AutoTokenizer.from_pretrained("roberta-base")
    inputs = tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt")

    with torch.no_grad():
        outputs = model(**inputs)
        predicted_label = torch.argmax(outputs.logits, dim=1).item()

    class_labels = ["World", "Sports", "Business", "Sci/Tech"]
    predicted_class = class_labels[predicted_label]

    return predicted_class

# Streamlit Navigation
st.set_page_config(page_title="News Classifier", page_icon="📰")

# **Page 1: User Entry**
if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    st.title("Welcome to News Classifier 📰")
    name = st.text_input("Enter your name:")

    if st.button("Proceed"):
        if name:
            interaction_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            st.session_state.name = name
            st.session_state.time = interaction_time
            store_data(name, interaction_time)
            st.session_state.page = "classify"
            st.rerun()
        else:
            st.warning("Please enter your name before proceeding.")

# **Page 2: News Classification**
elif st.session_state.page == "classify":
    st.title("News Classification")
    st.write("Enter the news content below:")

    news_text = st.text_area("Paste the news article here:")

    if st.button("Classify News"):
        if news_text:
            label = classify_news(news_text)
            st.success(f"Predicted Category: **{label}**")
        else:
            st.warning("Please enter a news article.")

# Run the app: `streamlit run app.py`
