import numpy as np
from numpy.random import exponential as Exp
import random
import scipy

# Use a fixed seed for the random number generator so results are repeatable
np.random.seed(42)

for _ in range(460000):
    v = Exp()
    print("bad stall,%.3f" % (v*30))
