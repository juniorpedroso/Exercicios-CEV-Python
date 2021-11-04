# SISTEMA do Exercício 115
from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'ex115\cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas',
                    'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[1;31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
