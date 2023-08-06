import sys
import zipfile
import os
import shutil
exe = sys.executable
asset_path = os.getcwd()+"//__temp_bit7__"
def extract_assets():
    try:
        os.mkdir(asset_path)
    except:
        pass
    exez=zipfile.ZipFile(exe)
    exez.extractall(asset_path)
def close_assets():
    try:
        shutil.rmtree(asset_path)
    except:
        pass