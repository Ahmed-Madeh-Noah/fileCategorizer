from glob import iglob
from os.path import isfile

from config import *


def get_files_iter():
    files_iter = iglob(MAIN_DIR, recursive=INC_CHILD_DIRS, include_hidden=INC_HIDDEN_DIRS)
    for file_path in files_iter:
        should_ignore = False
        for ignored_path in IGNORED_DIRS:
            if ignored_path in file_path:
                should_ignore = True
        if not should_ignore and isfile(file_path):
            yield file_path


if __name__ == '__main__':
    pass
