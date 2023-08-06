import string
import boto3
import pyperclip
import playsound
import os
from tempfile import gettempdir
from super_secret_key_location import *


def words_that_kill(x):
    polly_client = boto3.Session(aws_access_key_id=supa_secret_access_key_id,
                                 aws_secret_access_key=very_much_secret_sneaky_access_key,
                                 region_name=region_name_iz_secret_too).client('polly')

    response = polly_client.synthesize_speech(Engine='standard', LanguageCode='ru-RU', OutputFormat='mp3',
                                              TextType='ssml', Text=x, VoiceId='Tatyana')

    filename = 'temp.mp3'

    output = './temp.mp3'

    with open(output, "wb") as file:
        file.write(response['AudioStream'].read())

    playsound.playsound(output, True)

    os.remove(output)


def would_you_speak_them_to_me(x):
    phrase_list = x.split(' ')

    new_list = []
    for single_word in phrase_list:
        for eng_letters in list(string.ascii_letters):
            if eng_letters in single_word:
                single_word = f"<lang xml:lang='en-US'>{single_word}</lang>"
                break
        new_list.append(single_word)

    edited_line = ' '.join(new_list)

    return f'<speak>{edited_line}</speak>'


def with_your_breath_so_still():
    while True:
        pyperclip.waitForNewPaste()
        x1 = pyperclip.paste()
        x2 = would_you_speak_them_to_me(x1)
        words_that_kill(x2)


if __name__ == '__main__':
    with_your_breath_so_still()
