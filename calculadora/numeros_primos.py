

num = int(input('dgite um número:'))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
print('O número {} foi divisivel {} vezes.'.format(num, tot))
if tot == 2:
    print('E por isso é primo!')
else:
    print('E por isso não é primo!')
