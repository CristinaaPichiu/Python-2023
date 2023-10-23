def group_by_rhyme(words):

    groups = []  # Lista pentru a stoca grupurile de cuvinte

    for word in words:
        # Găsește ultimele 2 litere ale cuvântului

        '''
        Caracterul -1 se referă la ultimul caracter din șir
        iar -2 se referă la al doilea caracter de la sfârșit
        deci word[-2:] va returna un subșir care conține ultimele două caractere ale șirului word.
        '''
        end_letters = word[-2:]

        # Caut un grup existent în care să adaug cuvântul
        added = False
        for group in groups:

            #group[0] reprezintă primul cuvânt din grupul respectiv
            #group[0][-2:] reprezintă ultimele două litere ale primului cuvânt din grupul respectiv
            if group and group[0][-2:] == end_letters:
                group.append(word)
                added = True
                break

        # Dacă cuvântul nu a fost adăugat în niciun grup existent, creează un nou grup
        if not added:
            groups.append([word])

    return groups

# Exemplu de utilizare:
words = ['ana', 'banana', 'carte', 'arme', 'parte']
result = group_by_rhyme(words)
print(result)
