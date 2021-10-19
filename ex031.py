# Exercício extraído da aula 10 do Curso em Vídeo
distancia = int(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {distancia}Km.')
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
# Abaixo uma versão simplificada da função if
# preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'E o preço de sua passagem será de R${preco:.2f}')
