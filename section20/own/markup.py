class Parser(object):
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

class BasicTextParser(Parser):
    def __init__(self, handler):
        Parser.__init__(self,handler)
        # todo: rulesを追加

        # todo: filtersを追加


#
# マークアップの実行
#
handler = HTMLRenderer()
parser = BasicTextParser(handler)

parser.parse(sys.stdin)