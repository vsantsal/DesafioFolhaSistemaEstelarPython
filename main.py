from avaliador import Avaliador

"""
Levados do planeta Terra por uma nave alienígena, um grupo de 75 engenheiros 
espera saber qual será o seu destino solucionando um enigma proposto pelos seus 
novos amigos. As informações que receberam dizem que a espaçonave seguirá pelo espaço 
até atingir um de cinco sistemas estelares próximos: 
SIRIUS, LALANDE, PROCION, ALPHA CENTAURI ou BARNARD.


O local de chegada pode ser conhecido sabendo que as vogais do nome da estrela 
são atribuídas à uma sequência Fibonacci que começa em 1 e termina em 8, 
onde A = 1, E = 2, I = 3, O = 5 e U = 8. 
Se a multiplicação das vogais der o mesmo número 
que a quantidade de engenheiros, a estrela de destino será conhecida.


Qual estrela será o destino da espaçonave?
"""

def main():    

    # solicitamos a um dos engenheiros para ser o avaliador
    engenheiro = Avaliador()

    # engenheiro avalia e retorna sua avaliação
    avaliacao = engenheiro.avalia()

    # avaliação é retornada na tela
    print(f"A estrela destino da espaçonave será {avaliacao}")

# se algum erro ocorrer, retorna o erro na tela
try:
    main()
except Exception as e:    
    print(e)