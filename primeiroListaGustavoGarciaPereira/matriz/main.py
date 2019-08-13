import ler_matriz
import adicao_subutra
import multiplicacoa_divisao_por_escalar
import multiplicacao_divisao_por_vetor
import multiplicao_divisao_matriz_por_matriz

def menu():
    print("Opcẽos: ")
    print(
        '''
            :: Operacao entro matrizes :: 
            
            (1) Adicao Matriz por Matriz
            (2) Subtracao Matriz por Matriz
            (3) Multiplicao Matriz por escalar
            (4) Divisao Matriz por escalar
            (5) Multiplicao Matriz por vetor
            (6) Divisao Matriz por vetor
            (7) Multiplicao Matriz por Matriz
            (8) Divisao Matriz por Matriz         
        '''

        
    )
    op = int(input('Ler a Opção: '))
    while(op != 0):

        if op == 1:
            res = adicao_subutra.adicao(ler_matriz.ler_matriz())
        if op == 2:
            res = adicao_subutra.subtracao(ler_matriz.ler_matriz())
        if op == 3:
            res = multiplicacoa_divisao_por_escalar.muntiplicao(ler_matriz.ler_matriz())
        if op == 4:
            res = multiplicacoa_divisao_por_escalar.divisao(ler_matriz.ler_matriz())
        if op == 5:
            res = multiplicacao_divisao_por_vetor.muntiplicao(ler_matriz.ler_matriz())
        if op == 6:
            res = multiplicacao_divisao_por_vetor.divisao(ler_matriz.ler_matriz())
        if op == 7:
            res = multiplicao_divisao_matriz_por_matriz.multiplicacao(ler_matriz.ler_matriz())
        if op == 8:
            res = multiplicao_divisao_matriz_por_matriz.divisao(ler_matriz.ler_matriz())


        print("resposta : \n",res)
        op = int(input('Ler a Opção: '))


menu()