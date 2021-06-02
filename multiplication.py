def multiply(numOne, numTwo):
    try:
        multiplyNum = numOne * numTwo
        return multiplyNum
    
    except ValueError:
        print("please enter a number")