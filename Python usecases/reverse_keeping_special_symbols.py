def reverse_keeping_special_symbols(text):
    temp = text
    for char in temp:
        if not char.isalnum():
            temp = temp.replace(char,'')
    reversed_text = temp[::-1]
    reversed_text_list = list(reversed_text)
    for i in range(0,len(text)):
        if not text[i].isalnum():
            reversed_text_list.insert(i,text[i])
    
    reversed_text = "".join(reversed_text_list)
    return reversed_text

text = "Ta!nm$ay" #ya!mn$aT
reversed_string = reverse_keeping_special_symbols(text)
print(reversed_string)