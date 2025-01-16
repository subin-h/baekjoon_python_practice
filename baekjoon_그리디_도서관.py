N,M = map(int,input().split())
books = sorted(list(map(int,input().split())))

number1 = [i for i in books if i > 0]
number2 = [abs(i) for i in books if i < 0]


