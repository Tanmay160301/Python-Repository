# Question: Write a function that finds the most repeated character in a string.

# dict1 = {
#     "a":1,
#     "b":2,
#     "c":1,
# }

# max_count = 0
# max_char = None
# 
# for i in dict1.items():
#     print(i) # here it will be a tuple of key value pair for that particular iteration (key , value)
#     if i[1] > max_count:
#         max_char = i[0]
#         max_count = i[1]

# print(max_char, max_count)

def most_repeated_chars(string):
    temp = {}
    for char in string:
        if char in temp.keys():
            temp[char] = temp[char]+1
        else:
            temp[char] = 1

    max_count = 0
    for item in temp.items():
        if item[1]>max_count:
            max_count = item[1]
            max_char = item[0]
    
    return (max_char,max_count)
    
        

string = "aabbbccdccddddddeeaaaaaaaaaaaaa"

max_char,max_count = most_repeated_chars(string)
print(f"The maximum character in string {string} is '{max_char}' which occured {max_count}")