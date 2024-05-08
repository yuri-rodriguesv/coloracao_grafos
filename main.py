import matplotlib.pyplot as plt  # Importa a biblioteca para plotagem de gráficos
import seaborn as sns  # Importa a biblioteca seaborn para estilização dos gráficos

def eh_valido(tabuleiro, linha, coluna, num):
    # Verifica se o número já está na linha
    if num in tabuleiro[linha]:
        return False  # Retorna False se o número já estiver na linha
    
    # Verifica se o número já está na coluna
    for r in range(len(tabuleiro)):
        if tabuleiro[r][coluna] == num:
            return False  # Retorna False se o número já estiver na coluna
    
    # Verifica se o número já está na submatriz
    sqrt_n = int(len(tabuleiro) ** 0.5)  # Calcula a raiz quadrada do tamanho do tabuleiro
    inicio_linha, inicio_coluna = sqrt_n * (linha // sqrt_n), sqrt_n * (coluna // sqrt_n)  # Encontra o início da submatriz
    for r in range(inicio_linha, inicio_linha + sqrt_n):
        for c in range(inicio_coluna, inicio_coluna + sqrt_n):
            if tabuleiro[r][c] == num:
                return False  # Retorna False se o número já estiver na submatriz
    
    return True  # Retorna True se o número for válido na posição especificada

def resolver_sudoku(tabuleiro, linha, coluna):
    if linha == len(tabuleiro):  # Verifica se atingiu a última linha, indicando o final da resolução
        return True  # Retorna True indicando que o tabuleiro foi resolvido com sucesso
    
    proxima_linha = linha + (coluna + 1) // len(tabuleiro)  # Calcula a próxima linha
    proxima_coluna = (coluna + 1) % len(tabuleiro)  # Calcula a próxima coluna
    
    if tabuleiro[linha][coluna] != 0:  # Verifica se a célula já contém um número pré-definido
        return resolver_sudoku(tabuleiro, proxima_linha, proxima_coluna)  # Continua para a próxima célula
    
    for num in range(1, len(tabuleiro) + 1):  # Tenta colocar números de 1 a N no tabuleiro
        if eh_valido(tabuleiro, linha, coluna, num):  # Verifica se o número é válido na posição atual
            tabuleiro[linha][coluna] = num  # Coloca o número na posição atual do tabuleiro
            if proxima_linha == len(tabuleiro):  # Se chegou na última linha
                return resolver_sudoku(tabuleiro, 0, 0)  # Reinicia na posição (0, 0)
            if resolver_sudoku(tabuleiro, proxima_linha, proxima_coluna):
                return True  # Se o tabuleiro foi resolvido com sucesso, retorna True
            tabuleiro[linha][coluna] = 0  # Se a solução falhar, volta e tenta outro número
    
    return False  # Retorna False se não foi possível encontrar uma solução válida para o tabuleiro

def imprimir_tabuleiro(tabuleiro, tamanho_fonte):
    plt.figure(figsize=(6,6))  # Configura o tamanho da figura
    sns.set(style="dark", font_scale=1.5)  # Configura o estilo e o tamanho da fonte
    ax = sns.heatmap(tabuleiro, annot=True, fmt="d", cmap="YlGnBu", linewidths=1, cbar=False, square=True, 
                     linecolor='black', annot_kws={"size": tamanho_fonte, "weight": "bold", "color": "black"})  # Cria o mapa de calor
    ax.set_facecolor('white')  # Configura a cor de fundo
    ax.set_xticklabels([])  # Remove os rótulos do eixo x
    ax.set_yticklabels([])  # Remove os rótulos do eixo y
    plt.show()  # Mostra o tabuleiro

def imprimir_tabuleiro_cmd(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(map(str, linha)))  # Imprime cada linha do tabuleiro separando os elementos por espaço

# Exemplo de uso:
ordens_permitidas = [1, 4, 9, 16]  # Lista de ordens permitidas para o tabuleiro Sudoku
while True:
    n = int(input("Informe a ordem do tabuleiro (1, 4, 9 ou 16): "))  # Solicita ao usuário a ordem do tabuleiro
    if n in ordens_permitidas:
        break  # Sai do loop se a ordem informada for válida
    else:
        print("Ordem inválida. Por favor, escolha entre 1, 4, 9 ou 16.")  # Informa ao usuário que a ordem é inválida

print("Você escolheu a ordem {}.".format(n))  # Informa ao usuário a ordem escolhida

tabuleiro = [[0 for _ in range(n)] for _ in range(n)]  # Cria um tabuleiro vazio com a ordem escolhida

print("Tabuleiro de Sudoku:")
imprimir_tabuleiro_cmd(tabuleiro)  # Imprime o tabuleiro vazio no formato de texto

linha_inicial = int(input("Informe a linha inicial: "))  # Solicita ao usuário a linha inicial para começar a resolver
coluna_inicial = int(input("Informe a coluna inicial: "))  # Solicita ao usuário a coluna inicial para começar a resolver

if n == 1:
    tamanho_fonte = 36  # Tamanho da fonte para tabuleiros de ordem 1
elif n == 4 or n == 9:
    tamanho_fonte = 16  # Tamanho da fonte para tabuleiros de ordem 4 ou 9
elif n == 16:
    tamanho_fonte = 9  # Tamanho da fonte para tabuleiros de ordem 16

if resolver_sudoku(tabuleiro, linha_inicial, coluna_inicial):  # Tenta resolver o tabuleiro
    print("\nSolução:")  # Informa ao usuário que uma solução foi encontrada
    imprimir_tabuleiro_cmd(tabuleiro)  # Imprime a solução no formato de texto
    imprimir_tabuleiro(tabuleiro, tamanho_fonte)  # Plota a solução
else:
    print("\nNão há solução para o tabuleiro.")  # Informa ao usuário que não foi possível encontrar uma solução