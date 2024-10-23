def angled_triangle(i = 5):
    for j in range(1,i+1):
        for k in range(j):
            print('*', sep='', end='')
        print('\n')


angled_triangle()