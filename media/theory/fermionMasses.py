
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt

X = [0.8, 1, 1.2, 1.8, 2, 2.2, 2.8, 3, 3.2]
Y = [0.511, 4.8, 2.4, 105.7, 104, 1270, 1777, 4200, 171200 ]
labels = [ "$e$", "$d$", "$u$", r"$\mu$", "$s$", "$c$", r"$\tau$", r"$b$", r"$t$" ]

plt.rc('text', usetex=True)
plt.rc('font', family='serif')


plt.subplots_adjust(bottom = 0.1)

plt.scatter(
        X, Y, marker = 'o', c = '#0077ff', s = 70, alpha=0.8,
        cmap = plt.get_cmap('Spectral'))

for label, x, y in zip(labels, X, Y):
    plt.annotate(
            label, 
            xy = (x, y), xytext = (-5, 5),
            textcoords = 'offset points', ha = 'center', va = 'bottom',
            bbox = dict(boxstyle = 'round,pad=0.5', alpha = 0.0), fontsize=20)

xAxis = [1, 2, 3]
xAxisLabels = ["1$^{st}$ gen", "2$^{nd}$ gen", "3$^{rd}$ gen"]
plt.xticks(xAxis, xAxisLabels)
plt.yscale("log")
plt.ylabel("Mass [GeV]", fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)
#plt.show()
plt.savefig("fermionMasses.pdf")

