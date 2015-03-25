HIERARCHY=':hierarchy'

class HieraConfig(object):
    def __init__(self):
        self.yaml_doc = ""
        self.hierarchy = []


class ConsulHiera(object):
    def __init__(self):
        self.hiera_file_path = 'files/hiera.yaml'
