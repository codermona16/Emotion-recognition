import streamlit as st
import requests

st.set_page_config(page_title="This is a Multipage WebApp")
st.title("Check your Emotion")

# Define the URL where you want to send the audio file
url = 'http://192.168.1.14:8080/'

# File uploader for uploading audio files
uploaded_file = st.file_uploader(label="Upload here")

# Radio buttons for selecting language
selected_language = st.radio("Select language", ("Bengali", "Sanskrit", "Assamese", "Hindi"))

# If a file is uploaded
if uploaded_file:
    st.write(uploaded_file.type)
    # Check if the uploaded file is an audio file
    if "audio" in uploaded_file.type or "wav" in uploaded_file.type:
        if st.button("Submit"):
            # Send the uploaded file and selected language as part of the POST request
            files = {'audio_file': uploaded_file}
            data = {'language': selected_language}  # Data to be sent along with the request
            response = requests.post(url + 'process', files=files, data=data)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                st.write('Request successful!')
                st.write('Response body:', response.text)
            else:
                st.write('Request failed with status code:', response.status_code)
    else:
        st.write("Please upload an audio file (WAV format)")

