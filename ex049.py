n = int(input('Digite um número: '))
print('-=-' * 7)
print(' \033[1;33mTabuada do número {}\033[m'.format(n))
print('-=-' * 7)
for c in range(1, 11):
    print('|    \033[1;33m{}\033[m X {:2} = {:2}    |'.format(n, c, n * c))
print('-=-' * 7)