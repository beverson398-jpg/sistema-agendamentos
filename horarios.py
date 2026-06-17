from datetime import datetime, timedelta
from dados import dados

def gerador_horarios():

    horarios = []

    inicial = datetime.strptime('8:00', '%H:%M')
    final = datetime.strptime('18:00', '%H:%M')
    entre = timedelta(minutes = 30)

    while inicial < final:
        horarios.append(inicial.strftime('%H:%M'))
        inicial += entre

    return horarios

def horarios_disponiveis(data, horarios):

    disponiveis = []

    agendamentos = dados['agendamentos']
    horarios = gerador_horarios()

    for horario in horarios:
        indisponivel = False

        for agendamento in agendamentos:
            if data == agendamento['data'] and horario == agendamento['horario']:
                indisponivel = True

        if not indisponivel:
            disponiveis.append(horario)

    return disponiveis







