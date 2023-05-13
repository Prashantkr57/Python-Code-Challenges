n = 0o000000000000000000001010

res = 0
while n:
    res += n % 2
    n = n >> 1

print(res)
