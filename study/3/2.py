year =2000
month = 10
day = 27
hour = 11
minute = 43
second = 59

print(year, month, day, sep=('/'), end=(' '))
print(hour, minute, second, sep=(':'))


year, month, day, hour, minute,second = input().split()
print(year, month, day, sep='-', end='T')
print(hour, minute, second, sep=':')