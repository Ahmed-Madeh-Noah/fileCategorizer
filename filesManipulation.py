import os
from glob import iglob

from config import *


def prep_dst_dir():
    if os.path.isdir(DESTINATION_DIR):
        dir_not_empty = len(tuple(iglob(DESTINATION_DIR + '\\**', include_hidden=True)))
        if dir_not_empty:
            raise IsADirectoryError('The destination directory exists and is not empty')
        os.rmdir(DESTINATION_DIR)
    os.mkdir(DESTINATION_DIR)


def get_files_iter():
    files_iter = iglob(MAIN_DIR, recursive=INC_CHILD_DIRS, include_hidden=INC_HIDDEN_DIRS)
    for file_path in files_iter:
        should_ignore = False
        for ignored_path in IGNORED_DIRS:
            if ignored_path in file_path:
                should_ignore = True
        if not should_ignore and os.path.isfile(file_path):
            yield file_path


def extract_file_extension(file_path):
    file_path = file_path[::-1]
    dot_index = file_path.find('.')
    return file_path[:dot_index][::-1] if dot_index != -1 else 'Unknown'


def prep_type_dir(file_type):
    type_path = DESTINATION_DIR + '\\' + file_type
    if not os.path.isdir(type_path):
        os.mkdir(type_path)
    return type_path


if __name__ == '__main__':
    pass
