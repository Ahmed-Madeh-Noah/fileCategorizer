import categorizingFunctions as cF

if __name__ == '__main__':
    print('Checking the destination directory')
    cF.prep_dst_dir()
    print('The destination directory is alright')

    print('Collecting files\' paths')
    filesPath = cF.get_files_iter()
    print('Files\' paths collected')

    print('Checking if there is enough storage')
    totalStorage = cF.enough_storage(filesPath)
    print('Enough storage is present')

    doneStorage = 0
    lastPrint = cF.time_ns()
    print('Process started')
    for index, filePath in enumerate(filesPath):
        try:
            fileName, fileType = cF.extract_file_attr(filePath)
            typePath = cF.prep_type_dir(fileType)
            newDist = cF.generate_path_name(filePath, typePath, fileName, fileType, index)
            cF.paste_file(filePath, newDist)
            doneStorage += cF.os.path.getsize(filePath)
            currentTime = cF.time_ns()
            if currentTime - lastPrint >= cF.UPDATING_DURATION:
                lastPrint = currentTime
                completed = round(doneStorage * 100 / totalStorage, 2)
                print(completed, '% of the process is completed')
                cF.progress_bar(completed)
        except BaseException as error:
            print(filePath)
            cF.log_file.close()
            raise
    cF.progress_bar(100)
    print('Process Completed Successfully')
    cF.log_file.write(str(cF.time_ns()) + '  ||  ' + cF.ctime() + '>>>>>' + '\n')
    cF.log_file.close()
