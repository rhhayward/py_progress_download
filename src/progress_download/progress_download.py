import requests
import shutil

def download(url, target, preFunction=None, postFunction=None, chunkSize=None):
    if preFunction != None:
        preFunction()

    with requests.get(url, stream=True, timeout=300) as downloadResponse:
        contentLength = int(downloadResponse.headers['Content-length'])
        downloadedSoFar=0
        if chunkSize == None:
            chunkSize=int(contentLength/100)
        with open(target, 'wb') as f:
            for chunk in downloadResponse.iter_content(chunk_size=chunkSize):
                downloadedSoFar += len(chunk)
                f.write(chunk)
                _write_status(downloadedSoFar, contentLength)
    print()

    if postFunction != None:
        postFunction()

def _write_status(curbytes, maxbytes):
    (w,h) =  shutil.get_terminal_size()
    w -= 20
    percent = int(curbytes/maxbytes * 100)
    complete_width = int(curbytes/maxbytes * w)
    print("[{}{}] {:8s}/{:8s}".format(u"#"*complete_width, "."*(w-complete_width), _sizeof_fmt(curbytes), _sizeof_fmt(maxbytes)), end='\r', flush=True)

def _sizeof_fmt(num, suffix=""):
    for unit in ["B", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"
