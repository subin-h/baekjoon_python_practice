import sys
n = int(input())
def roundUp(num):
    if(num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)
if n == 0:
    print(0)
else:
    number = [int(sys.stdin.readline()) for _ in range(n)]
    number.sort()
    k = int(roundUp(n*0.15))
    print(int(roundUp((sum(number[k:n-k])/(len(number)-2*k)))))