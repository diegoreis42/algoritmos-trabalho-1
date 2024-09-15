#! /usr/bin/env python3

import sys

def are_files_equal(file1_path, file2_path):
    try:
        with open(file1_path, 'rb') as file1, open(file2_path, 'rb') as file2:
            while True:
                chunk1 = file1.read(8192)
                chunk2 = file2.read(8192)

                if chunk1 != chunk2:
                    return False

                if not chunk1:  
                    return True

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return False
    except IOError as e:
        print(f"Error: {e}")
        return False

def main():
    if len(sys.argv) != 3:
        print("Usage: python compare_files.py <file1> <file2>")
        sys.exit(1)

    file1_path = sys.argv[1]
    file2_path = sys.argv[2]

    if are_files_equal(file1_path, file2_path):
        print("The files are equal.")
    else:
        print("The files are not equal.")

if __name__ == "__main__":
    main()
