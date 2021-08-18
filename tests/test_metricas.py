import unittest

from src.metricas import (
    Balanca,
    Calculadora
)


class TestBalanca(unittest.TestCase):
    def test_balanca_compara_objetos_que_implementam_eq(self):
        lista_de_objetos_comparaveis = [(1, 2), (1.0, 1), ('a', 2),
                                        ('abc', 'ABC'), (20, 20)]
        for obj1, obj2 in lista_de_objetos_comparaveis:
            comparacao: bool = Balanca.compara(obj1, obj2)
            self.assertEqual(
                obj1 == obj2,
                comparacao
            )


class TestCalculadora(unittest.TestCase):
    def setUp(self) -> None:
        self.calculadora: Calculadora = Calculadora()

    def test_calculadora_retorna_inteiro_conforme_regra(self):
        lista_de_palavras_resultados = [('TestE', 4),
                                        ('KakAroto', 25),
                                        ('oásis', 15)]
        for palavra, resultado_esperado in lista_de_palavras_resultados:
            resultado_obtido: int = self.calculadora.calcula(palavra)
            self.assertEqual(resultado_esperado, resultado_obtido)
