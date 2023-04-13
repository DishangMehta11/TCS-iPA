

def getDate(date, month):
    # lst31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
    # lst30 = ['', 'February', 'April', 'June', 'September', 'November']
    dic = {'January': 31, 'February': 29, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30,  'October': 31, 'November': 30, 'December': 31}

    month = 'January'
    days = 183
    for i, mon in enumerate(dic.keys()):
        days -= dic[mon]
        month = mon
        if days < dic[mon]:
            date += days
            month = dic

    # days = 183
    # while days > 30:
    #     if month in lst31:
    #         month = lst30[lst31.index(month)+1]
    #         days -= 31
    #     elif month in lst30:
    #         month = lst31[lst30.index(month)]
    #         days -= 30
    return date, month


print(getDate(15, 'January'))
