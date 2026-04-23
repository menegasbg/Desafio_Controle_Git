from colorama import Fore, init
from assets.map import criar_tabuleiro, posicionar_navios, exibir_tabuleiro, atirar

init(autoreset=True)

if __name__ == "__main__":
    TOTAL_NAVIOS = 5
    navios_abatidos = 0
    
    # NOVAS VARIÁVEIS DE MUNIÇÃO
    MUNICAO_TOTAL = 15 
    municao_atual = MUNICAO_TOTAL 
    
    oceano = criar_tabuleiro(10)
    oceano = posicionar_navios(oceano, quantidade=TOTAL_NAVIOS)
    
    print(Fore.YELLOW + "Bem-vindo ao Batalha Naval, Comandante!")
    
    while True:
        exibir_tabuleiro(oceano, mostrar_navios=False)
        
        # PLACAR ATUALIZADO COM A MUNIÇÃO
        print(Fore.GREEN + f"\n🎯 Placar: {navios_abatidos}/{TOTAL_NAVIOS} navios abatidos")
        print(Fore.CYAN + f"🔋 Munição: {municao_atual}/{MUNICAO_TOTAL} tiros restantes")
        print("="*30)
        print("Preparar canhões! (Digite 'q' a qualquer momento para sair)")
        
        entrada = input("\nDigite a linha e coluna (ex: 2 5): ")
        
        if entrada.lower() == 'q':
            print(Fore.YELLOW + "Recuando tropas. Até a próxima batalha!")
            break
            
        try:
            linha, coluna = map(int, entrada.split())
            resultado = atirar(oceano, linha, coluna)
            
            # Gasta munição apenas se o tiro for válido (água ou navio)
            if resultado is not None:
                municao_atual -= 1
            
            if resultado == True:
                print(Fore.RED + "\n💥 BOOOM! Você acertou um navio em cheio!")
                navios_abatidos += 1
                
                if navios_abatidos == TOTAL_NAVIOS:
                    exibir_tabuleiro(oceano, mostrar_navios=True)
                    print(Fore.GREEN + "\n🏆 VITÓRIA SUPREMA! Você afundou toda a frota inimiga, Comandante!")
                    break 
                    
            elif resultado == False:
                print(Fore.CYAN + "\n💦 SPLASH! Tiro na água.")
            else:
                print(Fore.YELLOW + "\n⚠️ Atenção: Você já atirou nessa coordenada, Comandante!")
                
            # --- NOVA CONDIÇÃO DE DERROTA ---
            if municao_atual <= 0 and navios_abatidos < TOTAL_NAVIOS:
                exibir_tabuleiro(oceano, mostrar_navios=True) # Revela os navios que faltaram
                print(Fore.RED + "\n💀 GAME OVER! Sua munição acabou. A frota inimiga venceu a guerra.")
                break # Encerra o jogo
                
        except ValueError:
            print(Fore.RED + "\n❌ Entrada inválida! Digite apenas números.")
        except IndexError:
            print(Fore.RED + "\n❌ Coordenada fora do mapa! Digite números entre 0 e 9.")