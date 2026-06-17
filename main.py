from cadastro import menu_cadastro
from agenda import menu_agenda
from arquivo import carregar


def menu_principal():

    print('=-' *11)
    print('SISTEMA DE AGENDAMENTO')
    print('=-' *11)

    while True:
        print('-=' * 11)
        print('''[1] área de cadastro
[2] área da agenda
[3] editar
[4] sair ''')

        #usuario
        usuario = int(input('Digite sua opcao: '))

        #finalizar
        if usuario == 4:
            print('-=' * 11)
            print('programa finalizado')
            print('=-' *11)
            break

        #menu
        elif usuario == 1:
            menu_cadastro()
        elif usuario == 2:
            menu_agenda()
        elif usuario == 3:
            menu_editar()

carregar()
menu_principal()