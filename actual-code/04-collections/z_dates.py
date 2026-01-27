import datetime

today = datetime.datetime(2026,1,27)
yesterday =datetime.datetime(2026,1,26) 

days = [today, yesterday]
days.sort()
print(days)


start = datetime.date(2026, 1, 1)
end = datetime.date(2026, 1, 31)
target = datetime.date(2026, 2, 15)

is_in_range = start <= target <= end

print(is_in_range)

  