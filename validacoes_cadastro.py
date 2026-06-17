from dados import dados

def telefone_duplicado(telefone):

    cadastros = dados['cadastros']

    for cad in cadastros:
        if telefone == cad['telefone']:
            return False
    return True



