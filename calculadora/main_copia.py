
while True:
    operacao = input ('qual operação (+,-,*,/,) você que fazer, \'p\' primos, \'f\' para fatorial ou \'q\' para sair \n')
    if operacao == 'q' or operacao =='Q':
        break
    if operacao == 'p' or operacao == 'P':
        num = int(input('dgite um número:'))
        tot = 0
        for c in range(1, num + 1):
            if num % c == 0:
                tot += 1
        print('O número {} foi divisivel {} vezes.'.format(num, tot))
        if tot == 2:
            print('E por isso é primo!')
    if operacao == 'f' or operacao == 'F':
        n = int (input('digit um numero para calcular seu fatorial:'))
        c = n
        f = 1
        print('calculondo {}! ='.format(n),end='')
        while c > 0:
            print('{}'.format(c), end='')
            print('x' if c > 1 else ' = ', end='')
            f *= c
            c -= 1
        print('{}'.format(f))
        
        else:
            print('E por isso não é primo!')
        
    elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/':
        num1 = int (input('digite o primeiro numero:'))
        num2 = int (input('digite o segundo numero:'))
        
    else:
        print('Operacao invalida')

    if operacao == '+':
        total = num1 + num2
        print (total)
    if operacao == '-':
        total = num1 - num2
        print (total)
    if operacao == '*':
        total = num1 * num2
        print (total)
    if operacao == '/':
        total = num1 / num2
        print (total)
