# Question: Write a function that returns the number of words in a string.

# def num_of_words(string):
#     count_spaces = 0
#     for char in string:
#         if char == ' ':
#             count_spaces = count_spaces + 1
#     return count_spaces + 1

def num_of_words(string):
    print(len(string.split()))

string = "I am Heisenberg and I am great  man"
print(f"This statement has '{string}' has {num_of_words(string)}")