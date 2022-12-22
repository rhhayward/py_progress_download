### py_progress_download

This package provides a convenient way to download a URL to a file with a
progress status written to the screen during the download.  The only
installation requirement is `requests`.

### Usage

Import as `from progress_download import progress_download`.  This will
give a `progress_download.download` method.  It takes two mandatory
arguments: URL and filename to write to.  `chunkSize` may be provided
as a positive integer.  `preFunction` and `postFunction` may be
provided as functions which will be called before and after the download
executes.

### Example

```
from progress_download import progress_download

URL = 'http://u.r.l/file.zip'

### Simple usage
progress_download.download(URL, './file.zip')

### Set how much to download at a time.  Default is size of file / 100
progress_download.download(URL, './file.zip', chunkSize=1024)

### Execute a function before and after download
def before():
    print("before")

def after():
    print("after")

progress_download.download(URL, './file.zip', preFunction=before, postFunction=after)

```
