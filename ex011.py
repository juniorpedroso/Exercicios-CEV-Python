l = float(input('Qual é a largura da parede? '))
a = float(input('Qual é a altura da parede? '))
m2 = l * a
#print(m2)
lit = m2 / 2
#print(lit)
print('Sua parede tem a dimensão de {:.2f}m X {:.2f}m e sua área é de {:.2f}m²'.format (l, a, m2))
print('Para pintar esta parede você precisará de {:.2f} litros de tinta'.format(lit))
