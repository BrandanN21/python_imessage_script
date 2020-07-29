from time import sleep
from py_imessage import imessage
# title: send imessages script

# get words from lyrics text
def get_lyrics():
    with open('text.txt') as file:
            list = [line.strip() for line in file]
            string = " ".join(list)
            return string

# turn into a list of words
def get_words(lyrics_str):
    return lyrics_str.split()

# loop through the words
def send_messages(messages, phone_num):
    for message in messages:
        send_message(message, phone_num)
        sleep(.5)

# send a message for each word
# open imessage client
def send_message(message, phone_num):
    imessage.send(phone_num, message)

def get_lyrics_and_send_messages(phone_num, lyrics):
    words_list = get_words(lyrics)
    send_messages(words_list, phone_num)

get_lyrics_and_send_messages(phone_num, get_lyrics())