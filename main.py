def torre_hanoi(numero_discos, origem, destino, auxiliar):
    if numero_discos == 1:
        print(f"Mova o disco 1 da torre {origem} para a torre {destino}.")
    else:
        torre_hanoi(numero_discos - 1, origem, auxiliar, destino)
        print(f"Mova o disco {numero_discos} da torre {origem} para a torre {destino}.")
        torre_hanoi(numero_discos - 1, auxiliar, destino, origem)

def main():
    numero_discos = int(input("Digite o número de discos: "))
    origem = input("Digite a torre de origem (A, B ou C): ").upper()
    destino = input("Digite a torre d   e destino (A, B ou C): ").upper()

    torres_possiveis = {'A', 'B', 'C'}
    if origem not in torres_possiveis or destino not in torres_possiveis:
        print("Torre inválida. Por favor, escolha entre A, B ou C.")
        return
    if origem == destino:
        print("A torre de origem e destino devem ser diferentes.")
        return

    torres = torres_possiveis - {origem, destino}
    auxiliar = torres.pop()

    print(f"\nPassos para resolver a Torre de Hanói com {numero_discos} discos:")
    torre_hanoi(numero_discos, origem, destino, auxiliar)

if __name__ == "__main__":
    main()
