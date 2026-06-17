from dados import dados
from arquivo import salvar
from validacoes_cadastro import telefone_duplicado

def menu_cadastro():

    while True:
        print('-=' * 11)
        print('''[1] fazer cadastro
[2] excluir cadastro
[3] editar cadastro
[4] voltar''')
        print('-=' * 11)

        #usuario
        usuario = int(input('digite sua opcao: '))

        #voltar
        if usuario == 4:
            return

        #menu
        elif usuario == 1:
            cadastrar()
        elif usuario == 2:
            excluir()
        elif usuario == 3:
            editar()

def cadastrar():

    cadastros = dados['cadastros']

    print('-=' * 11)
    nome = input('digite seu nome: ')
    telefone = input('digite seu telefone: ')
    print('-=' * 11)

    #validacao de telefone
    if not telefone_duplicado(telefone):
        print('cadastro inválido. telefone já possui cadastro')
        return

    #id
    maior_id = 0

    for cliente in cadastros:
        if cliente['id'] > maior_id:
            maior_id = cliente['id']

    novo_id = maior_id + 1

    cadastrado = {'id' : novo_id, 'nome': nome, 'telefone': telefone}
    cadastros.append(cadastrado)
    salvar()
    print('-=' * 11)
    print('seu cadastro foi realizado com sucesso.')
    print('-=' * 11)

def excluir():

    cadastros = dados['cadastros']

    print('-=' * 11)
    nome = input('digite seu nome: ')
    telefone = input('digite seu telefone: ')
    print('-=' * 11)

    for cad in cadastros:

        #localizado
        if nome == cad['nome'] and telefone == cad['telefone']:
            cadastros.remove(cad)
            print('-=' * 11)
            print('o cadastro foi excluido com sucesso.')
            print('-=' * 11)
            salvar()
            return

        #nao localizado
        else:
            print('-=' * 11)
            print('cliente não encontrado')
            print('-=' * 11)







