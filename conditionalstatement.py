temperature = 32

if temperature > 37:
    print("It is hot")

else:
    print("It is cold")

# A Program that prints the largest number among three numbers
num1 = 45
num2 = 89
num3 = 32

if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")


elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")

else:
    print(num3, "is the largest number")

# A program that checks whether a number is even or odd
# For an odd number after division with two the outcome should be zero
number = 56
if number % 2 == 0:
    print(number, "is even")

else:
    print(number, "is odd")

# Determining a prime number
num = 17
if num > 1:
    for i in range(2, int(num / 2)):
        if num % i == 0:
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is a prime number")

else:
    print(num, "is not a prime number")



# Determining a prime number
numeral = int(input("Enter a number: "))
if numeral > 1:
    for i in range(2,numeral):
        if numeral % i == 0:
            print(numeral, "is not a prime number")
            break
        else:
            print(numeral, "is a prime number")
    else:
        print(numeral, "is not a prime number")






