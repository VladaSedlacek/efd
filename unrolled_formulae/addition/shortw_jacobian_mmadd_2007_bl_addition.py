from sage.all import PolynomialRing, ZZ

pr = PolynomialRing(ZZ, ('a', 'b', 'X1', 'X2', 'Y1', 'Y2'), 6)
a, b, X1, X2, Y1, Y2 = pr.gens()
ZZ1, ZZZ1, ZZ2, ZZZ2 = 1, 1, 1, 1
b2 = 2 * b
b4 = 4 * b
half = 1 / 2
Z1, Z2 = 1, 1
formula = {}
H = X2 - X1
formula['H'] = H
HH = H ** 2
formula['HH'] = HH
I = 4 * HH
formula['I'] = I
J = H * I
formula['J'] = J
t0 = Y2 - Y1
formula['t0'] = t0
r = 2 * t0
formula['r'] = r
V = X1 * I
formula['V'] = V
t1 = r ** 2
formula['t1'] = t1
t2 = 2 * V
formula['t2'] = t2
t3 = t1 - J
formula['t3'] = t3
X3 = t3 - t2
formula['X3'] = X3
t4 = V - X3
formula['t4'] = t4
t5 = Y1 * J
formula['t5'] = t5
t6 = 2 * t5
formula['t6'] = t6
t7 = r * t4
formula['t7'] = t7
Y3 = t7 - t6
formula['Y3'] = Y3
Z3 = 2 * H
formula['Z3'] = Z3
