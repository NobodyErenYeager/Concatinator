import cv2
import os
import numpy as np
from moviepy.editor import VideoFileClip, concatenate_videoclips
from datetime import timedelta


def add_videos(folder, separator):

    # folder = input("Enter folder name: ")
    print("[STARTED]")
    save_dir = os.path.join(
        os.getcwd(), 'files', folder)

    files = os.listdir(save_dir)
    files.sort()
    for file in files:

        # other
        # height = 540
        # width = 960
        # pos = (100, 400)

        # 720
        height = 720
        width = 1280
        pos = (100, 640)

        # 1080
        # pos = (200, 880)
        # height = 1080
        # width = 1920

        image = np.zeros((height, width, 3), np.uint8)
        image[:, 0:width] = (30, 30, 33)

        cv2.putText(
            image,
            file.split(separator)[0],
            pos, cv2.FONT_HERSHEY_SIMPLEX,
            2, (195, 197, 224), 5, cv2.LINE_AA, False)

        destination_dir = os.path.join(
            save_dir, f"{file.split(separator)[0]}.mp4")
        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        video_fps = 30
        out = cv2.VideoWriter(destination_dir, fourcc,
                              video_fps, (width, height))
        for i in range(5 * video_fps):
            out.write(image)
        out.release()
        print(f"[COMPLETED] {file.split(separator)[0]}")

    return save_dir


def combine_video(folder, save_dir):

    total_seconds = 0
    clips = []
    files = os.listdir(save_dir)
    files.sort()

    with open(os.path.join(os.getcwd(), 'savefiles', f"{folder}.txt"), "w") as txt_file:
        for index, file in enumerate(files):
            if index % 2 == 0:
                # name = file.split(separator)
                # name.pop(0)
                name = file.split(".")
                name.pop(-1)
                line = f"{timedelta(seconds=total_seconds)} {'.'.join(name)}\n"
                txt_file.writelines(line)

                num_video_path = os.path.join(save_dir, files[index+1])
                num_video = cv2.VideoCapture(num_video_path)
                frames = num_video.get(cv2.CAP_PROP_FRAME_COUNT)
                fps = num_video.get(cv2.CAP_PROP_FPS)
                total_seconds += round(frames / fps)

                video_path = os.path.join(save_dir, file)
                video = cv2.VideoCapture(video_path)
                frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
                fps = video.get(cv2.CAP_PROP_FPS)
                total_seconds += round(frames / fps)

                clips.append(VideoFileClip(
                    os.path.join(save_dir, files[index+1])))
                clips.append(VideoFileClip(os.path.join(save_dir, file)))

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(os.path.join(
        os.getcwd(), 'savefiles', f"{folder}.mp4"))
    print("[COMPLETED]")
