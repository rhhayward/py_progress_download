### py_progress_download

This package provides a convenient way to download a URL to a file with a
progress status written to the screen during the download.  The only
installation requirement is `requests`.

### Usage

Import as `from progress_download import progress_download`.  This will
give a `progress_download.download` method.

download arguments:
* `URL` - mandatory string, url to download from.
* `filename`  - mandatory string, filename to write to.
* `chunkSize`  - optional positive integer, defaults to 1/100 of file size
* `preFunction` and `postFunction` - optional functions to execution
   before and after download.
* `bandwidthLimit` - optional positive integer, defaults to `+inf`.
   download will be throttled to this many bytes per second.

### Example

```
from progress_download import progress_download

URL = 'http://u.r.l/file.zip'

### Simplest usage
progress_download.download(URL, './file.zip')

### Set how much to download at a time.  Default is size of file / 100
progress_download.download(URL, './file.zip', chunkSize=1024)

### Execute a function before and after download
def before():
    print("before")

def after():
    print("after")

progress_download.download(URL, './file.zip', preFunction=before, postFunction=after)

### Limit bandwidth to 1 MB/s
progress_download.download(URL, './file.zip', bandwidthLimit=1024*1024)

```
