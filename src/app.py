from utils.file_reader import read_file
from hashing.sha import hash_block

def main():
    file_lines = read_file("resources/FuncoesResumo - SHA1.mp4")
    print(file_lines.__sizeof__())

main();
