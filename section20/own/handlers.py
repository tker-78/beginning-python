class Handler(object):
    def callback(self, prefix, name, *args):
        """
        callbackは、与えられた情報から該当するメソッドを
        探して、見つかればそれを実行する
        """
        # handler.start_paragraph の形式でメソッドを探し
        # 見つからなければNoneを返す
        method = getattr(self, prefix + name, None)
        if callable(method):
            # メソッドが呼び出し可能であれは、
            # 引数を渡して実行する
            return method(*args)

    def start(self, name):
        # callbackメソッドのprefixに'start_'を渡すラッパー
        return self.callback('start_', name)

    def end(self, name):
        # callbackメソッドのprefixに'end_'を渡すラッパー
        return self.callback('end_', name)

    def sub(self, name):
        # 置換を行うメソッドを探し出して
        # メソッドを返すメソッド(実行はしない)
        # todo: あとで実装する
        pass



class HTMLRenderer(Handler):
    """
    start_heading:
    end_heading:
    """

    def start_heading(self):
        print('<h2>')

    def end_heading(self):
        print('</h2>')

    def feed(self, data):
        """
        ruleに該当しない部分をprintする
        """
        print(data)


