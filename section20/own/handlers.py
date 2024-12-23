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

    # callbackメソッドのprefixに'start_'を渡すラッパー
    def start(self, name):
        return self.callback('start_', name)

    # callbackメソッドのprefixに'end_'を渡すラッパー
    def end(self, name):
        return self.callback('end_', name)

    # 置換を行うメソッドを探し出して
    # メソッドを返すメソッド(実行はしない)
    def sub(self, name):
        # todo: あとで実装する
        pass



class HTMLRenderer(Handler):
    pass