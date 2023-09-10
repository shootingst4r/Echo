import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import pyjokes
from nltk.stem import WordNetLemmatizer
import time


#TTS
def say(input):
    engine.say(input)
    engine.runAndWait()

# obtain audio from the microphone
def getSpeech():
    with sr.Microphone() as source:
        print("Say something!")
        say("Please say something!")
        return r.listen(source)

#Processing Keywords
keywords_Recal = ["recal", "restart", "microphone"]
keywords_Web = ["web", "website", "go to" ".com"]
keywords_Wiki = ["wiki", "pedia", "summary", "summarize"]
keywords_Search = ["search", "what's", "what is", "google"]
keywords_Joke = ["joke", "pun"]
keywords_Exit = ["exit", "close", "stop"]

# Processing
def process(uncleanText):
    cleanText = lemmatizer.lemmatize(uncleanText).lower().strip()
    print(cleanText)

    if any(keyword in cleanText for keyword in keywords_Web):
        print("What website do you want to go to")
        say("Which Website?")
        processExtra("web")

    elif any(keyword in cleanText for keyword in keywords_Wiki):
        print("Which Wikipedia Summary do you want?")
        say("Which Wikipedia Summary?")
        processExtra("wiki")

    elif any(keyword in cleanText for keyword in keywords_Search):
        print("What do you want to Search")
        say("What to Search?")
        processExtra("search")

    elif any(keyword in cleanText for keyword in keywords_Joke):
        run("null", "joke")

    elif any(keyword in cleanText for keyword in keywords_Recal):
        run("null", "recal")

    elif any(keyword in cleanText for keyword in keywords_Exit):
        say("Bye!")
        run("null", "exit")

#Extra Input
def processExtra(mode):
    time.sleep(0.5)
    input =  lemmatizer.lemmatize(r.recognize_whisper(getSpeech(),"tiny.en")).lower().strip()
    run(input, mode)
    
#Runners
def run(input, mode):
    if mode == "web":
        print(input+" opened")
        webbrowser.open_new_tab("https://"+input)
    
    if mode == "wiki":
        summary = wikipedia.summary(wikipedia.search(input)[0], sentences=2)
        print(summary)
        say(summary)

    if mode == "search":
        webbrowser.open_new_tab("https://duckduckgo.com/?q="+input)
    
    if mode == "joke":
        joke = (pyjokes.get_joke())
        print(joke)
        say(joke)
    
    if mode == "recal":
        with sr.Microphone() as source:
            print("Wait a sec")
            say("Please wait a second.")
            r.adjust_for_ambient_noise(source, 0.5)
            print("recalibrated")

    if mode == "exit":
        exit()
        

# Main
lemmatizer = WordNetLemmatizer()
# start the TTS engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
say("Hello!")


# start the recognizer and adjust for ambient noise
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Wait a sec")
    say("Please wait a second.")
    r.adjust_for_ambient_noise(source, 0.5)


while True:
    output = r.recognize_whisper(getSpeech(),"base.en")
    print(output)
    process(output)
    time.sleep(4)
    
    

