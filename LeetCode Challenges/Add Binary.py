a = "1010"
b = "1010"

a, b = a[::-1], b[::-1]

loop_count = max(len(a), len(b))

carry = 0

bi_string = ""

for i in range(loop_count):
    digitA = a[i] if i < len(a) else 0
    digitB = b[i] if i < len(b) else 0

    if ((int(digitA) + int(digitB)) + carry) == 0:
        bi_string += "0"
        carry = 0

    elif ((int(digitA) + int(digitB)) + carry) == 1:
        bi_string += "1"
        carry = 0

    elif ((int(digitA) + int(digitB)) + carry) == 2:
        bi_string += "0"
        carry = 1

    elif ((int(digitA) + int(digitB)) + carry) == 3:
        bi_string += "1"
        carry = 1

if carry == 1:
    bi_string += "1"

print(bi_string[::-1])

