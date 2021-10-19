nome = str(input('Digite seu nome: ')).upper()
divisao = nome.split()
print('Seu nome tem Silva?', end = ' ')
print('SILVA' in divisao)
