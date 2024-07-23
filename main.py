from time import time_ns

import filesManipulation as fM

if __name__ == '__main__':
    fM.prep_dst_dir()
    filesPath = fM.get_files_iter()
    totalStorage = fM.enough_storage(filesPath)
    doneStorage = 0
    lastPrint = time_ns()
    for index, filePath in enumerate(filesPath):
        fileName, fileType = fM.extract_file_attr(filePath)
        typePath = fM.prep_type_dir(fileType)
        newDist = fM.generate_path_name(filePath, typePath, fileName, fileType, index)
        fM.paste_file(filePath, newDist)
        doneStorage += fM.os.path.getsize(filePath)
        currentTime = time_ns()
        if currentTime - lastPrint >= fM.UPDATING_DURATION:
            lastPrint = currentTime
            completed = round(doneStorage * 100 / totalStorage, 1)
            print(completed, '% of the process is completed')
            fM.progress_bar(completed)
    print('Process Completed Successfully')
