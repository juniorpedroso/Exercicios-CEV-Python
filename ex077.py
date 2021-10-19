palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for pos in range(len(palavras)):
    print(f'Na palavra {palavras[pos].upper()} temos ', end='')
    palavra = str(palavras[pos].upper())
    for cont in range(0,len(palavra)):
        if palavra[cont] in 'AEIOU':
            print(palavra[cont], end=' ')
        if cont == (len(palavra) - 1):
            print()
