def spiral_order(m, n, a):
    k = 0
    l = 0
    result = []  # Inițializăm o listă goală pentru a stoca caracterele în ordine spirală

    while (k < m and l < n):
        # Print the first row from the remaining rows
        for i in range(l, n):
            result.append(a[k][i])

        k += 1

        # Print the last column from the remaining columns
        for i in range(k, m):
            result.append(a[i][n - 1])

        n -= 1

        # Print the last row from the remaining rows
        if (k < m):
            for i in range(n - 1, (l - 1), -1):
                result.append(a[m - 1][i])

            m -= 1

        # Print the first column from the remaining columns
        if (l < n):
            for i in range(m - 1, k - 1, -1):
                result.append(a[i][l])

            l += 1

    '''
     ''.join(result) ia fiecare element din lista result și le concatenează într-un singur șir de caractere
        fără să adauge niciun separator între ele.
    '''

    return ''.join(result)  # Returnăm șirul rezultat

if __name__ == "__main__":
    n = 4
    m = 4
    matrix = [
        ['f', 'i', 'r', 's'],
        ['n', '_', 'l', 't'],
        ['o', 'b', 'a', '_'],
        ['h', 't', 'y', 'p']
    ]

    spiral_string = spiral_order(n, m, matrix)
    print(spiral_string)
