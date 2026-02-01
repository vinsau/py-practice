import sys

# check for arguments otherwise exit
try:
    if len(sys.argv) > 2:
        raise ValueError

    filename = sys.argv[1]
except IndexError:
    print("Error: argument is expected but not received.")
    sys.exit(1)
except ValueError:
    print("Error: only one argument is expected.")
    sys.exit(1)


try:
    count = word1_count = word2_count = 0
    word1 = 'bash'
    word2 = 'nologin'

    with open(filename, 'r') as f:
        for line in f:
            count += 1
            
            if word1 in line:
                word1_count += 1
            
            if word2 in line:
                word2_count += 1
        
        print(f"The total # of lines in '{filename}' is {count}")
        print(f"The total # of '{word1}' is {word1_count}")
        print(f"The total # of '{word2}' is {word2_count}")
except FileNotFoundError:
    print(f"Error: the file '{filename}' is invalid")
    sys.exit(1)


