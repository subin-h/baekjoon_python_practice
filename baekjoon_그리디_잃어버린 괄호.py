number=input().split('-')
result = 0

result += sum(map(int,number[0].split('+')))

for part in number[1:]:
    result -= sum(map(int,part.split('+')))
    
print(result)