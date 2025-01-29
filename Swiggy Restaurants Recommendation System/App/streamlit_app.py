# Streamlit-based Recommendation System
import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load Cleaned DataFrame
cleaned_df = pd.read_csv(f"D:\\Kishanth\\Guvi Project\\Swiggy_Recommendation_System\\cleaned_csv.csv")

# Load encoders, scaler, and model
with open(f'D:\\Kishanth\\Guvi Project\\Swiggy_Recommendation_System\\encoder.pkl', 'rb') as f:
    encoders = pickle.load(f)

with open(f'D:\\Kishanth\\Guvi Project\\Swiggy_Recommendation_System\\kmeans_model.pkl', 'rb') as f:
    kmeans = pickle.load(f)

image_url = f"D:\\Kishanth\\Guvi Project\\Swiggy_Recommendation_System\\swiggy1.webp"
title = "Swiggy Restaurants Recommendation System"

# Create two columns
col1, col2 = st.columns([1, 3])

# Display Image in the first column
with col1:
    st.image(image_url, width=150)

# Display Title in the second column
with col2:
    st.title(f"{title}")

# User Input
city = st.selectbox('Select City', options=cleaned_df['city'].unique())
cuisine = st.selectbox('Select Cuisine', options=cleaned_df['cuisine'].unique())
cost = st.number_input('Enter Cost', min_value=0.0, step=0.1)
rating = st.slider("Select a Rating:", min_value=0.0, max_value=5.0, step=0.1)

if st.button('Get Recommendations'):

    # Encode city with One-Hot Encoding
    city_encoded = pd.DataFrame(
        encoders["city_encoder"].transform([[city]]),
        columns=encoders["city_encoder"].get_feature_names_out(["city"])
    )

    # Encode cuisine with Label Encoding
    cuisine_encoded = pd.DataFrame(
        [encoders["cuisine_encoder"].transform([cuisine])],
        columns=["cuisine_encoded"]
    )

    rating_scaled = pd.DataFrame(
        encoders["rating_scaler"].transform([[rating]]),  # Extract only the scaled cost
        columns=["rating_scaled"]
    )

    # Scale the cost feature
    cost_scaled = pd.DataFrame(
        encoders["cost_scaler"].transform([[cost]]),  # Extract only the scaled cost
        columns=["cost_scaled"]
    )

    # Combine all features using pd.concat
    user_input_df = pd.concat([cuisine_encoded, rating_scaled, cost_scaled, city_encoded], axis=1)

    # Predict the cluster for user input
    predicted_cluster = kmeans.predict(user_input_df)[0]
    print(f"Predicted Cluster: {predicted_cluster}")

    # Step 4: Get Recommendations
    # Filter encoded data based on the cluster and map back to cleaned data
    cluster_indices = (kmeans.labels_ == predicted_cluster)
    result = cleaned_df.loc[cluster_indices]


    recommended_restaurants = result[["name", "link"]].rename(
        columns={
            "name": "Restaurant_Name",
            "link": "Link"
        }
    )

    recommended_restaurants.reset_index(drop=True,inplace=True)

    st.subheader('Recommended Restaurants:')
    st.table(recommended_restaurants.iloc[1:11,:])
