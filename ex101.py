# Exercício 101 do Curso em Vídeo
# Crie um programa que tenha uma função chamada voto()
# que vai receber como parâmetro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições


def voto(nasc):                 # Importando a classe date dentro da função causa uma grande economia de memória
    from datetime import date   # Pois ela só vai ser usada durante a execução da função
    ano = date.today().year  # Como buscar o ano atual usando a função date.today()
    idade = ano - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA!'
    elif 16 <= idade < 18 or idade > 70:
        return f'Com {idade} anos: VOTO OPCIONAL!'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO!'


# Programa principal
print('-=' * 30)
nascimento = int(input('Em que ano você nasceu? '))
print(voto(nascimento))
