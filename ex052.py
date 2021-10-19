# NÚMEROS PRIMOS
# Crivo de Erastóstenes
# Passo 1 – Tendo em vista as regras de divisibilidade, sabemos que o único número par primo é o número dois.
# Então, excluímos todos os demais pares da tabela, ou seja, os múltiplos de 2.
# Passo 2 - De acordo com as regras de divisibilidade por 3, sabemos que um número é divisível por 3
# caso a soma dos algarismos também seja. Assim, vamos excluir todos os números que são múltiplos de 3.
# Passo 3 – Do critério de divisibilidade por 5, sabemos que um número é divisível por 5 caso ele termine em 0 ou em 5.
# Vamos excluir todos os números que terminam em 0 e em 5.
# Passo 4 – De maneira análoga, verificando o critério de divisibilidade, vamos excluir todos os múltiplos de 7.
# Feito todo esse processo, os números que sobrarem são os primos de 2 até o número desejado.
n = int(input('Digite um número: '))
cont = 0
for c in range(1, n +1):
    if n % c ==0:
        cont += 1
        print(c, end= ' ')
print('\nO número {} é divisível {} vezes,' .format(n, cont), end= ' ')
if cont == 2:
    print('então ele É PRIMO.')
else:
    print('então ele NÃO É PRIMO.')
