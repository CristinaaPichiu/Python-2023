from Merge_Package.merge import merge_text_files

if __name__ == "__main__":
    file_paths = [
        'data/file1.txt',
        'data/file2.txt',
        'data/file3.txt'
    ]

    output_file = 'merged_output.txt'
    separator = '_________'  

    merge_text_files(file_paths, output_file, separator)
