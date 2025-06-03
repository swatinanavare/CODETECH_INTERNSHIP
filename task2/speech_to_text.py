import speech_recognition as sr

# Load recognizer
r = sr.Recognizer()

# Load audio file
with sr.AudioFile("sample.wav") as source:
    audio = r.listen(source)

# Convert to text
try:
    print("You said:", r.recognize_google(audio))
except:
    print("Could not understand audio.")

