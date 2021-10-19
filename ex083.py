lista = []
aberto = 0 # Variável utilizada para verificar parênteses abertos
expressao = str(input('Digite a expressão: '))
for i in range(0, len(expressao)):
    lista.append(expressao[i])
for cont, v in enumerate(lista):
    if v == '(':
        aberto += 1
    elif v == ')':
        aberto -= 1
        if aberto == -1:
            break
if aberto != 0: # Se aberto for positivo é porque ficaram abertos e se for negativo é porque foi fechado sem abrir
    print('Sua expressão está errada!')
else:
    print('Sua expressão está válida!')
