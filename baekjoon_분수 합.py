# 2025-02-13
# baekjoon 1735번 분수 합

# 두 분수의 합을 기약분수의 형태로 표현하기
# 최대공약수를 구하기 위해 유클리드 호제법 참고

num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))
denominator = num1[1] * num2[1]
numerator = num1[0]*num2[1] + num2[0]*num1[1]

def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

max_a = max(denominator,numerator)
min_b = min(denominator, numerator)
gcd_num12 = gcd(max_a,min_b)

print(numerator//gcd_num12, denominator//gcd_num12)