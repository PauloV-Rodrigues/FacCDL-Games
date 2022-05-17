# Código Principal (main code)

# Início do Jogo (Game Start)
# Lista de Opções de Jogos (List of Game Options)
print("""
\033[31m****** Bem-vindos ao FCDL-Games ******\033[m
************ J O G O S *************
1 – Forca
2 – Jogo da Velha
3 – JokenPo
4 - Sair
*************************************""")

# Indica ao usuário que escolha uma opção (Indicates the user to choose an option)
choice = input("Digite sua escolha: ")

while choice != '4':
    # Jogo da Forca (Hangman Game)
    if choice == '1':
        # Importa o jogo (imports the game)
        from hangman_game import hangman_game
        # Roda o jogo (run the game)
        hangman_game
        break
    
    # Jogo da Velha (Tic Tac Toe Game)
    elif choice == '2':
        # Importa o jogo (imports the game)
        from tic_tac_toe_game import tic_tac_toe_game
        # Roda o jogo (run the game)
        tic_tac_toe_game
        break
    
    # Jogo do Pedra, Papel, Tesoura (Paper, Scissor, Rock Game)
    elif choice == '3':
        # Importa o jogo (imports the game)
        from paper_scissor_rock_game import paper_scissor_rock_game
        # Roda o jogo (run the game)
        paper_scissor_rock_game
        break
    
    # Opção inválida (Invalid option)
    elif choice != '4':
        print("Opção inválida!")
        choice = input("Digite sua escolha: ")

# Fim de aplicação (application ending)
if choice == '4':
    print("\nObrigado por escolher o FCDL Games. Até mais!")