import streamlit as st
import speech_recognition as sr

st.title("🎙️ Speech-to-Text App")

st.write("Click the button below to start recording.")

# Initialize the recognizer
recognizer = sr.Recognizer()

# Button to start recording
if st.button("Start Recording"):
    with sr.Microphone() as source:
        st.write("🎤 Recording... Speak now.")
        try:
            audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds
            st.write("🔄 Converting speech to text...")
            text = recognizer.recognize_google(audio)  # Use Google Speech Recognition API
            st.success(f"✅ Transcription: {text}")
        except sr.UnknownValueError:
            st.error("❌ Could not understand the audio.")
        except sr.RequestError:
            st.error("❌ Could not request results from Google Speech Recognition.")

st.write("🚀 Built with Streamlit and SpeechRecognition!")
