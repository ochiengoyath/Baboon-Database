# Demographics
from NdulaliMainV4 import ListOfTupples, Loop, Logo, ModuleReload, Switch, IntInput, Expresion
from importlib import reload

print()
print('  This Module Displays the Membership of Study Groups')

n = None
# InputPrompt(n)
print('  Enter a Number to Access a Group')
print('  1. Acacia\'s''        ''2. Europa\'s''       ''3. Hokey\'s''      ''4. Narasha\'s', '      ''5. Yoda\'s')

n = IntInput(None)
valid = [1, 2, 3, 4, 5]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 5')
    n = IntInput(None)

ListOfMembers = []
MaleIndex = 0
FemaleIndex = 0


def StudyGroup(group):
    for tups in ListOfTupples:
        if tups[7][:3] == group[:3]:
            ListOfMembers.append(tups)


ListOfMales = []
ListOfFemales = []

Male = ListOfMales
Female = ListOfFemales
print()
if n == 1:
    print('  ACACIA\'S')
    print()
    print('  MALES:')
    print('  No.  Name:', '          ', 'Date of Birth:', '     ', 'Mother:', '      ', 'Mat Group:')

    StudyGroup('Acacia\'s')
    for tups in ListOfMembers:
        if tups[8][:3] == 'Mal':
            Male.append(tups)
        elif tups[8][:3] == 'Fem':
            Female.append(tups)

    for M in Male:
        MaleIndex = MaleIndex + 1
        print(' ', MaleIndex, '  ', str.capitalize(M[1]), '       ', M[3] + ' ' + M[4] + ' ' + M[9], '        ', M[2],
              '       ', M[6])

    print()
    print('  FEMALES:')
    print('  No.  Name:', '          ', 'Date of Birth:', '     ', 'Mother:', '      ', 'Mat Group:')
    for F in Female:
        FemaleIndex = FemaleIndex + 1
        print(' ', FemaleIndex, '  ', str.capitalize(F[1]), '       ', F[3] + ' ' + F[4] + ' ' + F[9], '        ', F[2],
              '       ', F[6])

    print()
    print('  Males:', MaleIndex, '  Females:', FemaleIndex, '  Total:', MaleIndex + FemaleIndex)

if n == 2:
    print('  EUROPA\'S')
    print()
    print('  MALES:')
    print('  No.  Name:', '          ', 'Date of Birth:', '     ', 'Mother:', '      ', 'Mat Group:')

    StudyGroup('Europa\'s')
    for tups in ListOfMembers:
        if tups[8][:3] == 'Mal':
            Male.append(tups)
        elif tups[8][:3] == 'Fem':
            Female.append(tups)

    for M in Male:
        MaleIndex = MaleIndex + 1
        print(' ', MaleIndex, '  ', str.capitalize(M[1]), '       ', M[3] + ' ' + M[4] + ' ' + M[9], '        ', M[2],
              '       ', M[6])

    print()
    print('  FEMALES:')
    print('  No.  Name:', '          ', 'Date of Birth:', '     ', 'Mother:', '      ', 'Mat Group:')
    for F in Female:
        FemaleIndex = FemaleIndex + 1
        print(' ', FemaleIndex, '  ', str.capitalize(F[1]), '       ', F[3] + ' ' + F[4] + ' ' + F[9], '        ', F[2],
              '       ', F[6])

    print()
    print('  Males:', MaleIndex, '  Females:', FemaleIndex, '  Total:', MaleIndex + FemaleIndex)

if n == 3:
    print('  HOKEY\'S')
    print()
    print('  MALES:')
    print('  No.  Name:', '          ', 'Date of Birth:', '     ', 'Mother:', '      ', 'Mat Group:')

    StudyGroup('Hokey\'s')
    for tups in ListOfMembers:
        if tups[8][:3] == 'Mal':
            Male.append(tups)
        elif tups[8][:3] == 'Fem':
            Female.append(tups)



    for M in Male:
        MaleIndex = MaleIndex + 1
        print(' ', MaleIndex, '  ', str.capitalize(M[1]), '       ', M[3] + ' ' + M[4] + ' ' + M[9], '        ', M[2],
              '       ', M[6])

    print()
    print('  FEMALES:')
    print('  No.  Name:', '          ', 'Date of Birth:', '     ', 'Mother:', '      ', 'Mat Group:')
    for F in Female:
        FemaleIndex = FemaleIndex + 1
        print(' ', FemaleIndex, '  ', str.capitalize(F[1]), '       ', F[3] + ' ' + F[4] + ' ' + F[9], '        ', F[2],
              '       ', F[6])
    print()
    print('  Males:', MaleIndex, '  Females:', FemaleIndex, '  Total:', MaleIndex + FemaleIndex)

if n == 4:
    print('  NARASHA\'S')
    print()
    print('  MALES:')
    print('  No.  Name:', '          ', 'Date of Birth:', '     ', 'Mother:', '      ', 'Mat Group:')

    StudyGroup('Narasha\'s')
    for tups in ListOfMembers:
        if tups[8][:3] == 'Mal':
            Male.append(tups)
        elif tups[8][:3] == 'Fem':
            Female.append(tups)

    for M in Male:
        MaleIndex = MaleIndex + 1
        print(' ', MaleIndex, '  ', str.capitalize(M[1]), '       ', M[3] + ' ' + M[4] + ' ' + M[9], '        ', M[2],
              '       ', M[6])

    print()
    print('  FEMALES:')
    print('  No.  Name:', '          ', 'Date of Birth:', '     ', 'Mother:', '      ', 'Mat Group:')
    for F in Female:
        FemaleIndex = FemaleIndex + 1
        print(' ', FemaleIndex, '  ', str.capitalize(F[1]), '       ', F[3] + ' ' + F[4] + ' ' + F[9], '        ', F[2],
              '       ', F[6])
    print()
    print('  Males:', MaleIndex, '  Females:', FemaleIndex, '  Total:', MaleIndex + FemaleIndex)

if n == 5:
    print('  YODA\'S')
    print()
    print('  MALES:')
    print('  No.  Name:', '          ', 'Date of Birth:', '     ', 'Mother:', '      ', 'Mat Group:')

    StudyGroup('Yoda\'s')
    for tups in ListOfMembers:
        if tups[8][:3] == 'Mal':
            Male.append(tups)
        elif tups[8][:3] == 'Fem':
            Female.append(tups)

    for M in Male:
        MaleIndex = MaleIndex + 1
        print(' ', MaleIndex, '  ', str.capitalize(M[1]), '       ', M[3] + ' ' + M[4] + ' ' + M[9], '        ', M[2],
              '       ', M[6])

    print()
    print('  FEMALES:')
    print('  No.  Name:', '          ', 'Date of Birth:', '     ', 'Mother:', '      ', 'Mat Group:')
    for F in Female:
        FemaleIndex = FemaleIndex + 1
        print(' ', FemaleIndex, '  ', str.capitalize(F[1]), '       ', F[3] + ' ' + F[4] + ' ' + F[9], '        ', F[2],
              '       ', F[6])
    print()
    print('  Males:', MaleIndex, '  Females:', FemaleIndex, '  Total:', MaleIndex + FemaleIndex)

# Logo()
Expresion()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    for x in Loop:
        import NdulaliMembershipV4

        reload(NdulaliMembershipV4)

elif n == 2:
    for x in Loop:
        import NdulaliExitV4

        reload(NdulaliExitV4)

import NdulaliExitV4

reload(NdulaliExitV4)
