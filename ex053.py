frase = str(input('Digite uma frase: ')).strip().upper()
qtdbranco = frase.count(' ')
fraselimpa = ''
branco = 0
fraseinvertida = ''

# Este laço tira os espaços em branco da frase
for c in range(0, qtdbranco):
    branco = frase.find(' ')
    fraselimpa = frase[0: branco]
    frase = fraselimpa + frase[branco + 1:]
print(frase)

# Este laço inverte a frase
for c in range((len(frase)-1), -1, -1):
    fraseinvertida = fraseinvertida + frase[c]
print(fraseinvertida)

# Agora é só conferir se as duas frases são iguais
if frase == fraseinvertida:
    print('Esta frase é um palíndromo.')
else:
    print('Esta frase não é um palíndromo')