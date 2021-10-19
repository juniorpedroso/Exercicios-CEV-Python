frase = str(input('Digite uma frase: ').strip().upper())
print('A letra a aparece {} vezes'.format(frase.count('A')))
print('Sua primeira aparição é na posição {}'.format(frase.find('A') + 1))
print('Ela aparece pela última vez na posição {}'.format(frase.rfind('A') + 1))
