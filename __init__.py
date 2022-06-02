
#  _                            _                 _                  _               _    _                 _
# | |                          | |               (_)                (_)             | |  | |               (_)
# | |__  _   _    __ _ _ __ ___| |__   __ ___   ___ _ __   _ __ ___  _ _ __ ______ _| | _| |__   __ _ _ __  _ 
# | '_ \| | | |  / _` | '__/ __| '_ \ / _` \ \ / / | '__| | '_ ` _ \| | '__|_  / _` | |/ / '_ \ / _` | '_ \| |
# | |_) | |_| | | (_| | |  \__ \ | | | (_| |\ V /| | |    | | | | | | | |   / / (_| |   <| | | | (_| | | | | |
# |_.__/ \__, |  \__,_|_|  |___/_| |_|\__,_| \_/ |_|_|    |_| |_| |_|_|_|  /___\__,_|_|\_\_| |_|\__,_|_| |_|_|
#         __/ |                                                                                               
#        |___/                                                                                                


def extract(list, to):

    for x in range(len(list)):

        is_list = type(list[x]) == list

        if is_list == True:

            for y in range(len(list[x])):

                mov = list[x][y]

                try :
                    to.index(mov)

                except :
                    to.append(mov)
        else:

            try :

                to.index(list[x])

            except :
                to.append(list[x])

def merge(list1 , list2 , to ):

    for x in range(len(list1)):

        is_list1 = type(list1[x]) == list1

        if is_list1 == True:

            for y in range(len(list1[x])):

                mov = list1[x][y]

                try :
                    to.index(mov)

                except :
                    to.append(mov)
        else:

            try :

                to.index(list1[x])

            except :
                to.append(list1[x])

    for x in range(len(list2)):

        is_list2 = type(list2[x]) == list2

        if is_list2 == True:

            for y in range(len(list2[x])):

                mov = list2[x][y]

                try :
                    to.index(mov)

                except :
                    to.append(mov)
        else:

            try :

                to.index(list2[x])

            except :
                to.append(list2[x])