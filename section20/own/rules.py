class Rule(object):
    def action(self, block, handler):
        """
        handlerのメソッドを呼び出す
        :return:
        """
        handler.start(self.type)
        handler.end(self.type)
        return True


class HeadingRule(Rule):
    """
    見出しに関するルール
    """
    type = "heading"
    def condition(self, block):
        """
        ブロックが見出しであればTrueを返す
        """
        # headlineと判定する条件を指定する
        # - 70文字以内
        # - 改行文字を含まない
        # - 行末に. 。:を含まない
        return not '\n' in block and len(block) < 70 and \
            not (block[-1] == "." or block[-1] == "。" or block[-1] == ":")
