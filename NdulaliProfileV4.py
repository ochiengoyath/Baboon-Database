from NdulaliMainV4 import ListOfTupples, Loop, Logo, Switch, ModuleReload, IntInput, SnameEntry, ThreeChar, UpperChar, \
    CapChar, Expresion
from importlib import reload

# for t in ListOfTupples:
#  print(t)

print()
print('  This Module Displays the Profile of an Individual.')
print('  Enter the Sname of Any Individual to view its Profile.')

Input = SnameEntry(None)
Tri = ThreeChar(Input)
Upper = UpperChar(Tri)
Cap = CapChar(Tri)

# print(Cap)
print()
for tups in ListOfTupples:
    if Upper == tups[0]:
        print('  Name:', str.capitalize(tups[1]))
        print('  Sex:', tups[8])
        print('  Date of Birth:', tups[3] + ' ' + tups[4] + ' ' + tups[9])
        print('  Mother:', tups[2])
for tups in ListOfTupples:
    if Upper == tups[0] and tups[11] != 'unknown':
        print('  Father:', tups[12])
for tups in ListOfTupples:
    if Upper == tups[0]:
        print('  Mat Group:', tups[6])
for tups in ListOfTupples:
    if Upper == tups[0] and tups[6][:3] != tups[7][:3] != 'unk':
        print('  Current Group:', tups[7])

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

        import NdulaliProfileV4
        for x in Loop:

            reload(NdulaliProfileV4)

if n == 2:
    for x in Loop:

        import NdulaliExitV4

        reload(NdulaliExitV4)

import NdulaliExitV4

reload(NdulaliExitV4)
