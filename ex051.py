termo1 = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
# Fórmula do Termo Geral ->
# an = a1 + (n - 1) * r
# an -> Termo que queremos calcular
# a1 -> Primeiro termo da PA
# n  -> Posição do termos que queremos descobrir
# r  -> Razão
termo10 = termo1 + (10 - 1) * razao
print('Estes são os primeiros 10 termos da sua razão:')
for c in range(termo1, (termo10 + 1), razao):
    print(c, end=' ')
print('Acabou')
