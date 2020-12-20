import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_text_from_speech():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            text = listener.recognize_google(voice)
            print(text)
            return text.lower()
    except Exception as e:
        print("Exception while converting speech to text", e)
        exit()


def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('USER_NAME', 'USER_PASSWORD')
    email = EmailMessage()
    email['From'] = 'SENDER_EMAIL'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)


address_book = {
    'example': 'example@gmail.com',
    'example1': 'example2@gmail.com',
    'example2': 'example3@gmail.com'
}


def get_info_and_send_email():
    talk('Who do you want to send the email to?')
    name = get_text_from_speech()
    if name not in address_book:
        talk("Name not found in address book, please try again")
        get_info_and_send_email()
    receiver = address_book[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_text_from_speech()
    talk('What is the message?')
    message = get_text_from_speech()
    send_email(receiver, subject, message)
    talk('Email Sent Successfully')
    talk('Do you want to send another email?')
    send_more = get_text_from_speech()
    if 'yes' in send_more:
        get_info_and_send_email()


get_info_and_send_email()