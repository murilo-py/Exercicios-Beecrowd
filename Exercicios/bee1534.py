'''
Leia um valor inteiro N que é o tamanho da matriz que deve ser impressa conforme o modelo fornecido.

Entrada
A entrada contém vários casos de teste e termina com EOF. Cada caso de teste é composto por um único inteiro N (3 ≤ N < 70), que determina o tamanho (linhas e colunas) de uma matriz que deve ser impressa.

Saída
Para cada N lido, apresente a saída conforme o exemplo fornecido.
'''

while True:
    try:
        valor = int(input())
        matriz = []

        for i in range(valor): # transforma tudo em 3 ou em 1
            linha = []
            for j in range(valor):
                if i == j:
                    linha.append(1)
                else:
                    linha.append(3)
            matriz.append(linha)

        contador = valor - 1 
        for x in range(valor): #sobrepoe a diagonal inversa como 2
            for y in range(valor - 1, -1, -1):
                
                if y == contador - 1:
                    matriz[x][contador] = 2
                    contador -= 1
                    break
        matriz[-1][0] = 2
        for v in range(valor):
            for k in range(valor):
                print(matriz[v][k], end='')
            print()
    except EOFError:
        break