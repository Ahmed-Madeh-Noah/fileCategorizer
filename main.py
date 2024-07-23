import filesManipulation as fM

if __name__ == '__main__':
    # fM.prep_dst_dir() remove comment at exec
    filesPath = fM.get_files_iter()
    for filePath in filesPath:
        fileName, fileType = fM.extract_file_attr(filePath)
        typePath = fM.prep_type_dir(fileType)
        newDist = fM.generate_path_name(filePath, typePath, fileName, fileType)
