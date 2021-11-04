# Exercício 114 do Curso em Video - Testando se um site está disponível

import urllib.request

try:
    site = urllib.request.urlopen("http://pudim.com.br/")
except urllib.error.URLError:
    print('\033[1;31mO site pudim não está acessível no momento.\033[m')
else:
    print('\033[1;32mConsegui acessar o site pudim com sucesso.\033[m')
