alunos = [[], []]
notas = []
while True:
    alunos[0].append(str(input('Nome: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    alunos[1].append(notas[:])
    notas.clear()
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N] ')).strip().upper()
    if continua == 'N':
        break
print('-=' * 30)
print('Nº   Nome          Média')
print('------------------------')
for cont in range(0, len(alunos[0])):
    media = (alunos[1][cont][0] + alunos[1][cont][1]) / 2
    print(f'{cont:<5}{alunos[0][cont]:<15}{media:>4}')
print('-=' * 30)   
while True:
    escolhido = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if escolhido == 999:
        break
    if escolhido <= len(alunos[0]) - 1:
        print(f'As notas de {alunos[0][escolhido]} são {alunos[1][escolhido]}')
        print('-=' * 30) 
    else:
        print('Aluno não cadastrado, tente outro.')
