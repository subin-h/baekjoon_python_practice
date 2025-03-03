import sys
input = sys.stdin.readline
limit = 1000000

num = [True] * (limit + 1)
for i in range(2, int(limit ** 0.5) + 1):
    if num[i]:
        for j in range(i*i, limit + 1, i):
            num[j] = False
num[0] = num[1] = num[2] = False

prime = [num for num, is_prime in enumerate(num) if is_prime]
prime_set = set(prime)

while(True):

    number = int(input())
    if number == 0:
        break

    for i in prime:
        K = number - i
        if i> number //2:
            print("Goldbach's conjecture is wrong.")
            break
        if K in prime_set:
            print(number,'=',i,'+',number-i)
            break
