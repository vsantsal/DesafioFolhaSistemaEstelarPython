from math import prod

"""
Classe responsável em que se a regra de negócio RN1 para descobrir o destino
da espaçonave está definida

RN1:O local de chegada pode ser conhecido sabendo que as vogais do nome da estrela 
são atribuídas à uma sequência Fibonacci que começa em 1 e termina em 8, 
onde A = 1, E = 2, I = 3, O = 5 e U = 8. 
Se a multiplicação das vogais der o mesmo número 
que a quantidade de engenheiros, a estrela de destino será conhecida.

"""

class Balanca:
    def compara(self, valor, peso):
        # função que compara duas variáveis e retorna o booleano da comparação
        return valor == peso

class Calculadora:
        
        def calcula(self, nome):
            
            # converte a string fornecida em lista de inteiros
            lista_a_multiplicar = self.converte_nome_em_lista_de_inteiros(nome)

            # multiplica os elementos da lista de inteiros
            resultado = self.multiplica_itens_de_lista_de_inteiros(lista_a_multiplicar)

            return resultado

        def multiplica_itens_de_lista_de_inteiros(self, lista_de_inteiros):
            # multiplica os elementos da lista de inteiros           
            return prod(lista_de_inteiros)

        def converte_nome_em_lista_de_inteiros(self, nome):
            # inicializa lista para armazenar inteiros
            resultado = []

            for letra in nome:
                # para cada letra, converter em número por RN1
                resultado.append(self.converte_letra_em_inteiro(letra))

            return resultado

        # conversão das letras em números conforme RN1
        def converte_letra_em_inteiro(self, letra):
            if letra.lower() in 'aeiou':       
                if letra.lower() == 'a':
                    return 1  
                elif letra.lower() == 'e':
                    return 2
                elif letra.lower() == 'i':
                    return 3
                elif letra.lower() == 'o':
                    return 5
                elif letra.lower() == 'u':
                    return 8
            else:
                return 1