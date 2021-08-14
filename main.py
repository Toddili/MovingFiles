import os


source_path = r"C:\Users\HITRA\Downloads" + '\\'
target_path = r"C:\Users\HITRA\Desktop\Filmovi" + '\\'
target_file_format = '.mp4'

for path, dir, files in os.walk(source_path):
    try:
        if files:
            for file in files:
                if file.endswith(target_file_format):
                    os.rename(path + '\\' + file,target_path + file)

    except Exception as e:
        print(e)
