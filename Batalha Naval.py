#Vinicius Santos Nascimento. Matricula: 31747167. 14/08/2017
import random
import os

def fromTXTMatrix(file):
    f = open(file, 'r' , encoding='utf-8-sig')
    f.close
    return [list(list(line[:-1])) for line in f]

def inicializar_grid():
    exemplo_grid = []
    linhas = 10
    colunas = 10
    contador = 0
    for i in range(linhas):
        exemplo_linha = []
        for j in range(colunas):
            exemplo_linha.append(".")
            contador += 1
        exemplo_grid.append(exemplo_linha)
    return exemplo_grid


# GRID DE FORA #


def ini_grid():
    exemplo_grid = []
    linhas = 10
    colunas = 10
    contador = 0
    for i in range(linhas):
        exemplo_linha = []
        for j in range(colunas):
            exemplo_linha.append("0")
            contador += 1
        exemplo_grid.append(exemplo_linha)
    return exemplo_grid


# IMPRIME GRIDS #


def imprimir_grid(grid):
    linhas = len(grid)
    print('  ', end=' ')
    for i in range(linhas):
        col = i % 10
        print(" "+str(col), end=" ")
    print()
    print(' +', end=' ')
    print('‐‐' * linhas)
    letra = 'A'
    for i in range(linhas):
        colunas = len(grid[i])
        print(letra + ' |', end=' ')
        for j in range(colunas):
            print(str(grid[i][j]) + ' ', end=' ')
        print()
        letra = chr(ord(letra) + 1)
        
        
#POSICIONA EMBARCAÇÕES #
        

def cabe(matrix,linha,coluna,tamanho,vert):
    x = coluna
    y = linha
    if vert == '0':
        #cresce x
        for i in range(x,x+tamanho):
            if not (i < 10 and matrix[i][y] == '.'):
                return False
    else:
        #cresce y
        for i in range(y,y+tamanho):
            if not (i < 10 and matrix[x][i] == '.'):
                return False
    return True

def insertBarco(matrix,linha,coluna,tamanho,vert,char):
    x = coluna
    y = linha
    if vert == '0':
        for i in range(x,x+tamanho):
            matrix[i][y] = char
    else:
        for i in range(y,y+tamanho):
            matrix[x][i] = char
    return matrix

def posicionar_embarcacoes(tab,tamanho,char):
    coluna = 50
    linha = 50
    ver = random.choice(['0', '1'])
    tentativa = 0
    while tentativa < 100:
        if cabe(tab,linha,coluna,tamanho,ver):
            insertBarco(tab,linha,coluna,tamanho,ver,char)
            break
        else:
            tentativa +=1
            coluna = random.randrange(10)
            linha = random.randrange(10)
            ver = random.choice(['0', '1'])
    if tentativa == 10:
        print(char, ' nao coube!')

def posicionar_porta_avioes(tab):
    posicionar_embarcacoes(tab,5,'P')
      
def posicionar_encouracado(tab):
      posicionar_embarcacoes(tab,4,'E')
  
def posicionar_cruzador(tab):
    posicionar_embarcacoes(tab,3,'C')
    
def posicionar_submarino(tab):
    posicionar_embarcacoes(tab,2,'S')
    

# TIRO, VERIFICAÇÃO E GANOU #


def tiroaleatorio():
    x = random.randrange(10)
    y = random.randrange(10)
    return [x,y]

def tiro():
    print("onde atirar?")
    x = int(input("linha:"))
    y = int(input("coluna:"))
    return [x,y]

def verif(x,y,acertou):
    acertoChar = "X"
    aguaChar = "0"
    erroChar = "."
    if  not cpu_grid[x][y]== '.':
        print("Acertou!")
        mostra_grid[x][y] = cpu_grid[x][y]
        cpu_grid[x][y] = '.'
        acertou = acertou +1
    elif mostra_grid[x][y] == aguaChar:
        print("Agua!")
        mostra_grid[x][y] = erroChar
    else:
        print("Voce ja atirou ai!")
    return acertou

def verifCpu(x,y,acertou):
    acertoChar = "X"
    aguaChar = "."
    erroChar = "*"
    if  not player_grid[x][y]== '.':
        if player_grid[x][y] == 'P':
            print("Acertei no[Porta - Aviôes] na célula [",x," ",y,"]")
        elif player_grid[x][y] == 'E':
            print("Acertei no[Encouraçado] na célula [",x," ",y,"]")
        elif player_grid[x][y] == 'C':
            print("Acertei no[Cruzador] na célula [",x," ",y,"]")
        elif player_grid[x][y] == 'S':
            print("Acertei [Submarino] na célula [",x," ",y,"]")
        player_grid[x][y] = "X"
        acertou = acertou +1
    elif player_grid[x][y] == aguaChar:
        print("Acertei [água] na célula [",x," ",y,"]")
        player_grid[x][y] = erroChar
    else:
        print("")
    return acertou

def tabIsEmpty(tabuleiro):
    for linha in tabuleiro:
        for letra in linha:
            if not letra=='.':
                return False
    return True


# MAIN #


acertoChar = "X"
aguaChar = "0"
erroChar = "."


player_grid = inicializar_grid()
cpu_grid = inicializar_grid()
mostra_grid = ini_grid()

posicionar_cruzador(cpu_grid)
posicionar_encouracado(cpu_grid)
posicionar_submarino(cpu_grid)
posicionar_porta_avioes(cpu_grid)

player_grid = fromTXTMatrix('jogador.txt')
print("=========== GRID DO COMPUTADOR ===========")
imprimir_grid(mostra_grid)
print("=========== MINHAS EMBARCAÇÕES ===========")
imprimir_grid(player_grid)
vez = 0
acertou = 0
while not tabIsEmpty(cpu_grid) or tabIsEmpty(player_grid):
    while vez !=3:
        if acertou == 0:
            print("---------------------------------")
            #print(acertou)
            coords = tiro()
            acertou = verif(coords[0], coords[1],acertou)
            #print(acertou)
        vez += 1
    vez = 0
    #print(acertou)
    acertou = 0
    while vez !=3:
        if acertou == 0:
            coords = tiroaleatorio()
            acertou = verifCpu(coords[0], coords[1],acertou)
            os.system("pause");
        vez +=1
    vez = 0
    acertou = 0

    print("=========== GRID DO COMPUTADOR ===========")
    imprimir_grid(mostra_grid)
    print("=========== MINHAS EMBARCAÇÕES ===========")
    imprimir_grid(player_grid)

if tabIsEmpty(cpu_grid):
    print("Você Ganhou!")

elif tabIsEmpty(player_grid):
    print("Você Perdeu!")
