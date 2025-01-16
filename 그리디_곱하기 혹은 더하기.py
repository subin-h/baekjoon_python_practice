#from functools import reduce
num=list(map(int,input().strip()))
result = num[0]

for i in num[1:]:
    if i <= 1 or result <= 1:
        result += i
    else:
        result *= i

#def multiply(x,y):
#    return x*y

#result = reduce(multiply, num)
print(result)