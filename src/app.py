import os
from utils.file_reader import read_file
from core.process import process_file

def main():
    dirname = os.path.dirname(__file__)
    file_bytes = read_file(dirname +  "/" + "resources/FuncoesResumo - SHA1.mp4")
    process_file(file_bytes)
main();
