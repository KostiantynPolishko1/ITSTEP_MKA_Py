from datetime import datetime, timedelta

today = datetime.today()
print(today)

# today2 = datetime.utcnow()
# print(today2)
#
# today3 = datetime.now()
# print(today3)

begin = today.strftime('%A %d %H:%M')
period = timedelta(days=17, hours=4)
end = (today + period).strftime('%A %d %H:%M')

print(f"time start is {begin}")
print(f"time finish is {end}")

birthday = datetime.date(datetime.strptime('06/02/1985', '%d/%m/%Y'))
print(birthday)

birthday = birthday + period
print(birthday)