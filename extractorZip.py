# coding: utf-8

import os.path
import sys
import zipfile

def principal(path):
    if not os.path.exists(path):
        print("Arquivo {} não existe".format(path))
        sys.exit(-1)
    else:
        zfile = zipfile.ZipFile(path)
        zfile.extractall()
        print("Arquivos Extraidos")

if __name__ == "__main__":
    principal(sys.argv([1]))
