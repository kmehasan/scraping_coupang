import urllib.request
import shutil

def download(link, fn):
    with urllib.request.urlopen(link) as response, open(fn, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

with open("data/images.json","r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.split(":")
        link = ":".join(line[1:])
        try:
            if link.__contains__("48x48ex"):
                download(link,"images/48x48ex/"+line[0]+".jpg")
                link = link.replace("48x48ex","492x492ex")
                download(link,"images/492x492ex/"+line[0]+".jpg")
            else:
                download(link,"images/main/"+line[0]+".jpg")
            print("Downloaded: "+line[0]+".jpg")
        except Exception as e:
            print("Error: "+link,e)

