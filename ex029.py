# Exercício passado na aula 10 do Curso em Vídeo
velocidade = int(input('Digite a velocidade do carro: '))
print()
if velocidade <= 80:
    print('\033[1;97;42m VELOCIDADE PERMITIDA \033[m')
else:
    print('\033[1;97;41m LIMITE ULTRAPASSADO!! \033[m')
    multa = (velocidade - 80) * 7
    print(f'Você foi multado em R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')
