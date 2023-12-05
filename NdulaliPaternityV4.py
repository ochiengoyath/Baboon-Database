# NdulaliPaternityV3
from NdulaliMainV4 import ListOfTupples, Loop, Logo, Switch, ModuleReload, IntInput, ThreeChar, CapChar, FatherEntry, Expresion
from importlib import reload

print()
print('  This Module Displays the Infants of a Male.')

Input = FatherEntry(None)
Tri = ThreeChar(Input)
Cap = CapChar(Tri)
# print(Cap)
print()
for tups in ListOfTupples:
    if Cap == tups[12][:3]:
       # print(tups[12])
        print('  Father:', tups[12])

        print()
        print('  No.  Infants:', '        ', 'Sex:', '                ', 'Conception Date:', '        ',
              'Mother:', '          ', 'Mat Group:')
        break

index = 0
for tups in ListOfTupples:
    if Cap == tups[12][:3]:
        index = index + 1
        print(' ', index, '  ', str.capitalize(tups[1]), '         ', tups[8], '            ',
              tups[14] + ' ' + tups[15] + ' ' + tups[16], '             ', tups[2],
              '         ', tups[6])

Fathers = []
for tups in ListOfTupples:
    Fathers.append(tups[12])
# print(Fathers)
FatTriChar = []
for father in Fathers:
    Mmm = FatTriChar.append(father[:3])
# print(FatTriChar)

for Mmm in FatTriChar:
    if Cap not in FatTriChar:
        print('  No Father by the Sname', Cap, 'in the data base.')
        break

# Logo()
Expresion()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    for x in Loop:
        import NdulaliPaternityV4

        reload(NdulaliPaternityV4)

elif n == 2:
    for x in Loop:
        import NdulaliExitV4

        reload(NdulaliExitV4)

import NdulaliExitV4

reload(NdulaliExitV4)
