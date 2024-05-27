import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import platform
import subprocess

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio).lower()
        print("User said:", query)
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print("Request error:", e)
        return ""

# Function to open a browser
def open_browser():
    speak("Opening browser")
    webbrowser.open("https://www.google.com")

# Function to tell the current time
def tell_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%I:%M %p")
    speak("The current time is " + current_time)

# Function to open YouTube
def open_youtube():
    speak("Opening YouTube")
    webbrowser.open("https://www.youtube.com")

# Function to search YouTube and play a song
def play_song(song_name):
    speak("Playing " + song_name)
    url = "https://www.youtube.com/results?search_query=" + "+".join(song_name.split())
    webbrowser.open(url)

# Function to search Wikipedia
def search_wikipedia(query):
    speak("Searching Wikipedia")
    try:
        result = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia, " + result)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("Can you please provide more specific information?")
    except wikipedia.exceptions.PageError as e:
        speak("Sorry, I couldn't find any information on that topic.")

# Function to open Google Chrome
def open_chrome():
    speak("Opening Chrome")
    if platform.system() == "Windows":
        subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe"])
    elif platform.system() == "Darwin":
        subprocess.Popen(["/usr/bin/open", "-a", "/Applications/Google Chrome.app"])
    else:
        subprocess.Popen(["google-chrome"])

# Function to search query on Chrome
def search_chrome(query):
    speak("Searching on Chrome")
    search_url = "https://www.google.com/search?q=" + "+".join(query.split())
    webbrowser.open(search_url)

# Main function
def main():
    speak("Hello! How can I assist you today?")
    while True:
        query = listen()

        if "open browser" in query:
            open_browser()
        elif "what time is it" in query or "tell me the time" in query:
            tell_time()
        elif "open youtube" in query:
            open_youtube()
        elif "play song" in query:
            play_song("Despacito")  # Default song, you can modify this to play any other song
        elif "search wikipedia" in query:
            search_query = query.replace("search wikipedia", "").strip()
            search_wikipedia(search_query)
        elif "open chrome" in query:
            open_chrome()
        elif "search on chrome" in query:
            search_query = query.replace("search on chrome", "").strip()
            search_chrome(search_query)
        elif "exit" in query or "quit" in query:
            speak("Goodbye!")
            break
        else:
            speak("I'm sorry, I didn't understand that.")

if __name__ == "__main__":
    main()