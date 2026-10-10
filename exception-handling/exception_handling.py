def divideByZero(number: int):
    result = number / 0
    return result


try:
    result = divideByZero(10)
    print(result)
except ZeroDivisionError as e:
    print("Error unable to divide a number by 0")
