import streamlit as st
import pandas as pd
import pickle
from sklearn.neighbors import KNeighborsClassifier

label_mapping = {
    0: 'low income and high spending',
    1: 'high income and low spending',
    2: 'mid income and mid spending',
    3: 'low income and low spending',
    4: 'high income and high spending'
}

# Load the pre-trained KNN model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Home page
def home():
    st.title('Cluster Prediction App')
    st.caption('Made by: Zuhdan Arif')
    st.write('This app predicts clusters on Mall customer based on age, salary, and score. This project aims to predict clusters among Mall 
              customers based on their age, salary, and score using the K-Nearest Neighbors (KNN) algorithm. 
              The KNN method has been found to be the most effective in this particular case after rigorous testing and evaluation.')
    st.subheader('Files')
    st.write('The dataset used for this project consists of customer information collected from a shopping mall. Feel free to check my code')
    st.markdown(
        """
        <style>
        .stMarkdown a {
            color: red !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display hyperlink
    st.markdown("[Google Colab](https://colab.research.google.com/drive/12L7IqBXO5VJwn6gQ9KA0dglGLfeEvtQR)")
    st.markdown('[CSV file](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python)')

# Data input and prediction page
def predict():
    st.title('Cluster Prediction')

    # Data inputation
    st.subheader('Input Data')
    age = st.number_input('Age', 18, 70)
    salary = st.number_input('Salary', 15, 137)
    answer_score = st.number_input('Answer Score', 1, 99)

    # Perform prediction
    input_data = [[age, salary, answer_score]]
    prediction = model.predict(input_data)[0]
    predicted_label = label_mapping[prediction]

    st.subheader('Prediction')
    st.write('The predicted cluster for the input data is:', predicted_label)

def EDA():
    st.title('Explanatory Data Analysis')



# App navigation
def main():
    st.sidebar.title('Navigation')
    pages = ['Home', 'Prediction']
    choice = st.sidebar.selectbox('Go to', pages)

    if choice == 'Home':
        home()
    elif choice == 'Prediction':
        predict()

if __name__ == '__main__':
    main()
