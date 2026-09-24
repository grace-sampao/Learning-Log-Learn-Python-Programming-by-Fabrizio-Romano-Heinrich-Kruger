def minimum(*n):
    # print(type(n))        # n is a tuple
    if n:
        mn = n[0]
        for value in n[1:]:
            if value < mn:
                mn = value
        print(mn)

n = (1, 3, -7, 9)
minimum(n)          # prints: -7

n = ()
minimum()           # prints: nothing
