import re
from mendeleev import element
from collections import Counter


def split_into_brackets(molecule):
    split_by_brackets = re.findall(r"(\(([^()]+)\)*)([0-9]*)|([A-Z][a-z]*)(\d*)", molecule)
    return split_by_brackets


def stoichiometry(molecule):
    counted = Counter()
    split = split_into_brackets(molecule)

    for segment in split:
        *other, bracket_number, atom_type, atom_number = segment

        if atom_type == '':
            elements = split_into_brackets(segment[1])

            for element in elements:
                *other, atom_type, atom_number = element
                if bracket_number == '':
                    bracket_number = 1
                if atom_number == '':
                    atom_number = 1

                number_of_atom = str(atom_type) * int(atom_number) * int(bracket_number)
                counted += Counter({atom_type: int(len(number_of_atom)/len(atom_type))})
        else:
            if atom_number == '':
                atom_number = 1

            number_of_atom = str(atom_type) * int(atom_number)
            counted += Counter({atom_type: int(len(number_of_atom)/len(atom_type))})

    return dict(counted)


def calculate_mr(molecule):
    stoich = stoichiometry(molecule)
    mr_total = 0
    for atom, number in stoich.items():
        name = element(atom)
        mr_total += name.mass * number
   
    print(f'{mr_total:.2f} g/mol')
    return mr_total
