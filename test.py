import os
import shutil

# set the source and destination directories
src_dir = 'C:/Users/KME-Hasan/Downloads/compressed_main/'
dst_dir = 'C:/Users/KME-Hasan/Downloads/output_main/'
chunk_size = 450
# create a list of all the files in the source directory
files = os.listdir(src_dir)

# loop through the files and move every 100 files to a separate folder
for i in range(4500, len(files), chunk_size):
    # create a new folder to hold the 100 files
    folder_name = f'Folder_{i+1}'
    folder_path = os.path.join(dst_dir, folder_name)
    os.mkdir(folder_path)
    
    # move the 100 files to the new folder
    for file in files[i:i+chunk_size]:
        file_path = os.path.join(src_dir, file)
        shutil.copy(file_path, folder_path)
