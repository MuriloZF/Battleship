# Batalha Naval v1

# Autores: Hassan Ali El Gazouini, Hussein Ali El Gazouini e Murilo Zimerman Fortaleza.

  Este projeto foi desenvolvido a pedido da Professora Marina.
Este é um simples jogo de Batalha Naval desenvolvido em Python. Abaixo está uma breve explicação do código e como jogar.

## Como Jogar

1. **Nome do Jogador**: Você será solicitado a inserir o seu nome para iniciar o jogo.
2. **Tutorial**: Você tem a opção de visualizar um tutorial sobre as regras do jogo.
3. **Posicionamento dos Navios**: Você vai ter que posicionar 5 navios no tabuleiro. Cada navio ocupa uma posição do tabuleiro.
4. **Ataque**: Em cada rodada, você e o computador vão atacar posições no tabuleiro do outro. O objetivo é afundar todos os navios do oponente.
5. **Final do Jogo**: O jogo termina quando todos os navios de um dos jogadores forem afundados.

## Explicação do Código

- **`def definir_nome():`**: Esta função pede ao jogador que insira o seu nome e retorna o nome como uma string.
- **`def exibir_tutorial():`**: Esta função mostra um tutorial com as regras do jogo.
- **`tutorial = ""`**: Inicia a variável `tutorial` como uma string vazia para iniciar o loop.
- **`while tutorial != "2":`**: Um loop que continua até que o jogador escolha iniciar o jogo (`2`).
- **`def create_random_ship():`**: Esta função gera aleatoriamente as coordenadas de um navio.
- **`def get_player_ship_positions():`**: Esta função solicita ao jogador as posições dos seus navios.
- **`def play_again():`**: Esta função pergunta ao jogador se ele deseja jogar novamente.
- **`def clear_screen():`**: Esta função limpa a tela do console.
- **`def center_text(text, width=80):`**: Esta função centraliza o texto na tela.
- **`def print_map(board, title, width=80):`**: Esta função imprime o tabuleiro do jogo com um título.

## Iniciando o Jogo

Quando o jogador inserir o seu nome, ele vai ter a  opção de olhar o tutorial para ter um melhor entendiemnto de como jogar ou iniciar o jogo imediatamente. Durante o jogo, o jogador e o computador vão alternar os ataques até que todos os navios de um dos jogadores sejam afundados. Após o término do jogo, o jogador terá a opção de jogar novamente ou sair do jogo.

## Créditos

Este jogo foi desenvolvido por Hussein Ali El Gazouini, Hassan Ali El Gazouini e Murilo Zimerman Fortaleza.

Divirta-se jogando Batalha Naval!
