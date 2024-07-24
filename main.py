import categorizingFunctions as cF

if __name__ == '__main__':
    print('Checking the destination directory')
    cF.prep_dst_dir()
    print('The destination directory is alright\n')

    print('Collecting files\' paths')
    filesPath = cF.get_files_iter()
    print('Files\' paths collected\n')

    print('Checking if there is enough storage')
    totalStorage = cF.enough_storage(filesPath)
    print('Enough storage is present\n')

    doneStorage = 0
    lastFileIndex = len(filesPath) - 1
    startTime = cF.time_ns()
    lastPrint = startTime
    print('Process started\n')
    for index, filePath in enumerate(filesPath):
        try:
            fileName, fileType = cF.extract_file_attr(filePath)
            typePath = cF.prep_type_dir(fileType)
            newDist = cF.generate_path_name(filePath, typePath, fileName, fileType, index)
            doneStorage += cF.os.path.getsize(filePath)
            cF.paste_file(filePath, newDist)
            currentTime = cF.time_ns()
            if currentTime - lastPrint >= cF.UPDATING_DURATION or index == lastFileIndex:
                lastPrint = currentTime
                completed = round(doneStorage * 100 / totalStorage, 2)
                print(completed, '% of the process is completed,', round((currentTime - startTime) / 10 ** 9, 1),
                      'seconds has passed')
                cF.progress_bar(completed)
        except BaseException as error:
            print(filePath)
            cF.log_file.close()
            raise
    print('\nProcess Completed Successfully')
    cF.log_file.write(cF.ctime() + '|' + str(cF.time_ns()) + ' >>>>>' + '\n')
    cF.log_file.close()
