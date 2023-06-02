# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random

def affirmation_generator():
    affirmation_number = random.randint(0,4)
    if affirmation_number == 0:
        print('You can do this')
    elif affirmation_number == 1:
        print('You have come so far')
    elif affirmation_number == 2:
        print('My past mistakes do not define who I am now')
    elif affirmation_number == 3:
        print('You can do anything you set your mind to')
    elif affirmation_number == 4:
        print('I am doing an amazing job')
    else:
        print('Maybe you cannot do it 😬')
def quadratic_equation_intercept_finder(a, b, c):
    #To square https://www.freecodecamp.org/news/how-to-square-a-number-in-python-squaring-function/
    b_square = pow(b, 2)
    discriminant_number = b_square - (4*a*c)
    if discriminant_number < 0:
        print('There are no intercepts!')
        exit()
    else:
        first_x_intercept = (-b + b_square - (4 * a * c))/2*a
        second_x_intercept = (-b - b_square - (4 * a * c))/2*a
        print("your first intercept is: ", first_x_intercept, "your second intercept is: ", second_x_intercept )


affirmation_generator()
quadratic_equation_intercept_finder(2, 4, 2)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
