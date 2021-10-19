from time import sleep
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
menu = '''  [ 1 ] somar
  [ 2 ] multiplicar
  [ 3 ] maior
  [ 4 ] novos números
  [ 5 ] sair do programa'''
opcao = 0
while opcao != 5:
    print(menu)
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, (n1 + n2)))
    elif opcao == 2:
        print('A multiplicação entre os dois números é {}'.format(n1 * n2))
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior número é {}'.format(n1, n2, n1))
        elif n2 > n1:
            print('Entre {} e {} o maior número é {}'.format(n1, n2, n2))
        else:
            print('Os dois números são iguais')
    elif opcao == 4:
        print('Informe os números novamente:')
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))
    elif opcao == 5:
        print('Finalizando.... ')
    else:
        print('Opção inválida!!!')
    sleep(2)
    print('-=' * 15)
print('Acabou. Volte sempre')
