# Bruce Wong	
# STD ID: 101266031
# comp1405_f22_101266031_tutorial_03_a.py

tutorial = float(input("Average mark for Tutorials: "))

assignments = float(input("Average mark for Assignments: "))

quiz = float(input("Average mark for quizzes: "))

final = float(input("Final exam mark: "))

mark = int((tutorial * 0.1) + (assignments * 0.4) + (quiz * 0.3) + (final * 0.2))


# print(str(mark))

if mark < 50:
    print("You got an F")
elif mark > 49 and mark < 53:
    print("You got a D-")
elif mark > 52 and mark < 57:
    print("You got a D")
elif mark > 56 and mark < 60:
    print("You got a D+")
elif mark > 59 and mark < 63:
    print("You got a C-")
elif mark > 62 and mark < 67:
    print("You got a C")
elif mark > 66 and mark < 70:
    print("You got a C+")
elif mark > 69 and mark < 73:
    print("You got a B-")
elif mark > 72 and mark < 77:
    print("You got a B")
elif mark > 76 and mark < 80:
    print("You got a B+")
elif mark > 79 and mark < 85:
    print("You got a A-")
elif mark > 84 and mark < 90:
    print("You got a A")
elif mark > 89:
    print("You got a A+")    
