# simple_script.py

def read_file(file_path):
    """Read and print the contents of a file."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: An IOError occurred while reading the file '{file_path}'.")

def main():
    """Main function to run the script."""
    # Replace 'example.txt' with the path to your file
    file_path = 'example.txt'
    read_file(file_path)

if __name__ == '__main__':
    main()
