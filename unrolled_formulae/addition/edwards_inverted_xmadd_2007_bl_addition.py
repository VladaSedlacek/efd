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
A = Z1 * Z2
formula['A'] = A
t0 = A ** 2
formula['t0'] = t0
B = d * t0
formula['B'] = B
D = Y1 * Y2
formula['D'] = D
E = X1 * D
formula['E'] = E
F = E - B
formula['F'] = F
G = E + B
formula['G'] = G
H = X1 - D
formula['H'] = H
t1 = X1 * Y2
formula['t1'] = t1
I = t1 + Y1
formula['I'] = I
t2 = G * H
formula['t2'] = t2
X3 = c * t2
formula['X3'] = X3
t3 = F * I
formula['t3'] = t3
Y3 = c * t3
formula['Y3'] = Y3
t4 = H * I
formula['t4'] = t4
Z3 = A * t4
formula['Z3'] = Z3
