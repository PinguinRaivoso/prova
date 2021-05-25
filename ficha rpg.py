# Crie um programa que gere fichas de rpg:
# ---- Parte 1 ----
# O programa deve perguntar para o usuario se ele deseja importar uma ficha de rpg já existente (em um txt) ou se ele gostaria de criar uma
# Caso o ususario queira importar uma ficha já existente o programa vai pedir o nome do txt onde está localizado a ficha
# E após pegar o nome da ficha o programa ira importar os atributos do jogador pra dentro do sistema
# Mas se o usuario quiser criar uma, o programa irá requisitar o nome do personagem e sua a classe (Guerreiro, assasino ou mago)
# Posteriormente o programa ira gerar os seguintes valores de maneira randomica:
# Mana (de 1 a 20), vida (de 1 a 20), carisma (1 a 4), o tipo de arma (espada, adagas, arco e flecha e cajado) e fome (de 1 a 4)

# ---- Parte 2 ----
# Após gerar a ficha ou importa-la vocês deverão dar opções para o jogador de manipular os valores de sua ficha como no exemplo abaixo:
# Você gostaria de: Mudar a vida (1) // Mudar a mana (2) // Mudar a fome (3) // Salvar a ficha em um txt (4) // Jogar dado (5) // Sair (6) --->

# Ps: Se o jogador inserir algum valor no programa que não seja valido o programa deve alerta-lo e pedir para  inserir o valor novamente
# Ps2: Não se esqueça do try e do except
# Ps3: Se a mana, vida ou fome do jogador tiver em "0" o programa deve alertar o usuario
from random import randint

#criando função para criar ficha:
def criarficha(nomedaficha):

    ficha = open(f"{nomedaficha}.txt", "w+")
    while True:
        classe = input("qual a classe do seu personagem?(Guerreiro, assasino ou mago)").upper()
        if classe != "MAGO"  and classe != "GUERREIRO" and classe != "ASSASSINO":
            print("Selecione uma classe válida")
        else:
            break
    ficha.write(f"NOME: {nomedaficha}\nCLASSE: {classe}\nMANA:\n{randint(1, 20)}\nVIDA:\n{randint(1, 20)}\nCARISMA:\n{randint(1, 4)}\nARMA:\n{randint(1, 5)} (1 - espada 2 - adagas 3 - arco 4 - flecha 5 - cajado)\nFOME:\n{randint(1,4)}")
    ficha.close()
    print("ficha criada com sucesso!")
def mostrarficha(nomedaficha):
    ficha = open(f"{nomedaficha}.txt", "r")
    ficha2 = ficha.read()
    ficha.close()
    return ficha2
def modificarficha(nomedaficha, modificado):

    ficha = open(f"{nomedaficha}.txt", "r")
    moom = ficha.readlines()
    sos = moom.index(f"{modificado}:\n")
    novo = input(f"digite o novo valor de {modificado.lower()}: ")
    del moom[sos + 1]
    moom.insert(sos+1, novo+"\n")
    ficha = open(f"{nomedaficha}.txt", "w")
    moom2 = "".join(moom)
    ficha.write(moom2)
    ficha.close()







sus = int(input("Você deseja criar uma nova ficha ou importar uma ficha já criada?(1 - criar ficha/2 - entrar em uma existente)"))
nome = input("qual o nome do seu personagem?")
if sus == 1:
    criarficha(nome)
elif sus == 2:
    print(f"sua ficha está assim:\n{mostrarficha(nome)}")
    pergunta = int(input("Você gostaria de: Mudar a vida (1) // Mudar a mana (2) // Mudar a fome (3) // Salvar a ficha em um txt (4) // Jogar dado (5) // Sair (6) --->"))
    if pergunta == 1:
        modificarficha(nome, "VIDA")
    elif pergunta == 2:
        modificarficha(nome, "MANA")
    elif pergunta == 3:
        modificarficha(nome, "FOME")