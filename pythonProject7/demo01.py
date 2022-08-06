# 失败
import os
from PIL import Image

file_dir = "D:\ProgramD\x30~39\hh30~39"
for i in os.listdir(file_dir):
    dir_path = os.path.join(file_dir,i)
    if os.path.isdir(dir_path):
        file_label = Image.open(os.path.join(dir_path,"label.png"))
        file_name = i.split("_")[0]
        file_label.save("label/{}.png".format(file_name))
        print(file_name)