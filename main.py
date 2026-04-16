import numpy as np
from colorama import Fore, Back, Style, init

# Inicializa o colorama para funcionar no Windows/Linux/WSL
init(autoreset=True)

def criar_tabuleiro(tamanho=10):
    # Cria uma matriz de zeros usando Numpy (0 representa água)
    return np.zeros((tamanho, tamanho), dtype=int)

def exibir_tabuleiro(tabuleiro):
    print("\n" + " " * 4 + "🚢 BATALHA NAVAL 🚢")
    print("    " + " ".join([str(i) for i in range(len(tabuleiro))]))
    
    for i, linha in enumerate(tabuleiro):
        # Mostra o número da linha
        print(f"{i:2} ", end="")
        for quadrante in linha:
            if quadrante == 0:
                # Mar: Quadrado azul
                print(Back.BLUE + "  ", end="")
            else:
                # Navio ou tiro (veremos depois)
                print(Back.WHITE + "  ", end="")
        print(Style.RESET_ALL) # Reseta a cor no fim da linha

if __name__ == "__main__":
    oceano = criar_tabuleiro(10)
    exibir_tabuleiro(oceano)
    print(Fore.GREEN + "\nO mar está calmo... por enquanto.")