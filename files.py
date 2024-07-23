import cv2
import os

source_dir = r"/workspaces/Concatinator/files/Digital painting with Krita 5.0 for Intermediate"

folders = os.listdir(source_dir)
folders.sort()

unwanted_files = ['tutflix.org.url']

with open(os.path.join(source_dir, 'files.txt'), 'w') as file_list:
    for folder in folders:
        folder_path = os.path.join(source_dir, folder)
        if os.path.isdir(folder_path):

            # name = folder.replace("[TutFlix.ORG]", '')
            # os.rename(folder_path, os.path.join(source_dir, name))

            # try:
            #     num = int(folder.split(".")[0])
            #     if num < 10:
            #         os.rename(folder_path, os.path.join(source_dir, f'0{folder}'))
            #         folder_path = os.path.join(source_dir, f'0{folder}')
            # except Exception as e:
            #     pass
            files = os.listdir(folder_path)
            files.sort()
            file_list.writelines(f"{folder}\n")
            for file in files:
                # if "[TutFlix.ORG]" in file:
                #     name = file.replace("[TutFlix.ORG]", '')
                #     os.rename(os.path.join(folder_path, file), os.path.join(folder_path, name))
                # try:
                #     num = int(file.split(".")[0])
                #     if num < 10:
                #         os.rename(os.path.join(folder_path, file), os.path.join(folder_path, f'0{file}'))
                # except Exception as e:
                #     pass
                if file in unwanted_files:
                    os.remove(os.path.join(folder_path, file))
                if ".mp4" in file:
                    file_path = os.path.join(folder_path, file)
                    video = cv2.VideoCapture(file_path)
                    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
                    width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
                    file_list.writelines(
                        f"\t{int(width), int(height)} | {file}\n")
                    # name = file.split(" ")
                    # name.pop(0)
                    # os.rename(os.path.join(folder_path, file), os.path.join(folder_path, ' '.join(name)))
                elif ".srt" in file:
                    os.remove(os.path.join(folder_path, file))
                elif ".vtt" in file:
                    os.remove(os.path.join(folder_path, file))
