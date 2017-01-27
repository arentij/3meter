from scipy import signal
import random
import matplotlib as plt

n = 1000
a = [random.random()-0.5 for i in range(n)]

fs = 20

f, x = signal.periodogram(a, fs)

plt.semilogy(f, x)
plt.show()

print(x)

## aslfjhaklw dfhwfhg
