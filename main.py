from functions import ler, criar_perfil, excluir, ler_especifico, atualizar

espaco_de_menu1 = '=' * 15
espaco_de_menu2 = '=-=' * 10

print(f'''{espaco_de_menu2}
Bem-vindo(a) ao sistema da Python Gym!
O que pretende fazer por agora?''')
while True:
    operar = input('''[1] - Criar,
[2] - Ler.
[3] - Atualizar.
[4] - Excluir.
[0] - Sair.

F: ''').upper()

    #criar
    if operar == '1':
        criar_perfil()

    #ler
    elif operar == '2':
        ler_quais = input('''Deseja visualizar todos, ou um específico?
[1] - Todos.
[2] - Especificar.
                          
F: ''')
        if ler_quais == '1':
            perfis = ler()
            for perfil in perfis:
                print(perfil['id'], perfil['nome'])
        if ler_quais == '2':
            perfil = ler_especifico()
            print(perfil)
            

    #atualizar
    elif operar == '3':
        id = input('Insira o ID de qual perfil atualizar: ')
        atualizar(id)

    #excluir
    elif operar == '4':
        id = input('Insira o ID de qual perfil excluir: ')
        excluir(id)

    #sair
    elif operar == '0':
        break
    print(f"""{espaco_de_menu2}
Insira o próximo comando: """)
print(f'''={espaco_de_menu2}
O sistema foi encerrado! Até a próxima!
f{espaco_de_menu2}''')