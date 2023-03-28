#!/usr/bin/env python
import sys
from functools import partial
from itertools import count
from multiprocessing.dummy import Pool # use threads
from urllib.request import HTTPError, Request, urlopen


def download_chunk(url, byterange):
    req = Request(url, headers=dict(Range='bytes=%d-%d' % byterange))
    try:
        return urlopen(req).read()
    except HTTPError as e:
        return b''  if e.code == 416 else None  # treat range error as EOF
    except EnvironmentError:
        return None
def download(url, filename):
    pool = Pool(4) # define number of concurrent connections
    chunksize = 1 << 16
    ranges = zip(count(0, chunksize), count(chunksize - 1, chunksize))
    with open(filename, 'wb') as file:
        for s in pool.imap(partial(download_chunk, url), ranges):
            if not s:
                break # error or EOF
            file.write(s)
            if len(s) != chunksize:
                break  # EOF (servers with no Range support end up here)

with open("data/images.json","r") as file:
    lines = file.readlines()
    for line in lines:
        line = line.split(":")
        link = ":".join(line[1:])
        try:
            print(link)
            download(link,"images/"+line[0]+".jpg")
            print("Downloaded: "+link)
        except:
            pass

