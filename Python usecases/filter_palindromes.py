# 3. Question: You are given a list of strings. Write a function to filter out all strings that are palindromes.
# nurses run, Madam, I'm Adam ->  considered palindromes if cases, spaces and punctuation is ignored

def is_palindrome(word):
    # Retain only alpha numeric characters
    word = "".join([char for char in word if char.isalnum()])
    return word.lower() == word[::-1].lower()

def filter_palindromes(list):
    filtered_res = [word for word in list if is_palindrome(word)]
    return filtered_res

list = ["radar", "python", "level", "world"]
print(filter_palindromes(list))