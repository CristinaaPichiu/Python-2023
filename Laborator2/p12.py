def group_by_rhyme(words):
    rhyme_groups = []  # Inițializăm o listă goală pentru a stoca grupurile de cuvinte care rimează

    for word in words:
        # Flag pentru a indica dacă cuvântul a fost adăugat la un grup existent
        added_to_existing_group = False

        for group in rhyme_groups:
            # Comparam ultimele două litere ale cuvântului cu ultimele două litere ale cuvintelor din grup
            if len(word) >= 2 and any(w.endswith(word[-2:]) for w in group):
                group.append(word)
                added_to_existing_group = True
                break

        # Dacă cuvântul nu a fost adăugat la un grup existent, creăm un grup nou pentru el
        if not added_to_existing_group:
            rhyme_groups.append([word])

    return rhyme_groups

# Exemplu de utilizare:
word_list = ['ana', 'banana', 'carte', 'arme', 'parte']
result = group_by_rhyme(word_list)
print(result)
