def loop(mapping):
    visited = set()  # Folosim un set pentru a urmări cheile pe care le-am vizitat
    result = []  # Lista în care vom adăuga obiectele pe care le găsim

    current_key = 'start'

    while current_key not in visited:
        visited.add(current_key)  # Adăugăm cheia curentă în setul de vizitate
        result.append(current_key)  # Adăugăm cheia curentă în lista rezultat

        # Obținem următoarea cheie din dicționar
        next_key = mapping.get(current_key)

        # Dacă cheia următoare nu există în dicționar sau este o buclă, oprim procesul
        if next_key is None or next_key in visited:
            break

        current_key = next_key  # Actualizăm cheia curentă cu cheia următoare

    return result

# Exemplu de utilizare:
mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
result = loop(mapping)
print(result)
