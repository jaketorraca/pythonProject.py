minutes = int(input('Enter number of minutes: '))
days = minutes / 60 / 24 % 365
years = minutes / 60 / 24 / 365
print(minutes, 'minutes is ', int(years), 'and', int(days), 'days')