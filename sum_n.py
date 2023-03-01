# 1 + 2 + 3 + ... 10
n = 100
sum = 0
for i in range(1, n+1):
    sum = sum + i
    #print(i)

print("sum = ", sum)
print("sum2 = ", n / 2 * (n + 1))

# 1 + 10 = 11
# 2 + 9 = 11
# 3 + 8 = 11
# 4 + 7 = 11
# 5 + 6 = 11

# (n * (n + 1)) / 2
# (10 * 11) / 2
# 10 / 2 * 11
