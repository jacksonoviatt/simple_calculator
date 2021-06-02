# import the traceback that will be used in the except block
import traceback

# this function will divide the the two numbers in the argument
def divide(numOne, numTwo):
    # try to return the quotient
    # except if the use rtries to divide by 0
    try:
        divideNum = numOne / numTwo
        return divideNum
    except ZeroDivisionError:
        traceback.print_exc()
        print("NO DIVISION BY 0")

    except ValueError:
        print("please enter a number")