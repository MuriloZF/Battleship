import random
import os

def create_random_ship():
    return random.randint(0, 4), random.randint(0, 9)

def get_player_ship_positions():
    player_ships = set()
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
    try_again = input("Deseja Jogar novamente? <sim> ou <nao> ").strip().lower()
    if try_again == "sim":
        play_game()
    else:
        print("Obrigado por jogar o nosso jogo! \n Feito por: \nHussein Ali El Gazouini \n Hassan Ali El Gazouini \n Murilo Zimerman Fortaleza.")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def center_text(text, width=80):
    return text.center(width)

def print_map(board, title, width=80):
    print(center_text(title, width))
    for row in board:
        print(center_text(' '.join(row), width))
    print("\n")

def play_game():
    term_width = 80  # Default width for simplicity
    
    # Mapa do computador
    player_attack_board = [
        ["0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 \n"],
        ["0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 \n"],
        ["0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 \n"],
        ["0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 \n"]
        ["0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 \n"], 
    ]
    
    # Mapa do jogador
    computer_attack_board = [
        ["0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 \n"], 
        ["0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 \n"],
        ["0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 \n"],
        ["0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 \n"],
        ["0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 ", "0 \n"]
    ]
    
    # cria navios para o jogador
    player_ships = get_player_ship_positions()
    # cria navios para o computador
    computer_ships = {create_random_ship() for _ in range(5)}
    player_ships_left = 5
    computer_ships_left = 5

    while player_ships_left != 0 and computer_ships_left != 0:
        clear_screen()
        print_map(player_attack_board, "--MAPA DO COMPUTADOR--", term_width)
        print_map(computer_attack_board, "--MAPA DO JOGADOR--", term_width)

        # JOGADOR
        print(center_text("== Jogador, é a sua vez de atacar! ==", term_width))
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

        input(center_text("Pressione Enter para continuar...", term_width))

    clear_screen()
    print_map(player_attack_board, "Mapa do Ataque do Jogador", term_width)
    print_map(computer_attack_board, "Mapa do Ataque do Computador", term_width)

    if player_ships_left == 0:
        print(center_text("O computador venceu! Todos os seus navios foram afundados.", term_width))
    elif computer_ships_left == 0:
        print(center_text("Você venceu! Todos os navios do computador foram afundados.", term_width))
    
    play_again()

play_game()
