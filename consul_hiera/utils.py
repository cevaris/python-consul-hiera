import fnmatch
import os

import yaml

from consul_hiera import (
    HieraConfig,
    HIERARCHY,
)

def find_files(directory, pattern='*'):
    if not os.path.exists(directory):
        raise ValueError("Directory not found {}".format(directory))
    if not os.path.isdir(directory):
        raise ValueError("File not directory: {}".format(directory))

    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, pattern):
            matches.append(os.path.join(root, filename))
    return matches


def find_yaml_files(directory):
    return find_files(directory, pattern='*.yaml')


def parse_hiera_config(config_path):
    """
    Given file path to valid hiera yaml file, parse yaml
    return HieraConfig object
    """
    if not os.path.exists(config_path):
        raise ValueError("File not found {}".format(config_path))

    hconfig = HieraConfig()
    with open(config_path) as config_file:
        hash = yaml.load(config_file)

        if HIERARCHY in hash:
            hconfig.hierarchy = hash[HIERARCHY]

        hconfig.yaml_doc = hash

    return hconfig
