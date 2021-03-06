from sage.all import PolynomialRing, ZZ

pr = PolynomialRing(ZZ, ('a', 'b', 'X1', 'X2', 'Y1', 'Y2'), 6)
a, b, X1, X2, Y1, Y2 = pr.gens()
ZZ1, ZZZ1, ZZ2, ZZZ2 = 1, 1, 1, 1
b2 = 2 * b
b4 = 4 * b
half = 1 / 2
Z1, Z2 = 1, 1
formula = {}
A = Z1 ** 2
formula['A'] = A
E = X2 * Z1
formula['E'] = E
G = Y2 * A
formula['G'] = G
H = X1 - E
formula['H'] = H
I = Y1 - G
formula['I'] = I
II = I ** 2
formula['II'] = II
J = Z1 * H
formula['J'] = J
t0 = J * H
formula['t0'] = t0
K = 2 * t0
formula['K'] = K
t1 = X1 + E
formula['t1'] = t1
t2 = t1 * K
formula['t2'] = t2
t3 = 2 * II
formula['t3'] = t3
X3 = t3 - t2
formula['X3'] = X3
JJ = J ** 2
formula['JJ'] = JJ
t4 = J + I
formula['t4'] = t4
t5 = t4 ** 2
formula['t5'] = t5
t6 = X1 * K
formula['t6'] = t6
t7 = t5 - JJ
formula['t7'] = t7
t8 = t7 - II
formula['t8'] = t8
t9 = t6 - X3
formula['t9'] = t9
t10 = K ** 2
formula['t10'] = t10
t11 = Y1 * t10
formula['t11'] = t11
t12 = t8 * t9
formula['t12'] = t12
Y3 = t12 - t11
formula['Y3'] = Y3
Z3 = 2 * JJ
formula['Z3'] = Z3
