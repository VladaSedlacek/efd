from sage.all import *

pr = PolynomialRing(ZZ, ('a', 'd', 'X1', 'X2', 'Y1', 'Y2'), 6)
a, d, X1, X2, Y1, Y2 = pr.gens()
Z1, Z2 = 1, 1
formula = {}
t0 = Z1 ** 2
formula['t0'] = t0
B = d * t0
formula['B'] = B
C = X1 * X2
formula['C'] = C
D = Y1 * Y2
formula['D'] = D
E = C * D
formula['E'] = E
t1 = a * D
formula['t1'] = t1
H = C - t1
formula['H'] = H
t2 = X1 + Y1
formula['t2'] = t2
t3 = X2 + Y2
formula['t3'] = t3
t4 = t2 * t3
formula['t4'] = t4
t5 = t4 - C
formula['t5'] = t5
I = t5 - D
formula['I'] = I
t6 = E + B
formula['t6'] = t6
X3 = t6 * H
formula['X3'] = X3
t7 = E - B
formula['t7'] = t7
Y3 = t7 * I
formula['Y3'] = Y3
t8 = H * I
formula['t8'] = t8
Z3 = Z1 * t8
formula['Z3'] = Z3
for key, value in formula.items():
    print(f'{key} = {value}')
