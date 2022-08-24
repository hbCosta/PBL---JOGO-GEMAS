from random import randint
import string

def boas_vindas():
    print('*'*93)
    print('*'*30,'BEM VINDO AO JOGO QUEBRA LETRAS','*'*30)
    print('*'*93)


# Funções para validar a entrada do usuario (linhas, colunas e elementos)
def validar_linha(entrada_linha):
    while entrada_linha < 3 or entrada_linha > 10:
        entrada_linha = int(input(' Digite novamente a dimensão n da matriz: [3/10] '))
    return entrada_linha

def validar_coluna(entrada_coluna):
    while entrada_coluna < 3 or entrada_coluna > 10:
        entrada_coluna = int(input(' Digite novamente a dimensão m da matriz: [3/10] '))
    return entrada_coluna
def validar_elemento(entrada_elemento):
    while entrada_elemento < 3 or entrada_elemento > 26:
        entrada_elemento = int(input('Digite novamente a quantidade de elementos: [3/26] '))
    return entrada_elemento



def dimensao():
    linhas = validar_linha(int(input(' Digite a dimensão n da matriz: [3/10] ')))
    colunas = validar_coluna(int(input(' Digite a dimensão m da matriz: [3/10] ')))
    elementos = validar_elemento(int(input(' Digite os elementos da matriz: [3/26] ')))
    return linhas, colunas, elementos


# Construção da matriz em linha
def matriz1(linhas, colunas, elementos):
    matriz = [[string.ascii_uppercase[randint(0, elementos - 1)] for j in range(colunas)] for i in range(linhas)] # Uso do list comprehension.
    return matriz                                                                                            # Diminuimos para 1 linha o que seria feito em 4


def formarMatriz(matriz, formlinhas, formcolunas, pont):
    for i in range(formlinhas):
        for j in range(formcolunas):
            print(matriz[i][j], end=' ')  # Faz a matriz ficar na sua form sua
        print('')                         # mais conhecida
    print('Pontuação do jogador: ',pont)


def analisar_horizontal(matriz, formlinhas, formcolunas, ):
    for i in range(formlinhas):
        contador = 1
        for j in range(formcolunas - 1):
            if matriz[i][j].lower() == matriz[i][j+1].lower():  #Determina se a letra da linha é igual a proxima letra
                contador += 1
            else:
                contador = 1
            if contador >= 3:
                k = j + 1
                while k > j + 1 - contador and matriz[i][k].isupper():
                    matriz[i][k] = matriz[i][k].lower()
                    k -= 1
    return matriz



def analisar_vertical(matriz,formlinhas, formcolunas):
    for j in range(formcolunas):
        contador = 1
        for i in range(formlinhas - 1):
            if matriz[i][j].lower() == matriz[i+1][j].lower():  # Determina se a letra da coluna é igual a proxima letra da coluna
                contador += 1
            else:
                contador = 1
            if contador >= 3:
                k = i + 1
                while k > i + 1 - contador:
                    matriz[k][j] = matriz[k][j].lower()
                    k -= 1
    return matriz




def quebrarGemas_vertical(matriz, formlinhas, formcolunas):
    for j in range(formcolunas):
        contador = 1
        for i in range(formlinhas - 1):
            if matriz[i][j].lower() == matriz[i+1][j].lower():
                contador += 1
            else:
                contador = 1
            if contador >= 3:
                k = i + 1
                while k > i + 1 - contador and matriz[k][j].isupper():
                    matriz[k][j] = matriz[k][j].lower()
                    k -= 1
    for j in range(formcolunas):
        for i in range(formlinhas):
            if matriz[i][j].islower():
                matriz[i][j] = '0'    #Atribuindo 0 para o endereço da matriz que esteja com letra minuscula
    return matriz


