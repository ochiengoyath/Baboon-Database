# Family Menu
from NdulaliMainV4 import IntInput, InputPrompt

from importlib import reload

print()
print('  Family Menu')

n = None
InputPrompt(n)
print('  1. Parents''        ''2. Siblings''        ''3. Matriline')

n = IntInput(None)
valid = [1, 2, 3]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 3')
    n = IntInput(None)

if n == 1:
    import NdulaliParentsV4

    reload(NdulaliParentsV4)


elif n == 2:
    import NdulaliSiblingsV4

    reload(NdulaliSiblingsV4)

elif n == 3:
    import NdulaliMatrilineV4
    reload(NdulaliMatrilineV4)
