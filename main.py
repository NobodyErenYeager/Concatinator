from concatinator import add_videos, combine_video


folders = [
    "01 - INTRODUCTION",
    "02 - TRANSFORMATION AND DISTORTION",
    "03 - ADVANCED LAYER FEATURES",
    "04 - PATTERNS AND TEXTURES",
    "05 - PHOTOBASHING",
    "06 - PROJECT ATLANTIC TREASURE",
    "07 - BRUSH PARAMETERS",
    "08 - PAINTERLY STYLE AND CHEAT METHODS",
    "09 - PROJECT COWBOY CACTUS",
]

for folder in folders:
    save_dir = add_videos(folder, separator=" ")
    combine_video(folder, save_dir)
