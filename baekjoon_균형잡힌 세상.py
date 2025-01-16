while True:
    queue = []
    input_ = input()
    if input_ == '.':
        break
    for i in input_:
        if i == '(' or i == '[':
            queue.append(i)
        elif i == ')':
            try:
                pop_par = queue.pop()
                if pop_par != '(':
                    print('no')
                    break
            except IndexError:
                print('no')
                break
        elif i == ']':
            try:
                pop_ba = queue.pop()
                if pop_ba != '[' :
                    print('no')
                    break
            except IndexError:
                print('no')
                break
    else:
        if len(queue) == 0:
            print("yes")
        else:
            print("no")