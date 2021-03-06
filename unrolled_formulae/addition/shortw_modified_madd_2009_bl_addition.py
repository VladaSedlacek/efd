from sage.all import PolynomialRing, ZZ

pr = PolynomialRing(ZZ, ('a', 'b', 'X1', 'X2', 'Y1', 'Y2'), 6)
a, b, X1, X2, Y1, Y2 = pr.gens()
ZZ1, ZZZ1, ZZ2, ZZZ2 = 1, 1, 1, 1
b2 = 2 * b
b4 = 4 * b
half = 1 / 2
Z1, Z2 = 1, 1
formula = {}
ZZ1 = Z1 ** 2
formula['ZZ1'] = ZZ1
t0 = X2 * ZZ1
formula['t0'] = t0
H = t0 - X1
formula['H'] = H
HH = H ** 2
formula['HH'] = HH
I = 4 * HH
formula['I'] = I
J = H * I
formula['J'] = J
t1 = Z1 * ZZ1
formula['t1'] = t1
t2 = Y2 * t1
formula['t2'] = t2
t3 = t2 - Y1
formula['t3'] = t3
r = 2 * t3
formula['r'] = r
V = X1 * I
formula['V'] = V
t4 = r ** 2
formula['t4'] = t4
t5 = 2 * V
formula['t5'] = t5
t6 = t4 - J
formula['t6'] = t6
X3 = t6 - t5
formula['X3'] = X3
t7 = V - X3
formula['t7'] = t7
t8 = Y1 * J
formula['t8'] = t8
t9 = 2 * t8
formula['t9'] = t9
t10 = r * t7
formula['t10'] = t10
Y3 = t10 - t9
formula['Y3'] = Y3
t11 = Z1 + H
formula['t11'] = t11
t12 = t11 ** 2
formula['t12'] = t12
t13 = t12 - ZZ1
formula['t13'] = t13
Z3 = t13 - HH
formula['Z3'] = Z3
ZZ3 = Z3 ** 2
formula['ZZ3'] = ZZ3
t14 = ZZ3 ** 2
formula['t14'] = t14
T3 = a * t14
formula['T3'] = T3
