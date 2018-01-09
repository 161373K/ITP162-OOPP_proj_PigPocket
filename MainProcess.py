from Users import Users

def processUserDetails():
    detailsList = []
    user_file = open('file/accountDetails', 'r')
    for dlist in user_file:
        list = dlist.split(',')
        s = Users(list[0], list[1], list[2], float(list[3]), float(list[4]))

        detailsList.append(s)
    return detailsList
