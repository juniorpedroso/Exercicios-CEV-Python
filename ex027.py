nome = str(input('Digite o nome: ')).strip()
primeiro = int(nome.find(' ')) + 1
ultimo = int(nome.rfind(' ')) + 1
print('O seu primeiro nome é {}'.format(nome[0:primeiro]))
print('O seu último nome é {}'.format(nome[ultimo:]))
