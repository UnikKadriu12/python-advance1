import datetime


tani = datetime.datetime.now()

print(tani)


print(tani.year)
print(tani.month)
print(tani.day)
print(tani.hour)
print(tani.second)
print(tani.microsecond)


eventi = datetime.date(2024,4,5)



print(f"eventi mbahet ne muajin {eventi.month}, dhe ne diten {eventi.day}")