peso = int(input('Qual o seu peso? (Kg) '))
altura = float(input(('Qual a sua altura? (m) ')))
imc = peso / (altura ** 2)
print('O seu IMC é {:.1f}, '.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está com o peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está obeso.')
else:
    print('Você está com obesidade mórbida.')

