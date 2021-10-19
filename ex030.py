# Este exercício faz parte da aula 10 do Curso em Vídeo
numero = int(input('Digite um número qualquer:'))
if numero % 2 == 0:
    print(f'O número {numero} é \033[1;34mPAR!\033[m')
else:
    print(f'O número {numero} é \033[1;34mÍMPAR!\033[m')
