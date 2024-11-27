import numpy as np
import os

def Menu():
    os.system('cls')
    
    print('=================================')
    print('SISTEMA DE MATRIZES')
    print('=================================')
    print('1. Lei de Formação de Matrizes')
    print('2. Multiplicação Escalar de Matriz')
    print('3. Produto de Matrizes (Em desenvolvimento)')
    print('4. Sair')

    op = int(input("Escolha uma opção -> "))

    if op == 1:
        Formacao_De_Matrizes()
    elif op == 2:
        Multiplicacao_Escalar_De_Matriz()
    elif op == 3:
        print("Função Produto de Matrizes ainda não implementada.")
    elif op == 4:
        print('Saindo...')
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        Menu()

# FUNÇÃO DE FORMAÇÃO DE MATRIZES ------------------------------------------------------------------------------------
def Formacao_De_Matrizes():
    print('=================================')
    print('LEI DE FORMAÇÃO DE MATRIZES')
    print('=================================')

    n = int(input("Digite o tamanho da matriz (Quadrada): "))

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

    n = int(input("Digite o tamanho da matriz (Quadrada): "))
    multi = int(input("Digite o valor do multiplicador: "))

    matriz = np.zeros((n, n), dtype=int)

    for l in range(n): 
        for c in range(n):
            i = l + 1
            j = c + 1
            numero = int(input(f'Digite o número na posição {i},{j}: '))
            matriz[l][c] = numero * multi

    print("\nMatriz resultante:")
    for linha in matriz:
        print(linha)

    input("\nPressione Enter para voltar ao menu.")
    Menu()

# PRODUTO DE MATRIZES -----------------------------------------------------------------------------------------------
def Produto_De_Matrizes():
    print('=================================')
    print('PRODUTO DE MATRIZES (EM DESENVOLVIMENTO)')
    print('=================================')
    n1 = int( input('Digite o tamanho da matriz A e B(Quadrada): ') )
    n2 = n1

    # Matriz A
    matA = np.zeros((n1, n1), dtype=int)
    for l in range(n1):
        for c in range(n1):
            i = l + 1
            j = c + 1
            numero = int(input(f'Digite o número na posição {i},{j} da matriz A: '))
            matA[l][c] = numero
Menu()
