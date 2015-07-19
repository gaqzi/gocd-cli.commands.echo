__all__ = ['Echo']


class Echo(object):
    def __init__(self, server, output):
        self.server = server
        self.output = output

    def run(self):
        print(self.output)
