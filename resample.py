import numpy as np
import random
import scipy

# Use a fixed seed for the random number generator so results are repeatable
np.random.seed(42)

def read_values(filename):
    f = open(filename, "r")
    strs = f.readlines()
    f.close()
    return [float(s.strip().split(",")[1]) for s in strs[1:]]

stalls = read_values("data/stalls-real.csv")

# Approximate the data's probability density function using kernal-density estimation
kde = scipy.stats.gaussian_kde(stalls)

# Generate new random stalls from the kde
random_stalls = kde.resample(size=len(stalls))[0]

# Save these new stalls to a file
f = open("stalls-resampled.csv", "w")
f.write("type,value\n")
for s in random_stalls:
    f.write("good random stall,%.3f\n"%s)
f.close()
