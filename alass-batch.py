#!/usr/bin/env python3
import os
import sys
import subprocess

def main():
    folderPaths = sys.argv[1:][0]
    video_files = []
    subtitle_files = []
    subtitle_extensions = ['.srt', '.ssa', '.ass', '.idx']
    movie_extensions = ['.mkv', '.mp4']
    

    for root, _, files in os.walk(folderPaths, topdown=False):
        for file in files:
            if file[-4:] in movie_extensions:
                full_path_video = os.path.join(root, file)
                video_files.append(full_path_video)
            if file[-4:] in subtitle_extensions:
                full_path_subtitle = os.path.join(root, file)
                subtitle_files.append(full_path_subtitle)

    for video_file in video_files:
        for subtitle_file in subtitle_files:
            if (video_file[:-4]) in subtitle_file:
                process = subprocess.Popen(os.getcwd() +'/alass-linux64 "' + video_file + '" "' + subtitle_file + '" "' + subtitle_file + '"', shell=True)
                print(process.wait())
                
                
if __name__ == "__main__":
    main()
