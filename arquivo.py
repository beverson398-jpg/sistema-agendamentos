import json
from dados import dados

def salvar():

    with open('dados.json', 'w') as arquivo:
        json.dump(dados, arquivo)

def carregar():

    with open('dados.json', 'r') as arquivo:
        dados_carregados = json.load(arquivo)

    dados['cadastros'] = dados_carregados.get('cadastros', [])
    dados['agendamentos'] = dados_carregados.get('agendamentos', [])



