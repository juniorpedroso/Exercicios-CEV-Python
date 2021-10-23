from time import sleep

def maior(* valores):
    print('-=' * 40)
    print('Analisando os valores passados...')
    sleep(1.5)
    maxvalor = 0
    if len(valores) == 0:
        print('Nenhum valor foi informado!')
    else:
        for num in valores:
            print(f'{num} ', end='', flush=True)
            sleep(0.5)
            if num > maxvalor:
                maxvalor = num
        print(f'Foram informados {len(valores)} valores ao todo.')
        print(f'O maior valor informado foi {maxvalor}.')


# Programa principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)
maior()