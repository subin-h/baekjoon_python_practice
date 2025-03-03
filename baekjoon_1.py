import sys
lines = map(int,sys.stdin.readlines())

for n in lines:
    K = 1
    while True:
        if K%n == 0:
            break
        else:
            K = K*10 + 1

    print(len(str(K)))