def is_functional(s):
    global result

    if len(s) ==1:
        result = "AKARAKA"
        return
    else:
        if s != s[::-1]:
            return
        else:
            N=len(s)//2
            is_functional(s[:N])
            is_functional(s[-N:])
S=input()

result="IPSELSENTI"
is_functional(S)
print(result)