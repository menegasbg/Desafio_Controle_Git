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

def atirar(tabuleiro, linha, coluna):
    """
    Registra um tiro no tabuleiro.
    Retorna True se acertou um navio, False se acertou a água, 
    e None se já havia atirado no local.
    """
    if tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = 2 # 2 = Tiro na água
        return False
    elif tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = 3 # 3 = Tiro no navio (Fogo!)
        return True
    else:
        # Se for 2 ou 3, significa que o jogador já atirou aqui antes
        return None 

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
            elif quadrante == 2:
                print(Back.CYAN + "  ", end="") # Água atingida (Ciano)
            elif quadrante == 3:
                print(Back.RED + "  ", end="") # Navio atingido (Vermelho)
        print(Style.RESET_ALL)