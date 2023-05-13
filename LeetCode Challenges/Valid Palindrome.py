s = "A man, a plan, a canal: Panama"
new_str = ""

for c in s:
    if c.isalnum():
        new_str += c.lower()
print(new_str == new_str[::-1])