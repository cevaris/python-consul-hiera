import os

import yaml

from consul_hiera import HieraConfig
from consul_hiera import (
    HIERARCHY,
)

import os


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