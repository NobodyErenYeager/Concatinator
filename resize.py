import cv2
import os
import moviepy.editor as mp

source_dir = r"C:\MyPythonPrograms\Deepak\Concatinator\files\The Complete SQL Bootcamp"
resized_dir = os.path.join(os.getcwd(), 'resized')

folders = os.listdir(source_dir)
folders.sort()

resolution = (1280, 720)


for folder in folders:
    folder_path = os.path.join(source_dir, folder)
    if os.path.isdir(folder_path):
        print(folder)
        files = os.listdir(folder_path)
        files.sort()
        for file in files:
            if ".mp4" in file:
                file_path = os.path.join(folder_path, file)
                video = cv2.VideoCapture(file_path)
                width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
                height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)

                if (width, height) != resolution:
                    resized_folder = os.path.join(resized_dir, folder)
                    if not os.path.exists(resized_folder):
                        os.mkdir(resized_folder)
                    clip = mp.VideoFileClip(file_path)
                    clip_resized = clip.resize(width=resolution[0], height=resolution[1])
                    clip_resized.write_videofile(os.path.join(resized_folder, file))