# MatSiblings

from NdulaliMainV4 import ListOfTupples, Loop, Logo, ModuleReload, Switch, IntInput, SnameEntry, ThreeChar, UpperChar, \
    CapChar, Expresion
from importlib import reload

print()
print('  This Module Displays the Paternal Siblings of an Individual.')
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
        Sibling = tups[12]
        print('  Individual:', str.capitalize(tups[1]), '   ', '  Father:', str.capitalize(tups[12]))
        print()
        print('  No.  Paternal Siblings:', '        ', 'Sex:', '          ', 'Conception Date:', '        ', 'Mother:', '         ', 'Mat Group:')
        for tups in ListOfTupples:
            if Upper == tups[0] and Sibling == ' ------ ':
                print()
                print('  No Paternal Siblings of ', str.capitalize(tups[1]), 'in the Database.')
                break

        for tups in ListOfTupples:
            if Sibling == tups[12] != ' ------ ':
                index = index + 1
                print(' ', index, '  ', str.capitalize(tups[1]), '                 ', str.capitalize(tups[8]), '         ', tups[14] + ' ' + tups[15] + ' ' + tups[16], '           ', tups[2], '        ', tups[6])

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
        import NdulaliPatSiblingsV4

        reload(NdulaliPatSiblingsV4)

elif n == 2:
    for x in Loop:
        import NdulaliExitV4

        reload(NdulaliExitV4)

import NdulaliExitV4

reload(NdulaliExitV4)
