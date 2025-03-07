
month = 10
month_to_season = int(month)


if 1 <= month <= 2 or month == 12:
    print ("зима")
elif 6 <= month <= 8:
    print ("лето")
elif 9 <= month <= 11:
    print("осень")
elif 3 <= month <= 5:
    print("весна")
else:
    print("Неверный номер месяца") 
