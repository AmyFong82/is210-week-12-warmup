#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03 module"""


import time


class CustomLogger(object):
    """A simple custom Logger."""

    def __init__(self, logfilename):
        """Constructor for CustomLogger Class."""
        self.logfilename = logfilename
        self.msgs = []

    def log(self, msg, timestamp=None):
        """Logger"""
        if timestamp is None:
            timestamp = time.time()
        self.msgs.append((timestamp, msg))

    def flush(self):
        """Error Handler."""
        handled = []

        try:
            fhandler = open(self.logfilename, 'a')
        except IOError as open_error:
            self.log(self.logfilename)
            raise open_error
        try:
            for index, entry in enumerate(self.msgs):
                fhandler.write(str(entry) + '\n')
                handled.append(index)
        except IOError as msgs_loop:
            self.log(msgs_loop)
        else:
            for index in handled[::-1]:
                del self.msgs[index]
        finally:
            fhandler.close()
