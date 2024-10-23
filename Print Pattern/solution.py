def print_pattern(i = 4):
    num = i
    for line in range(i):
        for column in range(num):
            print('*', sep='', end='')
        print('\n')
        
print_pattern()
        