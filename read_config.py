import sys

try:
    filename = sys.argv[1]
except IndexError:
    print(f"Error: you must provide a file name as an argument.")
    sys.exit(1)

try:
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()

            if line and not line.startswith('#'):
                print(line)
except FileNotFoundError:
    print(f"Error: The file '{filename}' path is bad")
    sys.exit(1)


