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

def criarficha(nomedaficha):
    open(f"{nomedaficha}.txt", "w+")


sus = int(input("Você deseja criar uma nova ficha ou importar uma ficha já criada?(1 - criar ficha/2 - entrar em uma existente)"))
nome = input("qual o nome do seu personagem?")
if sus == 1:
    criarficha(nome)