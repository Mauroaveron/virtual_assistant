import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Voice
voice_id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0'


# Listen to our microphone the audio as text
def convert_audio_to_text():

    # Store recognizer in variable
    r = sr.Recognizer()

    # Set up the microphone
    with sr.Microphone() as origin:

        # Wait time
        r.pause_threshold = 0.8

        # Inform recording start
        print('You can talk now')

        # Save what is heard as audio
        audio = r.listen(origin)

        try:
            # Search in Google
            request = r.recognize_google(audio, language='en-us')

            # Proof that the audio could be correctly entered
            print('You said: ' + request)

            # Return request
            return request

        # In case the audio is not understood
        except sr.UnknownValueError:

            # Proof that the audio could not be correctly entered
            print("Oops, I couldn't understand")

            # Return error
            return 'I am still waiting'

        # In case of not being able to solve the request
        except sr.RequestError:

            # Proof that the audio could not be correctly entered
            print("Oops, no service")

            # Return error
            return 'I am still waiting'

        # Unexpected error
        except:

            # Proof that the audio could not be correctly entered
            print("Oops, something went wrong")

            # Return error
            return 'I am still waiting'


# Function for the assistant to be heard
def speak(message):

    # Starting the pyttsx3 engine
    engine = pyttsx3.init()
    engine.setProperty('voice', voice_id1)

    # Speak message
    engine.say(message)
    engine.runAndWait()


# Report day of the week
def ask_day():

    # Create variable with data of today
    day = datetime.datetime.today()

    # Create variable for the day of the week
    weekday = day.weekday()

    # Dictionary with names of the days
    calendar = {0: 'Monday',
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday'}

    # Say day of the week
    speak(f'Today is {calendar[weekday]}')


# Report time
def ask_time():

    # Create a variable with time data
    time = datetime.datetime.now()
    time = f'At this moment it is {time.hour} hours, {time.minute} minutes and {time.second} seconds.'
    print(time)
    # Report time
    speak(time)


# Initial greeting function
def initial_greeting():

    # Create variable with time data
    time = datetime.datetime.now()
    if time.hour < 6 or time.hour > 20:
        moment = 'Good night'
    elif 6 <= time.hour < 13:
        moment = 'Good morning'
    else:
        moment = 'Good afternoon'

    # Say hello
    speak(f"{moment}, I'm Hazel, your personal assistant. Please tell me how can I help you.")


# Central assistant function.
def ask_for_things():

    # Activate initial greeting
    initial_greeting()

    # Cutoff variable
    start = True

    # Central loop
    while start:

        # Activate microphone and save request in a string
        request = convert_audio_to_text().lower()

        if 'open youtube' in request:
            speak('Understood, opening Youtube.')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'open browser' in request:
            speak('Understood, opening browser.')
            webbrowser.open('https://www.google.com')
            continue
        elif 'what day is today' in request:
            ask_day()
            continue
        elif 'what time is it' in request:
            ask_time()
            continue
        elif 'search on wikipedia' in request:
            speak('Understood, searching on Wikipedia.')
            request = request.replace('search on wikipedia', '')
            wikipedia.set_lang('en')
            result = wikipedia.summary(request, sentences=1)
            speak('Wikipedia says the following: ')
            speak(result)
            continue
        elif 'search on the internet' in request:
            speak('Understood, searching on the internet.')
            request = request.replace('search on the internet', '')
            pywhatkit.search(request)
            speak("This is what I have found: ")
            continue
        elif 'play' in request:
            speak('Excellent, starting playback.')
            pywhatkit.playonyt(request)
            continue
        elif 'joke' in request:
            speak(pyjokes.get_joke())
            continue
        elif 'stock price' in request:
            stock = request.split('of')[-1].strip()
            briefcase = {'apple': 'APPLS',
                         'amazon': 'AMZN',
                         'google': 'GOOGL'}
            try:
                searched_stock = briefcase[stock]
                searched_stock = yf.Ticker(searched_stock)
                actual_price = searched_stock.info['regularMarketPrice']
                speak(f'I have found it, the price of {stock} is {actual_price}')
                continue
            except:
                speak('I am sorry, I could not find it.')
                continue
        elif 'goodbye' in request:
            speak("Goodbye, until next time")
            break


ask_for_things()
