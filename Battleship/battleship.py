import random
import os

def definir_nome():
    nome = str(input('Digite o seu nome: '))
    return nome

# Acessa a função definir_nome para pegar a variável local nome.
nome_jogador = definir_nome()

print(f'Seja bem-vindo ao jogo de Batalha Naval {nome_jogador}! Esperamos que você se divirta!')

# Função que mostra o tutorial
def exibir_tutorial():
    print('Batalha Naval é jogado em um tabuleiro 5x10.')
    print('Cada jogador deve posicionar 5 navios no tabuleiro, sem contar ao adversário as posições.')
    print('Em cada rodada, cada jogador irá atacar uma posição do tabuleiro.')
    print('Vence quem destruir a frota inimiga primeiro.')

# Caso o input do usuário seja 1, o programa exibirá um texto com as regras do jogo, caso o input seja igual a 2, o looping se encerrará.
# Caso o usuário responda qualquer número diferente de 2, o looping continuará a repetir.
# Foi utilizado string ao invés de int para que, caso o usuário responda com alguma letra, o programa continue rodando.
tutorial = ""
while tutorial != "2":
    tutorial = str(input(f"{nome_jogador}, você deseja ver o tutorial?\nDigite 1 para ver o tutorial.\nDigite 2 para iniciar o jogo."))
    if tutorial == "1":
        exibir_tutorial()

def create_random_ship():
    return random.randint(0, 4), random.randint(0, 9)

def get_player_ship_positions():
    player_ships = set()  # player position =({0,1}, {0,2})
    for i in range(1, 6):
        while True:
            try:
                row = int(input(f"Digite a linha do navio {i} (0-4): "))
                column = int(input(f"Digite a coluna do navio {i} (0-9): "))
                if (row, column) not in player_ships and 0 <= row <= 4 and 0 <= column <= 9:
                    player_ships.add((row, column))
                    break
                else:
                    print("Posição inválida ou já ocupada. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Por favor, digite números válidos.")
    return player_ships

def play_again():
    try_again = input("Deseja jogar novamente? <sim> ou <nao> ").strip().lower()
    if try_again == "sim":
        play_game()
    else:
        print("Obrigado por jogar o nosso jogo! \nFeito por: \nHussein Ali El Gazouini \nHassan Ali El Gazouini \nMurilo Zimerman Fortaleza.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def center_text(text, width=80):
    return text.center(width)

def print_map(board, title, ships_left, width=80):
    print(center_text(title, width))
    for row in board:
        print(center_text(' ' + '  '.join(row) + ' ', width))
    print(center_text(f"Navios restantes: {ships_left}", width))
    print("\n")

def play_game():
    term_width = 80  # Default width for simplicity
    
    # Mapa do computador
    player_attack_board = [["0"] * 10 for _ in range(5)]
    
    # Mapa do jogador
    computer_attack_board = [["0"] * 10 for _ in range(5)]
    
    # Cria navios para o jogador
    player_ships = get_player_ship_positions()
    # Cria navios para o computador
    computer_ships = {create_random_ship() for _ in range(5)}
    player_ships_left = 5
    computer_ships_left = 5

    while player_ships_left != 0 and computer_ships_left != 0:
        clear_screen()
        print_map(player_attack_board, "--MAPA DO COMPUTADOR--", computer_ships_left, term_width)
        print_map(computer_attack_board, f"--MAPA DO(A) {nome_jogador}--", player_ships_left, term_width)

        # JOGADOR
        print(center_text(f"== {nome_jogador}, é a sua vez de atacar! ==", term_width))
        try:
            row = int(input("Digite a linha onde deseja atacar (0-4): "))
            column = int(input("Digite a coluna onde deseja atacar (0-9): "))
            if (row, column) in computer_ships:
                print(center_text("Você acertou um navio!", term_width))
                player_attack_board[row][column] = 'X'
                computer_ships_left -= 1
                computer_ships.remove((row, column))
            else:
                print(center_text("Você errou o tiro!", term_width))
                player_attack_board[row][column] = '-'
        except ValueError:
            print(center_text("Entrada inválida. Por favor, digite números válidos.", term_width))
            continue
        except IndexError:
            print(center_text("Coordenadas fora do limite. Tente novamente.", term_width))
            continue

        if computer_ships_left == 0:
            break

        # COMPUTADOR
        while True:
            computer_row, computer_column = create_random_ship()
            if computer_attack_board[computer_row][computer_column] == "0":
                break

        print(center_text(f"O computador atacou a posição: ({computer_row}, {computer_column})", term_width))

        if (computer_row, computer_column) in player_ships:
            print(center_text("O computador acertou um navio!", term_width))
            computer_attack_board[computer_row][computer_column] = 'X'
            player_ships_left -= 1
            player_ships.remove((computer_row, computer_column))
        else:
            print(center_text("O computador errou o tiro!", term_width))
            computer_attack_board[computer_row][computer_column] = '-'
        
        print(f'O jogador possui: {player_ships_left} navios.')
        print(f'O computador possui: {computer_ships_left} navios.')
        input(center_text("Pressione Enter para continuar...", term_width))

    clear_screen()
    print_map(player_attack_board, f"Mapa do Ataque do {nome_jogador}", computer_ships_left, term_width)
    print_map(computer_attack_board, "Mapa do Ataque do Computador", player_ships_left, term_width)

    if player_ships_left == 0:
        print(center_text("O computador venceu! Todos os seus navios foram afundados.", term_width))
    elif computer_ships_left == 0:
        print(center_text(f"{nome_jogador} venceu! Todos os navios do computador foram afundados.", term_width))
    
    play_again()

play_game()
