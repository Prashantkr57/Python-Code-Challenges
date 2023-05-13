s = "I may yam i"
rev_s = ""

print(s.lower() == s.lower()[::-1])
for c in s:
    if c.isalnum():
        rev_s += c
print(rev_s)
if rev_s.lower() == rev_s.lower()[::-1]:
    print("True")

else:
    print("False")