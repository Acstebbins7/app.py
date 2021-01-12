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


# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# # items = (0, "a")
# # index, letter = items
# for index, letter in  enumerate(letters):
#     print(index, letter)


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

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# #  One way
# def sort_item(item):
#     return item[1]
#  Better way using lambda
# items.sort(key=lambda item:item[1])
# print(items)


#  MAP FUNCTIONS
#  one way
# prices = []
# for item in items:
#     prices.append(item[1])

# another way
# x = map(lambda item: item[1], items)
# for item in x:
#     print(item)


# prices = list(map(lambda item: item[1], items))
# print(prices)


#  FILTERING FUNCTIONS
# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# # filtered = list(filter(lambda item: item[1] >= 10, items))
# # print(filtered)

# # prices = [item[1] for item in items]

# filtered = [item for item in items if item[1] >= 10]

# Zip Function
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]

# print(list(zip(list1, list2)))



# #  STACKS
# browsing_session = []
# browsing_session.append(1)
# browsing_session.append(2)
# browsing_session.append(3)
# print(browsing_session)
# last = browsing_session.pop()
# print(last)
# print(browsing_session)
# print("redirect", browsing_session[-1])
# if not browsing_session:
#     print("disable")

#  QUEUES
# from collections import deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)
# if not queue:
#     print("empty")

#  TUPLES
# point = 1, 2
# print(type(point))

# point = (1, 2) + (3, 4)
# print(point)

# point = (1, 2) * 3
# print(point)

# point = tuple("Hello Adam")
# print(point)


#  SWAPPING VARIABLES
# x = 10
# y = 11

# z = x
# x = y
# y = z

# print("x", x)
# print("y", y)

# x, y =  y, x


#  ARRAYS
# from array import array

# array("i", [1,2,3])
# numbers[0]


#  SETS
# numbers = [1,1,2,3,4]
# # uniques = set(numbers)
# # second = {1, 4}
# # second.add(5)
# # second.remove(5)
# # len(second)
# # print(uniques)
# first = set(numbers)
# second = {1, 5}
# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)

# if 1 in first:
#     print("yes")


# DICTIONARY iterating over a dictionary
# point = {"x": 1, "y": 2}
# point = dict(x=1, y=2)
# print(point["x"])
# point["x"] = 10
# point["z"] = 20
# print(point)
# if "a" in point:
#     print(point["a"])
# print(point.get("a", 0))
# del point["x"]
# print(point)
# for key in point:
#     print(key, point[key])
# # Printing a Tuple
# for x in point.items():
#     print(x)
# # UNPACKING THEM
# for key, value in point.items():
#     print(key, value)


# List Comprehension
# values = []
# for x in range(5):
#     values.append(x * 2)


# values = {}
# for x in range(5):
#     values[x[] = x * 2
# CHANGE to this below
# dictionaries
# values = {x: x * 2 for x in range(5)}

# print(values)

# Generator Expressions
# from sys import getsizeof

# values = [x * 2 for x in range(10)]
# for x in values:
#     print(x)

# values = (x * 2 for x in range(10))
# for x in values:
#     print(x)

# values = (x * 2 for x in range(100000))
# print("gen:", getsizeof(values))

# values = [x * 2 for x in range(100000)]
# print("list:", getsizeof(values))

# UNPACKING OPERATOR
# numbers = [1, 2, 3]
# print(numbers)
# print(*numbers)
# print(1, 2, 3)

# values = list(range(5))
# values = [*range(5), *"Hello"]
# print(values)

# first = [1, 2]
# second = [3]
# values = [*first, "a", *second, *"Hello"]
# print(values)

# from pprint import pprint
# sentence = "This is a common interview question"

# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
# # print(char_frequency)
# # pprint(char_frequency, width=1)

# char_frequency_sorted = (
#     sorted(char_frequency.items(), 
#     key=lambda kv:kv[1], 
#     reverse= True)
# )
# print(char_frequency_sorted[0])


# Handling Exceptions
# try:
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
#     # print(ex)
#     # print(type(ex))
# else:
#     print("No exceptions were thrown")

# CLEANING THIS UP
# try:
#     file = open("app.py")
#     age = int(input("Age: "))
#     xfactor = 10 / age
# except (ValueError, ZeroDivisionError):
#     print("You didn't enter a valid age.")
# else:
#     print("No exceptions were thrown.")
# finally:
#     file.close()

# RAISING EXCEPTIONS dont use 

# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be zero or less.")
#     return 10 / age


# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     print(error)

# COST OF RAISING EXCEPTIONS
# from timeit import timeit

# code1 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError("Age cannot be zero or less.")
#     return 10 / age


# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     pass
# """

# code2 = """
# def calculate_xfactor(age):
#     if age <= 0:
#         return None
#     return 10 / age


# xfactor = calculate_xfactor(-1)
# if xfactor == None:
#     pass
# """

# print("first code=", timeit(code1, number=100))
# print("second code=", timeit(code2, number=100))

# CLASSES AND CONSTRUCTORS

# class Point:
#     default_color = "red"
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")
#         # print("draw")
# # CLASS ATTRIBUTES
# point = Point(1, 2)
# print(point.default_color)
# print(Point.default_color)
# point.draw()
# # print(point.x)
# # print(point.y)
# # print(type(point))
# # print(isinstance(point, Point))

# another = Point(3, 4)
# another.draw()

# point1 = Point(5, 6)
# point1.draw()

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # @classmethod
#     # def zero(cls):
#     #     return cls(0, 0)

#     def __str__(self):
#         return f"({self.x}, {self.y})"


#     def draw(self):
#         print(f"Point ({self.x}, {self.y})")


# # point = Point.zero()
# # point.draw()


# point = Point(1, 2)
# print(str(point))


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y


# point = Point(10, 20)    
# other = Point(1, 2)
# print(point > other)
# print(point < other)
# print(point == other)


# MAKING CUSTOM CONTAINERS

# class TagCloud:

# cloud = TagCloud()
# len(cloud)
# cloud["python"] = 10
# for tag in cloud:
#     print(tag)

# class TagCloud:
#     def __init__(self):
#         self.tags = {}

#     def add(self, tag):
#         self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

#     def __getitem__(self, tag):
#         return self.tags.get(tag.lower(), 0)

#     def __setitem__(self, tag, count):
#         self.tags[tag.lower()] = count

#     def __len__(self):
#         return len(self.tags)

#     def __iter__(self):
#         return iter(self.tags)
    
# cloud = TagCloud()
# cloud["python"] = 10
# len(cloud)
# cloud.add("python")
# print(cloud.tags)



# PROPERTIES

# class Product:
#     def __init__(self, price):
#         self.pice = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value

# #     price = property(get_price, set_price)


# product = Product(10)
# print(product.price)