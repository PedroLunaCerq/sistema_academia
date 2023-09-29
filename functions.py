def ler() -> list:
    '''Esta função extrai todo o arquivo como uma lista.'''
    with open('cadastros_academia.csv', 'r') as arquivo:
        perfis_todos = arquivo.read()
        lista_perfis = []
        for perfil in perfis_todos:
            lista_perfis.append(perfil)
        arquivo.close()
    return lista_perfis

def ler_todos():
    '''Esta função printa todos os perfis, na operação 2.'''
    perfis = ler()
    perfis = ''.join(perfis)
    perfis = perfis.split('\n')
    return perfis

#Função para criar cadastros únicos.
def criar_perfil():
    '''Esta função cria perfis, e importa para o arquivo.'''
    perfil = {'nome': '', 'genero': '', 'nascimento': '', 'faixa': '', 'ultima_grad': '', 'plano': '', 'status': ''}
    perfil['nome'] = input('Insira o nome: ').tittle()
    perfil['genero'] = input('Insira o genero [M/F]: ').upper()
    perfil['nascimento'] = input('Insira o nascimento: ')
    perfil['faixa'] = input('Insira a faixa atual: ').capitalize()
    perfil['ultima_grad'] = input('Insira a última graduação: ')
    perfil['plano'] = input('Insira o plano: ').capitalize()
    perfil['status'] = input('Insira o status do plano [ON/OFF]: ')
    with open('cadastros_academia.csv', 'a') as arquivo:
        arquivo.write('\n')
        perfil = transformar_str(perfil)
        arquivo.write(perfil)
        arquivo.close()
    return('Perfil adicionado!')

def transformar_str(dicionario) -> str:
    '''Esta função transforma um dicionário em uma string.'''
    perfil = f"{dicionario['nome']},{dicionario['genero']},{dicionario['nascimento']},{dicionario['faixa']},{dicionario['ultima_grad']},{dicionario['plano']},{dicionario['status']}"
    return perfil

##Arrumar.
def excluir(operar):
    with open('cadastros_academia.csv', 'r') as arquivo:
        perfis = arquivo.read()
        arquivo.close
    with open('cadastros_academia.csv', 'w') as arquivo:
        perfis_update = []
        for perfil in perfis:
            if perfil[0] != f'{operar}':
                perfis_update.append(perfil)
        perfis_upload = ''.join(perfis_update)
        arquivo.write(perfis_upload)
        arquivo.close()