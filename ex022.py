nome = str(input('Digite seu nome: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculo é', nome.upper())
print('Seu nome em minúsculo é', nome.lower())
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
nome = nome.split()
#print(nome)
print('O primeiro nome, que é {}, tem {} letras'.format(nome[0], len(nome[0])))
