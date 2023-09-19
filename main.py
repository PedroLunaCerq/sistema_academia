espaco_de_menu1 = '=' * 15
espaco_de_menu2 = '=-=' * 10

print(f'''{espaco_de_menu2}
Bem-vindo(a) ao sistema da Python Gym!
O que pretende fazer por agora?''')
while True:
    operar = input('[Criar, ler, atualizar, excluir sair] ').upper()

    #criar
    if operar == 'CRIAR':
        print('Estou aqui!)')

    #ler
    elif operar == 'LER':
        print('Estou aqui!')

    #atualizar
    elif operar == 'ATUALIZAR':
        print('Estou aqui!')

    #excluir
    elif operar == 'EXCLUIR':
        print('Estou aqui!')

    #sair
    elif operar == 'SAIR':
        break

print(f'''={espaco_de_menu2}
O sistema foi encerrado! Até a próxima!
f{espaco_de_menu2}''')