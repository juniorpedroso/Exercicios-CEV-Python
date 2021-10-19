from math import radians, sin, cos, tan
ang = int(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('O ângulo de {} tem o seno de {:.2f}'.format(ang, seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(ang, cosseno))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ang, tangente))
