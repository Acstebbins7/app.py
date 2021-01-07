# print("========================")
# print("Adam What Are You Doing?")
# print("========================")


# # students_count = 1000
# # rating = 4.99
# # is_published = True

# course = "Python \nProgramming"
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(len(course))
# print(course)

# print(course.find("Py"))
# print("pro" in course)
# print("swift" not in course)

# # \" to use quote within string
# # \' to use single quote within string
# # \\ to use backslash
# # \n new line

# first = "Adam"
# last = "Stebbins"
# full = f"{first} {last}"
# print(full)

# if 10 == "10":
#     print("a")
# elif "bag" > "apple" and "bag" > "cat":
#     print("b")
# else:
#     print("c")



#     # 
# for number in range(50):
#     print("Attempt", number + 1, (number + 1) * ".")


# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")


# # Nested Loops

# for x in range(6):
#     for y in range(6):
#         print(f"({x}, {y})")


# # Iterables

# print(type(5))
# print(type(range(5)))

# for x in "Python":
#     print(x)


# for x in [1,2,3,4,5]:
#     print(x)

# While Loops

# number = 100
# while number >0:
#     print(number)
#     number //= 2


# count = 0
# for number in range(1, 10):
#     if number % 2 == 0:
#         count += 1
#         print(number)
# print(f"We have {count} even numbers")


# Functions

# def greet(fname, lname):
#     print(f"Hey {fname} {lname}")
#     print("Welcome Aboard")


# greet("Adam", "Stebbins")
# greet("John", "Smith")

# def greet(name):
#     print(f"Hey {name}")


# def get_greeting(name):
#     return f"Hey {name}"


# message = get_greeting("Adam")
# file = open("content.txt", "w")
# file.write(message)

#  Keyword Arguments

# def increment(number, by):
#     return number + by


# print(increment(2, 5))


#  XARGS

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))


# XXARGS

# def save_user(**user):
#     print(user["id"])
#     print(user["name"])
#     print(user["age"])

# save_user(id=1, name="Adam", age=33)

# DEBUGGING

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print("Start")
# print(multiply(1, 2, 3))

# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 ==0):
#         return "FizzBuzz"
#     if input % 3 == 0:
#         return "Fizz"
#     if input % 5 == 0:
#         return "Buzz"
#     return input

# print(fizz_buzz(3))


#  LISTS

# letters = ["a", "b", "c"]
# letters[0] = "A"
# matrix = [[0, 1], [2, 3], [4, 5]]
# zeros = [0] * 5
# combined = zeros + letters
# numbers = list(range(20))
# chars = list("Hello Adam")
# print(combined)
# print(numbers)
# print(len(chars))
# print(letters[0:3])
# print(numbers[::-1])


# LIST UNPACKING

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9 , 10]
# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# # OR 
# first, second, *other = numbers
# print(first)
# print(second)
# print(other)


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# items = (0, "a")
# index, letter = items
for index, letter in  enumerate(letters):
    print(index, letter)


# # ADD
# letters.append("z")
# letters.insert(0, "-")

# # REMOVE
# letters.pop(0)
# letters.remove("z")
# del letters[0:3]
# letters.clear()
# print(letters)

# SORTING LISTS

items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

def sort_item(item):
    return item[1]

items.sort()
print(items)