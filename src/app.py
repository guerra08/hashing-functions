import os
from utils.file_reader import read_file
from crypto.sha import hash_block

def main():
    dirname = os.path.dirname(__file__)
    file_bytes = read_file(dirname +  "/" + "resources/FuncoesResumo - SHA1.mp4")
main();
