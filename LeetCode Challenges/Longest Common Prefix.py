strs = ["flower", "flow", "flight"]

common_str = ""

strs.sort()
print(strs)

i = 0

while i < len(strs[0]) and i < len(strs[-1]):
    if strs[0][i] == strs[-1][i]:
        common_str += strs[0][i]
        i += 1
    else:
        break

print(common_str)
