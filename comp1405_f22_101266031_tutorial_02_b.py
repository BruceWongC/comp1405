# Bruce Wong
# STD ID: 101266031
# comp1405_f22_101266031_tutorial_02_b.py

num = int(input("What is your phone number?: "))

firstnum = num // 10000

secondnum = num % 10000

# print(firstnum, secondnum)

print(firstnum)

result = firstnum * 50 
print(result)

result = result + 5
print(result)

result = result * 600
print(result)

result = result + (3 * secondnum)
print(result)

result = result / 3

result = str(int(result - 1000))
print(result)