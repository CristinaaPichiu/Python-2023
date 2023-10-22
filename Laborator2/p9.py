def coloane_neordonate_descrescator(matrice):
    index_coloane_neordonate = []

    for coloana in range(len(matrice[0])):
        este_descrescator = True
        for rand in range(1, len(matrice)):
            if matrice[rand][coloana] <=  matrice[rand - 1][coloana]:
                este_descrescator = False
                break
        if not este_descrescator:
            index_coloane_neordonate.append(coloana)
    return index_coloane_neordonate

def afiseaza_pozitii(matrice, coloane_neordonate):
    for coloana in coloane_neordonate:
        elemente_afisate = set()
        for rand in range(1, len(matrice)):
            element_curent = matrice[rand][coloana]
            for linie_deasupra in range(rand):
                if matrice[linie_deasupra][coloana] >= element_curent:
                    pozitie = (rand, coloana)
                    if pozitie not in elemente_afisate:
                        print(f"  ({rand}, {coloana})")
                        elemente_afisate.add(pozitie)


# Exemplu de utilizare:
matrice = [[1, 2, 3, 2, 1, 1],

[2, 4, 4, 3, 7, 2],

[5, 5, 2, 5, 6, 4],

[6, 6, 7, 6, 7, 5]]

indexe = coloane_neordonate_descrescator(matrice)
print("Coloanele care nu sunt ordonate descrescător sunt:", indexe)
afiseaza_pozitii(matrice, indexe)

