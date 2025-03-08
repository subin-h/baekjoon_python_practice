import sys
T = int(input())
input = sys.stdin.readline

for i in range(T):
    M,N,x,y = map(int,input().split())
    found = False
    year = x
    while year <= M*N :

        if (year-1)%N+1 == y :
            print(year)
            found = True
            break
        
        year += M

    if not found:
        print(-1)