def quebrarGemas_horizontal(matriz, formlinhas, formcolunas):
    for i in range(formlinhas):
        contador = 1
        for j in range(formcolunas - 1):
            if matriz[i][j].lower() == matriz[i][j + 1].lower():
                contador += 1
            else:
                contador = 1
            if contador >= 3:
                k = j + 1
                while k > j + 1 - contador and matriz[i][k].isupper():
                    matriz[i][k] = matriz[i][k].lower()
                    k -= 1
    for i in range(formlinhas):
        for j in range(formcolunas):
            if matriz[i][j].islower():
                matriz[i][j] = '0'   #Atribuindo 0 para o endereço da matriz que esteja com letra minuscula
    return matriz



def descer(matriz, formlinhas, formcolunas):
    for d in range(formlinhas):
        for i in range(formlinhas - 1, 0, -1):       #percorrendo a matriz
            for j in range(formcolunas-1,-1,-1):     # do fim para o inicio
                if matriz[i][j] == '0':
                    matriz[i][j], matriz[i-1][j] = matriz[i-1][j], matriz[i][j]
    return matriz


def gerar_gemas(matriz, elementos):
    cont = 0   # Vamos usar essa variavel para saber quando podemos deixar o usuario jogar novamente
    for i in range(len(matriz)):           #percorrendo a matriz para
        for j in range(len(matriz[0])):    #quando achar o valor 0 vamos adicionar de forma aleatoria letras do alfabeto.
            if matriz[i][j] == '0':
                cont += 1
                matriz[i][j] = string.ascii_uppercase[randint(0, elementos - 1)] # essa linha de codigo esta importando letras de
    return matriz, cont                                                          #forma aleatoria e adicionando onde existia 0
                                                                                 # (as letras já estão sendo importadas maiusculas)
def pontuacao(formlinha, formcoluna, matriz, pont):
    for i in range(formlinha):
        for j in range(formcoluna):
            if matriz[i][j] == '0':   #Se tiver zero na matriz saberemos que o usuario quebrou gemas
                pont += 1             # pont esta contando quantos zeros tem na matriz e retornando para o programa principal
    return pont                        # dai saberemos qual a pontuação do jogador


# Função de ciclagem.  Função responsavel por ciclar o tabuleiro de jogo
def ciclar(matriz, formlinhas, formcolunas, elementos, pont):
    tabuleiro = analisar_horizontal(matriz, formlinhas, formcolunas)
    tabuleiro = analisar_vertical(tabuleiro, formlinhas, formcolunas)
    tabuleiro = quebrarGemas_horizontal(tabuleiro, formlinhas, formcolunas)
    tabuleiro = quebrarGemas_vertical(tabuleiro, formlinhas, formcolunas)
    pont = pontuacao(formlinhas, formcolunas, matriz, pont)
    tabuleiro = descer(tabuleiro, formlinhas, formcolunas)
    tabuleiro, cont = gerar_gemas(tabuleiro, elementos)
    return tabuleiro, cont, pont

# Essa função sera o menu do jogo mostrando as opções que o usuario pode escolher
def escolher():
    print('1 - PERMUTAR GEMAS\n2 - SAIR\n')
    escolha = int(input('Digite a opção desejada: [1, 2] '))
    return escolha

# Função que vai pedir o movimento que o usuario deseja efetuar
def movimentar():
    linha_1 = int(input('Digite em qual linha o elemento que voce deseja trocar esta: '))
    coluna_1 = int(input('Digite em qual coluna o elemento que voce deseja trocar esta: '))
    linha_2 = int(input('Digite para qual linha o elemento deve ir: '))
    coluna_2 = int(input('Digite para qual coluna o elemento deve ir: '))
    return linha_1, coluna_1, linha_2, coluna_2


# Trocando as gemas de local
def trocar(matriz, linha1, coluna1, linha2, coluna2):
    pos1 = matriz[linha1][coluna1]                # Endereço da primeira gema que o usuario quer movimentar
    pos2 = matriz[linha2][coluna2]                # Endereço da segunda gema que o usuario quer movimentar
    matriz[linha2][coluna2] = pos1         # O endereço da segunda gema que o usuario digitou vai receber o da primeira
    matriz[linha1][coluna1] = pos2         # O endereço da primeira gema que o usuario digitou vai receber o da segunda
    return matriz