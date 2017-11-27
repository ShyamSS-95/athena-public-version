import numpy as np
import h5py
import pylab as pl

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

h5f = h5py.File('kh.out2.00000.athdf', 'r')

x = -0.5 + (0.5 + np.arange(256)) * 1/256
y = -0.5 + (0.5 + np.arange(256)) * 1/256

x, y = np.meshgrid(x, y)

h5f.close()

for i in range(1001):
    
    h5f = h5py.File('kh.out2.{:05d}.athdf'.format(i), 'r')
    rho = h5f['prim'][:][0].reshape(256, 256)
    h5f.close()
    
    pl.contourf(x, y, rho, np.linspace(0.8, 2.2, 100))
    pl.axes().set_aspect('equal')
    pl.title('Time = ' +  str(i * 0.01))
    pl.xlabel(r'$x$')
    pl.ylabel(r'$y$')
    pl.colorbar()
    pl.savefig('images/{:04d}.png'.format(i))
    pl.clf()
