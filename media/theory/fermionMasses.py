
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt

X        = [0.8,   1,     1.2,   1.8,      2,     2.2,   2.8,       3,      3.2,    3.8,    4,      4.2   ]
labels   = ["$e$", "$d$", "$u$", r"$\mu$", "$s$", "$c$", r"$\tau$", r"$b$", r"$t$", "$W$",  "$Z$",  "$h$" ]
Y        = [0.511, 4.8,   2.4,   105.7,    95,    1270,  1777,      4200,   173500, 80385,  91187,  125000]
YerrUp   = [0,     0.7,   0.7,   0,        5,     0,     0,         0,      1,      0,      0,      0     ]
YerrDown = [0,     0.5,   0.3,   0,        5,     0,     0,         0,      1,      0,      0,      0     ]

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.subplots_adjust(bottom = 0.1)

plt.errorbar(
        X, Y, yerr=[YerrUp,YerrDown], fmt = 'o', c = '#0099ff')

for label, x, y in zip(labels, X, Y):
    plt.annotate(
            label, 
            xy = (x, y), xytext = (-5, 5),
            textcoords = 'offset points', ha = 'center', va = 'bottom',
            bbox = dict(boxstyle = 'round,pad=0.5', alpha = 0.0), fontsize=20)

xAxis = [1, 2, 3, 4]
xAxisLabels = ["1$^{st}$ gen", "2$^{nd}$ gen", "3$^{rd}$ gen", "Bosons"]
plt.xticks(xAxis, xAxisLabels)
plt.yscale("log")
plt.ylabel("Mass [MeV]", fontsize=20)
plt.tick_params(axis='both', which='major', labelsize=20)

plt.savefig("fermionMasses.pdf")

