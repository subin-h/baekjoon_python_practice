num_list=[input() for _ in range(3)]
# 변수 미사용 시, _는 unpack 값으로 사용 가능
mul=1
count=[0 for i in range(10)]
for i in num_list:
    mul*=int(i)
for j in str(mul):
    count[ord(j)-ord('0')]+=1
print('\n'.join(map(str,count)))
