str1=input()
str2=input()
answer=0
for i in range(ord('a'),ord('z')+1):
    k=str1.count(chr(i))-str2.count(chr(i))
    l=str2.count(chr(i))-str1.count(chr(i))
    if chr(i) in str1 == chr(i) in str2 == 0:
        exit
    elif chr(i) in str2 == chr(i) in str1 == 1:
        if k>0:
            answer+=k
        elif l>0:
            answer+=l
        else:
            exit
    else:
        if k>0 and l<0:
            answer+=k
        else:
            answer+=l
print(answer)