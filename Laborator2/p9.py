def verificare_ordonare_coloane(matrice):
    n = len(matrice)
    m = len(matrice[0])

    elemente_neordonate = []

    for coloana in range(m):
        for rand in range(1, n):
            if matrice[rand][coloana] <= matrice[rand - 1][coloana]:
                elemente_neordonate.append((rand, coloana))

    if elemente_neordonate:
        for pozitie in elemente_neordonate:
            print(f"({pozitie[0]}, {pozitie[1]})")
    else:
        print("Toate coloanele sunt ordonate crescător de sus în jos.")

# Exemplu de utilizare:
matrice = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

verificare_ordonare_coloane(matrice)
