from sage.all import PolynomialRing, ZZ

pr = PolynomialRing(ZZ, ('c', 'd', 'X1', 'X2', 'Y1', 'Y2'), 6)
c, d, X1, X2, Y1, Y2 = pr.gens()
ccd = c * c * d
ccd2 = 2 * c * c * d
c2 = 2 * c
cc4 = 4 * c * c
k = 1 / c
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
R7 = R1 + R2
formula['R7'] = R7
R6 = R4 + R5
formula['R6'] = R6
R1 = R1 * R4
formula['R1'] = R1
R2 = R2 * R5
formula['R2'] = R2
R7 = R7 * R6
formula['R7'] = R7
R7 = R7 - R1
formula['R7'] = R7
R7 = R7 - R2
formula['R7'] = R7
R7 = R7 * R3
formula['R7'] = R7
R6 = R1 * R2
formula['R6'] = R6
R6 = d * R6
formula['R6'] = R6
R2 = R2 - R1
formula['R2'] = R2
R2 = R2 * R3
formula['R2'] = R2
R3 = R3 ** 2
formula['R3'] = R3
R1 = R3 - R6
formula['R1'] = R1
R3 = R3 + R6
formula['R3'] = R3
R2 = R2 * R3
formula['R2'] = R2
R3 = R3 * R1
formula['R3'] = R3
R1 = R1 * R7
formula['R1'] = R1
R3 = c * R3
formula['R3'] = R3
X3 = R1
formula['X3'] = X3
Y3 = R2
formula['Y3'] = Y3
Z3 = R3
formula['Z3'] = Z3
