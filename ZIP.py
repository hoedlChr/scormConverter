import zipfile
import shutil
import io
import os
import stat
def extract_files(zipfile_path):#file.zip
    with zipfile.ZipFile(zipfile_path, 'r') as zip_ref:
        zip_ref.extractall(zipfile_path[:-4])
    os.unlink(zipfile_path)


def zip_files(folder_to_zip):#folder
    with zipfile.ZipFile(folder_to_zip+".zip", 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_to_zip):
            for file in files:
                filepath = os.path.join(root, file)
                arcname = os.path.relpath(filepath, folder_to_zip)
                zipf.write(filepath, arcname)
    try:
        shutil.rmtree(folder_to_zip)
    except OSError as e:
        print("Error: %s : %s" % (folder_to_zip, e.strerror))