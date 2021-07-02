# author: Daniel Villano-Herrera
# date: July 02, 2021
#
# description: <fill in>

# --------------- Section 1 --------------- #

# 1.1 | Variable Creation | Strings
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# Variables
#   1) Create a variable that holds your name.
#   2) Create a variable that holds your birthday.
#   3) Create a variable that holds the name of an animal you like.
#
# Print
#   4) Print each variable, describing it when you print it.
#
# Example Code
example_name = 'elia'
print('EXAMPLE: my name is', example_name)

# WRITE CODE BELOW
name = 'Daniel'
print('My name is', name)

birthday = '07/03/2001'
print('My birthday is', birthday)

favorite_animal = 'Cat'
print('My favorite animal is', favorite_animal)



# 1.2 | Variable Creation | Integers / Floats
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# All variables created in this section should hold either an integer or float.
#
# Variables
#   1) Create a variable that holds your favorite number.
#   2) Create a variable that holds the day of the month of your birthday.
#   3) Create a variable that holds a negative number.
#   4) Create a variable that holds a floating (decimal) point number.
#
# Print
#   5) Print each variable, describing the value you print.

# WRITE CODE BELOW
favorite_number = 1738
birthday_day = 3
negative_number = -2
float_number = 4.61
print('My favorite number is', favorite_number)
print('The day of the month of my birthday is', birthday_day)
print('The negative number I chose is', negative_number)
print('The float number I chose is', float_number)



# 1.3 | Overwriting Variables
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# Variables
#   1) Overwrite the variable holding your name, and save a different name to it.
#   2) Overwrite the variable holding birthday with the day you think would be best to have a birthday on.
#   3) Overwrite the variable holding your favorite number and set it to a number you think is unlucky.
#
# Print
#   4) Print the variables you've overwritten, describing the values you print.
#
# Example Code
example_name = 'lucia'
print('EXAMPLE: my new name is', example_name)

# WRITE CODE BELOW

name = 'Raymond'
print('My new name is', name)
birthday_day = 4
print('I think it would be best to have my birthday on the', birthday_day)
favorite_number = 7
print('I think the unlucky number is', favorite_number)

# 1.4 | Operations
#
# Relevant Documentation
#   - https://www.w3schools.com/python/python_variables.asp
#   - https://www.w3schools.com/python/python_variables_names.asp
#
# Variables
#   1) Create a variable that is the sum of two numbers.
#   2) Create a variable that is the product of three numbers.
#   3) Create a variable by dividing the previously created sum, with the previously created product.
#
#   4) Create a variable that is the concatenation of your name and an animal you like (use the variables!)
#   5) Create a variable that is an acronym (like 'lol') multiplied by your birth day.
#
#   6) Create a variable that is difference of itself minus the number you think is unlucky.
#   7) Overwrite the lucky variable with the itself squared.
#
# Print
#   7) Print all the new variables you've created along with what the represent
#
# Example Code
example_sum = 11 + 21
print('EXAMPLE: the sum of 11 and 21 is', example_sum)

# WRITE CODE BELOW

sum_two_numbers = 53 + 21
print('The sum of 53 and 21 is', sum_two_numbers)
product_three_numbers = 45 * 32 * 21
print('The product of 45, 32 and 21 is', product_three_numbers)
division_sum_and_product = sum_two_numbers/product_three_numbers
print('The division of the sum and product above is', division_sum_and_product)
concatenation_animal_and_name = name + favorite_animal
print('My full name is', concatenation_animal_and_name)
duplicates = "LOL" * birthday_day
print(duplicates)
difference_with_unlucky_number = 23 - favorite_number
print('Here\'s the difference between the number and the unlucky number', difference_with_unlucky_number)
lucky = 12
lucky_squared = lucky ** lucky
print('Here\'s the lucky number', lucky)
print('Here\'s the lucky squared by itself', lucky_squared)

