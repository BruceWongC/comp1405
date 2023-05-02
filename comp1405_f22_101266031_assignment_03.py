# Bruce Wong
# Std ID: 101266031
# comp1405_f22_101266031_assignment_03.py

import sys

A = int(sys.argv[1])
D = int(sys.argv[2])
E = int(sys.argv[3])
H = int(sys.argv[4])
I = int(sys.argv[5])
J = int(sys.argv[6])

result1 = bool(((not A) or A) and ((not E) and D)) # casting to boolean because it converts to boolean 25% of the time

result2 = bool(((H or H) or (not I)) or J)

print("<",result1,", ",result2, ">")
