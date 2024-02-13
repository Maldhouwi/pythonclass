# Exceptions = errors
x = 5
try:
    print(x)
except:
    print("an error occurred")
finally:
    print("success")


num1 = 20
num2 = 0
try:
    print(num1 / num2)
except:
    print("ZeroDivision  Error occurred")

# User-Defined Functions
try:
    def multiply(number1, number2):
        print(number1 * number2)

except:
    print("Error occurred")

finally:
    print("success")


multiply(6,5)