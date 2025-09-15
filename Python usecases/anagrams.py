# 4. Question: Given a string, write a function to check if it is an anagram of another string
# 2 new methods here - sort and sorted

# numbers = [3, 1, 2]
# numbers.sort()   # modifies numbers in place
# print(numbers)   # [1, 2, 3]

# numbers = [3, 1, 2]
# new_list = sorted(numbers)
# print(new_list)  # [1, 2, 3]
# print(numbers)   # [3, 1, 2]  (original list unchanged)

def check_anagram(s1,s2):
    return sorted(s1) == sorted(s2)

s1 = "naman"
s2 = "manna"

print(check_anagram(s1,s2))

