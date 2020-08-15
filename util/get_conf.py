import sys
import os
import configparser
args = sys.argv[1:]

file_name = os.path.join(args[1], 'config.ini')


def get_config():
    config = configparser.ConfigParser()
    config.read(file_name)
    section = config.sections()
    conf_ = {}
    for sec in section:
        conf_[sec] = {}
        for key, values in config.items(sec):
            conf_[sec][key] = values

    return conf_


conf = get_config()
