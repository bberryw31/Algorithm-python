import sys

input = sys.stdin.readline().strip()
if input == "F":
    print("0.0")
else:
    grade = []
    grade.extend(input)
    if grade[0] == "A":
        result = 4.0
    elif grade[0] == "B":
        result = 3.0
    elif grade[0] == "C":
        result = 2.0
    elif grade[0] == "D":
        result = 1.0
    else:
        print("improper grade")
    
    if grade[1] == "+":
        result += 0.3
        print(result)
    elif grade[1] == "0":
        print(result)
    elif grade[1] == "-":
        result += -0.3
        print(result)
    else:
        print("improper grade")
