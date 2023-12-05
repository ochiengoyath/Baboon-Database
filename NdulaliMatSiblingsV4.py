# MatSiblings

from NdulaliMainV4 import ListOfTupples, Loop, Logo, ModuleReload, Switch, IntInput, SnameEntry, ThreeChar, UpperChar, \
    CapChar, Expresion
from importlib import reload

print()
print('  This Module Displays the Maternal Siblings of an Individual.')
print('  Enter an Sname of any Individual to view its Family.')

Input = SnameEntry(None)
Tri = ThreeChar(Input)
Upper = UpperChar(Tri)
Cap = CapChar(Tri)
# print(Cap)
print()
index = 0
for tups in ListOfTupples:
    if Upper == tups[0]:
        Sibling = tups[2]
        print('  Individual:', str.capitalize(tups[1]), '   ', '  Mother:', str.capitalize(tups[2]))
        print()
        print('  No.  Maternal Siblings:', '        ', 'Sex:', '           ', 'Date of birth:', '              ', 'Father:',
              '         ',
              'Mat Group:')
        for tups in ListOfTupples:
            if Upper == tups[0] and Sibling == 'unknown':
                print()
                print('  No Maternal Siblings of ', str.capitalize(tups[1]), 'in the Database.')
                break
            elif Sibling == tups[2] != 'unknown':
                index = index + 1
                print(' ', index, '  ', str.capitalize(tups[1]), '                 ', str.capitalize(tups[8]),
                      '            ',
                      tups[3] + ' ' + tups[4] + ' ' + tups[9], '              ', tups[12], '         ', tups[6])

Snames = []
for tups in ListOfTupples:
    Snames.append(tups[0])
# print(Sname)
for item in Snames:
    if Upper not in Snames:
        print('  No Individual by the Sname', Cap, 'in the data base.')
        break

# Logo()
Expresion()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    for x in Loop:
        import NdulaliMatSiblingsV4

        reload(NdulaliMatSiblingsV4)

elif n == 2:
    for x in Loop:
        import NdulaliExitV4

        reload(NdulaliExitV4)

import NdulaliExitV4

reload(NdulaliExitV4)
