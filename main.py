import numpy as np
import random
from colorama import Fore, Back, Style, init

# Inicializa o colorama para as cores funcionarem direitinho
init(autoreset=True)

def criar_tabuleiro(tamanho=10):
    return np.zeros((tamanho, tamanho), dtype=int)

def posicionar_navios(tabuleiro, quantidade=5):
    tamanho = len(tabuleiro)
    navios_posicionados = 0
    
    while navios_posicionados < quantidade:
        linha = random.randint(0, tamanho - 1)
        coluna = random.randint(0, tamanho - 1)
        
        # Só posiciona se o lugar estiver vazio (for 0)
        if tabuleiro[linha][coluna] == 0:
            tabuleiro[linha][coluna] = 1
            navios_posicionados += 1
    return tabuleiro

def exibir_tabuleiro(tabuleiro, mostrar_navios=False):
    print("\n" + " " * 4 + "🚢 BATALHA NAVAL 🚢")
    print("    " + " ".join([str(i) for i in range(len(tabuleiro))]))
    
    for i, linha in enumerate(tabuleiro):
        print(f"{i:2} ", end="")
        for quadrante in linha:
            if quadrante == 0:
                print(Back.BLUE + "  ", end="") # Água vazia
            elif quadrante == 1:
                if mostrar_navios:
                    print(Back.WHITE + "  ", end="") # Navio visível (Modo Dev)
                else:
                    print(Back.BLUE + "  ", end="") # Navio camuflado!
        print(Style.RESET_ALL)

if __name__ == "__main__":
    # 1. Cria a água
    oceano = criar_tabuleiro(10)
    
    # 2. Esconde 5 navios nela
    oceano = posicionar_navios(oceano, quantidade=5)
    
    # 3. Mostra para o jogador (escondido)
    print(Fore.GREEN + "\nVisão do Jogador (Tudo azul):")
    exibir_tabuleiro(oceano, mostrar_navios=False)
    
    # 4. Mostra o gabarito para você (desenvolvedor)
    print(Fore.YELLOW + "\nGabarito (Navios em branco):")
    exibir_tabuleiro(oceano, mostrar_navios=True)