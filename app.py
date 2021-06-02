import multiplication as m
import division as d
import addition as a
import subtraction as s


print("1: Add two numbers") 
print("2: Subtract two numbers")
print("3: Multiply two numbers")
print("4: Divide two numbers")
# except WrongNumber:
    # print

userChoice = int(input())
# print(userChoice)
if(userChoice == 1):
    print("please enter your first number:")
    numOne = int(input())
    print("please enter yout second number")
    numTwo = int(input())
    print(a.add(numOne, numTwo))
    print("Add more? y/N")
    addMore = input()

elif(userChoice == 2):
    print("please enter your first number:")
    numOne = int(input())
    print("please enter yout second number")
    numTwo = int(input())
    print(s.subtract(numOne, numTwo))
elif(userChoice == 3):
    print("please enter your first number:")
    numOne = int(input())
    print("please enter yout second number")
    numTwo = int(input())
    print(m.multiply(numOne, numTwo))
elif(userChoice == 4):
    print("please enter your first number:")
    numOne = int(input())
    print("please enter yout second number")
    numTwo = int(input())
    print(d.divide(numOne, numTwo))
    # userChoice = int(input())userChoice = int(input())userChoice = int(input()) userChoice = int(input())