import time

import pyttsx3

import random


# Initialize the TTS engine

engine = pyttsx3.init()


# Function to set the language for the TTS engine

def set_language(language='en'):

    voices = engine.getProperty('voices')

    if language == 'en':

        for voice in voices:

            if 'english' in voice.id.lower():

                engine.setProperty('voice', voice.id)

                break

    elif language == 'te':

        for voice in voices:

            if 'telugu' in voice.languages[0].lower():

                engine.setProperty('voice', voice.id)

                break

    elif language == 'hi':

        for voice in voices:

            if 'hindi' in voice.languages[0].lower():

                engine.setProperty('voice', voice.id)

                break

    else:

        engine.setProperty('voice', voices[0].id)  # Default to the first available voice


# Function to simulate voice output

def speak(text, language='en'):

    set_language(language)

    engine.say(text)

    engine.runAndWait()

    time.sleep(2)  # Simulate speech delay


# Function to simulate voice input

def get_input(prompt, language='en'):

    if language == 'en':

        return input(prompt)

    elif language == 'te':

        return input("దయచేసి ఇక్కడ కార్డు నిలుపుతారని నేను చెప్పినది. మీరు కార్డు నిలుపుతున్నారా? (Y/N): ")

    elif language == 'hi':

        return input("कृपया यहाँ कार्ड डालें। (Y/N): ")

    else:

        return input(prompt)  # Default to English if language code is not recognized


# Function to generate a random PIN

def generate_pin():

    return str(random.randint(1000, 9999))


# Function to simulate balance checking

def check_balance(language='en'):

    speak("Your current balance is 50,000 rupees.", language)


# Function to simulate ATM withdrawal process

def withdraw_money():

    language_choice = get_input("Please select your preferred language: 1. Telugu, 2. English, 3. Hindi: ")


    if language_choice == "1":

        speak("ఆటోమేట్ లో స్వాగతం!", 'te')

        speak("దయచేసి మీ కార్డు నిలుపుతారని చెప్పండి.", 'te')

        speak("మీరు డబ్బు తీసుకోవాలనుకుంటున్నారా? దయచేసి నిర్ణయం తీసుకోండి.", 'te')

        speak("దయచేసి మీ పిన్ నమోదు చేయండి.", 'te')

        # More instructions in Telugu...

    elif language_choice == "2":

        speak("Welcome to the ATM!", 'en')

        speak("Please insert your card.", 'en')

        speak("Would you like to make a withdrawal? Please make a decision.", 'en')

        speak("Please enter your PIN.", 'en')

        # More instructions in English...

    elif language_choice == "3":

        speak("एटीएम में आपका स्वागत है!", 'hi')

        speak("कृपया अपना कार्ड डालें।", 'hi')

        speak("क्या आप पैसे निकालना चाहते हैं? कृपया निर्णय लें।", 'hi')

        speak("कृपया अपना पिन दर्ज करें।", 'hi')

        # More instructions in Hindi...

    else:

        speak("Invalid choice. Please try again.", 'en')

        return


    # Continue with the transaction process...

    if language_choice in ["1", "2", "3"]:

        transaction_type = get_input("Select transaction type: 1. Withdraw Money, 2. Credit Money, 3. Exit: ", language_choice)


        if transaction_type == "1":

            amount = get_input("How much would you like to withdraw? (Please enter the amount): ", language_choice)

            speak(f"You have chosen to withdraw {amount} rupees. Please confirm.", language_choice)


            confirmation = get_input("Do you want to proceed? (Y/N): ", language_choice)

            if confirmation.lower() == "y":

                speak("Processing your transaction, please wait...", language_choice)

                time.sleep(3)  # Simulate transaction processing time

                speak("Transaction successful. Please take your cash.", language_choice)

            else:

                speak("Transaction cancelled.", language_choice)


        elif transaction_type == "2":

            amount = get_input("How much would you like to credit? (Please enter the amount): ", language_choice)

            speak(f"You have chosen to credit {amount} rupees. Please confirm.", language_choice)


            confirmation = get_input("Do you want to proceed? (Y/N): ", language_choice)

            if confirmation.lower() == "y":

                speak("Processing your transaction, please wait...", language_choice)

                time.sleep(3)  # Simulate transaction processing time

                speak("Amount credited successfully.", language_choice)

            else:

                speak("Transaction cancelled.", language_choice)


        elif transaction_type == "3":

            speak("Exiting the ATM. Thank you for using our services.", language_choice)

        else:

            speak("Invalid option. Please try again.", language_choice)


# Main function

def main():

    while True:

        button_pressed = get_input("Press the guidance button if you need assistance (Y/N): ", 'en')

        if button_pressed.lower() == "y":

            withdraw_money()

        else:

            speak("Thank you for using the ATM. Have a nice day.", 'en')

            break


if _name_ == "_main_":

    main()

