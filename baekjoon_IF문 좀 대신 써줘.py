import sys
N,M=map(int,input().split())
name=[]
standard=[]
for _ in range(N):
    data= sys.stdin.readline().split()
    name.append(data[0])
    standard.append(int(data[1]))
for _ in range(M):
    stat = int(sys.stdin.readline())
    start, end = 0, N-1
    while start <= end:
        mid = (start+end) // 2
        if standard[mid] >= stat:
            end = mid -1
        else:
            start = mid + 1
    print(name[start])

