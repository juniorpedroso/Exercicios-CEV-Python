valores = list()
for i in range(0, 5):
    novovalor = int(input('Digite um valor: '))
    if len(valores) == 0 or novovalor > valores[-1]:    # Se a lista estiver vazia ou for o maior valor inclui uma nova posição
        valores.append(novovalor)
        print('Adicionado ao final da lista...')
    else:
        for cont in range(0, len(valores)): # Um laço for para pesquisar se existe um valor maior
             if novovalor <= valores[cont]: # Se o novo valor for menor ou igual que o atual, inclui nesta posição
                valores.insert(cont, novovalor)
                print(f'Adicionado na posição {cont} da lista...')
                break
print('-=' * 30)
print(f'Os valores digitados em ordem foram {valores}')
