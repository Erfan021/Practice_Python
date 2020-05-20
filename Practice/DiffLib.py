# Implementation and practice of DiffLib library
import difflib

textA = """"
1- My first name is Irfan.
3- Will be copied.
5- Lets have party :)
"""

textB = """
2- My last name is Ahmed.
3- Will be copied.
4- Lets have party :D
"""

result = difflib.Differ().compare(textA.splitlines(), textB.splitlines())

# print('\n'.join(result))

from difflib import HtmlDiff

result_html = HtmlDiff().make_file(textA.splitlines(), textB.splitlines())
with open ('difflibresult.html', 'w') as f:
    f.write(result_html)

