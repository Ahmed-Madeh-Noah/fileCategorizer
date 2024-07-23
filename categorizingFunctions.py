import os
from glob import glob, iglob
from shutil import disk_usage
from time import time_ns, ctime

from config import *

log_file = open('log_file.txt', 'w')
log_file.write('::::::::::' + str(time_ns()) + '  ||  ' + ctime() + '\n')


def prep_dst_dir():
    if os.path.isdir(DESTINATION_DIR):
        if len(tuple(iglob(DESTINATION_DIR + '\\**', include_hidden=True))):
            raise IsADirectoryError('The destination directory exists and is not empty')
        os.rmdir(DESTINATION_DIR)
    os.mkdir(DESTINATION_DIR)


def get_files_iter():
    files_iter = glob(MAIN_DIR, recursive=INC_CHILD_DIRS, include_hidden=INC_HIDDEN_DIRS)
    files = []
    for file_path in files_iter:
        should_ignore = False
        for ignored_path in IGNORED_DIRS:
            if ignored_path in file_path:
                should_ignore = True
        if not should_ignore and os.path.isfile(file_path):
            files.append(file_path)
    return files


def enough_storage(files):
    needed_storage = 0
    for file in files:
        needed_storage += os.path.getsize(file)
    if disk_usage(DESTINATION_DIR)[2] - needed_storage < STORAGE_MARGIN and COPY_FILES:
        raise MemoryError('Not enough disk space to copy the files')
    return needed_storage


def extract_file_attr(file_path):
    file_path = file_path[::-1]
    slash_index = file_path.index('\\')
    dot_index = file_path[:slash_index].find('.')
    file_name = file_path[dot_index + 1:slash_index][::-1]
    file_type = file_path[:dot_index][::-1] if dot_index != -1 else 'Unknown'
    return file_name, file_type


def prep_type_dir(file_type):
    type_path = DESTINATION_DIR + '\\' + file_type
    if not os.path.isdir(type_path):
        os.mkdir(type_path)
    return type_path


def generate_path_name(file_path, type_path, file_name, file_type, index):
    if RENAME_FILES:
        file_name = id(file_path)
    new_file_path = type_path + '\\' + str(file_name) + ' - ' + str(index)
    new_file_path += '.' + file_type if file_type != 'Unknown' else ''
    return new_file_path


def paste_file(file_path, new_dist):
    if COPY_FILES:
        org_file = open(file_path, 'rb')
        tmp_file = open(new_dist, 'wb')
        tmp_file.write(org_file.read())
        tmp_file.close()
        org_file.close()
        log_file.write(':COPIED:' + file_path + ':' + new_dist + ':\n')
    else:
        os.rename(file_path, new_dist)
        log_file.write(':MOVED:' + file_path + ':' + new_dist + ':\n')


def progress_bar(completed):
    completed = round(completed)
    text = ''
    for i in range(100):
        text += '#' if i < completed else '_'
    print(text)


if __name__ == '__main__':
    pass
