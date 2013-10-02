import json

class PaperPass:

    # class var
    outline = {}

    def __init__(self, outline):
        self.outline = outline

    def outputjson(self, filename):
        fp = open(filename, 'w')
        json.dump(self.outline, fp)


if __name__ == "__main__":
    import sys

    a = PaperPass({3:2,2:1})
    a.outputjson(sys.argv[1])
