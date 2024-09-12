import speech_recognition as sr

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

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Starting speech recognition...")
    result = recognize_speech_from_mic(recognizer, microphone)
    
    if result["success"]:
        print("You said: " + result["transcription"])
    else:
        print("Error: " + result["error"])
