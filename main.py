import numpy as np
import os

def Menu():
    os.system('cls')
    
    print('=================================')
    print('SISTEMA DE MATRIZES')
    print('=================================')
    print('1. Lei de Formação de Matrizes')
    print('2. Multiplicação Escalar de Matriz')
    print('3. Produto de Matrizes')
    print('4. Sair')

    op = int(input("Escolha uma opção -> "))

    if op == 1:
        Formacao_De_Matrizes()
    elif op == 2:
        Multiplicacao_Escalar_De_Matriz()
    elif op == 3:
        Produto_De_Matrizes()
    elif op == 4:
        print('Saindo...')
        exit()
    else:
        print("Opção inválida. Tente novamente.\n")
        Menu()

# FUNÇÃO DE FORMAÇÃO DE MATRIZES ------------------------------------------------------------------------------------
def Formacao_De_Matrizes():
    print('=================================')
    print('LEI DE FORMAÇÃO DE MATRIZES')
    print('=================================')

    print('Escolha o tipo de Matriz:\n1. Matriz Retângular\n2. Matriz Quadrada')
    opTamanho = int( input('Escolha uma opção -> ') )

    if opTamanho == 1:
        nLinha = int( input('Digite o número de linhas da Matriz: ') )
        nColuna = int( input('Digite o número de colunas da Matriz: ') )

        matriz = np.zeros((nLinha, nColuna), dtype=int)

        for l in range(nLinha):
            for c in range(nColuna):
                i = l + 1
                j = c + 1

                if i == j:
                    numero = i ** 2 + j
                else:
                    numero = i - 2 * j
                matriz[l][c] = numero
        
    elif opTamanho == 2:
        n = int( input("Digite o tamanho da matriz (Quadrada): ") )

        matriz = np.zeros((n, n), dtype=int)

        for l in range(n): 
            for c in range(n):
                i = l + 1
                j = c + 1

                if i == j:
                    numero = i ** 2 + j
                else:
                    numero = i - 2 * j
                matriz[l][c] = numero

    else:
        print("Opção inválida. Tente novamente.\n")
        Formacao_De_Matrizes()

    print("\nMatriz resultante:")
    for linha in matriz:
        print(linha)

    input("\nPressione Enter para voltar ao menu.")
    Menu()

# FUNÇÃO DE MULTIPLICAÇÃO ESCALAR DE MATRIZES -----------------------------------------------------------------------
def Multiplicacao_Escalar_De_Matriz():
    print('=================================')
    print('MULTIPLICAÇÃO ESCALAR DE MATRIZES')
    print('=================================')

    print('Escolha o tipo de Matriz:\n1. Matriz Retângular\n2. Matriz Quadrada')
    opTamanho = int( input('Escolha uma opção -> ') )

    if opTamanho == 1:
        # Matriz Retângular
        nLinha = int( input('Digite o número de linhas da Matriz: ') )
        nColuna = int( input('Digite o número de colunas da Matriz: ') )
        multi = int(input("Digite o valor do multiplicador: "))

        matriz = np.zeros((nLinha, nColuna), dtype=int)

        for l in range(nLinha):
            for c in range(nColuna):
                i = l + 1
                j = c + 1
                numero = int(input(f'Digite o número na posição {i},{j}: '))
                matriz[l][c] = numero * multi

    elif opTamanho == 2:
        # Matriz Quadrada
        n = int(input("Digite o tamanho da matriz (Quadrada): "))
        multi = int(input("Digite o valor do multiplicador: "))

        matriz = np.zeros((n, n), dtype=int)

        for l in range(n): 
            for c in range(n):
                i = l + 1
                j = c + 1
                numero = int(input(f'Digite o número na posição {i},{j}: '))
                matriz[l][c] = numero * multi
    else:
        print("Opção inválida. Tente novamente.\n")
        Formacao_De_Matrizes()

    print("\nMatriz resultante:")
    for linha in matriz:
        print(linha)

    input("\nPressione Enter para voltar ao menu.")
    Menu()

# PRODUTO DE MATRIZES -----------------------------------------------------------------------------------------------
def Produto_De_Matrizes():
    print('=================================')
    print('PRODUTO DE MATRIZES')
    print('=================================')
    print('OBS: PARA O CÁLCULO É NECESSÁRIO A MATRIZ TER O MESMO NÚMERO DE LINHA PARA A COLUNA DA OUTRA E VICE-VERSA')

    print('Escolha o tipo de Matriz:\n1. Matriz Retângular\n2. Matriz Quadrada')
    opTamanho = int( input('Escolha uma opção -> ') )

    if opTamanho == 1:
        # Matriz Retângular A
        nALinha = int( input('Digite o número de linhas da Matriz A: ') )
        nAColuna = int( input('Digite o número de colunas da Matriz A: ') )

        matA = np.zeros((nALinha, nAColuna), dtype=int)

        for l in range(nALinha):
            for c in range(nAColuna):
                i = l + 1
                j = c + 1
                numero = int(input(f'Digite o número na posição {i},{j} da Matriz A: '))
                matA[l][c] = numero

        # Matriz Retângular B
        nBLinha = int(input('\nDigite o número de linhas da Matriz B: ') )
        nBColuna = int(input('Digite o número de colunas da Matriz B: ') )

        matB = np.zeros((nBLinha, nBColuna), dtype=int)

        for l in range(nBLinha):
            for c in range(nBColuna):
                i = l + 1
                j = c + 1
                numero = int(input(f'Digite o número na posição {i},{j} da Matriz B: '))
                matB[l][c] = numero

        # Produto das matrizes Retângulares
        if nALinha == nBColuna:
            matC = np.zeros((nALinha, nBColuna), dtype=int)
            for l in range(nALinha):
                for c in range(nBColuna):
                    for k in range(nAColuna):
                        matC[l][c] += matA[l][k] * matB[k][c]

        elif nAColuna == nBLinha:
            matC = np.zeros((nAColuna, nBLinha), dtype=int)
            for c in range(nAColuna):
                for l in range(nBLinha):
                    for k in range(nALinha):
                        matC[c][l] += matA[c][k] * matB[k][l]

        else:
            print("As matrizes não podem ser multiplicadas. Tente novamente.\n")
            Produto_De_Matrizes()

    elif opTamanho == 2:
        # Matriz Quadrada
        n1 = int( input('Digite o tamanho da matriz A e B (Quadrada): ') )
        n2 = n1

        # Matriz Quadrada A
        matA = np.zeros((n1, n1), dtype=int)
        for l in range(n1):
            for c in range(n1):
                i = l + 1
                j = c + 1
                numero = int(input(f'Digite o número na posição {i},{j} da matriz A: '))
                matA[l][c] = numero

        # Matriz Quadrada B
        matB = np.zeros((n2, n2), dtype=int)
        for l in range(n2):
            for c in range(n2):
                i = l + 1
                j = c + 1
                numero = int(input(f'Digite o número na posição {i},{j} da matriz B: '))
                matB[l][c] = numero

        # Produto das matrizes Quadradas
        matC = np.zeros((n1, n2), dtype=int)
        for l in range(n1):
            for c in range(n2):
                for k in range(n1):
                    matC[l][c] += matA[l][k] * matB[k][c]

    print("\nMatriz resultante:")
    for linha in matC:
        print(linha)

    input("\nPressione Enter para voltar ao menu.")
    Menu()
Menu()
