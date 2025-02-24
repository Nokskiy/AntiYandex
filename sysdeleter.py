import os
import shutil
from sys import argv


def delete(file_path: str):
    if os.path.isfile(file_path) or os.path.islink(file_path):
        os.unlink(file_path)
    elif os.path.isdir(file_path):
        shutil.rmtree(file_path)


for file in argv[1:]:
    delete(file)
