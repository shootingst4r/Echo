import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Wait a sec")
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

print(r.recognize_whisper(audio))
