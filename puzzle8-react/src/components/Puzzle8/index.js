import './Puzzle8.css'
import React from 'react';

function Puzzle8({ puzzleData }) {
  const correctOrder = [1, 2, 3, 4, 5, 6, 7, 8, 0]; // Ordem correta

  return (
    <div className="puzzleWrap">
      {
        puzzleData.map((cell, index) => (
          <div
            className="cell"
            key={index}
            style={
              cell === correctOrder[index]
                ? { backgroundColor: "rgb(21, 144, 56)" } // Cor verde para posição correta
                : cell > 0
                ? { backgroundColor: "rgb(21, 89, 144)" } // Azul para outras células
                : { backgroundColor: "#FFF" } // Branco para o espaço vazio
            }
          >
            {cell}
          </div>
        ))
      }
    </div>
  );
}

export default Puzzle8;