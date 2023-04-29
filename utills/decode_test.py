import zlib

with open('data/html_data.txt', 'rb') as f:
    data = f.read()
    print(zlib.decompress(data).decode('utf-8'))