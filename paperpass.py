import json

__version__ = "0.1"

class PaperPass:
    """ This Class construct first pass of a paper"""
    # class var
    outline = {}
    category = {}

    def __init__(self, outline):
        self.outline = outline

    def outputjson(self, filename):
        fp = open(filename, 'w')
        json.dump(self.outline, fp)


if __name__ == "__main__":
    import sys

    a = PaperPass({3:2,2:1})
    a.outputjson(sys.argv[1])
