from sage.all import PolynomialRing, ZZ

pr = PolynomialRing(ZZ, ('a', 'b', 'X1', 'X2', 'Y1', 'Y2'), 6)
a, b, X1, X2, Y1, Y2 = pr.gens()
ZZ1, ZZZ1, ZZ2, ZZZ2 = 1, 1, 1, 1
b2 = 2 * b
b4 = 4 * b
half = 1 / 2
Z1, Z2 = 1, 1
formula = {}
U1 = X1 * Z2
formula['U1'] = U1
U2 = X2 * Z1
formula['U2'] = U2
S1 = Y1 * Z2
formula['S1'] = S1
S2 = Y2 * Z1
formula['S2'] = S2
ZZ = Z1 * Z2
formula['ZZ'] = ZZ
T = U1 + U2
formula['T'] = T
M = S1 + S2
formula['M'] = M
t0 = T - ZZ
formula['t0'] = t0
t1 = T + ZZ
formula['t1'] = t1
t2 = U1 * U2
formula['t2'] = t2
t3 = t0 * t1
formula['t3'] = t3
R = t3 - t2
formula['R'] = R
F = ZZ * M
formula['F'] = F
L = M * F
formula['L'] = L
G = T * L
formula['G'] = G
t4 = R ** 2
formula['t4'] = t4
W = t4 - G
formula['W'] = W
t5 = F * W
formula['t5'] = t5
X3 = 2 * t5
formula['X3'] = X3
t6 = 2 * W
formula['t6'] = t6
t7 = G - t6
formula['t7'] = t7
t8 = L ** 2
formula['t8'] = t8
t9 = R * t7
formula['t9'] = t9
Y3 = t9 - t8
formula['Y3'] = Y3
t10 = F ** 2
formula['t10'] = t10
t11 = F * t10
formula['t11'] = t11
Z3 = 2 * t11
formula['Z3'] = Z3
