# NdulaliMain
import random
from csv import reader

# open file in read mode
with open('NdulaliCSVTable.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    ListOfTupples = list(map(tuple, csv_reader))

# Standard iteration used everywhere
Loop = list(range(100))


# This file contains print statements that are shared
def InputPrompt(n):
    print('  Enter a Number to Access a Module')
    return n


def SnameEntry(Input):
    Input = None
    while not Input:
        Input = input('  Enter an Sname:')
    return Input


def MotherEntry(Input):
    Input = None
    while not Input:
        Input = input('  Enter the Sname of a Mother:')
    return Input


def FatherEntry(Input):
    Input = None
    while not Input:
        Input = input('  Enter the Sname of a Father:')
    return Input


def ThreeChar(Input):
    Tri = Input[:3]
    return Tri


def UpperChar(Tri):
    Upper = str.upper(Tri)
    return Upper


def CapChar(Tri):
    Cap = str.capitalize(Tri)
    return Cap


def YearInput(n):
    n = None
    while not n:
        try:
            n = int(input('  Enter the Current Year in YYYY Format:'))
        except ValueError:
            print('  Invalid Input! ')

    return n


# Accepts integer inputs only
def IntInput(n):
    n = None
    while not n:
        try:
            n = int(input('  Enter a Number:'))
        except ValueError:
            print('  Invalid Input!')
    return n


# Month input
def Month(m):
    m = None
    while not m:
        m = (input('  Enter the Incoming Month in MMM Format:'))
        m = m.upper()
    return m


Months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

OneLiner = ['Amboseli Baboon Research Project', 'Ndulali sidai naling !', 'Ndulali DB by ochiengoyath',
            'We say whatever we want here.', 'You can choose to ignore what is said here.',
            'A little fun goes along way.',
            'Do you have a witty one-liner to add here?', 'Napenda nyani sana !', 'More interesting stuff coming up.',
            'We throw a random line here.']


def Expresion():
    print()
    random.shuffle(OneLiner)
    for i in OneLiner:
        print('          ---------------', i, '---------------')
        break
    print()


# Expresion()

def Logo():
    print()
    print('                                         Ndulali DB by ochiengoyath                    ')
    print()


# Runs at the end of every module
def ModuleReload():
    print('  1. Rerun Current Module.    2. Return to Main Menu.')


def Switch(n):
    valid = [1, 2]
    for i in Loop:
        while n not in valid:
            print('  Valid Numbers are: 1 and 2')
            n = IntInput(None)
    return n
