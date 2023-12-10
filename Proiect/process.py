import os
import sys


def get_command():
    try:
        return sys.argv[1]
    except IndexError:
        print("Trebuie să introduci una dintre comenzile: view, suspend, resume, kill, run, cu sintaxa potrivita!")
        return None


def is_syntax_correct(command, args):
    is_correct = False
    if command == "view" and not args:
        is_correct = True
    elif command == "suspend" and len(args) == 1 and args[0].isdigit():
        is_correct = True
    elif command == "resume" and len(args) == 1 and args[0].isdigit():
        is_correct = True
    elif command == "kill" and len(args) == 1 and args[0].isdigit():
        is_correct = True
    elif command == "run" and len(args) == 2 and os.path.isfile(args[0]):
        is_correct = True
    return is_correct


if __name__ == "__main__":
    comanda = get_command()
    argumente = sys.argv[2:]
    print(is_syntax_correct(comanda, argumente))
