# Bruce Wong
# STD ID: 101266031
# comp1405_f22_101266031_tutorial_02_a.py

Name = input("What is your name?: ")

year = int(input("What year is it?: "))

born = int(input("What year were you born?: "))

age1 = str(year - born)
age2 = str(year - born - 1)

age_leap2 = str((year - born) // 4)

print("Hi, "+ Name +". Possible age: " + age2 + "-" + age1 + ". If you were born on a leap year: " + age_leap2)

