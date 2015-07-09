import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import numpy as np

with plt.xkcd():

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.set_xlim([0,800])

    # Describe decay
    ax.text(550, 270, r'Stop $\rightarrow$ t + neutralino', fontsize=15)

    # Draw lines
        # deltam = 0
    ax.plot([0,   400], [0, 400], '-',  color="#777777")
    ax.text(315, 390, r'$\Delta$m = 0', fontsize=15, rotation=57)
        # deltam = mw
    ax.plot([80,  480], [0, 400], '--', color="#777777")
    ax.text(350, 390, r'$\Delta$m = W mass', fontsize=15, rotation=57)
        # deltam = mtop
    ax.plot([172, 572], [0, 400], '--', color="#777777")
    ax.text(425, 390, r'$\Delta$m = top mass', fontsize=15, rotation=57)

    # Draw ellipses
        # compressed
    ax.add_patch(Ellipse(xy=(140, 100), width=35, height=250, angle=-45, edgecolor='#0055dd', fc='None', lw=2))
    ax.annotate('compressed\n  spectrum',xy=(140,100), arrowprops=dict(arrowstyle='->'), xytext=(50, 250))
        # offshell top
    ax.add_patch(Ellipse(xy=(220, 100), width=35, height=250, angle=-45, edgecolor='#007755', fc='None', lw=2))
    ax.annotate('Off-shell\n   top',xy=(240,120), arrowprops=dict(arrowstyle='->'), xytext=(400, 170))
        # stealthy
    ax.add_patch(Ellipse(xy=(272, 100), width=15, height=250, angle=-45, edgecolor='#aa0055', fc='None', lw=2))
    ax.annotate('Stealthy',xy=(252,80), arrowprops=dict(arrowstyle='->'), xytext=(275, 30))
        # high deltam
    ax.add_patch(Ellipse(xy=(900, -100), width=650, height=600, angle=0,  edgecolor='#ddaa00', fc='None', lw=2))
    ax.annotate('High\n $\Delta$m',xy=(700,50), arrowprops=dict(arrowstyle='->'), xytext=(600, 120))

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


    plt.savefig('T2tt.pdf')
    plt.savefig('T2tt.png', dpi=200)
