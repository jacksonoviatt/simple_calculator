def subtract(numOne, numTwo):
    try:
        subtractNum = numOne - numTwo
        return subtractNum
    
    except ValueError:
        print("please enter a number")
