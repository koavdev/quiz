import os


# Criar um QUIZ de 10 PERGUNTAS
# 1 tentativa = 10 pts
# 2 tentativas = 5 pts
# Errou a 2 = 0 pts
# Mostrar a pontuação



perguntas = [
    ("Qual a numero vem primeiro?"),
    ("Qual o maior numero?"),
    ("Qual a raiz quadrada de 9?"),
    ("Qual não é um animal?"),
    ("1+1 = ?"),
    ("Qual não é uma cor?"),
    ("Qual a raiz quadrada de 9?"),
    ("Qual a riaz quadrada de 9?"),
    ("Qual a riaz quadrada de 9?"),
    ("Qual a riaz quadrada de 9")
]

respostas = [
    (0,2,1,4),
    (0,2,1,4),
    (5,2,3,1),
    ("Cachorro","Galo","Sapato","Porco"),
    (0,2,1,4),
    ("Azul", "Celular", "Vermelho", "Cinza"),
    (0,3,1,4),
    (0,3,1,4),
    (0,3,1,4),
    (0,3,1,4)
]

pontos = 0

attempts = 0


while True:
    os.system("cls")
    print("===============================")
    print("Seja bem-vindo ao Quiz UNIMAR!")
    print("===============================")

    print("\nComo funciona?")
    print("\nO quiz é composto por 10 perguntas e você possui 2 tentativas em cada resposta."
            +"\nSe acertar na 1ª tentativa: 10 PTS"
            +"\nSe acertar na 2ª tentaiva: 5 PTS"
            +"\nE se errar: 0 PTS" )

    print("\n\nVamos lá?")
    print("Aperte qualquer tecla para começar, ou 0 para sair")

    op = input()
    if op == "0":
        os.system("cls")
        print("Encerrando...")
        break
    

    
    os.system("cls")


    #Início do Quiz

    # Questão 1
    attempts = 0
    print("1 - {} ".format(perguntas[0]))

    print("\nEscolha uma alternativa:\n"
        +"a) {}\nb) {}\nc) {}\nd) {}\n".format(respostas[0][0], respostas[0][1], respostas[0][2], respostas[0][3]))
    
    #Validação das tentativas e respostas
    while attempts < 2:
        a1 = input("Resposta: ")
        if a1 == "a" and attempts == 0:    
            print("\nVocê acertou! + 10 PTS!\n\n")
            pontos = 10
            break
        elif a1 == "a" and attempts == 1:
            print("\n Você acertou! + 5 PTS! \n\n")
            pontos = 5
            break
        print("\nVocê errou, tente novamente!\n\n")
        attempts = attempts+1
    
    # Questão 2
    os.system("cls")
    attempts = 0
    print("2 - {} ".format(perguntas[1]))

    print("\nEscolha uma alternativa:\n"
        +"a) {}\nb) {}\nc) {}\nd) {}\n".format(respostas[1][0], respostas[1][1], respostas[1][2], respostas[1][3]))
    
    # Validação das tentativas e respostas
    while attempts < 2:
        a2 = input("Resposta: ")
        if a2 == "d" and attempts == 0:    
            print("\nVocê acertou! + 10 PTS!\n\n")
            pontos = pontos + 10
            break
        elif a2 == "d" and attempts == 1:
            print("\n Você acertou! + 5 PTS! \n\n")
            pontos = pontos + 5
            break
        print("\nVocê errou, tente novamente!\n\n")
        attempts = attempts+1

    # Questão 3  
    os.system("cls")
    attempts = 0
    print("3 - {} ".format(perguntas[2]))

    print("\nEscolha uma alternativa:\n"
        +"a) {}\nb) {}\nc) {}\nd) {}\n".format(respostas[2][0], respostas[2][1], respostas[2][2], respostas[2][3]))
    
    #Validação das tentativas e respostas
    while attempts < 2:
        a3 = input("Resposta: ")
        if a3 == "c" and attempts == 0:    
            print("\nVocê acertou! + 10 PTS!\n\n")
            pontos = pontos + 10
            break
        elif a3 == "c" and attempts == 1:
            print("\n Você acertou! + 5 PTS! \n\n")
            pontos = pontos + 5
            break
        print("\nVocê errou, tente novamente!\n\n")
        attempts = attempts+1

    # Questão 4
    os.system("cls")  
    attempts = 0
    print("4 - {} ".format(perguntas[3]))

    print("\nEscolha uma alternativa:\n"
        +"a) {}\nb) {}\nc) {}\nd) {}\n".format(respostas[3][0], respostas[3][1], respostas[3][2], respostas[3][3]))

    #Validação das tentativas e respostas
    while attempts < 2:
        a4 = input("Resposta: ")
        if a4 == "c" and attempts == 0:    
            print("\nVocê acertou! + 10 PTS!\n\n")
            pontos = pontos + 10
            break
        elif a4 == "c" and attempts == 1:
            print("\n Você acertou! + 5 PTS! \n\n")
            pontos = pontos + 5
            break
        print("\nVocê errou, tente novamente!\n\n")
        attempts = attempts+1

    # Questão 5
    os.system("cls")  
    attempts = 0
    print("5 - {} ".format(perguntas[4]))

    print("\nEscolha uma alternativa:\n"
        +"a) {}\nb) {}\nc) {}\nd) {}\n".format(respostas[4][0], respostas[4][1], respostas[4][2], respostas[4][3]))
    
    #Validação das tentativas e respostas
    while attempts < 2:
        a5 = input("Resposta: ")
        if a5 == "b" and attempts == 0:    
            print("\nVocê acertou! + 10 PTS!\n\n")
            pontos = pontos + 10
            break
        elif a5 == "b" and attempts == 1:
            print("\n Você acertou! + 5 PTS! \n\n")
            pontos = pontos + 5
            break
        print("\nVocê errou, tente novamente!\n\n")
        attempts = attempts+1

    # Questão 6  
    os.system("cls")
    attempts = 0
    print("6 - {} ".format(perguntas[5]))

    print("\nEscolha uma alternativa:\n"
        +"a) {}\nb) {}\nc) {}\nd) {}\n".format(respostas[5][0], respostas[5][1], respostas[5][2], respostas[5][3]))
    
    #Validação das tentativas e respostas
    while attempts < 2:
        a6 = input("Resposta: ")
        if a6 == "b" and attempts == 0:    
            print("\nVocê acertou! + 10 PTS!\n\n")
            pontos = pontos + 10
            break
        elif a6 == "b" and attempts == 1:
            print("\n Você acertou! + 5 PTS! \n\n")
            pontos = pontos + 5
            break
        print("\nVocê errou, tente novamente!\n\n")
        attempts = attempts+1

    # Questão 7  
    os.system("cls")
    attempts = 0
    print("7 - {} ".format(perguntas[6]))

    print("\nEscolha uma alternativa:\n"
        +"a) {}\nb) {}\nc) {}\nd) {}\n".format(respostas[6][0], respostas[6][1], respostas[6][2], respostas[6][3]))
    
    #Validação das tentativas e respostas
    while attempts < 2:
        a7 = input("Resposta: ")
        if a7 == "b" and attempts == 0:    
            print("\nVocê acertou! + 10 PTS!\n\n")
            pontos = pontos + 10
            break
        elif a7 == "b" and attempts == 1:
            print("\n Você acertou! + 5 PTS! \n\n")
            pontos = pontos + 5
            break
        print("\nVocê errou, tente novamente!\n\n")
        attempts = attempts+1

    # Questão 8  
    os.system("cls")
    attempts = 0
    print("8 - {} ".format(perguntas[7]))

    print("\nEscolha uma alternativa:\n"
        +"a) {}\nb) {}\nc) {}\nd) {}\n".format(respostas[7][0], respostas[7][1], respostas[7][2], respostas[7][3]))

    #Validação das tentativas e respostas
    while attempts < 2:
        a8 = input("Resposta: ")
        if a8 == "b" and attempts == 0:    
            print("\nVocê acertou! + 10 PTS!\n\n")
            pontos = pontos + 10
            break
        elif a8 == "b" and attempts == 1:
            print("\n Você acertou! + 5 PTS! \n\n")
            pontos = pontos + 5
            break
        print("\nVocê errou, tente novamente!\n\n")
        attempts = attempts+1

    # Questão 9 
    os.system("cls")
    attempts = 0
    print("9 - {} ".format(perguntas[8]))

    print("\nEscolha uma alternativa:\n"
        +"a) {}\nb) {}\nc) {}\nd) {}\n".format(respostas[8][0], respostas[8][1], respostas[8][2], respostas[8][3]))
    
    #Validação das tentativas e respostas
    while attempts < 2:
        a9 = input("Resposta: ")
        if a9 == "b" and attempts == 0:    
            print("\nVocê acertou! + 10 PTS!\n\n")
            pontos = pontos + 10
            break
        elif a9 == "b" and attempts == 1:
            print("\n Você acertou! + 5 PTS! \n\n")
            pontos = pontos + 5
            break
        print("\nVocê errou, tente novamente!\n\n")
        attempts = attempts+1

    # Questão 10 
    os.system("cls")
    attempts = 0 
    print("10 - {} ".format(perguntas[9]))

    print("\nEscolha uma alternativa:\n"
        +"a) {}\nb) {}\nc) {}\nd) {}\n".format(respostas[9][0], respostas[9][1], respostas[9][2], respostas[9][3]))

    #Validação das tentativas e respostas
    while attempts < 2:
        a10 = input("Resposta: ")
        if a10 == "b" and attempts == 0:    
            print("\nVocê acertou! + 10 PTS!\n\n")
            pontos = pontos + 10
            break
        elif a10 == "b" and attempts == 1:
            print("\n Você acertou! + 5 PTS! \n\n")
            pontos = pontos + 5
            break
        print("\nVocê errou, tente novamente!\n\n")
        attempts = attempts+1
    
    # Resultado final
    os.system("cls")
    if pontos < 25:
        print("Você fez {} pontos! Péssimo!".format(pontos))
    elif pontos < 50:
        print("Você fez {} pontos! Regular!".format(pontos))
    elif pontos < 75:
        print("Você fez {} pontos! Bom!".format(pontos))
    elif pontos < 100:
        print("Você fez {} pontos! Ótimo!".format(pontos))    
    elif pontos == 100:
        print("Você fez {} pontos! Excelente!".format(pontos))
    
    
    
    
    print("\n\n")
    print("[0] - Voltar para o Início")
    if int(input()) != 0:
        break