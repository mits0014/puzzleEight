from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from import_heapq import greedy_best_first_search  
from bfs_a_ import bfs

app = FastAPI()

# Configurar CORS para permitir chamadas do React
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Definir tabuleiro objetivo
objetivo = str([
    [1,2,3],
    [4,5,6],
    [7,8,0]
])

@app.get("/resolverBuscaGulosa")
async def resolver(puzzle: str):
    try:
        # Converter a string de entrada para uma matriz
        puzzle_matrix = [list(map(int, puzzle.split(",")))[i:i+3] for i in range(0, 9, 3)]
        inicio = str(puzzle_matrix)  # Transformar em string para compatibilidade

        # Chamar o algoritmo de resolução
        resultado = greedy_best_first_search(inicio, objetivo)
        
        return {"solucao": resultado}  # Retorna a solução em JSON
    
    except ValueError:
        return {"erro": "Formato inválido. Use números separados por vírgula."}
@app.get("/resolverBuscaLargura")
async def resolverLargura(puzzle: str):
    try:
        puzzle_matrix = [list(map(int, puzzle.split(",")))[i:i+3] for i in range(0, 9, 3)]
        inicio = str(puzzle_matrix)

        resultado = bfs(inicio, objetivo)
        print(resultado)
        return {"solucao" : resultado}
    
    except ValueError:
        return {"erro": "Formato inválido. Use números separados por vírgula."}
    
@app.get("/resolver")
async def resolver(puzzle: str):
    try:
        # Converter a string de entrada para uma matriz
        puzzle_matrix = [list(map(int, puzzle.split(",")))[i:i+3] for i in range(0, 9, 3)]
        inicio = str(puzzle_matrix)  # Transformar em string para compatibilidade

        # Chamar o algoritmo de resolução
        resultadoBuscaGulosa = greedy_best_first_search(inicio, objetivo)
        resultadoBuscaEmlargura = bfs(inicio,objetivo)

        
        return {"solucao": 
                {
                    "resultadoBuscaGulosa": resultadoBuscaGulosa,
                    "resultadoBuscaEmlargura": resultadoBuscaEmlargura
                }}  # Retorna a solução em JSON
    
    except ValueError:
        return {"erro": "Formato inválido. Use números separados por vírgula."}