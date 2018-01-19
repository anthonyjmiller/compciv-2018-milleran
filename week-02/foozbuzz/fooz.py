def fob(x):
    for i in range(1, x + 1):
        if i % 3 == 0 and i % 5 == 0:
            print(i, 'Foozbuzz')
            continue
        elif i%3 == 0:
            print(i, 'Fooz')
            continue
        elif i % 5 == 0:
            print(i, 'Buzz')
            continue
        print (i)
fob(24)
