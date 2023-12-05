# Main Menu
from NdulaliMainV4 import IntInput, InputPrompt

from importlib import reload

print()
print('  Main Menu:')

n = None
InputPrompt(n)
print('  1. Profile''        ''2. Family''      ''3. Demography')

n = IntInput(None)
valid = [1, 2, 3]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 3')
    n = IntInput(None)

if n == 1:
    import NdulaliProfileV4

    reload(NdulaliProfileV4)


elif n == 2:
    import NdulaliFamilyMenuV4

    reload(NdulaliFamilyMenuV4)

elif n == 3:
    import NdulaliDemographyV4

    reload(NdulaliDemographyV4)


