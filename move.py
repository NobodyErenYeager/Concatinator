import os

source_dir = r"C:\MyPythonPrograms\Deepak\Concatinator\files\The Ultimate React Course"
destination_dir = r'C:\MyPythonPrograms\Deepak\Concatinator\files'

folders = os.listdir(source_dir)
folders.sort()

for folder in folders:
    folder_path = os.path.join(source_dir, folder)
    if os.path.isdir(folder_path):
        files = os.listdir(folder_path)
        files.sort()
        d_path_folder = os.path.join(destination_dir, folder)
        if not os.path.exists(d_path_folder):
            os.mkdir(d_path_folder)
            print(f'CREATED: {folder}')
        for file in files:
            if ".mp4" in file:
                file_path = os.path.join(folder_path, file)
                d_path_file = os.path.join(d_path_folder, file)
                os.rename(file_path, d_path_file)
                print(f"\tMOVED: {file}")
                # print(f"\t{file_path} | {d_path_file}")
