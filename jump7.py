for i in range(1,101):
    a = i%7
    b = int(str(i)[0])
    c = int(str(i)[-1])
    if a == 0:
        continue
    elif b == 7:
        continue
    elif c == 7:
        continue
    else:
        print(i)

