from utils import *


class Parser(object):
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def add_filter(self, filter):
        self.filters.append(filter)

    def parse(self, file):
        for block in blocks(file):
            pass

class BasicTextParser(Parser):
    def __init__(self, handler):
        Parser.__init__(self,handler)
    # todo: rulesを追加

    # todo: filtersを追加


#
# マークアップの実行
#
from rules import *
from handlers import *
handler = HTMLRenderer()
parser = BasicTextParser(handler)
# parser.parse(sys.stdin)


# testの実行
