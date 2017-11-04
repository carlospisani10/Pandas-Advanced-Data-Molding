# Dependencies
from random import random

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import sem


# "Will you vote for a republican in this election?"
sample_size = 100
samples = [[True if random() < 0.5 else False for x in range(0, sample_size)] for y in range(0, 10)]
x_axis = np.arange(0, len(samples), 1)

means = [np.mean(s) for s in samples]
standard_errors = [sem(s) for s in samples]

# Setting up the plot
plt.errorbar(x_axis, means, yerr=standard_errors, fmt="o")

plt.xlim(-1, len(samples) + 1)

plt.xlabel("Sample Number")
plt.ylabel("Proportion of People Voting Republican")

plt.show()
