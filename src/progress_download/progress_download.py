import requests
import shutil
import time

def download(url, target, preFunction=None, postFunction=None, chunkSize=None, bandwidthLimit=None):
    if preFunction != None:
        preFunction()

    with requests.get(url, stream=True, timeout=300) as downloadResponse:
        contentLength = int(downloadResponse.headers['Content-length'])
        downloadedSoFar=0
        if chunkSize == None:
            chunkSize=int(contentLength/100)
        startTime = time.time() #### /1000
        with open(target, 'wb') as f:
            for chunk in downloadResponse.iter_content(chunk_size=chunkSize):
                downloadedSoFar += len(chunk)
                f.write(chunk)
                _write_status(downloadedSoFar, contentLength, startTime)
                if bandwidthLimit != None:
                    timeToSleep = downloadedSoFar/bandwidthLimit + startTime - time.time()
                    if timeToSleep > 0:
                        time.sleep(timeToSleep)
    print()

    if postFunction != None:
        postFunction()

def _write_status(curbytes, maxbytes, startTime):
    (w,h) =  shutil.get_terminal_size()
    w -= 26
    percent = int(curbytes/maxbytes * 100)
    complete_width = int(curbytes/maxbytes * w)
    bps = int(curbytes/(time.time()-startTime))
    print("[{}{}] {:6s}/{:6s} {:6s}".format(u"#"*complete_width, "."*(w-complete_width), _sizeof_fmt(curbytes), _sizeof_fmt(maxbytes), _sizeof_fmt(bps,'/s')), end='\r', flush=True)

def _sizeof_fmt(num, suffix=""):
    for unit in ["B", "K", "M", "G", "T", "P", "E", "Z"]:
        if abs(num) < 1000.0:
            return f"{num:3.1f}{unit}{suffix}"
        num /= 1024.0
    return f"{num:.1f}Yi{suffix}"
