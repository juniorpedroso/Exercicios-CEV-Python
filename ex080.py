valores = list()
for i in range(0, 5):
    novovalor = int(input('Digite um valor: '))
    if len(valores) == 0:                   # Se a lista estiver vazia, inclui o novo elemento na posição 0
        valores.append(novovalor)
        print('Adicionado ao final da lista...')
    else:
        for cont in range(0, len(valores)): # Um laço for para pesquisar se existe um valor maior
             if novovalor <= valores[cont]: # Se o novo valor for igual ou menor que o atual, inclui nesta posição
                valores.insert(cont, novovalor)
                print(f'Adicionado na posição {cont} da lista...')
                break
             elif (cont + 1) == len(valores):   # Se a lista estiver na última posição, acrescenta um novo elemento
                valores.append(novovalor)
                print(f'Adicionado na posição {cont + 1} da lista...')
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')
