import os
from glob import iglob
from random import random

from config import *


def prep_dst_dir():
    if os.path.isdir(DESTINATION_DIR):
        if len(tuple(iglob(DESTINATION_DIR + '\\**', include_hidden=True))):
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


def extract_file_attr(file_path):
    file_path = file_path[::-1]
    dot_index = file_path.find('.')
    file_name = file_path[dot_index + 1:file_path.find('\\')][::-1]
    file_type = file_path[:dot_index][::-1] if dot_index != -1 else 'Unknown'
    return file_name, file_type


def prep_type_dir(file_type):
    type_path = DESTINATION_DIR + '\\' + file_type
    if not os.path.isdir(type_path):
        os.mkdir(type_path)
    return type_path


def generate_path_name(file_path, type_path, file_name, file_type):
    if RENAME_FILES:
        file_name = id(file_path)
    first_iter = True
    new_file_path = ''
    while first_iter or os.path.isfile(new_file_path):
        new_file_path += type_path + '\\' + str(file_name)
        if not first_iter:
            new_file_path += str(random()).replace('.', '-')
        new_file_path += '.' + file_type if file_type != 'Unknown' else ''
        first_iter = False
    return new_file_path


if __name__ == '__main__':
    pass
