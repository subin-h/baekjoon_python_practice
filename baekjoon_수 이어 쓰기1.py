N = int(input())
K = len(str(N))
sum_num = (N - (10 ** (K-1)) + 1) * K

for i in range(K-1, 0, -1):
    sum_num += 9*(10 ** (i-1))*i

print(sum_num)
