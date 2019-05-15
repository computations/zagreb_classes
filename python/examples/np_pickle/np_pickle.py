#!/usr/bin/env python3

import pickle
import numpy

A = numpy.random.randn(100,100)

with open('array.pkl', 'wb') as pickle_file:
    pickle.dump(A, pickle_file)

numpy.save('array.npy', A)

with open('array.pkl', 'rb') as pickle_file:
    load_A = pickle.load(pickle_file)

print((load_A == A).all())
