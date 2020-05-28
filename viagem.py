"""
Arquivo com classes relacionadas à viagem proposta
"""

class Nave:
    """
    classe Nave, que conterá a propriedade numero_de_passageiros (int)    
    """
    def __init__(self):
        self.numero_de_passageiros = 75
    
    def get_numero_de_de_passageiros(self):
        return self.numero_de_passageiros

class SistemaEstelar:
    """
    classe SistemaEstelar, que conterá a propriedade estrelas (lista de strings)
    """
    def __init__(self):
        self.estrelas = ['SIRIUS', 'LALANDE',
                         'PROCION', 'ALPHA CENTAURI',
                         'BARNARD']
    
    def get_estrelas(self):
        return self.estrelas