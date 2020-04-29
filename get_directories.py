import os
import sys


def get_directories(labels_path, data_path):
    labels_dir = os.listdir(labels_path)
    data_dir = os.listdir(data_path)

    for file in labels_dir:
        if not file.endswith(".txt"):
            print(F"{file} was not a .txt file. Please remove this file from the directory and try again.")
            sys.exit(1)

    for file in data_dir:
        if not file.endswith(".jpg"):
            print(F"{file} was not a .jpg file. Please remove this file from the directory and try again.")
            sys.exit(2)

    labels_dir.sort()
    data_dir.sort()

    for i in range(len(data_dir)):
        img = data_dir[i]
        data_dir[i] = data_path + img

    return labels_dir, data_dir
