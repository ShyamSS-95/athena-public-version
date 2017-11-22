import athena_read
import pylab as pl
import numpy as np

# Optimized plot parameters to make beautiful plots:
pl.rcParams['figure.figsize']  = 12, 7.5
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

data = athena_read.athdf('Implode.out2.00000.athdf')

x = data['x1f'][1:] + data['x1f'][:-1]
y = data['x2f'][1:] + data['x2f'][:-1]
x, y = np.meshgrid(x, y)

for i in range(251):
    
    data = athena_read.athdf('Implode.out2.{:05d}.athdf'.format(i))
    rho = data['rho'].reshape(200, 200)
    pl.contourf(x, y, rho, np.linspace(0.1, 1.5, 100))
    pl.axes().set_aspect('equal')
    pl.title('Time = ' +  str(i * 0.01))
    pl.xlabel(r'$x$')
    pl.ylabel(r'$y$')
    pl.colorbar()
    pl.savefig('images/{:04d}.png'.format(i))
    pl.clf()
