from colorama import Back, Style
import numpy as np
import random
from enum import Enum

# 1. Aqui criamos o Enumerador que o Sênior pediu!
class StatusQuadrante(Enum):
    AGUA = 0
    NAVIO = 1
    TIRO_AGUA = 2
    TIRO_NAVIO = 3

def criar_tabuleiro(tamanho=10):
    return np.zeros((tamanho, tamanho), dtype=int)

def posicionar_navios(tabuleiro, quantidade=5):
    tamanho = len(tabuleiro)
    navios_posicionados = 0
    
    while navios_posicionados < quantidade:
        linha = random.randint(0, tamanho - 1)
        coluna = random.randint(0, tamanho - 1)
        
        # Substituímos o 0 pelo Enum
        if tabuleiro[linha][coluna] == StatusQuadrante.AGUA.value:
            tabuleiro[linha][coluna] = StatusQuadrante.NAVIO.value
            navios_posicionados += 1
    return tabuleiro

def atirar(tabuleiro, linha, coluna):
    # Substituímos os números mágicos 0, 1, 2 e 3 pelas palavras equivalentes
    if tabuleiro[linha][coluna] == StatusQuadrante.AGUA.value:
        tabuleiro[linha][coluna] = StatusQuadrante.TIRO_AGUA.value
        return False
    elif tabuleiro[linha][coluna] == StatusQuadrante.NAVIO.value:
        tabuleiro[linha][coluna] = StatusQuadrante.TIRO_NAVIO.value
        return True
    else:
        return None 

def exibir_tabuleiro(tabuleiro, mostrar_navios=False):
    print("\n" + " " * 4 + "🚢 BATALHA NAVAL 🚢")
    print("    " + " ".join([str(i) for i in range(len(tabuleiro))]))
    
    for i, linha in enumerate(tabuleiro):
        print(f"{i:2} ", end="")
        for quadrante in linha:
            # Visualização usando o Enum para as cores
            if quadrante == StatusQuadrante.AGUA.value:
                print(Back.BLUE + "  ", end="") 
            elif quadrante == StatusQuadrante.NAVIO.value:
                if mostrar_navios:
                    print(Back.WHITE + "  ", end="") 
                else:
                    print(Back.BLUE + "  ", end="") 
            elif quadrante == StatusQuadrante.TIRO_AGUA.value:
                print(Back.CYAN + "  ", end="") 
            elif quadrante == StatusQuadrante.TIRO_NAVIO.value:
                print(Back.RED + "  ", end="") 
        print(Style.RESET_ALL)