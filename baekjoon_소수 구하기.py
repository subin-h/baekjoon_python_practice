M,N = map(int,input().split())

is_prime = [True] * (N+1)
is_prime[0] = is_prime[1] = False

# N ** 0.5 = N의 제곱근
for K in range(2, int(N ** 0.5) +1 ):
    if is_prime[K]:
        for j in range(K*K, N+1, K):
            # ex) 2일 경우 (4, 31, 2), 3일 경우(9, 31, 3)
            # K*K인 이유: 3*2는 이미 2의 배수로 처리했기 때문
            is_prime[j] = False

for K in range(M,N+1):
    if is_prime[K]:
        print(K)
