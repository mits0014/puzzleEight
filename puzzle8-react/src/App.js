import React, { useState } from 'react';
import Puzzle8 from "./components/Puzzle8";
import './App.css';
import resolveAPI from './services/resolveAPI';
import ReactLoading from 'react-loading';

function App() {
  const [initialPuzzle, setInitialPuzzle] = useState([])
  const [puzzle, setPuzzle] = useState([0,1,2,3,4,5,6,7,8])
  const [valid, setValid] = useState(false)
  const [puzzleDataguloso, setPuzzleDataguloso] = useState([])
  const [puzzleDatabuscarlargura, setPuzzleDatabuscarlargura] = useState([])
  const [loading, setLoading] = useState(false)
  const [nosSolution, setNoSolution] = useState(false)

  const checkValue = () => {
    if(initialPuzzle.length !== 9){
      alert("voce deve inserir 9 valores numericos, o 0 indica vazio")
      return false 
    }
    let PuzzleValues = initialPuzzle.filter(number => !Number.isNaN(Number(number)))  
    if(PuzzleValues.length !== 9){
      alert("Todos os valores dvem ser numéricos")
      return false 
    }
    PuzzleValues = PuzzleValues.filter(number => Number(number) >= 0 && Number(number) <= 8) 
    if(PuzzleValues.length !== 9){
      alert("Os valores devem ser entre 0 e 8")
      return false 
    }

    PuzzleValues = PuzzleValues.filter((este, i, arr) => arr.indexOf(este) === i); 
    if(PuzzleValues.length !== 9){
      alert("Não pode haver valores repetidos")
      return false 
    } 

    return true
  }

  const loadResolve = async () => {
    setNoSolution(false);
    setLoading(true);
    
    try {
        const { data } = await resolveAPI(`?puzzle=${puzzle.toString()}`);
        
        console.log(data);

        if (!data.solucao) {
            setNoSolution(true);
            setPuzzleDatabuscarlargura([]);
            setPuzzleDataguloso([]);

        } else {
            // Trata os resultados de Busca Gulosa e Busca em Largura
            const { resultadoBuscaGulosa, resultadoBuscaEmlargura } = data.solucao;

            // Converte os passos de cada resultado para arrays
            const parsedGulosa = resultadoBuscaGulosa.map(step => JSON.parse(step).flat());
            const parsedLargura = resultadoBuscaEmlargura.map(step => JSON.parse(step).flat());
            
            // Combina os resultados em um único array para exibição
            setPuzzleDatabuscarlargura(parsedLargura);
            setPuzzleDataguloso(parsedGulosa);
            console.log("Busca Gulosa:", parsedGulosa);
            console.log("Busca em Largura:", parsedLargura);
        }
    } catch (error) {
        console.error("Erro ao buscar solução:", error);
        setNoSolution(true);
    }

    setLoading(false);
};

  return (
    <div className="App">
      <header className="App-header">
        <h3>
          Puzzle 8 Resolver
        </h3>
        <p>Insira os números de 0 à 8 separados por virgula, o numero 0 indica o espaço em branco</p>
        <input type="text" className="inputPuzzle" onChange={e => {
          setInitialPuzzle(e.target.value.split(","))
        }}/>
        <div className="puzzle-container">
          <div className="puzzle-item">
            <p>BuscaLargura</p>
            <Puzzle8 puzzleData={puzzle}/>
          </div>
          <div className="puzzle-item">
            <p>busca Gulosa</p>
            <Puzzle8 puzzleData={puzzle}/>
          </div>
        </div>
        {
              !loading &&
        <button onClick={() => {
            if(checkValue()){
              setPuzzle(initialPuzzle)
              setValid(true)
              setNoSolution(false)
            }
          }
        }>
        
          Carregar valores
        </button>
        }
        {
          valid &&
          <>
            
              <button onClick={loadResolve}>
                {
                  loading === true ?
                  <ReactLoading type={"spinningBubbles"} color={"#FFF"} height={'10px'} width={'10px'} /> : 
                  "Resolver"
                }
              </button>
            
            {
              (!loading && nosSolution) &&
              <h3>O padrão inserido faz parte de um conjunto de padrões que não tem solução</h3>
            }
            {
              <div className="puzzle-container-resolution">
              
                <div className="puzzle-item">
                  
                  {
                     puzzleDatabuscarlargura.map((step, index) => (
                      <>
                        <span>{index + 1}</span>
                        <Puzzle8 key={index} puzzleData={step} />
                      </>
                    ))
                  }
                </div>
                <div className="puzzle-item">
                  
                  {
                    puzzleDataguloso.map((step, index) => (
                      <>
                        <span>{index + 1}</span>
                        <Puzzle8 key={index} puzzleData={step} />
                      </>
                    ))
                  }
                </div>
              </div>
            }
          </>
        }
      </header>
    </div>
  );
}

export default App;
