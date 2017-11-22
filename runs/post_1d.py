import athena_read
import pylab as pl
import numpy as np

# Optimized plot parameters to make beautiful plots:
pl.rcParams['figure.figsize']  = 10, 14
pl.rcParams['figure.dpi']      = 100
pl.rcParams['image.cmap']      = 'jet'
pl.rcParams['lines.linewidth'] = 1.5
pl.rcParams['font.family']     = 'serif'
pl.rcParams['font.weight']     = 'bold'
pl.rcParams['font.size']       = 20
pl.rcParams['font.sans-serif'] = 'serif'
pl.rcParams['text.usetex']     = True
pl.rcParams['axes.linewidth']  = 1.5
pl.rcParams['axes.titlesize']  = 'medium'
pl.rcParams['axes.labelsize']  = 'medium'

pl.rcParams['xtick.major.size'] = 8
pl.rcParams['xtick.minor.size'] = 4
pl.rcParams['xtick.major.pad']  = 8
pl.rcParams['xtick.minor.pad']  = 8
pl.rcParams['xtick.color']      = 'k'
pl.rcParams['xtick.labelsize']  = 'medium'
pl.rcParams['xtick.direction']  = 'in'

pl.rcParams['ytick.major.size'] = 8
pl.rcParams['ytick.minor.size'] = 4
pl.rcParams['ytick.major.pad']  = 8
pl.rcParams['ytick.minor.pad']  = 8
pl.rcParams['ytick.color']      = 'k'
pl.rcParams['ytick.labelsize']  = 'medium'
pl.rcParams['ytick.direction']  = 'in'

data = athena_read.athdf('Sod.out1.00000.athdf')

x = data['x1f'][1:] + data['x1f'][:-1]

for i in range(252):
    
    data = athena_read.athdf('Sod.out1.{:05d}.athdf'.format(i))
    
    n = data['rho'].flatten()
    p = data['press'].flatten()
    v = data['vel1'].flatten()
    
    fig = pl.figure()

    ax1 = fig.add_subplot(3, 1, 1)
    ax1.plot(x, n)
    ax1.set_ylim([0, 1.1])
    ax1.set_ylabel(r'$\rho$')

    ax2 = fig.add_subplot(3, 1, 2)
    ax2.plot(x, v)
    ax2.set_ylabel(r'$v_x$')
    ax2.set_ylim([0, 1.1])

    ax3 = fig.add_subplot(3, 1, 3)
    ax3.plot(x, p)
    ax3.set_ylabel(r'$p$')
    ax3.set_ylim([0, 1.1])
    ax3.set_xlabel('$x$')

    fig.suptitle('Time = ' + str(i * 0.001))
    pl.savefig('images/{:04d}.png'.format(i))
    pl.close(fig)
    pl.clf()
