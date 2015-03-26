import fnmatch
import os
import re

import yaml

from consul_hiera import (
    HieraConfig,
    HIERARCHY,
)

def find_files(directory, pattern='*'):
    if not os.path.exists(directory):
        raise ValueError("Directory not found {}".format(directory))

    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            if fnmatch.filter([full_path], pattern):
                matches.append(os.path.join(root, filename))
    return matches


def find_files_regex(directory, pattern='.+'):
    pattern = re.compile(pattern)
    if not os.path.exists(directory):
        raise ValueError("Directory not found {}".format(directory))

    matches = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            if re.search(pattern, full_path):
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

        hconfig._yaml_doc = hash

    return hconfig



def convert_hierarchy_to_regex(line):
    """
    ...
    'customer/%{customer}/nodes/%{clientcert}',
    'customer/%{customer}/%{program}/%{deploy_environment}/%{role}',
    ...
    """
    pattern = r'%{\w+}'
    regex = re.compile(pattern)
    result = regex.sub('.*', line, re.DOTALL)
    return result
