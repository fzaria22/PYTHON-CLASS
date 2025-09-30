# # 2+2
# # print('helloworld')

# # LOOPS
# # FOR LOOP

# # fruits = ["Apple", "Mango", "Banana", "Orange"]
# # for fruit in fruits:
# #     print(fruit)

# # fruits and their index
# # fruits = ["Apple", "Mango", "Banana", "Orange",]
# # for index, fruit in enumerate(fruits):
# #     print(index, fruit)

# # for if in python
# # name = "John"
# # for char in name:
# #     print(char)

# # fruits = ["Apple", "Mango", "Banana", "Orange"]
# # for fruit in fruits:
# #     if fruit == "Banana":
# #         print(f"{fruit} you have found banana")
# #         break
# #     # else:
# #     print(f"{fruit} loop continues")

# # while loop
# # age = 5
# # while age < 10:
# #     print(f"Your still young")
# #     age += 1


# # first_array = [1, 2, 3, 4, 5]
# # second_array = [5, 4, 7, 8, 9]
# # sorted_array = sorted(first_array + second_array)
# # print(sorted_array)

# # set in python
# # a = {1, 2, 3, 4, 5}
# # b = {4, 5, 6, 7, 8, 1}
# # print('a union b', a | b)
# # print('a intersection b', a & b)
# # print('a difference b', a - b)

# # Dictionary in python
# # person = {
# #     "name": "John",
# #     "age": 30,
# #     "city": "New York"
# # }
# # # print(person)
# # print(person['age'])
# # for key, value in person.items():
# #     print(f"{key}: {value}")


# # def name(name):
# #     return name


# # print(name(name="John"))

# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # total = 0
# # for number in numbers:
# #     if number % 2 == 0:
# #         # print(number)
# #         total += number
# # print(total)

# # Highest = max(numbers)
# # print(Highest)

# # email =
# # password =
# # if email == 'faisalidrs@gmail.com' and password == '12345':
# #     print('Login Successful')
# # else:
# #     print('Login Failed')

# # height = "6 Ft"


# # def greeting(first_name, last_name, age):
# #     print('Hello', first_name, last_name, age)
# #     print(f"Hello, my name is  {first_name} {last_name}, i am {age} ")


# # greeting('ayoola', 'adewale', 40)
# # def sum_two_numbers(num1, num2):
# #     return [num1, num2]


# # result = sum_two_numbers(10, 10)
# # print(result)

# #
# #     sum_two_numbers(10, 10)

# def user_grade(grade1, grade2):
#     return (grade1 + grade2)/2


# ayoola = user_grade(10, 100)
# if ayoola > 60:
#     print('pass')
# elif ayoola > 50:
#     print('jst dey go')
# else:
#     print('repeat for me jor')


# def user_grade2(grade1, grade2):
#     result = (grade1 + grade2)/2
#     if result > 60:
#         print('pass')
#     elif result > 50:
#         print('jst dey go')
#     else:
#         print('repeat for me jor')


# user_grade2(10, 100)


# LIST COMPREHENSION
# salaries = [200000, 100000, 300000]
# increment = []
# for salary in salaries:
#     # print(salary+(salary*0.25))
#     new_Salary = salary + (salary*0.5)
#     increment.append(new_Salary)
# print(increment)

# gross_Allowances = [1000, 2000, 3000]
# deductions = [ for gross_Allowance in gross_Allowances]
#:
#     net_Allowances = gross_Allowances/100
#     deductions.append(net_Allowances)
# print(deductions)

# values = [10, 20, 30]
# new_values = [value * 2 for value in values]
# print(new_values)


# gross_Pays = [100, 200, 300]
# deduction = [gross_Pays * 20 for gross_Pay in gross_Pays]
# print(deduction)

# BUILT IN MODULES AND LIBARARIES
# MATHEMATICS OPS
# import math
# print(math.sqrt(8))

# import random
# # print(random.randint(1, 10))

# List = ['apple', 'orange']

# print(random.choice(List))

# import datetime
# from datetime import datetime
# print(datetime.now())
