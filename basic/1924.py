day = 0
arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

x, y = map(int, input().split())

for i in range(x-1):
    day = day + arr[i]
day = (day + y) % 7
print(week[day])

# calendear module 이용
# import calendar
#
# week = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
# x, y = map(int, input().split())
#
# day = calendar.weekday(2007, x, y)
# print(week[day])
