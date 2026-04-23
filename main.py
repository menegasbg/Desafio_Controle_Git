from colorama import Fore, init
from assets.map import criar_tabuleiro, posicionar_navios, exibir_tabuleiro, atirar

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
            linha = int(entrada_linha)
            coluna = int(entrada_coluna)
            
            if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
                print(Fore.RED + "Coordenadas inválidas! Atire dentro do tabuleiro (0 a 9).")
                continue
                
            resultado = atirar(oceano, linha, coluna)
            
            if resultado == True:
                print(Fore.RED + "\n💥 BOOOM! Você acertou um navio em cheio!")
                navios_abatidos += 1
                
                # A Condição de Vitória!
                if navios_abatidos == TOTAL_NAVIOS:
                    exibir_tabuleiro(oceano, mostrar_navios=True) # Mostra o mapa inteiro no final
                    print(Fore.GREEN + "\n🏆 VITÓRIA SUPREMA! Você afundou toda a frota inimiga, Comandante!")
                    break # Encerra o jogo
                    
            elif resultado == False:
                print(Fore.CYAN + "\n💦 SPLASH! Tiro na água.")
            else:
                print(Fore.YELLOW + "\n⚠️ Atenção: Você já atirou nessa coordenada, Comandante!")
                
        except ValueError:
            print(Fore.RED + "\n❌ Entrada inválida! Digite apenas números.")