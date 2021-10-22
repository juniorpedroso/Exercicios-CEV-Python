from time import sleep

def contagem(inicio, fim, passo):
    if passo == 0:      # Se o passo for 0, muda para 1
        passo = 1
    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(1.5)
    if inicio > fim:    # Se o início for maior que o final, o passo será negativo
        if passo > 0:
            passo *= -1
        fim -= 1
    else:
        fim += 1
    for i in range(inicio, fim, passo):
        print(i, end = ' ', flush=True)  # Foi necessário incluir na função print o flush=True, para
        sleep(0.5)                          # Evitar problemas com a chamada de sleep()
    print('FIM!')


# Programa principal
contagem(1, 10, 1)
contagem(10, 0, 2)
print('-=' * 20)
print('Agora é a sua vez de personalizar a contagem!')
ini = int(input('Início: '))
final = int(input('Fim: '))
passos = int(input('Passo: '))
contagem(ini, final, passos)
