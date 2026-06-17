from datetime import datetime, date, timedelta
from dados import dados

def data_passada(data):

    data_atual = date.today()

    data_convertida = datetime.strptime(data, '%d/%m/%Y').date()

    if data_convertida < data_atual:
        return False
    return True

def horario_duplicado(data, horario):

    agendamentos = dados['agendamentos']

    for ag in agendamentos:
        if data == ag['data'] and horario == ag['horario']:
            return False
    return True

def horario_funcionamento(horario):

    horario_convertido = datetime.strptime(horario, '%H:%M').time()

    abertura = datetime.strptime('8:00', '%H:%M').time()
    fechamento = datetime.strptime('18:00', '%H:%M').time()

    if horario_convertido < abertura or horario_convertido >= fechamento:
        return False
    return True




