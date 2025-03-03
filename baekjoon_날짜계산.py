E,S,M = map(int,input().split())
year = 1
a,b,c = 1,1,1
while(True):
    
    if a == E and b == S and c == M:
        break

    a = (a+1) % 15
    b = (b+1) % 28
    c = (c+1) % 19

    if a == 0:
        a = 15
    if b == 0:
        b = 28
    if c == 0:
        c = 19
        
    year += 1

print(year)