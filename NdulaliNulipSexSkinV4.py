from NdulaliMainV4 import ListOfTupples, YearInput, Loop, Month, Months, Expresion, IntInput,Switch, ModuleReload
from importlib import reload

print()
print('  This Module Displays Females to be Added to Sex Skin Sheets')

# print()

n = YearInput(None)
year = n
for year in Loop:
    if n < 1000:
        print('  Enter a 4 Digit No.')
        n = YearInput(None)

for year in Loop:
    if n > 9999:
        print('  Enter a 4 Digit No.')
        n = YearInput(None)

for year in Loop:
    if n < 2000:
        print('  Year out of Range!')
        n = YearInput(None)

for year in Loop:
    if n > 2050:
        print('  Year out of Range!')
        n = YearInput(None)

FourYears = str(n - 4)  # Convert Year integer to string
# print(FourYears)


# print(Nulips)

m = Month(None)
# print(m)

while m not in Months:
    print('  Invalid Format!')
    m = Month(None)

# print(FourYears)
M = m.upper()
Nulips = []
for tups in ListOfTupples:
    if FourYears == tups[9] and tups[8][:3] == 'Fem':
        Nulips.append(tups)

# print(Nulips)
PreciseNulipAge = []
for month in Nulips:
    if month[4] == M and month[7] != 'unknown':
        PreciseNulipAge.append(month)
# print(PreciseNulipAge)

print()
for nulip in PreciseNulipAge:
    print('  The Following Female(s) to be Added to Sex Skin Sheets as at ', M, n, '.')
    print('  (4 Years Old Female(s))')
    print('  Name:', '           ', 'Current Group:', '   ', 'Date of Birth:')
    break

none = str(len(PreciseNulipAge))

for x in Loop:
    if (len(PreciseNulipAge)) == 0:
        print('  No Juvenile Female to be Added to Sex Skin Sheets as at', M, n, '.')
        break


for nulip in PreciseNulipAge:
    if nulip in PreciseNulipAge:
        print(' ', str.capitalize(nulip[1]), '         ', nulip[7], '        ',
              nulip[3] + ' ' + nulip[4] + ' ' + nulip[9])


# Logo()
Expresion()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    for x in Loop:
        import NdulaliNulipSexSkinV4

        reload(NdulaliNulipSexSkinV4)

elif n == 2:
    for x in Loop:
        import NdulaliExitV4

        reload(NdulaliExitV4)

import NdulaliExitV4

reload(NdulaliExitV4)




