# default args, kwarg, args

# # Default Arguements

# def report(name, age='16', grade='X', result='passed'):
#     print(f'{name}, age {age}, from class {grade} has {result}.') 

# report('Sahil')
# report('Rishabh', result='failed')
# report('Sonal', age='15')
# report('Sanvi', grade='XII')
# report('Lakshya', age='18', grade='XII', result='failed')

# ---------------------------------------------------------------------------------

# *args

# example #1

# def add(*num_tuple):
#     sum = 0

#     for i in num_tuple:
#         sum = sum + i
    
#     print(f'Sum of {num_tuple} is {sum}.')

# add(2, 3)
# add(2, 3, 4)
# add(2, 3, 4, 5)
# add(2, 3, 4, 5, 6)
# add(2, 3, 4, 5, 6, 7)


# # example #2

# def addition(a, b, *args, option=True):
#     result = 0
#     if option:
#         for i in args:
#             result += i
#         return a + b + result
#     else:
#         return result

# print(addition(1, 4, 5, 6, 7))
# print(addition(1, 4, 5, 6, 7, option=False))

# ---------------------------------------------------------------------------------

# **kwargs

# # example #1

# def intro(**data):
#     print('\nData type of arguement : ', type(data))
#     print('-----------------------------------------')

#     for key, value in data.items():
#         print(f'{key} is {value}.')

#     print('-----------------------------------------')

# intro(First_Name='Rishabh', Last_Name='Pundir', Age='25', Phone='6978565156522')
# intro(First_Name='Singh', Last_Name='Singh', Dob='14 Apr 1998', Email='SachinSingh62@xyz.com')


# # example #2

# def printer(a, b, option=True, **kwargs):
#     print(f'{a} + {b} = {a+b}')
#     if option==True:
#         print(kwargs)

# printer(3, 4, parameter1=5, parameter2=6)
# printer(4, 5, option=False, parameter1='Rishabh', paramter2='Intern')
