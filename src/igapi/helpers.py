import logging
import os
import appdirs


def get_conf(file):
    with open(file, 'r') as conf:
        return conf.read()


print(get_conf())
