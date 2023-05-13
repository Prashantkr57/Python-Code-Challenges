s = "abcabcbb"

l, r = 0, 0
hashSet = set()
max_count = 0

while r < len(s):
    for n in s:
        if n not in hashSet:
            hashSet.add(n)
            max_count = max(max_count, r - l + 1)
            r += 1
        else:
            hashSet.remove(n)
            l += 1

print(max_count)
