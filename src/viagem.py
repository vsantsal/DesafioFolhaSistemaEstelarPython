#!/usr/bin/env python3.9
from typing import List
"""
Arquivo com classes relacionadas à viagem proposta
"""


class Nave:
    """
    classe Nave, que conterá a propriedade numero_de_passageiros (int)    
    """

    def __init__(self, numero_de_passageiros: int) -> None:
        self._numero_de_passageiros = numero_de_passageiros

    @property
    def numero_de_passageiros(self) -> int:
        return self._numero_de_passageiros


class SistemaEstelar:
    """
    classe SistemaEstelar, que conterá a propriedade estrelas (lista de strings)
    """

    def __init__(self, estrelas: List[str]) -> None:
        self._estrelas: List[str] = estrelas

    @property
    def estrelas(self):
        return self._estrelas
