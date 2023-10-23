"""
Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers)
and a start position (integer).
The function will return the song composed by going though the musical notes beginning with the start position and following the moves given as parameter.
"""


def compose(notes, moves, start_position):
    composition = []
    current_position = start_position

    for move in moves:
        composition.append(notes[current_position])
        current_position = (current_position + move) % len(notes)

    composition.append(notes[current_position])

    return composition


if __name__ == "__main__":
    notes = ["do", "re", "mi", "fa", "sol"]
    moves = [1, -3, 4, 2]
    start_position = 2

    result = compose(notes, moves, start_position)
    print(result)
