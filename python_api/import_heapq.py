import heapq

def move(tab_original):
    """
    Gera os possíveis movimentos do quebra-cabeça 8-Puzzle.
    """
    movimentos = []
    tab = eval(tab_original)
    i, j = next((x, row.index(0)) for x, row in enumerate(tab) if 0 in row)
    
    if i < 2:  # Mover para baixo
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i+1][j] = tab[i+1][j], tab[i][j]

    if i > 0:  # Mover para cima
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  
        movimentos.append(str(tab))
        tab[i][j], tab[i-1][j] = tab[i-1][j], tab[i][j]  

    if j < 2:  # Mover para a direita
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j+1] = tab[i][j+1], tab[i][j]

    if j > 0:  # Mover para a esquerda
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j] 
        movimentos.append(str(tab))
        tab[i][j], tab[i][j-1] = tab[i][j-1], tab[i][j]

    return movimentos

def greedy_best_first_search(start, end):
    """
    Busca Gulosa (Greedy Best-First Search) utilizando a heurística de Manhattan.
    """
    explorado = set()
    prioridade = []
    heapq.heappush(prioridade, (h_manhattan(start), [start]))

    while prioridade:
        _, caminho = heapq.heappop(prioridade)
        final = caminho[-1]

        if final in explorado:
            continue
        explorado.add(final)

        if final == end:
            return caminho

        for movimento in move(final):
            if movimento not in explorado:
                novo_caminho = caminho + [movimento]
                heapq.heappush(prioridade, (h_manhattan(movimento), novo_caminho))
    
    return None

def h_manhattan(tabuleiro):
    """
    Heurística de Manhattan: Soma das distâncias horizontais e verticais 
    de cada peça (exceto 0) até sua posição correta.
    """
    tab = eval(tabuleiro)
    distancia = 0
    # Para um tabuleiro 3x3 o objetivo é que os números 1 a 8 estejam em ordem,
    # sendo que o 0 representa o espaço vazio na última posição (posição [2][2]).
    for i in range(3):
        for j in range(3):
            valor = tab[i][j]
            if valor != 0:
                # Calcula a posição esperada para o valor.
                # Para o valor k, a posição é:
                # linha_objetivo = (k-1) // 3 e coluna_objetivo = (k-1) % 3
                linha_objetivo = (valor - 1) // 3
                coluna_objetivo = (valor - 1) % 3
                distancia += abs(i - linha_objetivo) + abs(j - coluna_objetivo)
    return distancia

def imprimir_tabuleiro(tabuleiro):
    """
    Exibe o tabuleiro formatado.
    """
    tab = eval(tabuleiro)
    print("+---+---+---+")
    for linha in tab:
        print("| " + " | ".join(str(num) if num != 0 else " " for num in linha) + " |")
        print("+---+---+---+")
    print("\n")

# Definição dos tabuleiros
inicio = str([
    [5,2,0],
    [8,4,7],
    [1,6,3]
])

objetivo = str([
    [1,2,3],
    [4,5,6],
    [7,8,0]
])
