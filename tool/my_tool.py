import sys

# Reverse file contents
def reverse_file(fname):
    with open(fname) as f:
        return reverse_string(f.read())

# Reverse a string
def reverse_string(s):
    return s[::-1]

# Driver code
if __name__ == '__main__':
    if len(sys.argv) < 2:
        quit('Usage: python3 my_tool.py [file]')
    print(reverse_file(sys.argv[1]))