

def read_format_file_no_re(filename):
    """
    Reads the chat file and breaks each message into three components:
    Time, User, Message
    """

    list_name = []
    master_list_time = []
    list_message = []

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

                # Identifies encryption line
                if 'Messages to this group are now secured with end-to-end encryption' in data:
                    name = 'Chat Encrypted!'
                    message = 'Chat Encrypted!'

                elif ': ' in data:
                    j = data.index(': ')
                    name = data[k + 2: j].strip()
                    message = data[j + 1:].strip()

                # Identifies group creation line
                elif 'created group' in data and not ': ' in data:
                    name = 'Chat Created!'
                    message = 'Chat Created!'

                master_list_time.append(list_time)
                list_name.append(name)
                list_message.append(message)

            # Manges multi-lined messages
            else:
                last_line = ''

                while not data[0] == '[':

                    data = file.readline()

                    if data[0] == '[':

                        break

                    message = data.strip()
                    message = last_line + '\n' + message
                    last_line = message

                list_message[-1] += message

                # FIXME: Still bug that deletes message after a multiline message

            # print(message)
            # print(time)

        print(len(master_list_time))
        print(len(list_name))
        print(len(list_message))


read_format_file_no_re('_chat.txt')
