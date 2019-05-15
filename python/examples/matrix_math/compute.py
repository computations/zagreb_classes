#!/usr/bin/env python3

import numpy

# Make random data

variables = 10
observations = 1000

numpy.random.seed(101231)
means = numpy.ones(variables)
cov = numpy.zeros((variables,variables))

for i in range(variables):
    random_vector = numpy.random.randn(variables)
    cov += numpy.outer(random_vector, random_vector)

print(numpy.linalg.matrix_rank(cov))
cov = cov @ cov.T

A = []

for i in range(observations):
    x = numpy.random.multivariate_normal(means, cov)
    A.append(x)



A = numpy.array(A)
print(numpy.linalg.cond(A))

e,v = numpy.linalg.eig(A.T@A)
X = A@v
print(X.shape)
