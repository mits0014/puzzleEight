import heapq
import time
import psutil
import os

def move(tab_original):
    """
    Gera os possíveis movimentos do quebra-cabeça 8-Puzzle.
    """
    movimentos = []
    tab = eval(tab_original)
    i, j = next((r, c) for r, row in enumerate(tab) for c, val in enumerate(row) if val == 0)

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

def bfs(start, end):
    """
    Busca em Largura (BFS)
    """
    explorado = set()
    banco = [[start]]

    while banco:
        caminho = banco.pop(0)
        final = caminho[-1]

        if final in explorado:
            continue
        explorado.add(final)

        if final == end:
            return caminho

        for movimento in move(final):
            if movimento not in explorado:
                banco.append(caminho + [movimento])
    
    return None

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



# Definição dos tabuleiros
estado_inicial = str([
    [8, 6, 7],
    [2, 5, 4],
    [3, 0, 1]
])

estado_objetivo = str([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
])

def medir_performance(metodo_busca, nome, start, goal):
    """
    Mede o tempo e o uso de memória, incluindo o pico de uso corretamente.
    """
    processo = psutil.Process(os.getpid())
    memoria_antes = processo.memory_info().rss / 1024  # KB
    tempo_inicio = time.time()

    solucao = metodo_busca(start, goal)

    tempo_fim = time.time()
    memoria_depois = processo.memory_info().rss / 1024  # KB

    # Pegando o pico de memória real (Windows usa peak_wset, Linux/mac usa peak_rss)
    if hasattr(processo.memory_info(), 'peak_wset'):
        pico_memoria = processo.memory_info().peak_wset / 1024  # Windows
    else:
        pico_memoria = processo.memory_info().peak_rss / 1024  # Linux/Mac

    tempo_total = tempo_fim - tempo_inicio
    memoria_usada = pico_memoria - memoria_antes  # Corrigindo o cálculo da memória usada

    print(f"\n🔹 {nome}")
    if solucao:
        print(f"🔹 Solução encontrada em {len(solucao) - 1} passos")
        print(f"🔹 Tempo: {tempo_total:.4f} segundos")
        print(f"🔹 Memória inicial: {memoria_antes:.2f} KB")
        print(f"🔹 Memória final: {memoria_depois:.2f} KB")
        print(f"🔹 Pico de memória: {pico_memoria:.2f} KB")
        print(f"🔹 Memória usada: {memoria_usada:.2f} KB")


    else:
        print("❌ Nenhuma solução encontrada.")
    
    dados = [[nome, tempo_total, memoria_antes, memoria_depois, pico_memoria, memoria_usada]]

    return tempo_total, memoria_antes, memoria_depois, pico_memoria, memoria_usada

# Comparação dos métodos
print("\n📊 Comparação entre BFS e Busca Gulosa com Heurística de Manhattan")
tempo_bfs, memoria_inicial_bfs, memoria_final_bfs, pico_bfs, memoria_usada_bfs = medir_performance(bfs, "Busca em Largura (BFS)", estado_inicial, estado_objetivo)
tempo_greedy, memoria_inicial_greedy, memoria_final_greedy, pico_greedy, memoria_usada_greedy = medir_performance(greedy_best_first_search, "Busca Gulosa", estado_inicial, estado_objetivo)


# Exibindo os resultados finais
print("\n📈 Resultados Comparativos:")
print(f"⏳ Tempo - BFS: {tempo_bfs:.4f}s | Busca Gulosa: {tempo_greedy:.4f}s")
print(f"📦 Memória - BFS: {memoria_final_bfs:.2f} KB | Busca Gulosa: {memoria_final_greedy:.2f} KB")
print(f"📊 Pico de Memória - BFS: {pico_bfs:.2f} KB | Busca Gulosa: {pico_greedy:.2f} KB")
print(f"📈 Memória Usada - BFS: {memoria_usada_bfs:.2f} KB | Busca Gulosa: {memoria_usada_greedy:.2f} KB")
