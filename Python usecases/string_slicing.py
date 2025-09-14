print("Printing for s")
s = "Tanmay"
print(s[:2:-1]) # yam
print(s[:2]) # Ta


print("Printing for text")
text = "Tanmay_is_my_name"
# Considering text[start:end:step]
# Normal slicing
print(text[2:9])# nmay_is
print(text[2:9:1]) # nmay_is
print(text[2:9:2]) # na_s

# Reverse slicing ...ithe string ulti read keli jaate that is why start will be greater than end if step is -1 
print(text[9:2:-1]) # _si_yam
print(text[:0:-1]) # eman_ym_si_yamna
print(text[:0:-2]) # ea_ms_an
print(text[::-1]) # eman_ym_si_yamnaT