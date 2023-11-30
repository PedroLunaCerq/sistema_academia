from alunos import Aluno

#Criar aluno.
def criar_aluno():
    nome = input('Insira o nome: ')
    nascimento = input('Insira o ano de nascimento: ')
    faixa = input('Insira a faixa: ')
    aluno = Aluno(nome, nascimento, faixa)
    return aluno

#Adicionar ao arquivo.
def adicionar_aluno(aluno):
    with open('perfis.txt', 'a') as arquivo:
        for key in range(0,3), aluno:
            arquivo.write(str(key))

def ler_todos():
    with open('perfis.txt', 'r') as arquivo:
        for item in arquivo:
            print(item)