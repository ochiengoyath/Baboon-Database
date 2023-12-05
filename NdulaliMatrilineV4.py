# NdulaliMatriline

from NdulaliMainV4 import ListOfTupples, Loop, Logo, Switch, ModuleReload, IntInput, ThreeChar, CapChar, SnameEntry, \
    Expresion, UpperChar
from importlib import reload
from csv import reader

print()
print('  This Module Displays the Matriline  of an Individual.')
print('  Enter the Sname of an Individual to view it\'s Matriline.')

Input = SnameEntry(None)
Tri = ThreeChar(Input)
Upper = UpperChar(Tri)
Cap = CapChar(Tri)

Names = []
for tups in ListOfTupples:
    Names.append(str.capitalize(tups[1][:3]))

# print(Names)
# print(Cap)


Snames = []
for tups in ListOfTupples:
    Snames.append(tups[0])
# print(Snames)
# print(Upper)
# print(Cap)

while Upper not in Snames:
    print('  No Individual by the Sname', Upper, 'in the data base.')
    Input = SnameEntry(None)
    Tri = ThreeChar(Input)
    Upper = UpperChar(Tri)

print()

ListOfMatTups = []
for tups in ListOfTupples:
    if Upper == tups[0]:
        ListOfMatTups.append(str.capitalize(tups[1]))
        ListOfMatTups.append(str.capitalize(tups[2]))
# print(ListOfMatTups)

x = []
MatriLine = []
y = []
MatTups = [((str.capitalize(tups[1])), (str.capitalize(tups[2]))) for tups in ListOfTupples]
print('  Please wait......')

# print(MatTups)
for tups in MatTups:
    counter = 0
    while counter < 15:
        for tups in MatTups:
            counter = counter + 1

            # x = []
            if ListOfMatTups[-1] == tups[0]:
                ListOfMatTups.append(tups[1])

                x = [i for i in ListOfMatTups if i != 'Unknown']  # Disqualify unknowns

MatAncestry = (x[:-1])  # slice out last element which will always be unknown
# print(MatAncestry)

MatAncestryReverse = MatAncestry[::-1]  # Reverse the MatAncestry order
# print(MatAncestryReverse)

print()

for i in MatAncestryReverse:
    print('  ', '----> ', i, end='')

for i in MatAncestryReverse:
    if i not in MatAncestryReverse:
        print('  ')

print()
print()
print('  Matriline Details.')
print()
print('  No.  Individual:', '        ', 'Date of birth:', '         ', 'Father:', '         ', 'Mat Group:')
index = 0
for individual in MatAncestryReverse:
    for tups in ListOfTupples:
        if individual == str.capitalize(tups[1]):
            index = index + 1
            print(' ', index, '  ', str.capitalize(tups[1]), '           ', tups[3] + ' ' + tups[4] + ' ' + tups[9],
                  '           ', tups[12], '           ', tups[6], )
# Logo()
Expresion()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    for x in Loop:
        import NdulaliMatrilineV4

        reload(NdulaliMatrilineV4)

elif n == 2:
    for x in Loop:
        import NdulaliExitV4

        reload(NdulaliExitV4)

import NdulaliExitV4

reload(NdulaliExitV4)
