import sys

N,M = map(int,input().split())
num_to_name = {}
name_to_num = {}

input = sys.stdin.readline

for i in range(1, N+1):
    pokemon_name = input().strip()
    num_to_name[i] = pokemon_name
    name_to_num[pokemon_name] = i

for _ in range(M):
    question = input().strip()

    if question.isdigit():
        print(num_to_name[int(question)])
    else:
        print(name_to_num[question])

