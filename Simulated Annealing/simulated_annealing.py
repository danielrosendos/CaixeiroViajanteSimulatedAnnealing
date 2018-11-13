import random
import numpy as np
from classes import No
import math

subValue = lambda l, i, v: l[:i] + [v] + l[i + 1:]
f = lambda S: funcCusto(S)

def funcCusto(estado):
    count = 0
    tam = len(estado)
    a = [x + estado[x] for x in range(tam)]
    b = [x - estado[x] for x in range(tam)]
    for i in range(tam - 1):
        for j in range(i + 1, tam):
            if estado[i] == estado[j]:
                count += 1
            if a[i] == a[j]:
                count += 1
            if b[i] == b[j]:
                count += 1
    return count

def randomSuccerssor(atual):
    aux = [x for x in atual.estado]
    tam = len(aux)
    sucessor = []

    for i in range(tam):
        l = [x for x in range(tam) if not aux[i] == x]

        for j in l:
            k = subValue(aux, i, j)
            sucessor.append(k)

    estado = random.choice(sucessor)
    custo = funcCusto(estado)
    no = No(estado=estado, valor=custo)

    return no

def recozimentoSimulado(estadoInicial, numeroDeIteracoes=1000, pertubacoes=100, sucessos=10, alpha=0.99):
    inicio = estadoInicial
    t0 = temperaturaInicial()
    j = 1
    print ("Temperatura inicial: {}".format(t0))
    numSucesso = 1
    while (numSucesso != 0) and (j <= numeroDeIteracoes):
        i = 1
        numSucesso = 0
        while (numSucesso < sucessos) and (i <= pertubacoes):
            novoEstado = Pertuba(inicio)
            deltaFi = f(novoEstado) - f(inicio)
            if deltaFi <= 0 or math.exp(-deltaFi/t0) > Randomiza():
                inicio = novoEstado
                numSucesso += 1
            i += 1
        t0 = alpha * t0
        j = j + 1

    print ("Iteracao: " + str(j) + "| Temperatura: " + str(t0))
    print ("Estado: {}".format(str(inicio)) + " | " + "Iteracao: {}".format(j) + " | " + "Ataques: {}".format(funcCusto(inicio)))
    print ("Numero de Sucessos: " + str(numSucesso))

    return inicio



def temperaturaInicial():
    return random.randint(50, 100)

def Pertuba(inicio):
    S = No(inicio)
    return randomSuccerssor(S).estado

def Randomiza():
    return random.random()

def estadoInicialRandomico(tamanhoDoTabuleiro = 4):
    rainhaProblem = []

    for i in range(tamanhoDoTabuleiro):
        rainhaProblem.append(random.randint(0, tamanhoDoTabuleiro - 1))

    return rainhaProblem

def salvarTabuleiro(tabuleiro, url='board.txt'):
    file = open(url, 'w')
    baseTabuleiro = np.zeros((len(tabuleiro), len(tabuleiro))).astype(int)

    for c in range(len(baseTabuleiro)):
        baseTabuleiro[tabuleiro[c]][c] = 1

    for l in range(len(baseTabuleiro)):
        for c in range(len(baseTabuleiro)):
            file.write(str(baseTabuleiro[l][c]) + "\t")
        file.write("\n")

    return baseTabuleiro


