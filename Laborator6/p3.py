import os
import sys


# cmd:  C:\Users\Hp\PycharmProjects\pythonProject31\p3.py C:\Users\Hp\Desktop\Python

def calculate_total_size(directory_path):
    try:
        # Verifica daca directorul exista
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' not found.")

        total_size = 0

        # Itereaza prin toate fisierele din director si subdirectoare
        for foldername, subfolders, filenames in os.walk(directory_path):
            for filename in filenames:
                filepath = os.path.join(foldername, filename)
                # Aduna dimensiunea fisierului la dimensiunea totala
                total_size += os.path.getsize(filepath)

        print(f"Total size of all files in '{directory_path}': {total_size} bytes")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)
    directory_path = sys.argv[1]
    calculate_total_size(directory_path)