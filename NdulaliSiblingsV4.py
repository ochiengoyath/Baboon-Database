# NdulaliSiblings

from NdulaliMainV4 import IntInput, InputPrompt
from importlib import reload

print()
print('  Siblings Menu')

n = None
InputPrompt(n)
print('  1. Maternal Siblings''        ''2. Paternal Siblings')

n = IntInput(None)
valid = [1, 2]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 2')
    n = IntInput(None)

if n == 1:
    import NdulaliMatSiblingsV4

    reload(NdulaliMatSiblingsV4)

if n == 2:
    import NdulaliPatSiblingsV4
    reload(NdulaliPatSiblingsV4)

