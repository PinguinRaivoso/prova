#criando uma função que checa os 3 ultimos dígitos e subtrai de acordo com eles
def coisinha(coisa, numero):
    global t
    global no
    global romano2
    if romano2[t] == coisa:
        if t == -1:
            pass
        else:
            no -= numero
            if romano2[t - 1] == coisa:
                if t - 1 < 0:
                    pass
                else:
                    no -= numero
                    if romano2[t - 2] == coisa:
                        if t - 2 < 0:
                            pass
                        else:
                            no -= numero
                            if romano2[t - 3] == coisa:
                                if t - 3 < 0:
                                    pass
                                else:
                                    print(f"não use {coisa} mais que 3 vezes")
                                    exit()
while True:
    try:
        index = 0
        romano = input('digite o número romano que deseja traduzir: ').upper()
        romano2 = list()
        no = 0
        #transformando a variavel em uma array
        for x in romano:
            romano2.append(x)
        #traduzindo dos numeros romanos
        for a in romano2:
            t = index - 1
            #adicionando o número 1
            if a == "I":
                no += 1
            #adicionando o número 5
            elif a == "V":
                no += 5
                coisinha("I", 2)
            #adicionando o número 10
            elif a == "X":
                no += 10
                coisinha("I", 2)
                if romano2[t] == "V":
                    if t == -1:
                        pass
                    else:
                        print("não use VX nos números, vá do maior pro menor.")
                        exit()
            #adicionando o número 50
            elif a == "L":
                no += 50
                coisinha("I", 2)
                coisinha("V", 10)
                coisinha("X", 20)
            #adicionando o número 100
            elif a == "C":
                no += 100
                coisinha("I", 2)
                coisinha("V", 10)
                coisinha("X", 20)
            #adicionando o número 500
            elif a == "D":
                no += 500
                coisinha("I", 2)
                coisinha("V", 10)
                coisinha("X", 20)
            #adicionando o número 1000
            elif a == "M":
                no += 1000
                coisinha("I", 2)
                coisinha("V", 10)
                coisinha("X", 20)
            else:
                print("use letras pertencentes aos numeros romanos: I V X L C D M")
                exit()
            if a.isnumeric():
                print("use apenas letras")
                exit()
            index += 1
        print(no)
    except Exception:
        print("comando iválido, tente novamente.")
        exit()
    break