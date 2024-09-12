#num_list=[input(_) for _ in range(3)]
A=int(input())
B=int(input())
C=int(input())
#mul=1
mul=A*B*C
count=[0 for i in range(10)]
#for i in num_list:
    #mul*=int(i)
for j in str(mul):
    count[ord(j)-ord('0')]+=1
print('\n'.join(map(str,count)))
