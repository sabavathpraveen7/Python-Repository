import speech_recognition as sr

def listen_and_convert():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Say something...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        
        # Save the transcript
        with open("transcript.txt", "a") as f:
            f.write(text + "\n")
            
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Could not request results from the service.")

# listen_and_convert()