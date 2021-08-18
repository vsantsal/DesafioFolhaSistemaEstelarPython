#!/usr/bin/env python3.9

from functools import reduce
from operator import mul
from typing import (
    Any,
    Dict,
    List,
    Protocol,
    TypeVar,
)

"""
Classe responsável em que se a regra de negócio RN1 para descobrir o destino
da espaçonave está definida

RN1:O local de chegada pode ser conhecido sabendo que as vogais do nome da estrela 
são atribuídas à uma sequência Fibonacci que começa em 1 e termina em 8, 
onde A = 1, E = 2, I = 3, O = 5 e U = 8. 
Se a multiplicação das vogais der o mesmo número 
que a quantidade de engenheiros, a estrela de destino será conhecida.

"""


class Comparavel(Protocol):
    def __eq__(self, other: Any) -> bool: ...


CT = TypeVar('CT', bound=Comparavel)


class Balanca:
    @staticmethod
    def compara(valor: CT, peso: CT):
        # função que compara duas variáveis e retorna o booleano da comparação
        return valor == peso


class Calculadora:
    _MAPA_DE_VALORES: Dict[str, int] = {
        'a': 1,
        'e': 2,
        'i': 3,
        'o': 5,
        'u': 8
    }

    def calcula(self, nome):
        # converte a string fornecida em lista de inteiros
        lista_a_multiplicar = self._converte_nome_em_lista_de_inteiros(nome)

        # multiplica os elementos da lista de inteiros
        resultado = reduce(mul, lista_a_multiplicar)

        return resultado

    def _converte_nome_em_lista_de_inteiros(self, nome: str) -> List[int]:
        # inicializa lista para armazenar inteiros
        resultado = [self._MAPA_DE_VALORES.get(letra.lower(),
                                               1)
                     for letra in nome]
        return resultado
