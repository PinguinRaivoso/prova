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
#criando função para mostrar a ficha
def mostrarficha(nomedaficha):
    ficha = open(f"{nomedaficha}.txt", "r")
    ficha2 = ficha.read()
    ficha.close()
    return ficha2
#função para modificar a ficha
def modificarficha(nomedaficha, modificado):
    while True:
        ficha = open(f"{nomedaficha}.txt", "r")
        moom = ficha.readlines()
        sos = moom.index(f"{modificado}:\n")
        novo = input(f"digite o novo valor de {modificado.lower()}: ")
        if modificado == "MANA" and int(novo) <= 20:
            pass
        elif modificado == "FOME" and int(novo) <= 4:
            pass
        elif modificado == "VIDA" and int(novo) <= 20:
            pass
        else:
            print("Use um valor até 20 para vida e mana e 4 para fome.")
            continue
        del moom[sos + 1]
        moom.insert(sos + 1, novo + "\n")
        ficha = open(f"{nomedaficha}.txt", "w")
        moom2 = "".join(moom)
        ficha.write(moom2)
        ficha.close()
        break
#função para copiar para um txt
def copiandparaumnovotxt(nomezin, nomezo):
    ficha = open(f"{nomezin}.txt", "r")
    sos = ficha.read()
    ficha2 = open(f"{nomezo}.txt", "w+")
    ficha2.write(sos)
    ficha.close()
    ficha2.close()
#criando um def que verifica se a fome/vida/mana estão em 0
def verificando(nome):
    ficha = open(f"{nome}.txt", "r")
    ficha2 = ficha.readlines()
    ficha.close()
    if int(ficha2[5]) <= 0:
        print("=-"*30, "\n")
        print("sua vida está em 0")
    elif int(ficha2[3]) <= 0:
        print("=-" * 30, "\n")
        print("EMTER21ALMERT!!1!sua mana está em 0")
    elif int(ficha2[11]) <= 0:
        print("=-" * 30, "\n")
        print("EMTER21ALMERT!!1!sua fome está em 0")

while True:
    try:
        #perguntando se ele quer entrar em uma ficha ou criar uma
        sus = int(input("Você deseja criar uma nova ficha ou importar uma ficha já criada?(1 - criar ficha/2 - entrar em uma existente)"))
        nome = input("qual o nome do seu personagem?")
        if sus == 1:
            criarficha(nome)
        elif sus == 2:
            #fazendo um sistema para selecionar o que a pessoa quer mudar.
            while True:
                print(f"sua ficha está assim:\n{mostrarficha(nome)}")
                verificando(nome)
                print("=-"*30)
                pergunta = int(input("Você gostaria de: Mudar a vida (1) // Mudar a mana (2) // Mudar a fome (3) // Salvar a ficha em um txt (4) // Jogar dado (5) // Sair (6) --->"))
                if pergunta == 1:
                    modificarficha(nome, "VIDA")
                elif pergunta == 2:
                    modificarficha(nome, "MANA")
                elif pergunta == 3:
                    modificarficha(nome, "FOME")
                elif pergunta == 4:
                    copiandparaumnovotxt(nome, input("digite o nome do arquivo novo"))
                elif pergunta == 5:
                    t = int(input("quantos lados tem o dado?"))
                    t2 = int(input("quantos dados você ques jogar?"))
                    for _ in range(0, t2):
                        print(f"O dado deu: {randint(1, t)}")
                elif pergunta == 6:
                    exit()
                else:
                    print(" digite um número válido")
                    continue

    except FileNotFoundError:
        print("Esse personagem não existe, tente novemente ou crie um!")
    except ValueError:
        print("Use um número.")

