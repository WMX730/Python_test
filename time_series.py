from datetime import datetime, timedelta
import time

now = datetime.now()
# print("Current date and time:", now)
# print(now.year, now.month, now.day, now.hour, now.minute, now.second)

# delta = datetime(2025, 4, 20) - datetime(2025, 4, 21)
# print(delta.days)
# print(delta.seconds)

stamp = datetime(2023,7,30)
print(str(stamp))
print(stamp.strftime('%Y-%m-%d'))

time.sleep(2)  # 暂停