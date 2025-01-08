from handlers import *
from rules import *
from util import *
import sys

class Parser():
    """
    与えられた文字列をブロックに分割して、
    解析を実行する
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def parse(self, file):

        self.handler.start('document')
        for block in blocks(file):
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last: break # 処理が終わったらblockを進める
        self.handler.end('document')

handler = HTMLRenderer()
parser = Parser(handler)
parser.add_rule(HeadingRule())
parser.add_rule(ParagraphRule())
parser.parse(sys.stdin)
