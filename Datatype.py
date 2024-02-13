#  datatype
number = 60  # int
num = 34.78  # float
greeting = "Hello there"  # str
isPythonInteresting = True  # bool

# A variable with multiple values
languages = ["python", "PHP", "java"]  # list
fruits = ("apple", "banana", "oranges")  # tuple
countries = {"kenya", "Ghana", "China"}  # set
# Dictionary
details = {
    "firstname": "Ashley",
    "course": "MIT",
    "age": 18,
    "nationality": "kenyan"

}

print(number)
print(num)
print(greeting)
print(countries)
print(details)
print(details["firstname"])
print(details["nationality"])

# Determining data type of a variable
print(type(details))
print(type(countries))
print(type(greeting))

# Typecasting - Converting one data type to another
print(float(number))
print(int(num))
