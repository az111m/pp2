import datetime

date1 = datetime.datetime(2024, 3, 23, 21, 35, 54)
date2 = datetime.datetime(2024, 6, 12, 7, 15, 13)
diff = date1 - date2
diff_in_seconds = diff.total_seconds()
print(int(abs(diff_in_seconds)))