# Importando a Biblioteca Random para selecionar as palavras aleatoriamente
from random import choice

# Abrindo e lendo arquivo que contém uma lista selecionada de palavras
# Palavras retirada de https://www.dicio.com.br/lista-de-palavras/
with open('hangman_game/words_list.txt') as words:
    lines = words.read()
    words_list = lines.split('\n')

# Selecionando uma palavra aleatória do arquivo e deixando todas as letras em maiúsculo
word = choice(words_list).upper()

# Criando o Board do Game
forca = """
######
     *
     -"""

empty = """


"""

head = """
     o
"""
body = """
     o
     |
"""
left_arm = """
     o
    /|
"""
right_arm = """
     o
    /|\\
"""
left_leg = """
     o
    /|\\
    /
"""
right_leg = """
     o
    /|\\
    / \\
"""

# Definindo a lista de chances do usuário
toys_chance = [
    empty,
    head,
    body,
    left_arm,
    right_arm,
    left_leg,
    right_leg,
]

# Quantidade de acertos e erros
right_guess = 0
wrong_guess = 0

# Letras já acertadas ou erradas
right_letters = ''
wrong_letters = ''

# Início do Game
print("""\033[31m****** JOGO DA FORCA ******\033[m""")
while right_guess != len(word) and wrong_guess != 7:
    message = ''
    for letter in word:
        if letter in right_letters:
            message += f'{letter} '
        else:
            message += '_ '

    # Incrementando o Board do Game
    print(forca+toys_chance[wrong_guess])

    # Exibindo a palavra com letras acertadas
    print(message)
    letter = input("Digite uma letra: ").upper()

    # Condição para caso o usuário digite a mesma letra mais de uma vez
    if letter in right_letters+wrong_letters:
        print('Você já tentou essa letra!')
        continue

    # Se a letra digitada estiver na palavra, ele acerta
    if letter in word:
        print("Você acertou a letra!")
        right_letters += letter
        right_guess += word.count(letter)
    # Se a letra digitada não estiver na palavra, ele erra
    else:
        print("Você errou a letra!")
        wrong_letters += letter
        wrong_guess += 1

if right_guess == len(word):
    print("Parabéns, você venceu!")
else:
    print("Você perdeu, tente novamente!")