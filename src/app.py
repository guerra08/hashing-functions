import sys
from utils.file_reader import read_file
from core.process import process_file

def main():
    file_bytes = read_file(sys.argv[1])
    h0 = process_file(file_bytes)
    print("H0: " + h0)
main();
