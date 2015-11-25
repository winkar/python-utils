# Install
```shell
pip install winkar_utils
```

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
import logging
from utils.log import stream_handler, formatter, logger

logger.warn("test")   # the logger has been set level to warn
                      # use formatter as its default output format
                      # and will only print to stdout
logger.setLevel(logging.INFO)
                      # change log level
logger.name = "test"  # change logger name
```


### Factor
```python
from utils.factor import factor
factor(130)         # => [2,5,13]
factor(131)         # => [1,131]
```

Which will also add a factor command like linux to PATH

# Useful third-party libraries

### Pwntools
A very useful integrated pwn library.

[Pwntools github repo](https://github.com/Gallopsled/pwntools)

Can just install through pip.

```python
from pwn import *
context(arch = 'i386', os = 'linux')

r = remote('exploitme.example.com', 31337)
# EXPLOIT CODE GOES HERE
r.send(asm(shellcraft.sh()))
r.interactive()
```

### libformatstr
Library specially for format string exploit.

Install with pip.

```python
import sys
from libformatstr import FormatStr

addr = 0x08049580
system_addr = 0x080489a3

p = FormatStr()
p[addr] = system_addr

# buf is 14th argument, 4 bytes are already printed
sys.stdout.write( p.payload(14, start_len=4) )
```
