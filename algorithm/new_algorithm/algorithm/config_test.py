#!/usr/local/bin/python
#Author: Benjamin Ross(bpross)
#Date: 11/10

"""
Tests the configuration class
"""

from configuration import Configuration

config = Configuration()

test = config.is_empty()
print test
