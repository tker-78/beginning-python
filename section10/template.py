import fileinput, re

compiled_pat = re.compile(r'\[(.+?)\]')
scope = dict()

def main():

    lines = []
    for line in fileinput.input():
        lines.append(line)

    text = ''.join(lines)
    print(text)

    print(compiled_pat.sub(replacement, text))

def replacement(match):
    code = match.group(1)
    try:
        return str(eval(code, scope))
    except SyntaxError:
        exec(code, scope)
        return ''



main()