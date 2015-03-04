



import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt



plt.rc('text', usetex=True)
plt.rc('font', family='serif', size=28)

# The slices will be ordered and plotted counter-clockwise.
labels = r'Not in\\ acceptance', r'$e/\mu$', r'$\tau \rightarrow e/\mu$', r'1-prong $\tau$', r'$\geq$3-prong $\tau$'
sizes = [16.8, 61.5, 6.6, 7.9, 7.1]
colors = ['#eeeeee', '#b9e6ff', '#ffc8c8', '#fff08c', '#c8f0a0']

plt.figure()
plt.pie(sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', startangle=90)
plt.axis('equal')

plt.show()

plt.savefig("initial.pdf")

