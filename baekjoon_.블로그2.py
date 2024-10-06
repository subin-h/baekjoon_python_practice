N=int(input())
str=input()
cnt_B, cnt_R, cnt=1,1,1
for i in str.split("B"):
        if i != '':
            cnt_B+=1
for j in str.split("R"):
        if j != '':
            cnt_R+=1
for k in range(len(str)-1):
      if str[k] != str[k+1]:
            cnt+=1
print(min(cnt_B, cnt_R, cnt))