class Handler(object):
    """
    handlersに持たせる役割は、
    コントローラーみたいな感じで、
    引数に応じて適切なメソッドを呼び出すこと

    """
    def callback(self, prefix: str , name: str, *args) :
        method = getattr(self, prefix + name)
        if callable(method):
            return method(*args)

    def start(self, name: str):
        self.callback(prefix="start_", name=name)

    def end(self, name: str):
        self.callback(prefix="end_", name=name)

    def sub(self, name: str):
        """
        *todo*: 正直この実装の意味がわからない
        """
        def substitution(match):
            result = self.callback("sub_", name, match)
            if result is None:
                return match.group(0)
            return result
        return substitution

class HTMLRenderer(Handler):
    def start_document(self):
        document = """
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Document</title>
        </head>
        <body>
        """
        print(document.strip())

    def end_document(self):
        print('</body></html>')

    def start_heading(self):
        print('<h2>')
    def end_heading(self):
        print('</h2')
    def start_list(self):
        print('<ul>')
    def end_list(self):
        print('</ul>')
    def start_listitem(self):
        print('<li>')
    def end_listitem(self):
        print('</li>')
    def start_paragraph(self):
        print('<p>')
    def end_paragraph(self):
        print('</p>')
    def feed(self, data):
        print(data)

    def sub_emphasis(self, match):
        return f'<span style="font-weight: bold;">{match.group(1)}</span>'




