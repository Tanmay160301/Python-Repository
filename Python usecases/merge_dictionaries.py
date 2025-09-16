# Question: Write a Python function to merge two dictionaries. If both dictionaries have the same key, prefer the second dictionary's value.

# dict1 = {
#     "a":1,
#     "b":2,
#     "c":3,
# }
# dict2 = {
#     "d":4,
#     "b":444,
#     "e":5,
#     "f":6,
# }

# dict2.update({"g":7}) 
# print("dict2",dict2) #{'d': 4, 'b': 444, 'e': 5, 'f': 6, 'g': 7}
# dict1.update(dict2) # dict1 will be modified in place
# print("dict1",dict1) #{'a': 1, 'b': 444, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}

# dummy = {}
# dummy = dict1.copy() 
# print("dummy dictionary",dummy) #{'a': 1, 'b': 444, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7}
# dict1["age"] = 24
# print("dict1",dict1) #{'a': 1, 'b': 444, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'age': 24}

# Actual Code
# def merge_dict(dict1,dict2):
#     result = {}
#     result = dict1.copy()
#     return

# Deep Copy and Shallow Copy
'''
    If we do dict2 = dict1.copy() -> then it will copy the top level structure of
    the dictionary as it(deep copy) is but if the dictionary contains mutable nested objects like dictionaries/lists/sets then it will store the references of that
    (kind of shallow copy) 
'''


dict1 = {
    "a":1,
    "b":2,
    "c":3,
}
dict2 = {
    "d":4,
    "b":444,
    "e":5,
    "f":6,
}

def merge_dict(dict1,dict2):
    result = {}
    result = dict1.copy()
    result.update(dict2)
    return result


result = merge_dict(dict1,dict2)
print(result)
