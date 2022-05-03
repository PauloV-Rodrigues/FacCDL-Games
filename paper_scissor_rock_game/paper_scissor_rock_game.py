from random import randint
from time import sleep

# Criando possibilidade de resultados
player_win = pc_win = tie = 0

# Criando variáveis auxiliares
i = 1

print('''\033[31m****** JOKENPÔ ******\033[m''')
matches = int(input("Digite a quantidade de partidas: "))

# Definindo as opções do jogo: Pedra, Papel e Tesoura
while i <= matches:
    rock = 'Pedra'
    paper = 'Papel'
    scissor = 'Tesoura'
    options = (rock, paper, scissor)
    pc = randint(0, 2)

    print('''
Escolha sua jogada:
0 - PEDRA
1 - PAPEL 
2 - TESOURA
''')
    player = ''
    list = [0, 1, 2]

    # Perguntando a jogada do player
    player = int(input('Sua jogada? '))
    # Caso a opção não esteja na lista de possibilidades
    while player not in list:
        player = int(input('Digite um valor válido [0, 1 ou 2]. Qual é a sua jogada? '))

    # Printando o game "Jo-Ken-Pô"
    print('\033[31mJO\033[m')
    sleep(.3)
    print('\033[31mKEN\033[m')
    sleep(.3)
    print('\033[31mPÔ!\033[m')

    # Exibindo a jogada de cada jogador
    print(f'\nComputador jogou {options[pc]}.')
    print(f'Jogador jogou {options[player]}.\n')

    # Definindo possibilidades de pontuação
    if pc == 0:
        if player == 0:
            tie += 1
        elif player == 1:
            player_win += 1
        elif player == 2:
            pc_win += 1

    elif pc == 1:
        if player == 0:
            pc_win += 1
        elif player == 1:
            tie += 1
        elif player == 2:
            player_win += 1

    elif pc == 2:
        if player == 0:
            player_win += 1
        elif player == 1:
            pc_win += 1
        elif player == 2:
            tie += 1

    # Exibindo pontuação
    print(f'''\033[31mPONTUAÇÃO\033[m
Você: {player_win}
Computador: {pc_win}''')
    i += 1

# Após o loop, exibe-se quem ganhou
if player_win > pc_win:
    print(f'\nVocê venceu o computador por {player_win} a {pc_win}.')
elif player_win < pc_win:
    print(f'\nO computador venceu você por {pc_win} a {player_win}.')
elif player_win == pc_win:
    print(f'\nEmpate.')