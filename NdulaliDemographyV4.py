# NdulaliDemography

from NdulaliMainV4 import IntInput, InputPrompt

from importlib import reload

print()
print('  Demography Menu:')

n = None
InputPrompt(n)
print('  1. Group Membership''        ''2. Sex Skins/Nulips''      ''3. Sampling/Juveniles')

n = IntInput(None)
valid = [1, 2, 3]
while n not in valid:
    print('  Valid Numbers Range from: 1 to 3')
    n = IntInput(None)

if n == 1:
    import NdulaliMembershipV4

    reload(NdulaliMembershipV4)

if n == 2:
    import NdulaliNulipSexSkinV4
    reload(NdulaliNulipSexSkinV4)

if n == 3:
    import NdulaliJuvSamplingV4
    reload(NdulaliJuvSamplingV4)
