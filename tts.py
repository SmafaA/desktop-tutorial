from gtts import gTTS
import os

def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("response.mp3")
    os.system("mpg321 response.mp3")

if __name__ == "__main__":
    text = "This is a test of the TTS system."
    text_to_speech(text)
