from colorama import Fore, init
from assets.map import criar_tabuleiro, posicionar_navios, exibir_tabuleiro, atirar

init(autoreset=True)

def jogar_partida():
    TOTAL_NAVIOS = 5
    navios_abatidos = 0
    MUNICAO_TOTAL = 15 
    municao_atual = MUNICAO_TOTAL 
    tentativas = 0 
    
    oceano = criar_tabuleiro(10)
    oceano = posicionar_navios(oceano, quantidade=TOTAL_NAVIOS)
    
    print(Fore.YELLOW + "\nBem-vindo ao Batalha Naval, Comandante!")
    
    while True:
        exibir_tabuleiro(oceano, mostrar_navios=False)
        
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
            
            if linha < 0 or linha > 9 or coluna < 0 or coluna > 9:
                print(Fore.RED + "Coordenadas inválidas! Atire dentro do tabuleiro (0 a 9).")
                continue

            resultado = atirar(oceano, linha, coluna)
            
            if resultado is not None:
                tentativas += 1
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
                
            if municao_atual <= 0 and navios_abatidos < TOTAL_NAVIOS:
                exibir_tabuleiro(oceano, mostrar_navios=True) 
                print(Fore.RED + "\n💀 GAME OVER! Sua munição acabou. A frota inimiga venceu a guerra.")
                break 
                
        except ValueError:
            print(Fore.RED + "\n❌ Entrada inválida! Digite apenas números.")
        except IndexError:
            print(Fore.RED + "\n❌ Coordenada fora do mapa! Digite números entre 0 e 9.")
            
    print(Fore.YELLOW + f"\nFim de jogo! Você realizou {tentativas} disparos válidos.")

# Ponto de partida do script
if __name__ == "__main__":
    while True:
        jogar_partida() # Chama o jogo inteiro
        
        # Quando o jogo acaba (vitória, derrota ou 'q'), ele cai aqui:
        print(Fore.CYAN + "\n" + "="*40)
        resposta = input(Fore.YELLOW + "Deseja jogar novamente, Comandante? (s/n): ").strip().lower()
        
        if resposta != 's':
            print(Fore.GREEN + "\nFrota recolhida com sucesso. Fim de transmissão!")
            break # Quebra o loop e encerra o script de vez