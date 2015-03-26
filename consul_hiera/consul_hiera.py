HIERARCHY=':hierarchy'

class HieraConfig(object):
    def __init__(self):
        self._yaml_doc = ""
        self.hierarchy = []

    def validate(self):
        return False


class ConsulHiera(object):
    def __init__(self):
        self.hiera_file_path = 'files/hiera.yaml'
