# Utils for python


### Concurrent
Utils for coding concurrently

```python

from utils.concurrent import multiThread

@multiThread(10)  # the param indicate how many threads to start
def ox(x):
    return x

ox(range(10))  # this will run concurrently
```

### Log
Utils for log

```python
from utils.log import stream_handler, formatter, logger

logger.warn("test")   # the logger has been set level to warn
                      # use formatter as its default output format
                      # and will only print to stdout
```
