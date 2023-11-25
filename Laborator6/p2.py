import os

# path: C:\Users\Hp\Desktop\Python2

def rename_files_with_sequential_prefix(directory_path):
    try:
        # verific dacă directorul există
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory '{directory_path}' not found.")

        #  lista de fișiere din director
        files = os.listdir(directory_path)

        # sortez fișierele în ordine lexicografică
        files.sort()

        # iterez prin fiecare fișier și redenumesc cu prefix numeric
        for i, filename in enumerate(files, start=1):
            old_path = os.path.join(directory_path, filename)
            new_name = f"file{i}.txt"
            new_path = os.path.join(directory_path, new_name)

            # Rename fișier
            os.rename(old_path, new_path)

            print(f"Renamed '{filename}' to '{new_name}'")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":

    directory_path = input("Enter the directory path: ")
    rename_files_with_sequential_prefix(directory_path)
