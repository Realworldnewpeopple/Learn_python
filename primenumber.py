for i in range(1, 100):
    j = 2
    counter = 0
    while j < i:
        if i % j == 0:
            counter = 1
            j += 1
        else:
            j += 1
    if counter == 0:
        print(i, end=', ')
    else:
        counter = 0
