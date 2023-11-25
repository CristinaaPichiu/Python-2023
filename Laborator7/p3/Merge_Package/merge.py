def merge_text_files(file_paths, output_file, separator='\n'):
    try:
        with open(output_file, 'w') as output:
            for file_path in file_paths:
                with open(file_path, 'r') as input_file:
                    content = input_file.read()
                    output.write(content + separator)
        print(f"Files merged successfully. Merged content saved in '{output_file}'.")
    except Exception as e:
        print(f"Error: {e}")
