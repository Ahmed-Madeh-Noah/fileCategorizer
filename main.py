from time import time_ns

import categorizingFunctions as cF

if __name__ == '__main__':
    cF.prep_dst_dir()
    filesPath = cF.get_files_iter()
    totalStorage = cF.enough_storage(filesPath)
    doneStorage = 0
    lastPrint = time_ns()
    for index, filePath in enumerate(filesPath):
        fileName, fileType = cF.extract_file_attr(filePath)
        typePath = cF.prep_type_dir(fileType)
        newDist = cF.generate_path_name(filePath, typePath, fileName, fileType, index)
        cF.paste_file(filePath, newDist)
        doneStorage += cF.os.path.getsize(filePath)
        currentTime = time_ns()
        if currentTime - lastPrint >= cF.UPDATING_DURATION:
            lastPrint = currentTime
            completed = round(doneStorage * 100 / totalStorage, 1)
            print(completed, '% of the process is completed')
            cF.progress_bar(completed)
    print('Process Completed Successfully')
