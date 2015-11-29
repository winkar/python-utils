#!/usr/bin/env python

import time

def now():
    # import pdb; pdb.set_trace()
    return time.strftime('%Y-%m-%d %X', time.localtime())
