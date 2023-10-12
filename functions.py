def ler() -> list:
    '''Esta função extrai todo o arquivo como uma lista.'''
    with open('cadastros_academia.csv', 'r') as arquivo:
        perfis_todos = arquivo.read().split('\n')
        cabecalho = perfis_todos.pop(0)
        lista_perfis = []
        for perfil in perfis_todos:
            perfil_dict = transformar_dict(cabecalho, perfil)
            lista_perfis.append(perfil_dict)
        arquivo.close()
    return lista_perfis


def ler_especifico() -> dict:
    '''Esta função lê um único perfil.'''
    id = input('Insira o cadastro do perfil: ')
    with open('cadastros_academia.csv', 'r') as arquivo:
        texto = arquivo.read()
        perfis = texto.split('\n')
        cabecalho = perfis.pop(0)
        perfil_escolhido = {}
        for perfil in perfis:
            perfil_dict = transformar_dict(cabecalho, perfil)
            if perfil_dict['id'] == id:
                perfil_escolhido = perfil_dict
        arquivo.close()
    return perfil_escolhido

def criar_perfil():
    '''Esta função cria perfis, e importa para o arquivo.'''
    perfis = ler()
    if len(perfis) == 0:
        id = '0'
    else:
        id = perfis[-1]['id']
    perfil = {'id': '', 'nome': '', 'genero': '', 'nascimento': '', 'faixa': '', 'ultima_grad': '', 'plano': '', 'status': ''}
    perfil['id'] = int(id) + 1
    perfil['nome'] = input('Insira o nome: ').title()
    perfil['genero'] = input('Insira o genero [M/F]: ').upper()
    perfil['nascimento'] = input('Insira o nascimento: ')
    perfil['faixa'] = input('Insira a faixa atual: ').capitalize()
    perfil['ultima_grad'] = input('Insira a última graduação: ')
    perfil['plano'] = input('Insira o plano: ').capitalize()
    perfil['status'] = input('Insira o status do plano [ON/OFF]: ').capitalize()
    with open('cadastros_academia.csv', 'a', encoding='utf-8') as arquivo:
        arquivo.write('\n')
        perfil = transformar_str(perfil)
        arquivo.write(perfil)
        arquivo.close()
    return('Perfil adicionado!')

def transformar_str(dicionario) -> str:
    '''Esta função transforma um dicionário em uma string.'''
    perfil = f"{dicionario['id']},{dicionario['nome']},{dicionario['genero']},{dicionario['nascimento']},{dicionario['faixa']},{dicionario['ultima_grad']},{dicionario['plano']},{dicionario['status']}"
    return perfil

def transformar_dict(cabecalho: str, perfil: str) -> dict:
    '''Esta função transforma uma string em um dicionário.'''
    cabecalho = cabecalho.split(',')
    perfil = perfil.split(',')
    perfil_dict = {
        cabecalho[0] : perfil[0],
        cabecalho[1] : perfil[1],
        cabecalho[2] : perfil[2],
        cabecalho[3] : perfil[3],
        cabecalho[4] : perfil[4],
        cabecalho[5] : perfil[5],
        cabecalho[6] : perfil[6],
        cabecalho[7] : perfil[7],
    }
    return perfil_dict


def excluir(id):
    '''Esta função exclui perfis do arquivo.'''
    with open('cadastros_academia.csv', 'r') as arquivo:
        texto = arquivo.read().split('\n')
        cabecalho = texto.pop(0)
        arquivo.close()

    novo_arquivo = [cabecalho]
    for perfil in texto:
        perfil_dict = transformar_dict(cabecalho, perfil)
        if perfil_dict['id'] != id:
            novo_arquivo.append(perfil)
    novo_arquivo = '\n'.join(novo_arquivo)

    with open('cadastros_academia.csv', 'w') as arquivo:
        arquivo.write(novo_arquivo)
        arquivo.close()
    return('Perfil excluído!')


def atualizar(id):
    '''Esta função atualiza perfis do arquivo.'''
    with open('cadastros_academia.csv', 'r') as arquivo:
        texto = arquivo.read().split('\n')
        cabecalho = texto.pop(0)
        arquivo.close()

    novo_arquivo = [cabecalho]
    for perfil in texto:
        perfil_dict = transformar_dict(cabecalho, perfil)
        if perfil_dict['id'] != id:
            novo_arquivo.append(perfil)
        elif perfil_dict['id'] == id:
            perfil_dict['nome'] = input('Insira o nome do perfil: ')
            perfil_dict['genero'] = input('Insira o genero [M/F]: ')
            perfil_dict['nascimento'] = input('Insira a data de nascimento: ')
            perfil_dict['faixa'] = input('insira a faixa: ')
            perfil_dict['ultima_grad'] = input('Insira a última gradução: ')
            perfil_dict['plano'] = input('Insira o plano: ')
            perfil_dict['status'] = input('Insira o status do plano: ')
            perfil_dict = transformar_str(perfil_dict)
            novo_arquivo.append(perfil_dict)
    novo_arquivo = '\n'.join(novo_arquivo)

    with open('cadastros_academia.csv', 'w') as arquivo:
        arquivo.write(novo_arquivo)
        arquivo.close()
    return('Perfil atualizado!')