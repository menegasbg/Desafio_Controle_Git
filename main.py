from colorama import Fore, init
from assets.map import criar_tabuleiro, posicionar_navios, exibir_tabuleiro

# Inicializa o colorama para as cores funcionarem direitinho
init(autoreset=True)

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