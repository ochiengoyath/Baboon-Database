from NdulaliMainV4 import ListOfTupples, IntInput, YearInput, Switch, Loop, Month, Months, Expresion, ModuleReload
from importlib import reload

print()
print('  This Module Displays Juveniles to be Added to Sampling Schedule Sheets')

n = YearInput(None)
year = n

for year in Loop:
    if n < 1000:
        print('  Enter a 4 Digit No.')
        n = YearInput(None)

Max = 9999
for year in Loop:
    if n > Max:
        print('  Enter a 4 Digit No.')
        n = YearInput(None)

Min = 2000
for year in Loop:
    if n < Min:
        print('  Year out of Range!')
        n = YearInput(None)


Range = 2050
for year in Loop:
    if n > Range:
        print('  Year out of Range!')
        n = YearInput(None)

# LastYear = str(n - 1)  # Convert Year integer to string
# print(type(LastYear))
m = Month(None)
# print(LastYear)
# print(m)

while m not in Months:
    print('  Invalid Format!')
    m = Month(None)

FirstHalfYearList = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN']
SecondHalfYearList = ['JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

Juveniles = []

for tups in ListOfTupples:
    if m in FirstHalfYearList and tups[9] == str(n - 1):
        Juveniles.append(tups)
    elif m in SecondHalfYearList and tups[9] == str(n):
        Juveniles.append(tups)

# print(' Juveniles:', Juveniles)

SixMonthsTup = [('jan', 'JUN'), ('feb', 'JUL'), ('mar', 'AUG'), ('apr', 'SEP'), ('may', 'OCT'), ('jun', 'NOV'),
                ('jul', 'DEC'),
                ('aug', 'JAN'), ('sep', 'FEB'), ('oct', 'MAR'), ('nov', 'APR'), ('dec', 'MAY')]


def Exchange():
    for x in SixMonthsTup:
        if x[0] == str.lower(m):
            return x[1]


M = Exchange()
# print(M)

print()

for tups in Juveniles:
    if M == tups[4] and tups[7] != 'unknown':
        print('  The Following Juvenile(s) to be Added to Sampling Schedule as at ', m, n, '.')
        print('  (6 months old Juvenile(s))')
        print('  Name:', '        ', 'Current Group:', '       ', 'Sex:', '                ', 'Date of Birth:')
        break


for tups in Juveniles:
    if M == tups[4] and tups[7] != 'unknown':
        print(' ', str.capitalize(tups[1]), '         ', tups[7], '           ', tups[8], '           ',
              tups[3] + ' ' + tups[4] + ' ' + tups[9])

L = []
for tups in Juveniles:
    if M == tups[4] and tups[7] != 'unknown':
        L.append(M)

#print(L)

for x in Loop:
    if len(L) == 0:
        print('  No Juvenile to be Added to Sampling Schedule as at', m, n, '.')
        break

# Logo()
Expresion()
ModuleReload()
n = None
n = IntInput(None)
Switch(n)
if n == 1:
    for x in Loop:
        import NdulaliJuvSamplingV4

        reload(NdulaliJuvSamplingV4)

elif n == 2:
    for x in Loop:
        import NdulaliExitV4

        reload(NdulaliExitV4)

import NdulaliExitV4

reload(NdulaliExitV4)
