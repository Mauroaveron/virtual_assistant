import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


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


convert_audio_to_text()
