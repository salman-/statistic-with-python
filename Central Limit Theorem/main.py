# Central limit theorem
# Generate some random variables and sum them up and then visualize the sum using a histogram

import numpy as np
import matplotlib.pyplot as plt

POPULATION_SIZE = 10000
SAMPLE_SIZE = 20

# population = np.random.normal(loc=20, scale= 100, size=POPULATION_SIZE)
# population = np.random.uniform(low=-100, high=20, size=DISTRIBUTION_SIZE)
# population = np.random.binomial(n=10, p=.2, size=DISTRIBUTION_SIZE)
# population = np.random.beta(a=2, b=3, size=DISTRIBUTION_SIZE)
population = np.random.gamma(shape=7, scale=12, size=POPULATION_SIZE)

sample_mean = []
for i in range(1000):
    sample = np.random.choice(population, SAMPLE_SIZE)
    sample_mean.append(np.mean(sample))

print("Mean of sample mean: ", np.mean(sample_mean), "| Mean of population: ", np.mean(population))

plt.hist(sample_mean, bins=range(int(np.min(sample_mean)), int(np.max(sample_mean)), 2))
plt.title('Central limit theorem visualization')
plt.show()
