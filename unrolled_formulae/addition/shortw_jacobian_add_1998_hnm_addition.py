from sage.all import *

pr = PolynomialRing(ZZ, ('a', 'b', 'X1', 'X2', 'Y1', 'Y2'), 6)
a, b, X1, X2, Y1, Y2 = pr.gens()
Z1, Z2 = 1, 1
formula = {}
R1 = X1
formula['R1'] = R1
R2 = Y1
formula['R2'] = R2
R3 = Z1
formula['R3'] = R3
R4 = X2
formula['R4'] = R4
R5 = Y2
formula['R5'] = R5
R6 = Z2
formula['R6'] = R6
R7 = R6 ** 2
formula['R7'] = R7
R1 = R1 * R7
formula['R1'] = R1
R7 = R6 * R7
formula['R7'] = R7
R2 = R2 * R7
formula['R2'] = R2
R7 = R3 ** 2
formula['R7'] = R7
R8 = R4 * R7
formula['R8'] = R8
R7 = R3 * R7
formula['R7'] = R7
R7 = R5 * R7
formula['R7'] = R7
R2 = R2 - R7
formula['R2'] = R2
R7 = 2 * R7
formula['R7'] = R7
R7 = R2 + R7
formula['R7'] = R7
R1 = R1 - R8
formula['R1'] = R1
R8 = 2 * R8
formula['R8'] = R8
R8 = R1 + R8
formula['R8'] = R8
R3 = R3 * R6
formula['R3'] = R3
R3 = R3 * R1
formula['R3'] = R3
R7 = R7 * R1
formula['R7'] = R7
R1 = R1 ** 2
formula['R1'] = R1
R8 = R8 * R1
formula['R8'] = R8
R7 = R7 * R1
formula['R7'] = R7
R1 = R2 ** 2
formula['R1'] = R1
R1 = R1 - R8
formula['R1'] = R1
R8 = R8 - R1
formula['R8'] = R8
R8 = R8 - R1
formula['R8'] = R8
R8 = R8 * R2
formula['R8'] = R8
R2 = R8 - R7
formula['R2'] = R2
R2 = half * R2
formula['R2'] = R2
X3 = R1
formula['X3'] = X3
Y3 = R2
formula['Y3'] = Y3
Z3 = R3
formula['Z3'] = Z3
for key, value in formula.items():
    print(f'{key} = {value}')
