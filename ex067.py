while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 35)
    if n < 0:
        break
    for cont in range(1, 11):
        print(f'{n:3} X {cont:2} = {n * cont:3}')
    print('-' * 35)
print('Programa TABUADA encerrado. Volte sempre.')
