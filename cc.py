rows = int(input("input:"))
i = 0
while i <= rows - 1:
    j = 0
    while j < i+1:
        # display space
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print()
    i += 2

i = rows - 1
while i >= 0:
    j = 0
    while j < i+1:
        print('', end=' ')
        j += 1
    k = i
    while k <= rows - 1:
        print('*', end=' ')
        k += 1
    print('')
    i -= 2