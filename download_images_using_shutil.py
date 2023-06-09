import urllib.request
import shutil
from time import sleep

def download(link, fn):
    with urllib.request.urlopen(link) as response, open(fn, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    sleep(1)

done_images = []
with open("data/done_images.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        done_images.append(line.strip())

with open("data/images.json","r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.split(":")
        link = ":".join(line[1:])
        if line[0] in done_images:
            # print("Already downloaded: "+line[0]+".jpg")
            continue
        try:
            if link.__contains__("48x48ex"):
                # download(link,"images/48x48ex/"+line[0]+".jpg")
                link = link.replace("48x48ex","492x492ex")
                download(link,"images/492x492ex/"+line[0]+".jpg")
            else:
                download(link,"images/main/"+line[0]+".jpg")
            print("Downloaded: "+line[0]+".jpg")
            done_images.append(line[0])
            with open("data/done_images.txt","a") as file:
                file.write(line[0]+"\n")
        except Exception as e:
            print("Error: "+link,e)

