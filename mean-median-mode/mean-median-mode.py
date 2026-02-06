import numpy as np
from collections import Counter

def mean_median_mode(x):
    x = list(x)
    x.sort()

    mean = float(np.mean(x))
    median = float(np.median(x))

    c = Counter(x)
    max_freq = max(c.values())
    mode = float(min(k for k, v in c.items() if v == max_freq))

    return (mean, median, mode)
