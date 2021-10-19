sexo = str(input('Digite o seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor informe seu sexo: ')).upper().strip()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
