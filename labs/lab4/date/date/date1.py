import datetime

x = datetime.date.today()
y = datetime.timedelta(days=5)
z = x - y
print('Current day:', x.strftime("%x"))
print('Five days ago:', z.strftime("%x"))