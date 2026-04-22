from colorama import Fore, init
from assets.map import criar_tabuleiro, posicionar_navios, exibir_tabuleiro, atirar

<<<<<<< HEAD
init(autoreset=True)

if __name__ == "__main__":
    TOTAL_NAVIOS = 5
    navios_abatidos = 0
    
    oceano = criar_tabuleiro(10)
    oceano = posicionar_navios(oceano, quantidade=TOTAL_NAVIOS)
    
    print(Fore.YELLOW + "Bem-vindo ao Batalha Naval, Comandante!")
    
    while True:
        exibir_tabuleiro(oceano, mostrar_navios=False)
        
        # Placar atualizado em tempo real
        print(Fore.GREEN + f"\n🎯 Placar: {navios_abatidos}/{TOTAL_NAVIOS} navios abatidos")
        print("="*30)
=======
# Inicializa as cores do terminal
init(autoreset=True)

if __name__ == "__main__":
    # 1. Configura o jogo nos bastidores
    oceano = criar_tabuleiro(10)
    oceano = posicionar_navios(oceano, quantidade=5)
    
    print(Fore.YELLOW + "Bem-vindo ao Batalha Naval, Comandante!")
    
    # 2. Inicia o loop interativo do jogo
    while True:
        exibir_tabuleiro(oceano, mostrar_navios=False)
        
        print("\n" + "="*30)
>>>>>>> aaf490b7ed49cb10eb06acfc8349faf3e96fe54c
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
<<<<<<< HEAD
            linha = int(entrada_linha)
            coluna = int(entrada_coluna)
            
=======
            # Converte o que o usuário digitou para números inteiros
            linha = int(entrada_linha)
            coluna = int(entrada_coluna)
            
            # Valida se o tiro está dentro do tabuleiro
>>>>>>> aaf490b7ed49cb10eb06acfc8349faf3e96fe54c
            if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
                print(Fore.RED + "Coordenadas inválidas! Atire dentro do tabuleiro (0 a 9).")
                continue
                
<<<<<<< HEAD
=======
            # Chama a função de atirar que criamos no map.py
>>>>>>> aaf490b7ed49cb10eb06acfc8349faf3e96fe54c
            resultado = atirar(oceano, linha, coluna)
            
            if resultado == True:
                print(Fore.RED + "\n💥 BOOOM! Você acertou um navio em cheio!")
<<<<<<< HEAD
                navios_abatidos += 1
                
                # A Condição de Vitória!
                if navios_abatidos == TOTAL_NAVIOS:
                    exibir_tabuleiro(oceano, mostrar_navios=True) # Mostra o mapa inteiro no final
                    print(Fore.GREEN + "\n🏆 VITÓRIA SUPREMA! Você afundou toda a frota inimiga, Comandante!")
                    break # Encerra o jogo
                    
=======
>>>>>>> aaf490b7ed49cb10eb06acfc8349faf3e96fe54c
            elif resultado == False:
                print(Fore.CYAN + "\n💦 SPLASH! Tiro na água.")
            else:
                print(Fore.YELLOW + "\n⚠️ Atenção: Você já atirou nessa coordenada, Comandante!")
                
        except ValueError:
            print(Fore.RED + "\n❌ Entrada inválida! Digite apenas números.")