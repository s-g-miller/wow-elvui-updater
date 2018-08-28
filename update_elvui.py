from urllib.request import urlopen
from zipfile import ZipFile
from io import BytesIO
from uuid import uuid4
from os import mkdir
from shutil import copytree, rmtree

elvui_url = "https://git.tukui.org/elvui/elvui/-/archive/master/elvui-master.zip"
wow_addon_dir = "C:/Program Files (x86)/World of Warcraft/Interface/AddOns"

print(f"Downloading latest ElvUI from {elvui_url} ... ", end="", flush=True)
response = urlopen(elvui_url)
archive = response.read()
response.close()
print(f"Downloaded {len(archive)} bytes", flush=True)

uniq = uuid4()
temp_dir = f"C:/Temp/{uniq}"
mkdir(temp_dir)

with ZipFile(BytesIO(archive)) as addon_zip:
    print(f"Extracting archive to {temp_dir} ... ", end="", flush=True)
    addon_zip.extractall(temp_dir)
    print("Completed", flush=True)
    print("Removing existing installation... ", end="", flush=True)
    rmtree(f"{wow_addon_dir}/ElvUI")
    rmtree(f"{wow_addon_dir}/ElvUI_Config")
    print("Completed", flush=True)
    print("Copying new version... ", end="", flush=True)
    copytree(f"{temp_dir}/elvui-master/ElvUI", f"{wow_addon_dir}/ElvUI")
    copytree(f"{temp_dir}/elvui-master/ElvUI_Config", f"{wow_addon_dir}/ElvUI_Config")
    print("Completed", flush=True)
    print("Tidying up... ", end="", flush=True)
    rmtree(temp_dir)
    print("Completed", flush=True)
