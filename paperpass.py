import json

__version__ = "0.1"

class PaperPass:
    " This Class constructs first pass of a paper "

    def __init__(self, outline):
        self.outline = outline

    def setCategory(self, category):
        self.category = category

    def setContext(self, context):
        self.context = context

    def setCorrectness(self, correctness):
        self.correctness = correctness

    def setContributions(self, contributions):
        self.contributions = contributions

    def setClarity(self, clarity):
        self.clarity = clarity

    def outputjson(self, filename):
        fp = open(filename, 'w')
        json.dump(self.outline, fp)

""""
if __name__ == "__main__":
    import sys

    a = PaperPass({3:2,2:1})
    a.outputjson(sys.argv[1])
"""
