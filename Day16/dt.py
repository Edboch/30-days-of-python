from datetime import datetime,timedelta

current = datetime.now()
print(current)

changed = current.strftime("%m/%d/%Y, %H:%M:%S")
print(changed)

date_string = '5 December, 2019'
converted_date = datetime.strptime(date_string,"%d %B, %Y")
print(converted_date)

new_year = datetime(year=2025,month=1,day=1)
print(new_year-current)

timestamp = datetime.now().timestamp()
t1 = timedelta(seconds=timestamp)
print(t1)