def fob(x):
    for i in range(1, x + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, 'foozbuzz')
            continue
        elif i%3 == 0:
            print(i, 'fooz')
            continue
        elif i % 5 == 0:
            print(i, 'buzz')
            continue
        print (i)
fob(22)
