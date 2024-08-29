import numpy

l = [[3,4,5],[6,7,8],[9,0,1]]
z = numpy.matrix(l)

print(z)

print("\nTransposta da matriz:")
print(z.T)

print("\nInversa da matriz")
print(z.I)

r = numpy.matrix([[3,2,1]])
print("\nMultiplicando matrizes:")
print(r * z)

print("\nResolvendo um sistema linear:")
print(numpy.linalg.solve(z, numpy.array([0,1,2])))
