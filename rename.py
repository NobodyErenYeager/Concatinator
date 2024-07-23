import os

source_dir = r"/workspaces/Concatinator/files/Digital Painting with Krita 5.0 Advanced"
separater = " "
red_num = 0

# files = os.listdir(source_dir)
# files.sort()

# for file in files:
#     name = file.split(separater)
#     name[0] = int(name[0]) - red_num
#     name[0] = f"0{name[0]}" if int(name[0]) < 10 else str(name[0])
#     # ext = name[-1]
#     # print(name[0], file)
#     # name = separater.join(name).split(" - ")
#     # name = f"{name[0]}.{ext}"
#     # print(name)
#     os.rename(os.path.join(source_dir, file), os.path.join(source_dir, separater.join(name)))
#     print(separater.join(name))


folders = os.listdir(source_dir)
folders.sort()


for folder in folders:
    files = os.listdir(os.path.join(source_dir, folder))
    files.sort()
    print(folder)
    red_num = int(files[0].split(separater)[0]) - 1
    for file in files:
        name = file.split(separater)
        name[0] = int(name[0]) - red_num
        name[0] = f"0{name[0]}" if int(name[0]) < 10 else str(name[0])
        # print(name[0], file)
        os.rename(os.path.join(source_dir, folder, file), os.path.join(source_dir, folder, separater.join(name)))
        print("\t", separater.join(name))
