# While loop
# Incrementing a value
number = 5
while number <= 10:
    print(number)
    number += 1

# Decrementing a value
num = 105
while num >= 100:
    print(num)
    num -= 1

# Break Statement - exits the entire loop
x = 1
while x <= 5:
    print(x)
    if x == 3:
        break
    x += 1

# Continue Statement - skips a specific number in the loop
count = 19
while count < 25:
    count += 1
    if count == 23:
        continue

    print(count)

# For loop
languages = ["python", "java", "C++"]
for lang in languages:
    print(lang)

# Range
for z in range(6):               # When you  don't  want to specify the starting and the ending number
    print(z)

for y in range(20, 31):      # When you want to specify the starting and the ending number
    print(y)

for i in range(30, 41, 2):    # When putting three vales in the brackets the last number is to show the increment value
    print(i)

for p in str("innovation"):
    print(p)