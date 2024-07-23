from concatinator import add_videos, combine_video


folders = [
    "1. INTRODUCTION",
    "2. ADVANCED SELECTION TECHNIQUES",
    "3. VECTOR GRAPHICS",
    "4. FILTER AND MASK",
    "5. STRAWBERRY HOUSE PROJECT",
    "6. GRADATION",
    "7. ROBOT WARRIOR PROJECT",
]

for folder in folders:
    save_dir = add_videos(folder, separator=".")
    combine_video(folder, save_dir)
