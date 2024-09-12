S = input()
b=[0 for i in range(26)]
for num in S:
    b[ord(num)-ord('a')] +=1
print(" ".join(map(str, b))) 

#map 함수 - 자료형 형변환
