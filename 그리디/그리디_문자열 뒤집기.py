S = list(map(int,input().strip()))
count_0 = 0
count_1 = 0

for i in range(0, len(S)-1):
    if S[i] == 0 and S[i+1] == 1 :
        count_0 += 1
    if S[i] == 1 and S[i+1] == 0:
        count_1 += 1

if S[-1] == 1:
    count_1 += 1
else:
    count_0 += 1

print(min(count_1, count_0))