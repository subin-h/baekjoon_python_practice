N,M = map(int,input().split())
ball = list(map(int,input().split()))
du_sum = 0

for i in range(1, M+1):
    R = ball.count(i)
    du_number = (R-1)*R/2
    du_sum += du_number

result = int((N-1)*N/2 - du_sum)
print(result)
