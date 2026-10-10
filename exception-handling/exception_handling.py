def divideByZero(number: int):
    result = number / 0
    return result


try:
    result = divideByZero(10)
    print(result)
except ZeroDivisionError as e:
    print("Error unable to divide a number by 0")


# reading a file
def readFile(filename: str):
    try:
        print("Attempting to open file -> "+filename)
        file = open(filename, 'r')
        content = file.read()
    except FileNotFoundError:
        print("File not found")
    else:
        print("File read successfully")
        print(content)
    finally:
        if 'file' in locals() and not file.closed:
            file.close()
            print("Closed file")


readFile("fake_document.txt")
