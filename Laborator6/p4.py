import os
import sys


# cmd: python C:\Users\Hp\PycharmProjects\pythonProject31\p4.py C:\Users\Hp\Desktop\Python
def count_files_by_extension(directory_path):
    try:
        # Verifica daca directorul exista
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' not found.")

        #  lista de fișiere din director
        files = os.listdir(directory_path)

        # Dictionar pentru a stoca numărul de fișiere pentru fiecare extensie
        extension_count = {}

        for filename in files:
            _, extension = os.path.splitext(filename)
            extension = extension.lower()  # Facem extensiile să fie în litere mici pentru uniformitate

            if extension in extension_count:
                extension_count[extension] += 1
            else: extension_count[extension] = 1

        print(f"File counts by extension in '{directory_path}':")
        for ext, count in extension_count.items():
            print(f"{ext}: {count} file(s)")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]

    count_files_by_extension(directory_path)
