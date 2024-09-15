def equalcheck(a, b):
    return (a-b) == 0

num1 = int(input("Please enter a number: "))
num2 = int(input("Please enter another number: "))

if equalcheck(num1, num2):
    print("Both the numbers are equal.")
else:
    print("The numbers are not equal.")
