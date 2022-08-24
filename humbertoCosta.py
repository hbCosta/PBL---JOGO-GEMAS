from bibliotecafunçoes import*

# Programa Principal

boas_vindas()
linhas, colunas, elementos = dimensao()
matriz = matriz1(linhas, colunas, elementos)
pont = 0

ciclar_matriz, cont, pont = ciclar(matriz, linhas, colunas, elementos, pont)

while cont > 0:
    ciclar_matriz, cont, pont = ciclar(matriz,linhas, colunas, elementos, pont)
print('*'*30,'TABULEIRO','*'*30)
formarMatriz(matriz, linhas,colunas, pont)
print()
print('*'*30,'MENU DE ESCOLHAS','*'*30)
escolha = escolher()
if escolha == 1:
    linha1, coluna1, linha2, coluna2 = movimentar()
    movimento = trocar(matriz, linha1, coluna1, linha2, coluna2), formarMatriz(matriz, linhas, colunas, pont)
    print()
    ciclar_matriz, cont, pont = ciclar(matriz, linhas, colunas, elementos, pont)
    while cont > 0:
        ciclar_matriz, cont, pont = ciclar(matriz, linhas, colunas, elementos, pont)
    print('*'*30,'NOVO TABULEIRO','*'*30)
    formarMatriz(matriz, linhas, colunas, pont)
if escolha == 2:
    print('*'*30,'FIM DE JOGO','*'*30)