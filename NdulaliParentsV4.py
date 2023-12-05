# NdulaliParents
from NdulaliMainV4 import IntInput, InputPrompt
from importlib import reload

print()
print('  Parents Menu')

n = None
InputPrompt(n)
print('  1. Maternity''        ''2. Paternity')

n = IntInput(None)
valid = [1, 2]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 2')
    n = IntInput(None)

if n == 1:
    import NdulaliMaternityV4

    reload(NdulaliMaternityV4)

if n == 2:
    import NdulaliPaternityV4
    reload(NdulaliPaternityV4)

