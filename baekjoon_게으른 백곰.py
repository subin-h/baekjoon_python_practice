import sys
N,K = map(int,input().split())
x_gram = [0] * 1000001
max_x = 0
for i in range(N):
    data = sys.stdin.readline().split()
    x = int(data[1])
    max_x = max(max_x,x)
    x_gram[x] = int(data[0])

pe = 2*K+1
present_gram = sum(x_gram[:pe])
max_gram = present_gram
for i in range(pe, max_x+1):
    present_gram = present_gram- x_gram[i-pe] + x_gram[i]
    max_gram = max(max_gram,present_gram)

print(max_gram)