import tamanho_vetor
import normalizar_vetor
import soma_vetor
import subtrair_vetor
import multiplicar_escalar
import divisao_escalar
import produto_escalar_de_vetores
import ler_vetor


def menu():
    print("Opcẽos: ")
    print(
        '''
        (1) Calcular o tamanho do vetor;
        (2) Normalizar o vetor, apresentando o vetor resultante da normalização;
        (3) Adicionar outro vetor ao que foi lido anteriormente, lendo os valores x, y e z deste novo vetor;
        (4) Subtrair outro vetor ao que foi lido anteriormente, lendo os valores x, y e z deste novo vetor;
        (5) Ler o valor de um escalar e realizar a multiplicação do mesmo pelo vetor, mostrando o vetor resultante;
        (6) Ler o valor de um escalar e realizar a divisão do mesmo pelo vetor, mostrando o vetor resultante;
        (7) Calcular o produto escalar do vetor lido anteriormente por outro vetor, lendo os valores x, y e z deste novo vetor e mostrando o resultado na tela.
        (0) Para sair'''

        
    )
    op = int(input('Ler a Opção: '))
    while(op != 0):

        if op == 1:
            res = tamanho_vetor.calcula_vetor(ler_vetor.informar_vetor())
        if op == 2:
            res = normalizar_vetor.normalizar(ler_vetor.informar_vetor())
        if op == 3:
            res = soma_vetor.somar(ler_vetor.informar_vetor())
        if op == 4:
            res = subtrair_vetor.subtrair(ler_vetor.informar_vetor())
        if op == 5:
            res = multiplicar_escalar.multiplicar_escalar(ler_vetor.informar_vetor())
        if op == 6:
            res = divisao_escalar.dividir_escalar(ler_vetor.informar_vetor())
        if op == 7:
            res = produto_escalar_de_vetores.produto_escalar(ler_vetor.informar_vetor())


        print("resposta : \n",res)
        op = int(input('Ler a Opção: '))
            

menu()