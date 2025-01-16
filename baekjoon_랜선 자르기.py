K, N = map(int, input().split())
length = [int(input()) for _ in range(K)]
length.sort()
mid=0
start = 1
end = length[-1]
while(start <= end):
    sum_N = 0
    mid = (start+end)//2
    for i in length:
        sum_N += i//mid
    if sum_N > N-1:
        start = mid+1
    else:
        end = mid-1

print(end)
