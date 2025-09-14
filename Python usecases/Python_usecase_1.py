# Given a list of numbers, write a Python function to find the second highest number.
# https://github.com/krishnaik06/The-Grand-Complete-Data-Science-Materials/blob/main/Python/Python%20Interview%20Usecases.md
def second_highest(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    return numbers[-2]

numbers = [1, 3, 2, 4, 4, 5, 6, 6]
print(second_highest(numbers))
