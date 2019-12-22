import numpy as np
import matplotlib.pyplot as plt
import datetime as date
import nltk
import re


def read_format_file(filename):
    """
    Reads the chat file and breaks each message into three components:
    Time, User, Message
    """

    with open(filename, 'r') as file:

        notdone = True

        while notdone:
            data = file.readline()
            # print(data)

            if data == '':
                notdone = False
                break
            # Breaks apart each line
            if data[0] == '[':
                k = data.index(']')

                time = data[1: k]
                list_time = time.split(', ')
                # print(list_time)

                if 'Messages to this group are now secured with end-to-end encryption' in data:
                    name = 'Chat Encrypted!'
                    message = 'Chat Encrypted!'

                elif ': ' in data:
                    j = data.index(': ')
                    name = data[k + 2: j].strip()

                elif 'created group' in data and not ': ' in data:
                    name = 'Chat Created!'
                    message = 'Chat Created!'

                print(name)


read_format_file('_chat.txt')
