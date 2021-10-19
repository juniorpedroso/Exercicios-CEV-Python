primeiro = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
print('Estes são os primeiros 10 termos da sua PA:')
while cont <= 10:
    print(termo, end=' -> ')
    termo += razao
    cont += 1
print('FIM')
