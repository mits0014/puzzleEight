# Trabalho de IA - Resolução do 8-Puzzle

Este projeto implementa a resolução do problema do 8-Puzzle utilizando algoritmos de busca, como a Busca Gulosa e a Busca em Largura. Ele é composto por duas partes: o backend (API em Python) e o frontend (aplicação React).

---

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas em sua máquina:

- **Node.js** (para rodar o frontend)
- **Python 3.8+** (para rodar o backend)
- **Gerenciador de pacotes pip** (para instalar dependências do Python)

---

## Como rodar o backend (API) manualmente

1. **Acesse a pasta do backend**:
   ```bash
   cd python_api
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**:
   ```bash
   python -m venv venv
   ```

3. **Ative o ambiente virtual**:
   - No Windows:
     ```bash
     venv\Scripts\activate
     ```
   - No Linux/Mac:
     ```bash
     source venv/bin/activate
     ```

4. **Instale as dependências**:
   ```bash
   pip install fastapi uvicorn
   ```

5. **Inicie o servidor**:
   ```bash
   uvicorn main_api:app --reload
   ```

6. **Acesse a API**:
   - Acesse a documentação interativa da API no navegador: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Como rodar o frontend (React) manualmente

1. **Acesse a pasta do frontend**:
   ```bash
   cd puzzle8-react
   ```

2. **Instale as dependências**:
   ```bash
   npm install
   ```

3. **Inicie o servidor de desenvolvimento**:
   ```bash
   npm start
   ```

4. **Acesse a aplicação**:
   - Abra o navegador e acesse: [http://localhost:3000](http://localhost:3000)

---

## Estrutura do Projeto

- **Backend**:
  - Local: `python_api`
  - Linguagem: Python
  - Framework: FastAPI
  - Arquivo principal: `main_api.py`

- **Frontend**:
  - Local: `puzzle8-react`
  - Linguagem: JavaScript
  - Framework: React
  - Arquivo principal: `src/App.js`

---

## Observações

- Certifique-se de que o backend esteja rodando antes de iniciar o frontend, caso execute os servidores manualmente.
- Caso encontre problemas, verifique se as portas padrão (8000 para o backend e 3000 para o frontend) estão disponíveis.

---