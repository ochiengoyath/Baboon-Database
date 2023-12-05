# NdulaliMaternity
from NdulaliMainV4 import ListOfTupples, Loop, Logo, Switch, ModuleReload, IntInput, ThreeChar, CapChar, MotherEntry, \
    Expresion
from importlib import reload

print()
print('  This Module Displays the Infants of a Female.')

Input = MotherEntry(None)
Tri = ThreeChar(Input)
Cap = CapChar(Tri)
# print(Cap)
print()
for tups in ListOfTupples:
    if Cap == tups[2][:3]:
        # print(tups[2])
        print('  Mother:', tups[2])

        print()
        print('  No.  Infants:', '        ', 'Sex:', '              ', 'Date of birth:', '           ',
              'Father:', '           ', 'Mat Group:')
        break

index = 0
for tups in ListOfTupples:
    if Cap == tups[2][:3]:
        index = index + 1
        print(' ', index, '  ', str.capitalize(tups[1]), '        ', tups[8], '            ',
              tups[3] + ' ' + tups[4] + ' ' + tups[9], '             ', tups[12],
              '         ', tups[6])

Mothers = []
for tups in ListOfTupples:
    Mothers.append(tups[2])
# print(Mothers)
MotTriChar = []
for mother in Mothers:
    Mmm = MotTriChar.append(mother[:3])
# print(MotTriChar)

for Mmm in MotTriChar:
    if Cap not in MotTriChar:
        print('  No Mother by the Sname', Cap, 'in the data base.')
        break

# Logo()
Expresion()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    for x in Loop:
        import NdulaliMaternityV4

        reload(NdulaliMaternityV4)

elif n == 2:
    for x in Loop:
        import NdulaliExitV4

        reload(NdulaliExitV4)

import NdulaliExitV4

reload(NdulaliExitV4)
