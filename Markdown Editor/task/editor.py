# JBA Python Core
# Project: Markdown Editor - https://hyperskill.org/projects/162
# Submitted by Chris Freeman - Stage 5/5: Save the Results
# Reference: https://www.markdownguide.org/basic-syntax/

from itertools import chain


formatters = ['new-line', 'plain', 'bold', 'italic', 'inline-code', 'header',
              'link', 'ordered-list', 'unordered-list']
cmds = ['!help', '!done']
doc = ['']                  # accumulated markdown document
new_line = ''
line_count = 0
save_file = 'output.md'     # in the current directory


def do_plain():
    return input('Text: ')


def do_bold():
    return '**' + input('Text: ') + '**'


def do_italic():
    return '*' + input('Text: ') + '*'


def do_inline():
    return '`' + input('Text: ') + '`'


def do_header():
    while True:
        level = int(input('Level: '))
        if 0 < level < 7:
            break
        else:
            print('The level should be within the range of 1 to 6')
    header_prefix = '#' * level
    return header_prefix + ' ' + input('Text: ')


def do_link():
    label = input('Label: ')
    url = input('URL: ')
    return '[' + label + '](' + url + ')'


def do_list(ordered: bool):
    rlist = []
    while True:
        rows = int(input('Number of rows: '))
        if rows > 0:
            break
        else:
            print('The number of rows should be greater than zero')
    for n in range(1, rows+1):
        suf = '* '
        if ordered:
            suf = f'{n}. '
        rlist.append(suf + input(f'Row #{n}: ') + '\n')
    return ''.join(rlist)


def do_help():
    print('Available formatters: plain bold italic header link inline-code new-line ordered-list unordered-list')
    print('Special commands: !help !done')


while True:
    fmt = input('Choose a formatter: ').strip().lower()
    if fmt not in list(chain(formatters, cmds)):
        print('Unknown formatting type or command')
    elif fmt == cmds[0]:        # HELP
        do_help()
    elif fmt == cmds[1]:        # DONE
        break
    elif fmt in formatters:
        if fmt == formatters[0]:    # NEW-LINE
            doc.append(doc.pop() + '\n')
        elif fmt == formatters[1]:  # PLAIN
            doc.append(doc.pop() + do_plain())
        elif fmt == formatters[2]:  # BOLD
            doc.append(doc.pop() + do_bold())
        elif fmt == formatters[3]:  # ITALIC
            doc.append(doc.pop() + do_italic())
        elif fmt == formatters[4]:  # IN_LINE
            doc.append(doc.pop() + do_inline())
        elif fmt == formatters[5]:  # HEADER
            if line_count == 0:
                doc.pop()
            doc.append(do_header() + '\n')
        elif fmt == formatters[6]:  # LINK
            doc.append(doc.pop() + do_link())
        elif fmt == formatters[7]:  # ORDERED-LIST
            if line_count == 0:
                doc.pop()
            doc.append(do_list(ordered=True))
        elif fmt == formatters[8]:  # UNORDERED-LIST
            if line_count == 0:
                doc.pop()
            doc.append(do_list(ordered=False))
        else:
            print("oops... format processing error")
            break
        line_count += 1
        for ln in doc:              # Print the document so far...
            print(ln)
    else:
        print('Logic error!')   # Should not get here...
        break
# now save the output to file "output.md"
with open(save_file, 'w', encoding='utf-8') as outfile:
    for ln in doc:
        outfile.write(ln)
# end
