print("Hello, World!")

print(type(e for e in "Hello World" if e.islower())) # Generator object

words = ["Hello", "world", "from", "Python"]
sentence = " ".join(words)
print(sentence)