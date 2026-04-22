from colorama import Fore, init
from assets.map import criar_tabuleiro, posicionar_navios, exibir_tabuleiro, atirar

# Inicializa as cores do terminal
init(autoreset=True)

if __name__ == "__main__":
    # 1. Configura o jogo nos bastidores
    oceano = criar_tabuleiro(10)
    oceano = posicionar_navios(oceano, quantidade=5)
    
    
    tentativas = 0 # ---- CONTRIBUIÇÃO EIJI: Contador de tentativas ---

    print(Fore.YELLOW + "Bem-vindo ao Batalha Naval, Comandante!")
    
    # 2. Inicia o loop interativo do jogo
    while True:
        exibir_tabuleiro(oceano, mostrar_navios=False)
        
        print(f"\n Tentativa nº: {tentativas}") # ---- CONTRIBUIÇÃO EIJI: print Contador de tentativas ---
        print("\n" + "="*30)
        print("Preparar canhões! (Digite 'q' a qualquer momento para sair)")
        
        entrada_linha = input("Digite a LINHA (0-9): ")
        if entrada_linha.lower() == 'q':
            print(Fore.YELLOW + "Recuando tropas. Fim de jogo!")
            break
            
        entrada_coluna = input("Digite a COLUNA (0-9): ")
        if entrada_coluna.lower() == 'q':
            print(Fore.YELLOW + "Recuando tropas. Fim de jogo!")
            break
            
        try:
            # Converte o que o usuário digitou para números inteiros
            linha = int(entrada_linha)
            coluna = int(entrada_coluna)
            
            # Valida se o tiro está dentro do tabuleiro
            if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
                print(Fore.RED + "Coordenadas inválidas! Atire dentro do tabuleiro (0 a 9).")
                continue
                
            # Chama a função de atirar que criamos no map.py
            resultado = atirar(oceano, linha, coluna)
            
            if resultado is not None: # ---- CONTRIBUIÇÃO EIJI: Soma uma tentativa apenas se o tiro for válido ---
                tentativas += 1

            if resultado == True:
                print(Fore.RED + "\n💥 BOOOM! Você acertou um navio em cheio!")
            elif resultado == False:
                print(Fore.CYAN + "\n💦 SPLASH! Tiro na água.")
            else:
                print(Fore.YELLOW + "\n⚠️ Atenção: Você já atirou nessa coordenada, Comandante!")
                
        except ValueError:
            print(Fore.RED + "\n❌ Entrada inválida! Digite apenas números.")
        
    print(Fore.YELLOW + f"\nFim de jogo! Você realizou {tentativas} disparos.") # ---- CONTRIBUIÇÃO EIJI: print final exibindo quantidade final de tentativas ---