import numpy as np

rng = np.random.default_rng()

rng = np.random.default_rng(seed=1) # so the ewsults dont CHANGE

print(rng.integers(low=1, high=7))

print(rng.integers(low=1, high=101,size=3))

print(rng.integers(low=1, high=101,size=3,2))
