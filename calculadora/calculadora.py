while True:
    operacao = input ('qual operação (+,-,*,/,) você que fazer, \'p\' primos ou \'q\' para sair \n')
    if operacao == 'q' or operacao =='Q':
        break
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
