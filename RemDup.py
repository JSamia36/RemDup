import argparse

def remove_duplicates(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    # Removing duplicates
    unique_lines = list(set(lines))

    with open(file, 'w') as f:
        f.writelines(unique_lines)
        print('File has been cleaned, duplicates removed')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Removes duplicate results from a file')
    parser.add_argument('-f', '--file', help='Path to file', required=True)
    args = parser.parse_args()
    remove_duplicates(args.file)