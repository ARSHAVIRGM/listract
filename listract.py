

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
