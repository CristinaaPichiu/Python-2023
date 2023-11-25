import os
import sys

# cmd: python C:\Users\Hp\PycharmProjects\pythonProject31\p1.py C:\Users\Hp\Desktop\Python .py

def read_and_print_files(directory_path, file_extension):
    try:
        # verific dacă directorul există
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' not found.")

        # itereaz prin toate fișierele cu extensia specificată în director
        for filename in os.listdir(directory_path):
            if filename.endswith(file_extension):
                file_path = os.path.join(directory_path, filename)

                # deschid fișierul și citesc conținutul
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        print(f"Content of '{filename}':\n{content}\n{'-' * 30}")
                except Exception as file_error:
                    print(f"Error reading file '{filename}': {file_error}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":

    # verifică dacă sunt furnizate suficiente argumente de linie de comandă
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory_path> <file_extension>")
        sys.exit(1)

    # argumentele de linie de comandă
    directory_path = sys.argv[1]
    file_extension = sys.argv[2]

    # execută funcția principală
    read_and_print_files(directory_path, file_extension)
