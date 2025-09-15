# Question: Write a function to flatten a nested list.
list1 = [1,2,3]
list2 = [4,5,6]
# print(type(list1))

# result = list1 + list2 #[1, 2, 3, 4, 5, 6]
# list1.extend(list2)# modifies existing list
# print(list1)

# ===================================================
def flatten(sample):
    result = []
    for item in sample:
        if isinstance(item,list):
            print("List type")
            result.extend(flatten(item))
        else:
            print("Normal number")
            result.append(item)

    return result

sample = [1,2,[3,4,[5,[6]]],7,8]
print("The sample list is : ", sample)
res = flatten(sample)
print("The output of the list is :", res)