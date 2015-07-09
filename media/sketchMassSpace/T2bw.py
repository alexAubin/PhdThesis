import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

with plt.xkcd():

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_xlim([0,800])

    # Comment "low x"
    ax.text(550, 270, r'Stop $\rightarrow$ b + chargino', fontsize=15)
    ax.text(600, 250, r'(Low x case)', fontsize=15)

    # Draw lines
        # deltam = 0
    ax.plot([0,   400], [0, 400], '-',  color="#777777")
    ax.text(315, 390, r'$\Delta$m = 0', fontsize=15, rotation=57)
        # deltam = m W / x
    ax.plot([172, 572], [0, 400], '--', color="#777777")
    ax.text(420, 390, r'$\Delta$m = W mass / x', fontsize=15, rotation=57)

    # Draw ellipses
        # offshell W
    ax.add_patch(Ellipse(xy=(185, 100), width=100, height=250, angle=-50, edgecolor='#007755', fc='None', lw=2))
    ax.annotate('Off-shell W',xy=(200,100), arrowprops=dict(arrowstyle='->'), xytext=(400, 170))
        # Light chargino
    ax.plot([60,   650], [50, 0], '-',  color="#ddaa00")
    ax.annotate('Light chargino',xy=(270,20), arrowprops=dict(arrowstyle='->'), xytext=(350, 50))

    # Tweak axes
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("stop mass")
    ax.set_ylabel("neutralino mass")

    #ax.arrow(800, -1, 1, 0, width=0.01, color="k", clip_on=False, head_width=5, head_length=5)
    #ax.arrow(1, 400, 0, 1,  width=0.01, color="k", clip_on=False, head_width=5, head_length=5)

    plt.savefig('T2bw.pdf')
    plt.savefig('T2bw.png', dpi=200)
