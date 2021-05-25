# gerando variaveis que serão usadas no código
tabuleiro = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
xou0 = "X"

rodada = 1
while True:
    try:
        # mostrando estado do tabuleiro e perguntando qual será a proxima jogada
        print(f"Rodada {rodada}. O tabuleiro está assim:\n", "".join(tabuleiro[0]), "\n", "".join(tabuleiro[1]), "\n",
              "".join(tabuleiro[2]))
        pergunta = list(input(f"vez do {xou0}. Digite a casa que você deseja modificar: "))
        # fazendo um sisteminha para trasnformar str em int
        linha = pergunta[0]
        coluna = pergunta[2]
        linha = int(linha) - 1
        coluna = int(coluna) - 1
    except ValueError:
        print("Digite a casa que você quer seguindo esse exêmplo: 2,3(sendo 2 a linha e 3 a coluna).")
        continue
    except IndexError:
        print("São só 3 linhas e 3 colunas, não use valores maiores que esses!")

    # adicionando X/0 na array
    if tabuleiro[linha][coluna] != '-':
        print("você não pode jogar em um lugar que já está sendo utilizado")
        continue
    else:
        tabuleiro[linha].insert(coluna, xou0)
        del tabuleiro[linha][coluna + 1]
    # vendo quem ganhou
    # horizontal:
    if tabuleiro[0][0] == "X" and tabuleiro[0][1] == "X" and tabuleiro[0][2] == "X":
        print("Prabéns X, você ganhou!")
        exit()
    elif tabuleiro[0][0] == "0" and tabuleiro[0][1] == "0" and tabuleiro[0][2] == "0":
        print("Prabéns 0, você ganhou!")
        exit()
    elif tabuleiro[1][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[1][2] == "X":
        print("Prabéns X, você ganhou!")
        exit()
    elif tabuleiro[1][0] == "0" and tabuleiro[1][1] == "0" and tabuleiro[1][2] == "0":
        print("Prabéns 0, você ganhou!")
        exit()
    elif tabuleiro[2][0] == "X" and tabuleiro[2][1] == "X" and tabuleiro[2][2] == "X":
        print("Prabéns X, você ganhou!")
        exit()
    elif tabuleiro[2][0] == "0" and tabuleiro[2][1] == "0" and tabuleiro[2][2] == "0":
        print("Prabéns 0, você ganhou!")
        exit()
    # vertical:
    elif tabuleiro[0][0] == "X" and tabuleiro[1][0] == "X" and tabuleiro[2][0] == "X":
        print("Prabéns X, você ganhou!")
        exit()
    elif tabuleiro[0][0] == "0" and tabuleiro[1][0] == "0" and tabuleiro[2][0] == "0":
        print("Prabéns 0, você ganhou!")
        exit()
    elif tabuleiro[0][1] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][1] == "X":
        print("Prabéns X, você ganhou!")
        exit()
    elif tabuleiro[0][1] == "0" and tabuleiro[1][1] == "0" and tabuleiro[2][1] == "0":
        print("Prabéns 0, você ganhou!")
        exit()
    elif tabuleiro[0][2] == "X" and tabuleiro[1][2] == "X" and tabuleiro[2][2] == "X":
        print("Prabéns X, você ganhou!")
        exit()
    elif tabuleiro[0][2] == "0" and tabuleiro[1][2] == "0" and tabuleiro[2][2] == "0":
        print("Prabéns 0, você ganhou!")
        exit()
    #diagonal:
    elif tabuleiro[0][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][2] == "X":
        print("Prabéns X, você ganhou!")
        exit()
    elif tabuleiro[0][0] == "0" and tabuleiro[1][1] == "0" and tabuleiro[2][2] == "0":
        print("Prabéns 0, você ganhou!")
        exit()
    elif tabuleiro[0][0] == "X" and tabuleiro[1][1] == "X" and tabuleiro[2][2] == "X":
        print("Prabéns X, você ganhou!")
        exit()
    elif tabuleiro[0][2] == "0" and tabuleiro[1][1] == "0" and tabuleiro[2][0] == "0":
        print("Prabéns 0, você ganhou!")
        exit()
    elif tabuleiro[0].count("-") == 0 and tabuleiro[1]. count("-") == 0 and tabuleiro[2].count("-") == 0:
        print("Deu velha =(")
        exit()
    rodada += 1
    if rodada // 2 == rodada / 2:
        xou0 = "0"
    else:
        xou0 = "X"