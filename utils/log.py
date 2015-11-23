#!/usr/bin/env python

import logging

logger = logging.getLogger("winkar_log_util")

logger.setLevel(logging.WARN)

ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)
