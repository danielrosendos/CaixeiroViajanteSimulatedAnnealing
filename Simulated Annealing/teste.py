# -*- coding: utf-8 -*-
from simulated_annealing import recozimentoSimulado, estadoInicialRandomico, salvarTabuleiro

def main():

    tamanhoDoTabuleiro = int(input("\tDefinir tamanho do tabuleiro (Exemplo : 4, 5, 6...) :  "))

    if tamanhoDoTabuleiro < 4:
        tamanhoDoTabuleiro = 4
        print ("\t\tO valor mínimo é 4")

    estado_inicial = estadoInicialRandomico(tamanhoDoTabuleiro)

    inicio = salvarTabuleiro(estado_inicial)

    print ("Estado inicial \n" + str(inicio))

    estado = recozimentoSimulado(estado_inicial, numeroDeIteracoes=1000, pertubacoes=100, sucessos=10, alpha=0.99)

    tabuleiro = salvarTabuleiro(estado)

    print ("Estado Final \n" + str(tabuleiro))

if __name__ == "__main__":
    main()
