import datetime

yesterday = datetime.timedelta(days=1)
today = datetime.date.today()
tomorrow = datetime.timedelta(days=1)
print('Yesterday:', today - yesterday)
print('Today:', today)
print('Tomorrow:', today + tomorrow)