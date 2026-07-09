# Suspicious Chat Detector

**Suspicious Chat Detector** is a machine learning-powered web application built with **Streamlit** that analyzes chat logs to detect suspicious or illegal content. The app uses pre-trained models to classify messages in chat logs (e.g., WhatsApp logs) and identify potentially harmful or inappropriate content.

This project is intended to provide a simple way to check chat logs for illegal activities, making it useful for monitoring conversations and ensuring compliance with chat policies.

## Features

- **Upload chat logs**: Upload WhatsApp exported `.txt` files.
- **Preprocesses chat logs**: Cleans chat data by removing metadata, emojis, and special characters.
- **Suspicious content detection**: Uses pre-trained models to identify suspicious messages.
- **Results visualization**: Displays whether the chat log is classified as **Legal** or **Illegal** based on the analysis.
- **User-friendly interface**: Simple and intuitive interface built with Streamlit.


## Usage

1. **Run the Application**:

   Start the Streamlit app with the following command:

   ```bash
   streamlit run crime.py
   ```

2. **Upload a Chat Log**:

   - Click on **Upload** in the sidebar and select a WhatsApp chat log exported as `.txt`.
   - The app will preprocess and clean the chat data.

3. **View the Results**:

   - After processing, the app will display a message indicating whether the chat log is classified as **Legal** or **Illegal** based on the percentage of suspicious messages.

---

## How It Works

1. **Preprocessing**:
   - The app reads the uploaded WhatsApp chat file and removes unnecessary metadata, emojis, and special characters from messages.

2. **Suspicious Content Detection**:
   - The cleaned chat messages are transformed using a pre-trained vectorizer, and the resulting vectorized data is passed into a pre-trained machine learning model (`trained_model.pkl`) to predict if the messages are suspicious.

3. **Thresholding**:
   - If a certain percentage of the messages are classified as suspicious, the entire chat log is flagged as **Illegal**.

---


## Customization

You can easily customize the app:

1. **Fine-Tune the Model**:
   - Replace the `trained_model.pkl` and `text_vectorizer.pkl` files with your own pre-trained models for better accuracy or to adapt it to a different dataset.

2. **Adjust the Detection Threshold**:
   - Modify the threshold for classifying the chat as **Legal** or **Illegal** by changing the `threshold` parameter in the `check_illegal_chat()` function within the `output.py` file.

---

## Technologies Used

- **Python**: Backend for data processing and machine learning.
- **Streamlit**: Frontend for the interactive web application.
- **Scikit-learn**: For model training and prediction.
- **Regex**: For text preprocessing (message extraction, cleaning).
- **Pickle**: For serializing and loading trained models.

---


