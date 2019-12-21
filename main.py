import numpy as np
import matplotlib.pyplot as plt
import datetime as date

class Main:

    def readtextfile(filename):
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

                if data[0] == '[':
                    k = data.index(']')

                    time = data[1: k]
                    list_time = time.split(', ')
                    print(list_time)






Main.readtextfile('_chat.txt')
