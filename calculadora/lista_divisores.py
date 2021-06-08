d = int(input('dgite um número:'))
for c in range(1, d + 1):
    if d % c == 0:
        print('{} '.format(c),end='')
