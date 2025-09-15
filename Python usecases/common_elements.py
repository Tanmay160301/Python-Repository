# Question: Given two lists, write a function that returns the elements that are common to both lists.

# result = {1,2,3} & {2,1,4,5}
# print(result) #{1, 2}

def common_elements(list1,list2):
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

print(common_elements(list1,list2))
