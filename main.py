import filesManipulation as fM

if __name__ == '__main__':
    fM.prep_dst_dir()
    filesPath = fM.get_files_iter()
    for filePath in filesPath:
        fileType = fM.extract_file_extension(filePath)
        type_path = fM.prep_type_dir(fileType)
