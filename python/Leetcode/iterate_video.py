import os
import subprocess

directory = "/Volumes/ONE TOUCH/Video/Decolonize"
os.chdir(directory)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".mov") and not file.startswith("."):
        print(filename) #do your video process here
        beginning_name, ending_string = filename.split(".mov")
        command = f'ffmpeg -i {filename} -vcodec h264 {beginning_name}.mp4'
        print(command)
        os.system(command)

    else:
        continue
