from dados import dados
from arquivo import salvar
from horarios import gerador_horarios, horarios_disponiveis
from validacoes_agenda import data_passada, horario_duplicado, horario_funcionamento

def menu_agenda():
    print('-=' * 11)
    print('''[1] agenda completa
[2] agendar horário
[3] buscar agendamento
[4] excluir agendamento
[5] editar agendamento
[6] voltar''')
    print('-=' * 11)

    usuario = int(input('Digite sua opcao: '))

    #voltar
    if usuario == 6:
        return

    #menu
    if usuario == 1:
        agenda()
    elif usuario == 2:
        agendar()
    elif usuario == 3:
        buscar()
    elif usuario == 4:
        excluir()
    elif usuario == 5:
        editar()

def agenda():

    agendamentos = dados['agendamentos']
    cadastros = dados['cadastros']

    for cadastro in cadastros:
        for ag in agendamentos:
            if cadastro['id'] == ag['id_ag']:
                print(f'{cadastro[ 'nome']} - {ag['data']} - {ag['horario']}')


def agendar():

    #variaveis de referencia
    agendamentos = dados['agendamentos']
    cadastros = dados['cadastros']

    nome = input('Digite o nome do agendamento: ')
    telefone = input('Digite o telefone do agendamento: ')

    for cliente in cadastros:
        if nome == cliente['nome'] and telefone == cliente['telefone']:
            print('cliente encontrado.')
            print()
            data = input('Digite o data do agendamento: ')

            #validacao de data passada
            if not data_passada(data):
                print('data inválida. tente cadastrar uma data atual.')
                return

            #horarios disponiveis
            horarios = gerador_horarios()
            disponiveis = horarios_disponiveis(data, horarios)

            print(f'horários disponiveis na data {data}.')
            print('-' * 10)
            for disponivel in disponiveis:
                print(f'{disponivel}')
            print('-' * 10)

            horario = input('Digite o horário do agendamento: ')

            #validacao de horario de funcionamento
            if not horario_funcionamento(horario):
                print('fora do horário de funcionamento. tente um que esteja na grade de horários.')
                return

            #validacao de horarios duplicados
            if not horario_duplicado(data, horario):
                print('horário já ocupado nessa data. tente outro.')
                return

            id_ag = cliente['id']

            agendado = {'id_ag' : id_ag, 'data': data, 'horario': horario}
            agendamentos.append(agendado)
            salvar()
            print('agendamento feito com sucesso.')

def excluir():

    cadastros = dados['cadastros']
    agendamentos = dados['agendamentos']

    nome = input('Digite o nome do agendamento: ')
    telefone = input('Digite o telefone do agendamento: ')

    for cad in cadastros:
        for ag in agendamentos:
            if nome == cad['nome'] and telefone == cad['telefone']:
                if cad['id'] == ag['id_ag']:
                    agendamentos.remove(ag)
                    print('agendamento excluido com sucesso.')
                    salvar()
















