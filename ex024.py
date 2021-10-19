cidade = str(input('Digite o nome de uma cidade: ')).strip()
print('Esta cidade começa com Santo?', end = ' ')
#print('SANTO' in cidade.upper())
print(cidade[0:5].upper() == 'SANTO')
