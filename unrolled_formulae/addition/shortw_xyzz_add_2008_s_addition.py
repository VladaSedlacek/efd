from sage.all import PolynomialRing, ZZ

pr = PolynomialRing(ZZ, ('a', 'b', 'X1', 'X2', 'Y1', 'Y2'), 6)
a, b, X1, X2, Y1, Y2 = pr.gens()
ZZ1, ZZZ1, ZZ2, ZZZ2 = 1, 1, 1, 1
b2 = 2 * b
b4 = 4 * b
half = 1 / 2
Z1, Z2 = 1, 1
formula = {}
U1 = X1 * ZZ2
formula['U1'] = U1
U2 = X2 * ZZ1
formula['U2'] = U2
S1 = Y1 * ZZZ2
formula['S1'] = S1
S2 = Y2 * ZZZ1
formula['S2'] = S2
P = U2 - U1
formula['P'] = P
R = S2 - S1
formula['R'] = R
PP = P ** 2
formula['PP'] = PP
PPP = P * PP
formula['PPP'] = PPP
Q = U1 * PP
formula['Q'] = Q
t0 = R ** 2
formula['t0'] = t0
t1 = 2 * Q
formula['t1'] = t1
t2 = t0 - PPP
formula['t2'] = t2
X3 = t2 - t1
formula['X3'] = X3
t3 = Q - X3
formula['t3'] = t3
t4 = S1 * PPP
formula['t4'] = t4
t5 = R * t3
formula['t5'] = t5
Y3 = t5 - t4
formula['Y3'] = Y3
t6 = ZZ2 * PP
formula['t6'] = t6
ZZ3 = ZZ1 * t6
formula['ZZ3'] = ZZ3
t7 = ZZZ2 * PPP
formula['t7'] = t7
ZZZ3 = ZZZ1 * t7
formula['ZZZ3'] = ZZZ3
