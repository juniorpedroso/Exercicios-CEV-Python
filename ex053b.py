frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split() # Separo a frase em palavras
junto = ''.join(palavras) # Junto as palavras sem espaços
#inverso = ''
#for letra in range(len(junto) - 1, -1, -1): # Aqui eu inverto a frase
#    inverso += junto[letra]

# Esta é outra maneira mais simples
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto: # Aqui eu testo se é um palíndromo
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
