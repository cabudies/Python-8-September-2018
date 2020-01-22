



# # exception handling
#
var_1 = input('Enter the value of first number: ')
var_2 = input('Enter the value of second number: ')

try:
    var_1 = int(var_1)
    var_2 = int(var_2)

    if (var_2 != 0):
        result = var_1 / var_2
        print('Division Result is: ', result)
    else:
        print('Value of second variable cannot be zero.')
except ValueError:
    print("Can only enter integers")
















# try:
#     var_1 = int(var_1)
#     var_2 = int(var_2)
#
#     if (var_2 != 0):
#         result = var_1 / var_2
#         print('Division Result is: ', result)
#     else:
#         print('Value of second variable cannot be zero.')
# except ValueError:
#     print("You can only enter integer numbers.")












# var_1 = input('Enter the value of first number: ')
# var_2 = input('Enter the value of second number: ')
#
# try:
#     var_1 = int(var_1)
#     var_2 = int(var_2)
#
#     if (var_2 != 0):
#         result = var_1 / var_2
#         print('Division Result is: ', result)
#     else:
#         print('Value of second variable cannot be zero.')
# except ValueError:
#     print("Enter integer values only.")





#
# # take input from the user till the time the values are not integer.
# while True:
#     var1 = input('Enter the first number: ')
#     var2 = input('Enter the second number: ')
#
#     try:
#         int_var1 = int(var1)
#         int_var2 = int(var2)
#         break
#     except ValueError:
#         print('Enter only integer values.')
#
#
# # take value from variable 1, 2 and 3. Compute the difference of variable 1, 2 and then
# # divide it's result from variable 3
# var1 = int(input('Enter the value of first number: '))
# var2 = int(input('Enter the value of second number: '))
# var3 = int(input('Enter the value of third number: '))
#
# result = var1 - var2
#
# division_result = var3/result
#
# print(division_result)























