class Rule:
    """
    構文解析を行い、テキストの変換処理を行う
    RuleはParserに持たせて、
    block毎にRuleを適用する
    つまり、
    for block in blocks:
        for rule in rules:
            rule.action(block, handler)
            ...
    の形で解析を実行する。
    """
    pass

class HeadingRule():
    type = "heading"
    def condition(self, block):
        # ブロックが見出しの定義に合致していれば、Trueを返す。
        if not '\n' in block and len(block) < 70 and \
            not (block[-1] == '.' or block[-1] == ':' or block[-1] == '。'):
            return True
        return False

    def action(self, block, handler):
        """
        ブロックに対してハンドラーを指定して変換処理を
        実行する
        例えば、handler.start('heading')などを呼び出す
        """
        handler.start('heading')
        handler.feed(block) # 処理の必要がない場合は送る
        handler.end('heading')
        return True

class ListItemRule():
    type = 'listitem'
    def condition(self, block):
        if block[0] == '-':
            return True
        return False

    def action(self, block, handler):
        handler.start('listitem')
        handler.feed(block)
        handler.end('listitem')
        return True

class ParagraphRule():
    """
    どのルールにも当てはまらないものは
    パラグラフとする
    """
    type = 'paragraph'
    def condition(self, block):
        return True

    def action(self, block, handler):
        handler.start('paragraph')
        handler.feed(block)
        handler.end('paragraph')
        return True

