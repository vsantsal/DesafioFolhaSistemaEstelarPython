#!/usr/bin/env python3.9
"""
Classe responsável por executar a regra de negócio RN1 para descobrir o destino
da espaçonave

RN1:O local de chegada pode ser conhecido sabendo que as vogais do nome da estrela 
são atribuídas à uma sequência Fibonacci que começa em 1 e termina em 8, 
onde A = 1, E = 2, I = 3, O = 5 e U = 8. 
Se a multiplicação das vogais der o mesmo número 
que a quantidade de engenheiros, a estrela de destino será conhecida.

"""

from typing import List

from src.metricas import Balanca, Calculadora
from src.viagem import Nave, SistemaEstelar


class Avaliador:

    @staticmethod
    def avalia(numero_de_passageiros: int, relacao_estrelas: List[str]):
        # instanciando a nave do problema
        nave = Nave(numero_de_passageiros=numero_de_passageiros)

        # instanciando o sistema estelar do problema
        sistema_estelar = SistemaEstelar(estrelas=relacao_estrelas)

        # instanciando a Calculadora para avaliação
        calculadora = Calculadora()

        # instanciando a Balança
        balanca = Balanca()
        
        for estrela in sistema_estelar.estrelas:

            # para cada elemento da lista de destino, comparar com o número de passageiros n
            # retorna o nome da estrela cujo processamento pela RN1 é igual a n
            if balanca.compara(calculadora.calcula(estrela), nave.numero_de_passageiros):
                return estrela        
