from Mr_calculator import *

print('Welcome to the Mr Calculator.')
print('To quit, type "quit" at any time')

molecule = input('Enter molecular formula: ')
while molecule != 'quit':
    calculate_mr(molecule)
    molecule = input('Enter molecular formula: ')
