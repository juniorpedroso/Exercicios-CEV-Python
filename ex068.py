from random import randint
venceu = 0 # iniciando a variável de quantas vezes o usuário venceu
print('-=' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
while True:
    print('-=' * 20)
    usuario_valor = int(input('Digite um valor: ')) # Recebe o valor do usuário
    computador = randint(0, 10)  # O computador escolhe um número aleatório
    soma = usuario_valor + computador  # Calcula a soma entre o valor do usuário e do computador
    usuario_pi = ' '
    while usuario_pi not in 'PI':
        usuario_pi = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0] # Recebe a opção Par ou Ímpar
    print(f'Você jogou {usuario_valor} e o computador {computador}. Total de {soma} ', end='')
    print('DEU PAR' if soma % 2 ==0 else 'DEU [IMPAR')
    if usuario_pi == 'P':
        if soma % 2 == 0:
            print('Você VENCEU!\nVamos jogar novamente...')
            venceu += 1
        else:
            break
    if usuario_pi == 'I':
        if soma % 2 == 1:
            print('Você VENCEU!\nVamos jogar novamente...')
            venceu += 1
        else:
            break
print(f'GAME OVER! Você venceu {venceu} vezes.')
