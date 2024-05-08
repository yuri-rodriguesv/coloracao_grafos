import matplotlib.pyplot as plt
import seaborn as sns

def eh_valido(tabuleiro, linha, coluna, num):
    # Verifica se o número já está na linha
    if num in tabuleiro[linha]:
        return False
    
    # Verifica se o número já está na coluna
    for r in range(len(tabuleiro)):
        if tabuleiro[r][coluna] == num:
            return False
    
    # Verifica se o número já está na submatriz
    sqrt_n = int(len(tabuleiro) ** 0.5)
    inicio_linha, inicio_coluna = sqrt_n * (linha // sqrt_n), sqrt_n * (coluna // sqrt_n)
    for r in range(inicio_linha, inicio_linha + sqrt_n):
        for c in range(inicio_coluna, inicio_coluna + sqrt_n):
            if tabuleiro[r][c] == num:
                return False
    
    return True

def resolver_sudoku(tabuleiro, linha, coluna):
    if linha == len(tabuleiro):
        return True
    
    proxima_linha = linha + (coluna + 1) // len(tabuleiro)
    proxima_coluna = (coluna + 1) % len(tabuleiro)
    
    if tabuleiro[linha][coluna] != 0:
        return resolver_sudoku(tabuleiro, proxima_linha, proxima_coluna)
    
    for num in range(1, len(tabuleiro) + 1):
        if eh_valido(tabuleiro, linha, coluna, num):
            tabuleiro[linha][coluna] = num
            if proxima_linha == len(tabuleiro):  # Se chegou na última linha
                return resolver_sudoku(tabuleiro, 0, 0)  # Reinicia na posição (0, 0)
            if resolver_sudoku(tabuleiro, proxima_linha, proxima_coluna):
                return True
            tabuleiro[linha][coluna] = 0
    
    return False


def imprimir_tabuleiro(tabuleiro, tamanho_fonte):
    plt.figure(figsize=(6,6))
    sns.set(style="dark", font_scale=1.5)
    ax = sns.heatmap(tabuleiro, annot=True, fmt="d", cmap="YlGnBu", linewidths=1, cbar=False, square=True, 
                     linecolor='black', annot_kws={"size": tamanho_fonte, "weight": "bold", "color": "black"})
    ax.set_facecolor('white')
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.show()

def imprimir_tabuleiro_cmd(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(map(str, linha)))

# Exemplo de uso:
ordens_permitidas = [1, 4, 9, 16]
while True:
    n = int(input("Informe a ordem do tabuleiro (1, 4, 9 ou 16): "))
    if n in ordens_permitidas:
        break
    else:
        print("Ordem inválida. Por favor, escolha entre 1, 4, 9 ou 16.")

print("Você escolheu a ordem {}.".format(n))

tabuleiro = [[0 for _ in range(n)] for _ in range(n)]

print("Tabuleiro de Sudoku:")
imprimir_tabuleiro_cmd(tabuleiro)

linha_inicial = int(input("Informe a linha inicial: "))
coluna_inicial = int(input("Informe a coluna inicial: "))

if n == 1:
    tamanho_fonte = 36
elif n == 4 or n == 9:
    tamanho_fonte = 16
elif n == 16:
    tamanho_fonte = 9

if resolver_sudoku(tabuleiro, linha_inicial, coluna_inicial):
    print("\nSolução:")
    imprimir_tabuleiro_cmd(tabuleiro)
    imprimir_tabuleiro(tabuleiro, tamanho_fonte)
else:
    print("\nNão há solução para o tabuleiro.")