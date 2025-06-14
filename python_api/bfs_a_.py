def move(tab_original):
    """
    Checa possíveis movimentos (os nós)
    da árvore
    """
    movimentos = []
    tab = eval(tab_original)
    i = 0
    j = 0
    while 0 not in tab[i]: i += 1
    j = tab[i].index(0)
    

    if i<2:         #mover o 0 para baixo 
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j]

    if i>0:         #mover o 0 para cima
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  
        movimentos.append(str(tab))
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  

    if j<2:         #mover o 0 para a direita
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j]
    
    if j>0:         #mover o 0 para a esquerda
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j]

    return movimentos

def bfs(start,end):
    """
    Usa busca em largura para 
    resolver o quebra-cabeça
    """
    explorado = []
    banco = [[start]]
    while banco:
        i = 0
        caminho = banco[i]
        banco = banco[:i] + banco[i+1:]
        final = caminho[-1]
        if final in explorado: 
            continue
        for movimento in move(final):
            if movimento in explorado:
                continue
            banco.append(caminho + [movimento])
        explorado.append(final)
        if final == end: break
    return caminho

def h_misplaced(tabuleiro):
    """
    Implementa a heurística de 
    checar quantas peças estão 
    fora do lugar
    """
    misplaced = 0
    comparador = 1
    tab = eval(tabuleiro)
    for i in range(0,3):
        for j in range(0,3):
            if tab[i][j] != comparador:
                misplaced += 1
            comparador += 1
    return misplaced

tabuleiro = str([
                [5,2,0],
                [8,4,7],
                [1,6,3]
            ])

obj_final = str([
                [1,2,3],
                [4,5,6],
                [7,8,0]
            ])