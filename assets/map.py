from colorama import Back, Style
import numpy as np
import random

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