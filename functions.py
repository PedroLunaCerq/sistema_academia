#Função 'Ler'.
def ler() -> list:
    '''Esta função extrai todo o arquivo como uma string.'''
    with open('cadastros_academia.csv', 'r') as arquivo:
        perfis_todos = arquivo.read()
        perfis_todos.split('\n')
        lista_perfis = []
        for perfil in perfis_todos:
            lista_perfis.append(perfil)
        arquivo.close()
    return lista_perfis

def ler_todos():
    '''Esta função printa todos os perfis, na operação 2.'''
    perfis = ler()
    perfis = ''.join(perfis)
    print(perfis)

#Função 'Criar'.
#matricula, nome, data de nascimento, faixa, ultima graduação, sexo, plano, status