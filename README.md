# 🚢 Batalha Naval - Desafio GitFlow

Este projeto é um simulador de Batalha Naval desenvolvido em Python para o desafio de controle de versão.

## 📜 Regras e Controles
- **Objetivo:** Destruir todos os 5 navios da frota inimiga antes que a sua munição acabe.
- **Como atirar:** Durante o seu turno, o console pedirá as coordenadas de disparo. Digite a linha (0 a 9) e a coluna (0 a 9) separadas por espaço (exemplo: `2 5`).
- **Níveis de Dificuldade:** Ao iniciar o jogo, você poderá escolher um modo de dificuldade que limitará a quantidade máxima de tentativas (mísseis).
- **Desistir:** Você pode recuar suas tropas a qualquer momento do jogo digitando a letra `q`.


## 🚀 Tecnologias
- **Python 3.10+** (Gerenciado via **ASDF**)
- **Numpy**: Para manipulação da matriz do tabuleiro.
- **Colorama**: Para estilização do terminal.

## 🛠️ Como rodar
1. **Instalar a versão do Python (via ASDF):**
   ```bash 
   asdf install
   ```
2. **Criar o Ambiente virtual:**
     ```bash 
     python -m venv .venv
     ```
3. **Ativar o Ambiente virtual:**
     ```bash 
     source .venv/bin/activate
     ```
4. **Instalar as dependências:**
     ```bash 
     pip install -r requirements.txt
     ```
5. **Executar o jogo:**
     ```bash 
     python main.py
     ```