# coding=utf-8

########################################################################################################################
####                                  Trabalho Inteligencia Artificial - Agentes de Busca                           ####
####                                  Aluno: Daniel Rosendo de Souza                                                ####
####                                  Professor: Ajalmar                                                            ####
####                                  Arquivo Classes - Arquivo que contém as classes do projeto                    ####
########################################################################################################################

class No(object):

    def __init__(self, estado, pai=None, custo_caminho=0, valor=None):
        self.estado = estado
        self.pai = pai

        if pai:
            self.action = pai.estado + " -> " + estado

        self.custo_caminho = custo_caminho
        self.valor = valor
        self.profundidade = 0

        if pai:
            self.profundidade = pai.profundidade + 1

    def __repr__(self):
        return self.estado + ", " + self.action

