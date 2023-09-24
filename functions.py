#Função 'Ler'.
def ler() -> list:
    '''Esta função extrai todo o arquivo como uma string.'''
    with open('cadastros_academia.csv', 'r') as arquivo:
        perfis_todos = arquivo.read()
        '\n'.join(perfis_todos)
        perfis_todos.split('\n')
        lista_perfis = []
        for perfil in perfis_todos:
            lista_perfis.append(perfil)
        arquivo.close()
    return lista_perfis

#Função para ler todos.
def ler_todos():
    '''Esta função printa todos os perfis, na operação 2.'''
    perfis = ler()
    perfis = ''.join(perfis)
    print(perfis)

#Função para criar perfil.
#def criar_perfil():
#    '''Esta função cria perfis, e importa para o arquivo.'''
#    #    matricula = 
#    perfil = {'nome': '', 'genero': '', 'nascimento': '', 'faixa': '', 'ultima_grad': '', 'plano': '', 'status': ''}
#    perfil['nome'] = input('Insira o nome: ').capitalize()
#    perfil['genero'] = input('Insira o genero [M/F]: ').upper()
#    perfil['nascimento'] = input('Insira o nascimento: ')
#    perfil['faixa'] = input('Insira a faixa atual: ').capitalize
#    perfil['ultima_grad'] = input('Insira a última graduação: ')
#    perfil['plano'] = input('Insira o plano: ').capitalize
#    perfil['status'] = input('Insira o status do plano [ON/OFF]: ')
#    with open('cadastros_academia.csv', 'a') as arquivo:
#        backup = arquivo.append(perfil)
#        arquivo.write(backup)
#        arquivo.close()
#    return('Perfil adicionado!')