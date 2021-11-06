def operacao (opcao ,num1 : int , num2 : int):
    '''
    Realiza operação de acordo com a opcão digitada
    '''
    global operador
    if opcao == '1':
        operador = '+'
        return num1 + num2
    if opcao == '2':
        operador = '+'
        return num1 - num2 , "-"    
    if opcao == '3':
        operador = '*'
        return num1 * num2 
    if opcao == '4':
        operador = '/'
        return num1 / num2 

operador = '+'
    
while True:    
    print("\nSelecione o número da operação desejada:\n")

    print("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n")

    opcao = input('\nDigite sua opção (1/2/3/4): ')

    aceitaveis = ['1','2','3','4']

    if opcao not in aceitaveis:
        print('opção inválida')
        continue
        
    

    try:
        num1 = int(input('\nDigite o primeiro número: '))
    except:
        print('Formato de número inválido')
        continue
    try:
        num2 = int(input('\nDigite o segundo número: '))
    except:
        print('Formato de número inválido')
        continue
    resultado = operacao(opcao, num1, num2)

    print(f'\n{num1} {operador} {num2} = {resultado}')