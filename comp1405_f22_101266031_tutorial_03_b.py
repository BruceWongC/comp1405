# Bruce Wong	
# STD ID: 101266031
# comp1405_f22_101266031_tutorial_03_b.py

print("Many kinds of people made the trip to Oregon.\nYou may:")
print(" 1. Be a banker from Boston ($1600) \n 2. Be a carpenter from Ohio ($800) \n 3. Be a farmer fomr Illinois ($400)")

var = input("\nWhat is your choice? ")

if var == "1":
    amount = 1600.0
elif var == "2":
    amount = 800.0
elif var == "3":
    amount = 400.0
        
oxen = float(input("Amount you have: $" + str(amount) + "\nHow many oxen do you want? ($20 per oxen): "))
amount -= oxen * 20

food = float(input("Amount you have: $" + str(amount) + "\nHow many pounds of food do you want? ($0.20 per pound): "))
amount -= food * 0.2

clothing = float(input("Amount you have: $" + str(amount) + "\nHow many sets of clothing do you want? ($10 per set): "))
amount -= clothing * 10
print(str(amount))

