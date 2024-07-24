from os import remove, makedirs, rename

from categorizingFunctions import time_ns, progress_bar

UPDATING_DURATION = 1 * 10 ** 9

if __name__ == '__main__':
    try:
        log_file = open('log_file.txt', 'r', encoding='utf-8')
        lines = log_file.readlines()
        copy_mode = lines[0].split('?')[1] == 'True'
        lastFileIndex = len(lines) - 3
        startTime = time_ns()
        lastPrint = startTime
        print('The undoing process has started\n')
        for index, line in enumerate(lines[1:-1]):
            if copy_mode:
                remove(line.strip())
            else:
                current, original = line.strip().split('|')
                path = original[::-1]
                path = path[-1:path.find('\\') - 1:-1]
                try:
                    makedirs(path)
                except FileExistsError:
                    pass
                rename(current, original)
            currentTime = time_ns()
            if currentTime - lastPrint >= UPDATING_DURATION or index == lastFileIndex:
                lastPrint = currentTime
                completed = round(index * 100 / lastFileIndex, 2)
                print(completed, '% of the process is completed,', round((currentTime - startTime) / 10 ** 9, 1),
                      'seconds has passed')
                progress_bar(completed)
        log_file.close()
    except FileNotFoundError:
        print('log_file.txt not found, can\'t undo anything')
