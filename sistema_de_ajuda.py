from time import sleep

cores = ('\033[m',        # 0 - Sem cor
         '\033[0;30;41m',  # 1 - Vermelho
         '\033[0;30;42m',   # 2 - Verde
         '\033[0;30;46m',   # 3 - Azul-claro
         '\033[0;30;47m'   # 4 - Cinza
)

def ajuda(string, cor=0):
    print(cores[cor])
    print(help(string))
    print(cores[0])


def titulo(string, cor=0):
    print(cores[cor], '~' * (len(string) + 4))
    print(f'  {string}')
    print('~' * (len(string) + 4))
    print(cores[0])


def subtitulo(comando, cor=0):
    print(cores[cor], '~' * (34 + len(comando)))
    print(f'  Acessando o manual do comando {comando}')
    print('~' * (34 + len(comando)))
    print(cores[0])


# Programa principal
while True:
    titulo('SISTEMA DE AJUDA PyHelp', cor=2)
    sleep(.7)
    opt = input('Função ou Biblioteca => ')
    if opt != 'fim':
        sleep(.4)
        subtitulo(opt, cor=3)
        sleep(.7)
        ajuda(opt, cor=1)
        sleep(.3)
    else:
        print('\033[1m Volte sempre!')
        break
