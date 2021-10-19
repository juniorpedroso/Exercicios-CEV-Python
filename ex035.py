reta1 = int(input('Informe a medida da reta 1: '))
reta2 = int(input('Informe a medida da reta 2: '))
reta3 = int(input('Informe a medida da reta 3: '))
med_reta_maior = reta1
reta_maior = 1
if med_reta_maior < reta2:
    med_reta_maior = reta2
    reta_maior = 2
if med_reta_maior < reta3:
    med_reta_maior = reta3
    reta_maior = 3            # Busca a reta maior
print('A reta maior é a reta {}, cuja medida é {}'.format(reta_maior, med_reta_maior))
med_reta_menor = reta1
reta_menor = 1
if med_reta_menor > reta2:
    med_reta_menor = reta2
    reta_menor = 2
if med_reta_menor > reta3:
    med_reta_menor = reta3
    reta_menor = 3           # Busca a reta menor
print('A reta menor é a reta {}, cuja medida é {}'.format(reta_menor, med_reta_menor))
med_reta_meio = (reta1 + reta2 + reta3) - med_reta_maior - med_reta_menor # Busca a reta do meio
if (med_reta_menor + med_reta_meio) > med_reta_maior: # Calcula a possibilidade de um triângulo
    print('\nEstas três retas podem formar um triângulo')
    print('Porque a soma das duas retas menores {} e {} resulta em {} que é maior que a reta maior {}'.format(med_reta_menor, med_reta_meio, med_reta_menor + med_reta_meio, med_reta_maior))
else:
    print('\nEstas três retas não podem formar um triângulo')
