import speech_recognition as sr
import openai
from gtts import gTTS
import os

def recognize_speech_from_mic(recognizer, microphone):
    with microphone as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unavailable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

def ask_gpt(text):
    openai.api_key = 'your-openai-api-key'

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        max_tokens=100
    )

    return response.choices[0].text.strip()

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Starting speech recognition...")
    result = recognize_speech_from_mic(recognizer, microphone)
    
    if result["success"]:
        print("You said: " + result["transcription"])
        gpt_response = ask_gpt(result["transcription"])
        print("GPT says: " + gpt_response)
        text_to_speech(gpt_response)
    else:
        print("Error: " + result["error"])
