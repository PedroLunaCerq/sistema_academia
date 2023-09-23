from functions import ler, ler_todos

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
        print('Estou aqui!)')

    #ler
    elif operar == '2':
        ler_quais = input('''Deseja visualizar todos, ou um específico?
[1] - Todos.
[2] - Especificar.
                          
F: ''')
        if ler_quais == '1':
            perfis = ler_todos()
            print(perfis)
        elif ler_quais == '2':
            print('Estou aqui!')

    #atualizar
    elif operar == '3':
        print('Estou aqui!')

    #excluir
    elif operar == '4':
        print('Estou aqui!')

    #sair
    elif operar == '0':
        break

print(f'''={espaco_de_menu2}
O sistema foi encerrado! Até a próxima!
f{espaco_de_menu2}''')