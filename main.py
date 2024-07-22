import filesManipulation as fM

if __name__ == '__main__':
    fM.prepare_dst_dir()
    filesPath = fM.get_files_iter()
    for filePath in filesPath:
        file_type = fM.extract_file_extension(filePath)
