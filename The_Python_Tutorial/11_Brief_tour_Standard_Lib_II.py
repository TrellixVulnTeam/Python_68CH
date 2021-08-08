import reprlib, pprint, textwrap


print(reprlib.repr(set('supercalifragilisticexpialidocious')))

t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width = 30)

doc = """The wrap() method is just like fill() except that it returns
 a list of strings instead of one big string with newlines to separate
 the wrapped lines."""

print(textwrap.fill(doc, width = 40)) 