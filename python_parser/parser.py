class Parser:
    def parse_file(self, filename):
        with open(filename, 'r') as f:
            return self.parse(f.read())

    def parse(self, content):
        raise NotImplementedError
