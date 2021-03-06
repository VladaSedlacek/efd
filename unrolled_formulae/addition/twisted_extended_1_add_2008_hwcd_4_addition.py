from sage.all import PolynomialRing, ZZ

pr = PolynomialRing(ZZ, ('a', 'd', 'X1', 'X2', 'Y1', 'Y2'), 6)
a, d, X1, X2, Y1, Y2 = pr.gens()
k, d2 = 2 * d, 2 * d
T1 = X1 * Y1
T2 = X2 * Y2
Z1, Z2 = 1, 1
formula = {}
t0 = Y1 - X1
formula['t0'] = t0
t1 = Y2 + X2
formula['t1'] = t1
A = t0 * t1
formula['A'] = A
t2 = Y1 + X1
formula['t2'] = t2
t3 = Y2 - X2
formula['t3'] = t3
B = t2 * t3
formula['B'] = B
t4 = 2 * T2
formula['t4'] = t4
C = Z1 * t4
formula['C'] = C
t5 = 2 * Z2
formula['t5'] = t5
D = T1 * t5
formula['D'] = D
E = D + C
formula['E'] = E
F = B - A
formula['F'] = F
G = B + A
formula['G'] = G
H = D - C
formula['H'] = H
X3 = E * F
formula['X3'] = X3
Y3 = G * H
formula['Y3'] = Y3
T3 = E * H
formula['T3'] = T3
Z3 = F * G
formula['Z3'] = Z3
