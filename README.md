# M<sub>r</sub> Calculator
A calculator that returns the molecular weight of many chemical compounds given a molecular formula in string format.

### General Information
I undertook this project in an early attempt to explore REGEX. As with all regular expressions, the ones used in this code are complex and I encourage users to have a glance at them. I write, at length, about my time developing this piece of code in my blog: www.runinswithpython.co.uk/post/regex-my-first-real-project.

### Technologies
Written orginally for Python 3.7, this code is supported by Python 3 for versions < 3.8.8 and requires the packages specified in requirements.txt.
Specifically, the module: mendeleev is required for this code.

### Using the M<sub>r</sub> Calculator Interface
When in the correct directory type:
~~~~
>> python calculateMr.py
~~~~

When prompted, enter a molecular formular.
~~~~
Welcome to the Mr Calculator.
To quit, type "quit" at any time
Enter molecular formula: CH4
~~~~

The calculator will print the M<sub>r</sub> of the compound (to 2 d.p) to the console.
~~~
>> 16.04 g/mol
~~~~

### Using the M<sub>r</sub> Calculator Functions
If using the functions directly from calculator_utils.py, the function takes a string and will print the statement to the console and return a float of the value (to 3 d.p).

~~~~
>> CH4 = calculate_mr('CH4')
16.04 g/mol

>> CH4
16.043
~~~~~

### Examples
The calculator supports molecular formulas containing every element in the Periodic Table thanks to the mendeleev module.
The REGEX strings support simple molecular formulas and formulas containing both one set of brackets and multiple embedded brackets. Whilst the calculator does not support the use of square brackets, curly brackets can be used as a supliment.

~~~~
Enter molecular formula: CH4
>> 16.04 g/mol

Enter molecular formula: (CH3CH2)2O
>> 74.12 g/mol

Enter molecular formula: (Cu(NH3)4(H2O)2)
>> 167.70 g/mol
~~~~



