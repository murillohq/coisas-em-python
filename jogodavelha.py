def exibir_tabuleiro(tab):
    for i in range(0, 9, 3):
        print(f" {tab[i]} | {tab[i+1]} | {tab[i+2]} ")
        if i < 6:
            print("---+---+---")

def verificar_vitoria(tab, jogador):
    condicoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8], 
        [0, 4, 8], [2, 4, 6]             
    ]
    for c in condicoes:
        if tab[c[0]] == tab[c[1]] == tab[c[2]] == jogador:
            return True
    return False

def jogar():
    tabuleiro = [str(i) for i in range(9)] 
    turno = "X"
    jogadas = 0

    while jogadas < 9:
        exibir_tabuleiro(tabuleiro)
        try:
            escolha = int(input(f"\nJogador {turno}, escolha uma posição (0-8): "))
            if tabuleiro[escolha] in ["X", "O"]:
                print("Posição ocupada! Tente novamente.")
                continue
        except (ValueError, IndexError):
            print("Entrada inválida! Digite um número de 0 a 8.")
            continue

        tabuleiro[escolha] = turno
        jogadas += 1

        if verificar_vitoria(tabuleiro, turno):
            exibir_tabuleiro(tabuleiro)
            print(f"\nParabéns! O jogador {turno} venceu!")
            return

        turno = "O" if turno == "X" else "X"

    exibir_tabuleiro(tabuleiro)
    print("\nEmpate! Deu velha.")

if __name__ == "__main__":
    jogar()
