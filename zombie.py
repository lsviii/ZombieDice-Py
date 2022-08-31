from time import sleep
import os
import random


def fazer_dado(cor, quantia):
    Dado = []
    if cor == "verde":
        for i in range(6):
            lados = "CPCTPC"
            Dado.append(cor)
            Dado.append(lados)
            sacola.append(Dado)
            Dado = []
    elif cor == "amarelo":
        for i in range(4):
            lados = "TPCTPC"
            Dado.append(cor)
            Dado.append(lados)
            sacola.append(Dado)
            Dado = []
    else:
        for i in range(3):
            lados = "TPTCPT"
            Dado.append(cor)
            Dado.append(lados)
            sacola.append(Dado)
            Dado = []

    return


def criar_dados():
    sacola = []
    fazer_dado("verde", 6)
    fazer_dado("amarelo", 4)
    fazer_dado("vermelho", 3)
    return


def remove_dado(dado_escolhido):
    sacola.remove(dado_escolhido)
    return


def sorteia_dado(quantia, dados_relanc):
    dado_pego = []
    utilizados_novamente = 0

    for dado_anterior in dados_relanc:
        if dado_anterior[1] == "P":
            if dado_anterior[0] == "verde":
                cor = "verde"
                lados = "CPCTPC"
            elif dado_anterior[0] == "amarelo":
                cor = "amarelo"
                lados = "TPCTPC"
            else:
                cor = "vermelho"
                lados = "TPTCPT"
            dado_pego.append([cor, lados])
            utilizados_novamente += 1

    for i in range(quantia - utilizados_novamente):
        dado_escolhido = (random.choice(sacola))
        dado_pego.append(dado_escolhido)
        remove_dado(dado_escolhido)

    return dado_pego


def jogar_dado(dados):
    sorteados = []
    resultado = []
    for dado in dados:
        face_sorteada = (random.choice(dado[1]))
        resultado = [dado[0], face_sorteada]
        sorteados.append(resultado)
    return sorteados


def mostra_resultado(dados_jogados):
    dados_relanc = []
    for dado in dados_jogados:
        if dado[0] == "verde":
            cor = 'verde'
        elif dado[0] == "amarelo":
            cor = "amarelo"
        else:
            cor = "vermelho"

        if dado[1] == "P":
            dados_relanc.append([cor, dado[1]])

        print(dado[1], cor)

    return dados_relanc


def atualiza_resultado(atualizar_jogador, dados_jogados):
    for dado in dados_jogados:
        if dado[1] == "T":
            atualizar_jogador[1] += 1
        elif dado[1] == "C":
            atualizar_jogador[2] += 1

        if atualizar_jogador[1] >= 3:
            if atualizar_jogador[3] == 0:
                atualizar_jogador[3] = 1
        elif atualizar_jogador[2] >= 13:
            print(
                atualizar_jogador[0], "13 PONTOS!!! Parabéns, comeu muitos cérebros, você venceu o jogo")
            exit

    return atualizar_jogador


def continuar_lancar(jogador):
    while True:
        resposta = int(input("Deseja jogar de novo? (1 - sim, 2 - não)"))
        if resposta < 0 or resposta > 2:
            print("Por favor digite 1 ou 2")
        else:
            if resposta == 2:
                print("Passou a vez")
                return 0
            else:
                return 1

    return


def placar(jogadores):
    print("\nJogador*********Tiros*********Cérebros\n")
    for jogador in jogadores:
        nome_do_jogador = jogador[0] + "            "
        print(nome_do_jogador[0:10], "      ",
              jogador[1], "      ", jogador[2])
    return


sacola = []
print("*********************************************** ZOMBIE DICE **********************************************\n")

while True:
    qnt_jogadores = int(input(
        "******************************** Qual a quantia de jogadores ente 2 e 99? ********************************\n(Digite 0 para sair do jogo!!!)"))
    if qnt_jogadores == 0:
        print("******************************** Você saiu do jogo!! ********************************")
        exit(0)
    elif qnt_jogadores < 2 or qnt_jogadores > 99:
        print("******************************** Digite um numero entre 2 e 99! ********************************")
    else:
        break

criar_dados()
jogadores = []
mortes = 0

for jogador in range(qnt_jogadores):
    passos = 0
    tiros = 0
    cerebros = 0
    morto = 0
    qnt = str(jogador + 1)
    nome = input("Jogador " + qnt + ": ")
    jogador = [nome, tiros, cerebros, morto]
    jogadores.append(jogador)

print("\n*************** QUE CEREBROS SEJAM DEVORADOS - BOM JOGO ***************\n")
for jogador in jogadores:
    print("Jogadores na Mesa: " + jogador[0])

i = 0
dados_novos = 3
dados_relanc = []
while True:
    if jogadores[i][3] == 0:
        print("\nÉ a vez do " + jogadores[i][0] + "\n")
        if mortes - 1 == 0:
            print("O Jogador " + jogadores[i][0] + "  Venceu\n")
            placar(jogadores)
            break
        input("PRESSIONE ENTER PARA JOGAR OS DADOS")
        dados_selecionados = sorteia_dado(dados_novos, dados_relanc)
        resultado_dado = jogar_dado(dados_selecionados)
        dados_relanc = mostra_resultado(resultado_dado)
        jogadores[i] = atualiza_resultado(
            jogadores[i], resultado_dado)
        placar(jogadores)

        if len(dados_relanc) + len(sacola) < 3:
            print("menos de 3 dados na bolsa")
            jogadores[i][1] = 0
            i += 1
            criar_dados()
            if i > (len(jogadores)-1):
                i = 0
        else:
            if jogadores[i][3] == 1:
                print("\n", jogadores[i][0], "Morreu!")
                i += 1
                mortes += 1
                criar_dados()
                if i > (len(jogadores) - 1):
                    i = 0
            else:
                if continuar_lancar(jogadores[i][0]) == 0:
                    jogadores[i][1] = 0
                    i += 1
                    criar_dados()
                    if i > (len(jogadores) - 1):
                        i = 0
    else:
        print(jogadores[i][0], "Morreu")
        i += 1
        criar_dados()
        if i > (len(jogadores) - 1):
            i = 0
