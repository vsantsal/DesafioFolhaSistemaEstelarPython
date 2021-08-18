import unittest

from src.viagem import (
    Nave,
    SistemaEstelar,
)


class TestNave(unittest.TestCase):
    def test_nave_possui_numero_de_passageiros_passado_ao_construtor(self):
        for num in range(100):
            nave = Nave(num)
            self.assertEqual(num, nave.numero_de_passageiros)


class TestSistemaEstelar(unittest.TestCase):
    def test_sistema_estelar_retorna_lista_de_estrelas_passadas(self):
        estrelas = ['SIRIUS', 'LALANDE', 'PROCION', 'ALPHA CENTAURI', 'BARNARD']
        sistema = SistemaEstelar(estrelas)
        self.assertEqual(
            estrelas,
            sistema.estrelas
        )
